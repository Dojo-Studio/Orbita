# DOJO ÓRBITA — Subir a Vercel en 5 pasos

1. Descomprime `DOJO_ORBITA_VERCEL_LISTO.zip`.
2. Crea un repositorio privado o público en GitHub y sube **los archivos internos de la carpeta** (deben verse `server.py`, `index.html`, `requirements.txt` y `vercel.json` en la raíz). Usa un repositorio **privado** si quieres que el código fuente no sea público.
3. Abre https://vercel.com/new → **Import Git Repository** → selecciona el repositorio.
4. En configuración usa **Framework Preset: FastAPI** y **Root Directory: `./`**. Deja vacíos Build Command y Output Directory. Añade estas variables de entorno:
   - `ORBITA_ACCESS_CODE`: contraseña larga y única que usará el equipo para habilitar los servicios del servidor. Imprescindible.
   - `OPENAI_API_KEY`: clave privada de OpenAI. Opcional si solo quieres diagnóstico contextual.
   - `OPENAI_MODEL`: un modelo al que tu organización tenga acceso, compatible con herramientas usadas. Verifica su disponibilidad.
5. Pulsa **Deploy** y accede a la URL. En la pantalla inicial ingresa el código privado. Comprueba `/api/health`, completa una Prueba Ácida y exporta un PDF.

Si Vercel ya había desplegado antes de configurar variables, ejecuta **Redeploy** para que queden activas.

## Alternativa sin GitHub

Instala la CLI oficial de Vercel, abre la terminal dentro de la carpeta descomprimida y ejecuta:

```bash
npm install -g vercel
vercel login
vercel
vercel --prod
```

Configura las variables en el panel de Vercel antes del despliegue final.

## Qué funciona en esta versión

- Brief de producto, cuestionarios contextuales, repreguntas por reglas, Prueba Ácida con 6 preguntas, radar, FODA, alertas, informe y guardado local en navegador.
- Exportación a PDF desde servidor, protegida por código del equipo.
- Plan por IA, preguntas de seguimiento por IA, auditoría, búsqueda web y análisis de archivos **solo si** has configurado `OPENAI_API_KEY` y un modelo compatible.

## Qué NO incluye todavía

- Autenticación individual con usuarios y roles.
- Base de datos compartida en la nube ni expedientes persistentes por cliente.
- Verificación autónoma exhaustiva de todas las fuentes. Los resultados de IA deben revisarse.
- Deployment efectivo: este ZIP fue probado localmente y preparado para Vercel, pero no ha sido publicado en tu cuenta.

**Protección de datos:** el código compartido es una barrera básica de prototipo, no reemplaza una solución de identidad de producción. Para subir datos de clientes reales, revisa autorización, privacidad y controles de acceso.
