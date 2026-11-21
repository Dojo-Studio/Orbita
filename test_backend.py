"""Pruebas offline; no gastan créditos de IA. Ejecutar: python test_backend.py"""
from fastapi.testclient import TestClient
import os
os.environ["ORBITA_ACCESS_CODE"] = "example-test-access-not-for-production"
import unittest
from pathlib import Path
from pypdf import PdfReader
from io import BytesIO
import server

class OrbitTests(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(server.app, headers={"X-Orbita-Access": "example-test-access-not-for-production"})
    def test_server_html(self):
        self.assertEqual(self.client.get('/api/health').status_code,200)
        self.assertEqual(self.client.get('/api/health').json()['version'],'4.1')
        html=self.client.get('/').text
        self.assertIn('id="screen-acid"',html)
        self.assertIn('function acidMetrics()',html)
        self.assertIn('id="answer-input"', html)
        self.assertNotIn('Describe qué tan cierta es esta afirmación',html)
    def test_six_questions_consistent(self):
        questions=self.client.get('/api/acid/questions').json()['questions']
        self.assertEqual([x['id'] for x in questions],['a1','a2','a3','a4','a5','a6'])
        html=Path(__file__).with_name('index.html').read_text()
        for x in questions:
            self.assertIn(x['text'], html.replace(chr(92)+chr(34), chr(34)))
    def test_acid_requires_six_answers(self):
        bad=self.client.post('/api/acid/review',json={'brief':{'product':'Test'},'acid':{'a1':{'answer':'algo único a demostrar'}}})
        self.assertEqual(bad.status_code,400)
    def test_acid_no_ai(self):
        if server.AI_KEY:return
        records={key:{'answer':f'Argumento razonado de prueba para {key}', 'evidence':2,'source':'Entrevista'} for key,_ in server.ACID_QUESTIONS}
        r=self.client.post('/api/acid/review',json={'brief':{'product':'Test'},'acid':records})
        self.assertEqual(r.status_code,503)
    def test_question_schema_rejects_generic_scale(self):
        q={"id":"q_1","dimension":"Precio","text":"¿Qué sucedió al ofrecer el precio?","type":"choice","options":[{"value":str(i),"label":v,"score":i*25} for i,v in enumerate(["No sé","Débil","Parcial","Sólido","Comprobado"])]}
        self.assertEqual(server.validate_questions([q]),[])

    def test_typed_question_schema(self):
        self.assertIn('type',server.QUESTION_SCHEMA['properties'])
        self.assertIn('options',server.QUESTION_SCHEMA['properties'])
        self.assertIn('number',server.QUESTION_SCHEMA['properties']['type']['enum'])

    def test_pdf_contains_acid(self):
        stats=[{'name':n,'score':60+i%5*5,'evidence':40+i%3*10} for i,n in enumerate(server.DIMENSIONS)]
        acid={key:{'answer':f'Respuesta de prueba con contexto, argumento {key}', 'evidence':3,'source':'Entrevista y comparativos', 'rebuttal':'Contraargumento documentado'} for key,_ in server.ACID_QUESTIONS}
        payload={'brief':{'client':'Demo','product':'Oferta','currency':'S/','sector':'inmo'},'acid':acid,'analysis':{'score':63,'evidence':42,'verdict':'VALIDAR','margin':120,'stats':stats,'errors':['Falta evidencia de demanda.']}}
        r=self.client.post('/api/report/pdf',json=payload)
        self.assertEqual(r.status_code,200)
        self.assertTrue(r.content.startswith(b'%PDF'))
        text=' '.join(p.extract_text() or '' for p in PdfReader(BytesIO(r.content)).pages)
        self.assertIn('PRUEBA ÁCIDA DEL DIFERENCIADOR',text)
        normalized=' '.join(text.split())
        for key,question in server.ACID_QUESTIONS:self.assertIn(' '.join(question.split()),normalized)
    def test_csv(self):
        r=self.client.post('/api/file',files={'file':('ventas.csv',b'fecha,ventas\n2026-11-01,12','text/csv')})
        self.assertEqual(r.status_code,200)
        self.assertIn('ventas',r.json()['excerpt'])
    def test_unsupported_file(self):
        r=self.client.post('/api/file',files={'file':('prueba.exe',b'program','application/octet-stream')})
        self.assertEqual(r.status_code,400)
    def test_unconfigured_ai(self):
        if not server.AI_KEY:
            r=self.client.post('/api/plan',json={'brief':{'product':'Test'}})
            self.assertEqual(r.status_code,503)
if __name__=='__main__':unittest.main()
