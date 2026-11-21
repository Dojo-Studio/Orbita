"""Pruebas de fallos simulados sin acceso a OpenAI ni consumo de tokens."""
import os
os.environ['ORBITA_ACCESS_CODE']='example-test-access-not-for-production'
import unittest
from unittest.mock import patch
from types import SimpleNamespace
from fastapi.testclient import TestClient
import httpx
# El SDK puede no estar instalado en el entorno de pruebas; simulamos solo sus clases.
import types, sys
fake_sdk=types.ModuleType('openai')
for name in ('RateLimitError','APIConnectionError','APITimeoutError','AuthenticationError','PermissionDeniedError','BadRequestError','NotFoundError','InternalServerError','APIStatusError'):
    setattr(fake_sdk,name,type(name,(Exception,),{}))
sys.modules.setdefault('openai',fake_sdk)
RateLimitError=fake_sdk.RateLimitError
import server


def provider_error(status=429, code='rate_limit_exceeded', retry=None):
    req=httpx.Request('POST','https://api.openai.com/v1/responses')
    body={'error':{'message':'Simulated, not real','type':code,'code':code}}
    response=httpx.Response(status,request=req,headers={'retry-after':str(retry)} if retry else {},json=body)
    e=RateLimitError('Simulated rate limit');e.response=response;e.body=body;return e

class AiErrors(unittest.TestCase):
    def setUp(self):
        self.client=TestClient(server.app,headers={'X-Orbita-Access':'example-test-access-not-for-production'})
    def test_billing_not_retryable(self):
        error=provider_error(code='insufficient_quota')
        detail=server.classify_provider_error(error)
        self.assertEqual(detail['code'],'quota_exhausted')
        self.assertFalse(detail['retryable'])
    def test_temporary_is_retryable(self):
        detail=server.classify_provider_error(provider_error(code='rate_limit_exceeded',retry=52))
        self.assertEqual(detail['code'],'rate_limited')
        self.assertEqual(detail['retry_after_seconds'],52)
        self.assertTrue(detail['retryable'])
    def test_actual_status_propagated_plan(self):
        with patch.object(server,'AI_KEY','fake-key'),patch.object(server,'RETRY_TRANSIENT',False),patch.object(server,'model_client',return_value=SimpleNamespace(responses=SimpleNamespace(create=lambda **kwargs: (_ for _ in ()).throw(provider_error(code='insufficient_quota'))))):
            r=self.client.post('/api/plan',json={'brief':{'product':'Prueba de negocio'}})
        self.assertEqual(r.status_code,429)
        self.assertEqual(r.json()['detail']['code'],'quota_exhausted')
        self.assertNotIn('sk-',str(r.json()))
    def test_actual_status_propagated_research(self):
        with patch.object(server,'AI_KEY','fake-key'),patch.object(server,'RETRY_TRANSIENT',False),patch.object(server,'model_client',return_value=SimpleNamespace(responses=SimpleNamespace(create=lambda **kwargs: (_ for _ in ()).throw(provider_error(code='rate_limit_exceeded',retry=40))))):
            r=self.client.post('/api/research',json={'brief':{},'query':'Investigar alternativas en Chiclayo'})
        self.assertEqual(r.status_code,429)
        self.assertEqual(r.json()['detail']['code'],'rate_limited')
        self.assertEqual(r.headers.get('retry-after'),'40')
    def test_actual_status_propagated_ai_report(self):
        with patch.object(server,'AI_KEY','fake-key'),patch.object(server,'RETRY_TRANSIENT',False),patch.object(server,'model_client',return_value=SimpleNamespace(responses=SimpleNamespace(create=lambda **kwargs: (_ for _ in ()).throw(provider_error(code='project_spend_limit_exceeded'))))):
            r=self.client.post('/api/report/ai',json={'brief':{},'questions':[]})
        self.assertEqual(r.status_code,429)
        self.assertEqual(r.json()['detail']['code'],'quota_exhausted')
    def test_api_unauthorized(self):
        client=TestClient(server.app)
        self.assertEqual(client.get('/api/ai/diagnose').status_code,401)
    def test_health_not_claim_operational(self):
        r=self.client.get('/api/health')
        self.assertIn('version',r.json())
        self.assertNotEqual(r.json()['mode'],'OPENAI_VERIFIED')

if __name__=='__main__':unittest.main()
