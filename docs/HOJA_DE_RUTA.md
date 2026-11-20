# Hoja de ruta de ÓRBITA — de prototipo a aplicación multiusuario

## Ya incluido en esta entrega
- Brief por cliente/sector/etapa/público/mercado/precio/costos.
- Examen sectorial local y motor de seguimientos por respuestas bajas.
- Modo opcional con generación de examen por IA desde backend.
- **Prueba Ácida del Diferenciador obligatoria con seis respuestas abiertas**, sustento declarado y contraargumento para cada pregunta.
- Endpoint IA `/api/acid/review` para crítica de las seis respuestas.
- Investigación web conectable con fuentes, adjuntos hasta 8 MB, reportes comerciales, FODA y PDF.
- Guardado local y exportar/importar avances JSON.

## Etapa 1: app interna segura (PRIORIDAD)
- Login y roles: administrador, consultor Dojo, cliente invitado, auditor.
- Datos de empresas aislados, consentimiento, eliminación de adjuntos y backups.
- Base de datos Postgres, versiones de diagnósticos y carga privada de archivos.
- QA y tests E2E en los cuatro sectores principales; control de coste y rate limiting.
- Auditorías humanas y aprobación del veredicto antes de compartirlo.

## Etapa 2: IA verdaderamente adaptativa
- Generador de preguntas por objetivo y riesgo con contexto de sesión.
- Detector de contradicciones entre brief, respuestas, PDFs, precio y comparación.
- Recuperación de evidencias con cita exacta (archivo/página/url/fecha).
- Entrevistas por voz opcionales, con consentimiento.
- Investigación de competidores y sustitutos directa e indirecta; comparación homogénea y trazable.
- Enlaces a fuentes caducados o ambiguos: marcar como «requiere verificación».

## Etapa 3: inteligencia operacional
- Dashboard por cliente/producto y comparativas 30/60/90 días.
- Experimentos con hipótesis, responsable, plazo, inversión, métrica y resultado.
- Integraciones opcionales con CRM / Meta Ads / Google Ads / analítica (con autorización).
- Panel de supervisión para dirección Dojo: qué productos están listos para pautar y cuáles no.
- Reportes PDF con branding editable y firma/revisión.

## Amenazas de seguridad a mitigar antes de lanzamiento
No exponer la demo ni `localStorage` a clientes reales con datos sensibles. Implementar: autenticación, multi-tenancy y Row Level Security, privacidad por archivo y sesión, validación completa de uploads y enlaces, filtrado SSRF, control de presupuesto de IA, respuestas sanitizadas, protección ante prompt injection, políticas de retención, trazas y revisión de cumplimiento legal aplicable.
