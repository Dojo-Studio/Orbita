# DOJO ÓRBITA 3.0 — Instrucciones para Claude Code

## Tu misión
Actúa como ingeniero senior full-stack, diseñador de producto y analista estratégico. Continúa construyendo **DOJO ÓRBITA — Product Intelligence**, una aplicación espacial de diagnóstico de productos para el equipo de **Dojo Studio** y sus clientes en reuniones. No conviertas este proyecto en un simple formulario o un horóscopo decorativo. El diseño cósmico es la metáfora visual; la metodología se basa en datos, contraste de mercado, análisis de ventas y criterio crítico.

## Contexto de marca
- Agencia: **Dojo Studio**, Chiclayo, Perú.
- Slogan: **Resultados que hacen ruido**.
- Voz: disruptiva, humana, didáctica y directa; evita tecnicismo vacío y promesas exageradas.
- Diferenciador de Dojo: estrategia empresarial con enfoque en resultados medibles, no diseño bonito por sí solo.
- Tipos de negocio: todos los sectores (B2B, B2C, productos y servicios).
- Uso inicial: un estratega de Dojo entrevista a un cliente, con posibilidad de guardar avances.

## Estado del repositorio
- `index.html`: SPA HTML/CSS/JS sin bundler; funciona sin servidor en **modo contextual local**.
- `server.py`: API FastAPI opcional que entrega archivos, plan de preguntas generado con OpenAI, seguimientos, investigación con fuentes, auditoría ácida, análisis estratégico y PDF.
- `requirements.txt`: dependencias Python.
- `.env.example`: variables de entorno. **Nunca** incrustes claves en `index.html` ni las confirmes en Git.
- `test_backend.py`: pruebas de regresión locales.
- `docs/PRUEBA_ACIDA.md`: contrato de seis preguntas y criterios de evaluación.
- `docs/HOJA_DE_RUTA.md`: funcionalidades restantes antes de producción.

## Invariantes obligatorios
1. La **Prueba Ácida del Diferenciador** es una etapa independiente y obligatoria después del examen inicial. Conserva sus **seis preguntas originales**, tal como están en `docs/PRUEBA_ACIDA.md`, y no sustituyas ninguna por preguntas genéricas.
2. El examen se crea a partir de brief, sector, país/mercado, etapa, precio, audiencia, alternativas y archivos; con IA conectada, genera preguntas verdaderamente adaptadas; sin IA, usa reglas locales y lo indica con honestidad.
3. Después de cada respuesta puede aparecer un contraargumento: no concedas una ventaja por autoafirmación. Pregunta por sustitutos, alternativas gratuitas, relevancia para la decisión de compra y pruebas externas.
4. Puntajes de preparación y **solidez de evidencia** separados. La evidencia declarada NO significa verificada.
5. Riesgo crítico financiero, legal, regulatorio o de demanda puede bloquear lanzar o escalar aunque el índice comercial sea alto. **Prueba Ácida incompleta o débil** también bloquea la recomendación de escala.
6. Distingue de forma explícita **afirmación del cliente / inferencia de IA / fuente externa fechada / resultado o transacción corroborada**.
7. No inventes competidores, precios, visitas, conversiones, ventas, enlaces ni leyes. Las propuestas de investigación sin fuentes son hipótesis.
8. El informe incluye mapa radial, diagnóstico, Prueba Ácida completa, FODA, experimentos con métricas/umbrales, recomendación, fuentes y PDF.
9. Evita afirmar que «probamos que tu producto es mejor» sin comparativas de mercado y conducta de compra reales.
10. Cuida datos personales, confidencialidad de clientes, documentos y secretos de negocio. La demo usa `localStorage`; no es almacenamiento apropiado para varios clientes en producción.

## Cómo ejecutar y verificar
```bash
python -m venv .venv
source .venv/bin/activate               # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                    # Configura OPENAI_API_KEY SOLO en servidor, si usarás IA
python test_backend.py
uvicorn server:app --reload --host 127.0.0.1 --port 8000
```
Abre http://127.0.0.1:8000. Sin clave, trabaja en modo local. Con clave válida, habilita endpoints de IA. Alternativamente, abre `index.html` directamente en el navegador para modo local.

## Primeras tareas recomendadas para Claude Code
1. Separar UI, motor de reglas, Prueba Ácida, API client, puntajes y reportes en módulos TypeScript y añadir pruebas unitarias/E2E.
2. Diseñar flujo de entrevista con progreso real, guardado por cliente, firma del analista y versionado del diagnóstico.
3. Implementar motor de seguimiento con IA por respuesta, con JSON Schema, presupuesto de tokens, deduplicación y límites.
4. Permitir evidencia adjunta por pregunta y trazabilidad de fuentes (archivo, página, URL, fecha y revisor), sin reutilizar datos de un cliente en otro.
5. Proveer integración seleccionable de modelos (p.ej. OpenAI o Anthropic) **en backend**, sin poner API keys en el navegador.
6. Añadir usuarios, organizaciones, roles, almacenamiento privado, auditoría de cambios y consentimiento antes de subir archivos.
7. Revisar lógica financiera por modelo (margen unitario, inmuebles con financiación, SaaS con churn, restauración con merma, servicios con horas, etc.).
8. Probar la integridad del contrato de las seis preguntas en UI, API y PDF después de cada cambio.

## Alcance técnico y limitaciones actuales
El motor local no es un modelo de IA ni realiza investigación independiente. El servidor ofrece puntos de integración con OpenAI, **pero no se probó aquí una llamada real con credenciales**. Los resultados de la evaluación son exploratorios y necesitan aprobación humana. **No publiques en internet** sin autenticación, aislamiento por cliente y endurecimiento de seguridad; ver la hoja de ruta.

## Criterios de aceptación para nuevas entregas
- Demo en sector inmobiliario, restaurante, salud y servicios: cambian preguntas sectoriales.
- Una respuesta débil genera contraargumento contextual, sin repetir indefinidamente la misma pregunta.
- Se responden seis preguntas ácidas exactas; se conservan al exportar e importar JSON.
- La puntuación nunca evita una alerta crítica ni una Prueba Ácida deficiente.
- El PDF contiene seis preguntas, respuestas, fuentes y veredicto.
- Toda funcionalidad que requiere IA o web indica explícitamente que no funciona offline.


## Despliegue Vercel añadido (3.1)
- El proyecto FastAPI se sirve desde `server.py:app`, entrada detectada automáticamente por Vercel.
- No elimines la autenticación por código del middleware ni coloques OPENAI_API_KEY en frontend.
- En todos los entornos es obligatorio `ORBITA_ACCESS_CODE` para activar endpoints privados. Para una versión multiusuario, reemplazar por autenticación real.
- `vercel.json` define `maxDuration:60`; la IA puede alcanzar límites de duración.
- Mantén Prueba Ácida a1..a6 y su obligatoriedad.
- Revisar README.md antes de nuevos deploys.
