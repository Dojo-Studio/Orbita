# Actualizar DOJO ÓRBITA a 4.1 SIN perder la URL

Tu URL actual es: https://orbita-dojo-studio.vercel.app/

## Método A — Vercel CLI (recomendado si el despliegue anterior fue por carga manual)

1. Descarga el ZIP `DOJO_ORBITA_41_LISTO_PARA_VERCEL.zip` y **descomprímelo**.
2. Abre Terminal en la carpeta del proyecto (donde están `server.py`, `index.html`, `vercel.json`).
3. Instala Vercel CLI si es necesario:

```bash
npm install -g vercel
vercel login
```

4. **Vincula el proyecto ya existente** (elige el equipo Dojo Studio y el proyecto `orbita`; NO crees otro):

```bash
vercel link
```

5. Publica la nueva versión:

```bash
vercel --prod
```

6. Abre la misma dirección `https://orbita-dojo-studio.vercel.app/` con recarga completa.

**Si Vercel pregunta si deseas vincular a un proyecto existente, responde que SÍ y selecciona `orbita`.**

## Método B — GitHub (si tu Vercel está conectado a un repositorio)

1. Descomprime el ZIP; no subas el ZIP cerrado al repositorio.
2. Actualiza los archivos de la raíz del repositorio (`index.html`, `server.py`, `requirements.txt`, `vercel.json`, `.python-version`, y documentos).
3. Haz commit y push a la rama que Vercel despliega en Production.
4. Comprueba en Vercel → Deployments → Production que el despliegue nuevo termine en **Ready**.

## Variables a conservar en el proyecto Vercel

En **Settings → Environment Variables**:

- `ORBITA_ACCESS_CODE`: contraseña que inventaste para acceso privado.
- `OPENAI_API_KEY`: secreto completo `sk-...` de OpenAI.
- `OPENAI_MODEL`: recomendado para esta versión `gpt-4.1-mini` si está disponible para tu proyecto. Si ya tienes otro modelo configurado, el código seguirá respetando ese valor.
- `ORBITA_RETRY_TRANSIENT`: opcional `1`.

Al actualizar el MISMO proyecto, las variables ya configuradas suelen conservarse. Si cambias alguna variable, vuelve a desplegar.

## Comprobar el despliegue

1. En la página debe aparecer `PRODUCT INTELLIGENCE / 4.1`.
2. Introduce tu código `ORBITA_ACCESS_CODE` y pulsa **Activar conexión**.
3. Pulsa **Comprobar la IA con una solicitud real**. Este botón consume una pequeña solicitud de API.
4. Si la IA responde, prueba investigación y análisis estratégico.
5. Si aparece un mensaje sobre saldo o límite, revisa `SOLUCION_ERROR_OPENAI.md`.
6. Comprueba que aún puedes completar un examen, la Prueba Ácida y exportar PDF aunque la IA falle.

## Nota importante sobre el uso público

Si desactivaste Vercel Authentication, el sitio está accesible al público. Eso no significa que los visitantes tengan permiso para usar tu API privada. Para IA pública sin contraseña hay que implementar autenticación/cotas de consumo con un backend seguro; no compartas la contraseña del equipo.

## ¿Qué hago si cambia la URL?

Es probable que hayas creado un proyecto nuevo por error. En Vercel selecciona el proyecto original `orbita` y vuelve a vincularlo con `vercel link` desde la carpeta correcta. El dominio se conserva en el proyecto original.
