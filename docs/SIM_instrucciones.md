# Instrucciones para producir un simulacro (SIM-NN)

Primer mensaje de cada sesión: «Lee docs/SIM_instrucciones.md y produce SIM-NN.»

## Antes de empezar
1. Lee `CLAUDE.md`, `docs/00_Pendientes.md` y `docs/SIM_temas.md` (temas ya usados: no se repiten).
2. Instala el entorno y comprueba la red hacia los cuatro dominios de `CLAUDE.md` (edge-tts, huggingface, Commons).
3. Mira cómo está hecho el simulacro anterior (`sim/SIM-(NN-1)/specs_*.py`) y reutiliza su estructura, no su contenido.

## Orden de trabajo (un commit al cerrar cada paper)
1. **RUE** — Parts 1–7. En la Part 4, ítems con pocas respuestas posibles; la clave recoge todas las aceptables.
2. **WRT** — Part 1 + Part 2 (tres géneros distintos). El revisor independiente comprueba la lógica de los modelos,
   no solo el inglés.
3. **LST** — Parts 1–4, por etapas (`--stage verify|audio|asr|pdf`). Reformula toda palabra que el ASR confunda.
4. **SPK** — **primero las fotos**: busca las cinco en Commons con licencia válida y escribe la Part 2 a partir de
   ellas, no al revés.

Montaje: `python3 src/gen_SIM.py [verify] rue|wrt|lst|spk sim/SIM-NN`.
Verificación de cada paper: la de `CLAUDE.md` (verify, resolución a ciegas, render de todas las páginas, ASR).

## Cierre
1. Añade los temas de SIM-NN a `docs/SIM_temas.md` y la línea de SIM-NN a `docs/00_Pendientes.md`
   (fecha, papers, léxico de la práctica que no está en ninguna teoría).
2. Abre un pull request a `main` y fusiónalo.
3. Da un resumen de cierre para el centro de mando: entregado, decisiones y qué debería heredar el siguiente simulacro.
   Si alguna lección vale para todos los simulacros, añádela también a este archivo.

## Lecciones de los simulacros anteriores
- **Material de práctica en `material/`.** Antes de cerrar, pasar las teorías por `pdftotext` y comprobar con script
  que el léxico «sin teoría» de `00_Pendientes.md` no aparece en ninguna (en SIM-02 sobraban 10 de 72) y que las
  frases de los ítems no copian sus ejemplos.
- **Paralelizar.** La síntesis del Listening (~5 min con la caché vacía) y el ASR de las cuatro partes (~10 min) van en
  segundo plano mientras se escribe el Speaking; los agentes de revisión, también en segundo plano.
- **Writing.** El revisor tiene que comprobar que el essay modelo no atribuye a un texto ideas que no dice (en SIM-02
  la postura final presentaba como «del texto 2» unas condiciones que eran del propio modelo) y que la propuesta de
  cada modelo de la Part 2 resuelve los problemas que el propio modelo plantea.
- **Part 4 del RUE.** El resolutor a ciegas encuentra casi siempre variantes defendibles (adverbios como [finally],
  sinónimos del adjetivo, perífrasis con [the one]): ampliar la clave con ellas es lo normal, no una excepción.
- **Listening.** Las diferencias de ortografía del ASR (realised/realized, any more/anymore, lamp post/lamppost) y los
  homófonos no piden cambios; sí las palabras que la voz deforma («you add up» → «you had up»): se reformulan.
  En la Part 4, que en uno o dos hablantes la respuesta de la Task Two llegue antes que la de la Task One.
- **Speaking.** Describir las fotos después de verlas a 960 px, no por la miniatura: los detalles cambian (de pie o
  sentada, lata o cartón de leche). Las reacciones del modelo tienen que ser coherentes entre sí a lo largo de la fase 2.
- **Commons.** Para ver candidatas, una sola consulta al API con varios títulos (`titles=A|B|C`, `iiurlwidth=330`).
  Los 429 pueden durar una hora (en SIM-02, de 20:30 a 21:30): no encadenar reintentos rápidos, que mantienen el
  límite; una consulta conjunta cada 5 minutos. Mientras tanto se puede sintetizar y comprobar el MP3 del Speaking,
  que no depende de las fotos. No usar `pkill -f` con un patrón que aparezca en la propia orden.
