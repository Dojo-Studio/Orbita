# DOJO ÓRBITA 4.1 — Product Intelligence

Sistema de diagnóstico comercial contextual de DOJO STUDIO, preparado para Vercel FastAPI.

## Qué incluye

- Brief contextual: sector, etapa, mercado, precio, costos, cliente y pruebas.
- Examen diferenciado por sector con preguntas de opción específica, texto, número, comparaciones y repreguntas.
- Prueba Ácida obligatoria con seis preguntas de diferenciación.
- Investigación con IA + búsqueda web, solo si el proveedor responde y se recuperan fuentes identificables.
- Evaluación de riesgos, FODA preliminar, 12 dimensiones, carta radial, exportación JSON y PDF.
- Auditoría de Prueba Ácida, examen generado por IA e informe enriquecido (requieren OpenAI API funcional).
- Guardado local del avance en el navegador y exportación/importación JSON. **No hay base de datos multiusuario.**
- Manejo de errores 429 de cuota y límites de peticiones. Los datos del examen NO se borran al producirse un fallo de IA.
- Diagnóstico manual en `/api/ai/diagnose` para comprobar la API con una solicitud real pequeña.

## Desplegar sin cambiar el enlace actual

**Lee `ACTUALIZAR_VERCEL.md`.** Se recomienda actualizar el proyecto existente `orbita`, no crear otro.

### Variables de entorno Vercel

| Variable | Función |
| --- | --- |
| `ORBITA_ACCESS_CODE` | Código secreto del equipo para llamadas de IA y PDF privadas. |
| `OPENAI_API_KEY` | Clave secreta de OpenAI. La facturación es distinta de ChatGPT. |
| `OPENAI_MODEL` | Opcional. Valor por defecto `gpt-4.1-mini`. |
| `ORBITA_RETRY_TRANSIENT` | Opcional. `1` = un reintento acotado para errores temporales muy breves; `0` = sin reintentos. |

El código `ORBITA_ACCESS_CODE` NO es el API key `sk-...`.

## ¿Qué cambió frente a V4?

Ahora un error 429 del proveedor NO se transforma en el engañoso `502 RateLimitError`. El servidor devuelve la causa diferenciada cuando el SDK la informa y el navegador explica el siguiente paso. El informe local siempre sigue disponible. Se muestra “IA configurada · sin verificar” hasta que una solicitud real confirma capacidad.

Además: se disminuyó la longitud de solicitudes y el número de repreguntas IA por sesión (máximo 4, además de repreguntas locales) para consumir menos tokens; se agregó la síntesis IA al PDF si está disponible. Ninguna de estas mejoras aumenta saldos, cuotas o límites de OpenAI.

## Funciona en local

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# Completar .env con tus credenciales si deseas IA; no publicarlo
uvicorn server:app --reload
```

Visita `http://127.0.0.1:8000`.

## Pruebas

```bash
python -m unittest -v test_backend.py test_errors.py
```

La prueba opcional de navegador `python test_browser_41.py` necesita `playwright` y Chromium. Todas las pruebas simulan errores sin utilizar claves reales ni gastar tokens.

## Seguridad y límites del piloto

- Nunca pongas `OPENAI_API_KEY` en JavaScript ni GitHub.
- No compartas `ORBITA_ACCESS_CODE` públicamente. La página puede ser pública, pero las funciones de IA son privadas.
- Si quieres IA pública sin contraseña, implementa autenticación por usuario o sesiones limitadas, protección anti-bot, límites de uso **en almacenamiento compartido durable** (Redis/DB, no memoria de la función), registro de consumo y límite de gasto antes de habilitar esos endpoints. Esta versión NO habilita IA pública anónima.
- Los archivos se procesan en el servidor y se devuelve un extracto; el cliente guarda datos en su navegador. Pide permiso explícito antes de analizar documentación confidencial de terceros.
- Un valor declarado por un cliente no queda automáticamente certificado. ÓRBITA evita inventar fuentes y no garantiza ventas.
