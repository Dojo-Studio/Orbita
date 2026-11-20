# DOJO ÓRBITA 3.1 — Despliegue en Vercel

Esta carpeta contiene la **aplicación original DOJO ÓRBITA 3.0 adaptada a Vercel** (FastAPI + HTML). Incluye brief, examen contextual, Prueba Ácida de 6 preguntas, investigación opcional con IA, carga de archivos, evaluación comercial y exportación PDF.

## Desplegar con GitHub (recomendado)

1. Sube **el contenido de esta carpeta** a la raíz de un repositorio nuevo en GitHub. No subas el ZIP como un único archivo.
2. En [Vercel](https://vercel.com/new), importa el repositorio (`Add New` > `Project`).
3. Mantén **Root Directory** en `./` y **Framework Preset** en `FastAPI` (si se detecta automáticamente, déjalo así). No establezcas manualmente `Build Command` ni `Output Directory`.
4. En **Environment Variables** configura:
   - `ORBITA_ACCESS_CODE`: frase larga privada, para que el equipo active funciones API. **Obligatoria** en Vercel.
   - `OPENAI_API_KEY`: tu clave de API de OpenAI para preguntas por IA, búsqueda, auditoría y análisis visual. Opcional; sin ella funciona en modo contextual local y PDF de servidor con código.
   - `OPENAI_MODEL`: modelo disponible para tu cuenta compatible con Responses API, Structured Outputs, entrada de imagen y web_search. El ejemplo es `gpt-5.4`, que debes confirmar según tu acceso.
5. Haz clic en **Deploy**. Si agregas variables después de desplegar, vuelve a desplegar para aplicarlas.
6. Entra a la URL y usa el código de `ORBITA_ACCESS_CODE` en la pantalla inicial. Comprueba `https://tu-proyecto.vercel.app/api/health` y exporta un PDF de prueba.

## Desplegar por terminal

```bash
npm install -g vercel
vercel login
cd DOJO_ORBITA_VERCEL
vercel
# configura variables desde Vercel Dashboard
vercel --prod
```

Vercel actualmente detecta aplicaciones FastAPI mediante `server.py` con una variable `app`; **no hacen falta rewrites ni API routes JS**. La función puede ejecutar hasta `maxDuration: 60` segundos (según permisos del plan). Consulta la documentación de Vercel si cambian límites.

## Desarrollo local

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env          # Windows: copy .env.example .env
# edita .env y define ORBITA_ACCESS_CODE y, opcionalmente, OPENAI_API_KEY
python -m unittest test_backend.py
uvicorn server:app --reload
```

Abre `http://127.0.0.1:8000/`. También puedes usar `vercel dev` para simular el enrutamiento de Vercel.

## Endpoints

- Público: `GET /`, `GET /api/health`, `GET /api/acid/questions`.
- Requieren siempre código: `GET /api/access/check`, `POST /api/plan`, `/api/branch`, `/api/research`, `/api/acid/review`, `/api/report/ai`, `/api/file`, `/api/report/pdf`.
- La cabecera del cliente es `X-Orbita-Access`; el código se almacena en `sessionStorage` y no se expone como variable pública.
- Sin `ORBITA_ACCESS_CODE`, los endpoints privados **no se habilitan**, tanto en Vercel como en desarrollo local.

## Límites importantes (antes de usarlo con datos sensibles)

- Este proyecto es un **piloto interno**, no una plataforma SaaS multiusuario lista para producción. Un código compartido **no equivale** a autenticación individual con roles, auditoría y revocación de usuarios. No entregues el código a terceros ni abras la app a clientes externos sin autentificación adecuada.
- Los diagnósticos se guardan en el navegador del dispositivo (localStorage), no en una base de datos remota. Si varias personas usan el mismo navegador, podrían ver datos guardados. Para uso real con clientes añade cuentas, base de datos y controles de acceso.
- Los archivos se procesan en memoria por solicitud; las imágenes y los fragmentos de texto pueden enviarse al proveedor de IA cuando éste esté configurado. Obtén el consentimiento pertinente.
- No afirmes que la IA verificó una ventaja competitiva cuando no se respaldó con evidencia identificable. Investigación en internet solo funciona con `OPENAI_API_KEY` configurada.
- Vercel Functions no son almacenamiento persistente. Para expedientes multiusuario implementa una base de datos y un proveedor de archivos persistentes.
- Las llamadas de IA consumen créditos y pueden agotarse los tiempos de función. Ajusta costos y límites antes de uso intensivo.

## Archivos

- `index.html`: interfaz espacial y cuestionarios.
- `server.py`: API FastAPI y motor de informes; entrada reconocida por Vercel.
- `vercel.json`: configuración de funciones y cabeceras de seguridad.
- `.python-version`: Python 3.12.
- `.env.example`: plantilla de variables privadas.
- `CLAUDE.md`: instrucciones originales para continuar el desarrollo en Claude Code.
- `docs/`: especificación y hoja de ruta para evolución de producto.

**DOJO Studio — Resultados que hacen ruido.**
