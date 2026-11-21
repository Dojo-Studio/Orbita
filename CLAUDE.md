# Instrucciones para continuar en Claude Code

DOJO ÓRBITA 4.1: aplicación FastAPI de diagnóstico comercial. Antes de modificar, lee README.md, SOLUCION_ERROR_OPENAI.md y CHANGELOG.md.

Principios: ningún dato, fuente, competencia o comprobante inventado; conservar distinción entre declaración, evidencia declarada y verificación; Prueba Ácida del Diferenciador obligatoria de 6 preguntas; cuestionario contextual con tipos adecuados; no usar escalas de 0-4 para preguntas abiertas; bloqueos críticos nunca se compensan con puntajes; proteger API privada con ORBITA_ACCESS_CODE.

No revertir el tratamiento de RateLimitError a 502 genérico. Revisar provider_code, clasificación y estados. No automatizar reintentos de cuota agotada. Al introducir IA pública exigir autenticación o rate limiting durable más anti-bot + límites de gasto. Mantener la raíz FastAPI compatible con Vercel.

Ejecutar: `python -m unittest -v test_backend.py test_errors.py`. La prueba navegador `test_browser_41.py` es opcional y requiere Playwright + Chromium. No utilizar claves reales durante pruebas.
