# Solución del error `RateLimitError` / 429

En la versión anterior la investigación y el informe mostraban `502 RateLimitError`. Esto escondía un error real del proveedor.

La nueva versión diferencia:

| Mensaje | Causa posible | Acción |
| --- | --- | --- |
| `quota_exhausted` / «saldo, cuota o límite de gasto» | Sin créditos, límite de proyecto u organización, facturación no activa | Revisar Billing, Usage y Limits. No sirve reintentar continuamente. |
| `rate_limited` / «demasiadas solicitudes o tokens» | Límite temporal RPM/TPM | Esperar Retry-After, evitar ráfagas, usar menos tokens, aumentar límites si corresponde. |
| `api_auth` | Clave o permisos incorrectos | Revisar `OPENAI_API_KEY` y permisos del proyecto. |
| `api_configuration` | Modelo no disponible o parámetros no admitidos | Revisar `OPENAI_MODEL`; re-desplegar tras cambiarlo. |
| `provider_unavailable` | Conexión/servicio temporal | Reintentar más tarde, continuar con modo contextual. |

### Revisión en OpenAI Platform

- Facturación: https://platform.openai.com/settings/organization/billing/overview
- Uso: https://platform.openai.com/usage
- Límites: https://platform.openai.com/settings/organization/limits
- Documentación oficial: https://help.openai.com/es-419/articles/5955604-troubleshooting-api-rate-limits-and-429-errors

Si tu clave es nueva, «Active» solo significa que existe; **no garantiza saldo disponible ni una cuenta de API habilitada para consumir**. ChatGPT Plus no incluye créditos de API.

### Qué hace la aplicación

- Identifica y comunica el error al usuario en español.
- Muestra `Retry-After` cuando el proveedor lo suministra.
- No reintenta automáticamente errores de saldo o gasto; solo puede hacer un reintento corto para límites estrictamente temporales.
- Mantiene examen, Prueba Ácida, datos guardados, cálculos e informe local disponibles.
- No inventa competidores, citas ni resultados de IA tras una solicitud fallida.
- En modo IA usa entradas más cortas y un máximo de 4 llamadas de repregunta (las demás repreguntas son contextuales y locales).
- Añade un botón de comprobación en el panel de acceso privado.

**Limitación:** estas correcciones no pueden eliminar una restricción impuesta a la cuenta de OpenAI. Necesitas resolver la causa que indique el error real.
