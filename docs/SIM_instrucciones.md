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
