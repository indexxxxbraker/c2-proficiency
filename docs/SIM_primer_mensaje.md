# Primer mensaje para la sesión de Claude Code (SIM-01)

Copiar y pegar tal cual al abrir la sesión sobre este repositorio:

---

Lee CLAUDE.md y docs/00_Pendientes.md. Vamos a producir el primer simulacro, SIM-01, nivel de examen.

Antes de generar nada:
1. Instala el entorno (requirements.txt, ffmpeg, poppler) y comprueba que `python3 src/gen_UOE-P3.py --demo /tmp/demo` produce un PDF con la maquetación correcta (renderízalo y míralo).
2. Lee la cabecera de cada generador que vayas a usar para conocer su spec y sus bloques para simulacros.
3. Haz una lista de los temas y textos ya usados en los archivos *_hojas.py y spk_specs.py, para no repetirlos.

Orden de trabajo, un paper por vez y con commit al cerrar cada uno:
- SIM-01_RUE.pdf (Parts 1–7). Specs en sim/SIM-01/specs_rue.py.
- SIM-01_WRT.pdf (Part 1 + Part 2 con tres tareas de géneros distintos). Specs en sim/SIM-01/specs_wrt.py.
- SIM-01_LST.pdf + .mp3 (Parts 1–4 con el guion completo del examen y el cierre). Specs en sim/SIM-01/specs_lst.py.
- SIM-01_SPK.pdf + .mp3 (test completo). Specs en sim/SIM-01/specs_spk.py.

Para cada paper: specs → verify() → PDF → resolución a ciegas por un agente independiente que solo recibe los enunciados → corrección de lo que difiera → render de todas las páginas y revisión visual → commit. En Listening, además, verificación del audio con el ASR por tramos.

Al terminar los cuatro, añade a docs/00_Pendientes.md la línea de SIM-01 (fecha, papers, léxico de la práctica que no está en ninguna teoría) y dame un resumen de cierre para el centro de mando: entregado, decisiones, qué debería heredar SIM-02.
