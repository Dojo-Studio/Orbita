# Cambios — DOJO ÓRBITA 4.1

- Corrección integral de los dos `502 RateLimitError` de las capturas (investigación e informe), además de examen IA, repreguntas y Prueba Ácida.
- Respuestas API estructuradas con código de error legible, indicación de reintento y paso siguiente; se conserva el estado del examen.
- Mensajes de error claros en cada etapa, sin simular investigación completada.
- Botón para comprobar que la API realmente funciona (a diferencia de una clave solo configurada).
- Un reintento breve opcional para saturación temporal; ninguno para falta de créditos/límites de gasto.
- Entradas y salidas de IA reducidas para moderar consumo; por defecto se propone `gpt-4.1-mini` cuando no se configuró un modelo explícito.
- Máximo cuatro repreguntas con IA por examen; seguimiento contextual local siempre disponible.
- Informe PDF actualizado para incluir la síntesis estratégica generada por IA cuando existe.
- Se mantienen las 12 dimensiones, las seis preguntas obligatorias de la Prueba Ácida, el diseño espacial y la compatibilidad con los avances V4 guardados en este navegador.
