"""Prueba integral en Chromium con API 429 simulada. No utiliza credenciales ni tokens."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).parent
HTML=(ROOT/'index.html').read_text()
FETCH_MOCK='''<script>
window.fetch=async function(path,opts){
 const key=String(path).replace(/^\\/api\\//,'');
 let info={status:200,body:{status:'ok',ai:true,access_required:true,access_configured:true,mode:'AI_CONFIGURED_NOT_VERIFIED'}};
 if(key==='access/check')info={status:200,body:{ok:true}};
 if(key==='ai/diagnose'||key==='plan')info={status:429,body:{detail:{code:'quota_exhausted',message:'Saldo de API insuficiente',retryable:false,action:'Revisa Billing'}}};
 if(key==='research'||key==='report/ai')info={status:429,body:{detail:{code:'rate_limited',message:'Límite temporal de solicitudes',retryable:true,retry_after_seconds:37,action:'Espera y reintenta'}}};
 return {ok:info.status>=200&&info.status<300,status:info.status,json:async()=>info.body};
};
</script>'''
HTML=HTML.replace('<script>',FETCH_MOCK+'\n<script>',1)
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1400,'height':930})
 page.set_default_timeout(8000)
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(HTML,wait_until='domcontentloaded')
 page.locator('#access-code').fill('only-for-local-tests')
 page.locator('#access-save').click()
 page.wait_for_function('document.querySelector("#access-save").textContent.includes("Conectado")')
 page.locator('#ai-diagnose').click()
 page.wait_for_function('document.querySelector("#ai-diagnose-status").textContent.includes("saldo")')
 assert 'sin saldo' in page.locator('#engine-status').inner_text().lower()
 page.locator('#b-client').fill('Caso de prueba')
 page.locator('#b-product').fill('Lotes residenciales')
 page.locator('#b-sector').select_option('inmo')
 page.locator('#b-location').fill('Chiclayo, Perú')
 page.locator('#b-price').fill('180000')
 page.locator('#b-cost').fill('120000')
 page.locator('#start-exam').click()
 page.wait_for_function('document.querySelector("#screen-exam").classList.contains("on")')
 assert 'examen contextual' in page.locator('#plan-ai-status').inner_text().lower()
 answered=0
 for i in range(105):
  if not page.locator('#screen-exam').get_attribute('class').endswith('on'):break
  area=page.locator('#answer-input')
  if area.locator('[data-answer-option]').count():area.locator('[data-answer-option]').first.click()
  elif area.locator('[data-answer-multi]').count():area.locator('[data-answer-multi]').first.click()
  elif area.locator('#answer-number').count():area.locator('#answer-number').fill('3')
  elif area.locator('#answer-text').count():area.locator('#answer-text').fill('Situación de prueba documentada con observaciones y alcance real.')
  elif area.locator('#answer-alternative').count():area.locator('#answer-alternative').fill('Alternativa A');area.locator('#answer-ours').fill('Producto y propuesta')
  else:raise AssertionError('No aparece respuesta coherente')
  page.locator('#q-next').click();answered+=1
 assert answered>15,answered
 assert page.locator('#screen-acid').get_attribute('class').endswith('on')
 for t in page.locator('#acid-form textarea[data-acid-key="answer"]').all():t.fill('Diferenciador de prueba con razonamiento, hipótesis y datos declarados.')
 page.locator('#acid-finish').click()
 page.locator('#research-query').fill('Competidores y demanda para lotes en Chiclayo')
 page.locator('#research-start').click()
 page.wait_for_function('document.querySelector("#research-status").textContent.includes("37")')
 assert 'fuentes ficticias' in page.locator('#research-status').inner_text()
 page.locator('#view-report').click()
 assert page.locator('#report-verdict').inner_text()
 page.locator('#enrich-report').click()
 page.wait_for_function('document.querySelector("#ai-report-status").textContent.includes("37")')
 assert 'diagnóstico local' in page.locator('#ai-report-status').inner_text().lower()
 page.screenshot(path=str(ROOT/'VISTA_PREVIA_41.png'),full_page=False)
 assert not errors,errors
 print('Prueba navegador OK | respuestas:',answered,'| investigación e informe 429 tratados')
 browser.close()
