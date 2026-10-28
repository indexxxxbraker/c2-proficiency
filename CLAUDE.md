# Proyecto C2 Proficiency · repositorio de generadores y simulacros

Material de preparación del Cambridge C2 Proficiency (examen previsto mayo/junio 2027) para Roberto.
Octubre–diciembre de 2026: producción de material. Desde enero de 2027: estudio con lo producido.
Todo el material de práctica (16 teorías, 116 hojas, 22 MP3) ya está hecho y vive en Google Drive (carpeta C2).
**Lo que se produce en este repositorio son los simulacros (SIM).**

## Estructura

```
src/      todos los generadores y módulos (carpeta plana: se importan entre sí por ruta)
fonts/    Carlito, Caladea y Poppins (c2_plantilla.py las busca aquí antes que en el sistema)
sim/      salida: una carpeta por simulacro (sim/SIM-01/, sim/SIM-02/, …)
docs/     00_Pendientes.md (estado y pendientes), LEX_entrada.md
```

Módulos en `src/`:
- `c2_plantilla.py` — plantilla visual. **No se modifica**: fuentes, colores y maquetación son fijos.
- `lst_audio.py` — motor de audio (edge-tts, guiones de Cambridge, caché, verificación con faster-whisper).
- `gen_UOE-P1..P4`, `gen_RDG-P5..P7`, `gen_WRT-P1..P2`, `gen_LST-P1..P4`, `gen_SPK` — un generador por parte.
  (Los generadores de LEX no están aquí: no hacen falta para los simulacros y siguen en el Project de claude.ai.)
  Cada uno expone bloques reutilizables para simulacros: `question_flowables`, `answer_sheet_flowables`,
  `solutions_flowables` (y `audio_events(standalone=False)` en Listening), más `verify()` y una hoja `--demo`.
  La cabecera de cada archivo documenta su `spec`. Léela antes de usarlo.
- `spk_specs.py` — contenido de los seis tests de Speaking ya entregados. El contenido del resto de hojas de práctica
  está en el `DEMO` de cada generador (una hoja) y en los PDFs de Drive. **Ni sus textos ni sus temas se reutilizan.**

## Entorno

```
pip install -r requirements.txt
apt-get install -y ffmpeg poppler-utils     # si faltan: ffmpeg para audio, pdftoppm para revisar PDFs
```
- ffmpeg siempre con `-nostdin`.
- Los generadores escriben por defecto en `/mnt/user-data/outputs` (ruta del contenedor de claude.ai): aquí se les
  pasa siempre la carpeta de salida (`sim/SIM-NN/`). La caché de audio se fija con `export LST_CACHE=$PWD/.cache/lst`.
- Si edge-tts falla con un error de certificado SSL, añadir el bundle del sistema al de certifi:
  `cat /etc/ssl/certs/ca-certificates.crt >> $(python3 -c "import certifi;print(certifi.where())")`
  (`lst_audio.setup()` ya lo hace). Si el entorno indica otro bundle del proxy (p. ej. `/root/.ccr/ca-bundle.crt`), añadir ese.
- El ASR (faster-whisper, modelo small.en) tarda 20–30 s por tramo con el modelo en caché.

## Simulacros: qué se produce

Seis simulacros, SIM-01 a SIM-06. Cada uno tiene cuatro papers, cada paper un PDF (y MP3 donde hay audio):

| Archivo | Contenido | Generadores |
|---|---|---|
| `SIM-NN_RUE.pdf` | Reading and Use of English: Parts 1–7, 53 ítems, 90 min | gen_UOE-P1..P4, gen_RDG-P5..P7 |
| `SIM-NN_WRT.pdf` | Writing: Part 1 (essay) + Part 2 (tres tareas a elegir, géneros distintos) | gen_WRT-P1, gen_WRT-P2 |
| `SIM-NN_LST.pdf` + `.mp3` | Listening: Parts 1–4, 30 ítems; audio completo con pausas de examen y cierre | gen_LST-P1..P4, lst_audio |
| `SIM-NN_SPK.pdf` + `.mp3` | Speaking: test completo con fotos y MP3 de examinador | gen_SPK |

Cada PDF: portada con instrucciones y tiempos → enunciados → salto de página → hoja de respuestas → soluciones
(con explicación, por qué falla cada distractor, y remisión a la teoría; en Writing y Speaking, modelos y rúbrica).
Cabecera y pie con `build(path, story, "SIM-NN · Reading and Use of English", "SIM-NN_RUE.pdf")`.
Los specs de cada simulacro se guardan en `sim/SIM-NN/specs_*.py` para poder regenerar y corregir.

Dificultad: SIM-01 y 02 nivel de examen; SIM-03 a 06 nivel de examen alto, sin pasarse.
Formato por parte, según el handbook oficial y las hojas ya hechas: P5 texto de 750–850 palabras; P6 texto base
de 600–720 palabras + 8 párrafos de 40–70; P7 unas 720 palabras en 4–6 secciones; Writing P1 dos textos de
90–110 palabras; Listening P4 cinco monólogos de unos 35 segundos.

## Reglas (las mismas que en todo el proyecto)

- **Contenido nuevo.** Ningún simulacro reutiliza textos, temas, ítems ni fotos de las hojas de práctica ni de otros simulacros.
  Tampoco el tema del sample test oficial (normas sociales e individualidad en Writing P1).
- **Explicaciones en español; todo el inglés en inglés británico** y con el estilo `en` (serif) de la plantilla.
- **Clave.** Opción múltiple y emparejamiento: una sola respuesta correcta. Respuesta abierta (P2, P3, P4, Listening P2):
  la clave recoge todas las respuestas aceptables y ninguna respuesta fuera de la clave es defendible.
- **Part 4:** si la frase 1 lleva *very*, la respuesta necesita un intensificador para el segundo punto, salvo que la
  palabra clave ya sea extrema. Se aceptan las variantes que aceptaría Cambridge (though/although, etc.).
- **Listening:** las preguntas de actitud se deducen de una frase concreta, nunca solo de la entonación. Narrador fijo
  (Thomas, GB), voces sin repetir dentro de un paper, pausas del guion de Cambridge. Revisar las diferencias que marque
  el ASR y reformular las palabras que la voz sintética deforma.
- **Speaking:** fotos de Wikimedia Commons con licencia libre (dominio público, CC0 o CC BY sin SA), con atribución.
- **Las frases de los ítems no copian los ejemplos de las teorías.**
- **Nada de documentos que comentan otros documentos.** Un simulacro es autocontenido.

## Verificación obligatoria antes de dar un paper por terminado

1. `verify()` de cada generador sin errores; recuento de palabras y formato comprobados con script.
2. **Resolución a ciegas por un agente independiente** que solo recibe los enunciados (sin clave ni soluciones).
   Cada ítem en que su respuesta difiera de la clave se revisa y se corrige o se amplía la clave. Para Writing y
   Speaking, el agente revisa el inglés de modelos y enunciados.
3. Renderizar el PDF (`pdftoppm -r 60 -png`) y mirar todas las páginas: títulos huérfanos, tablas partidas, restos de marcado.
4. En Listening, escuchar por tramos con el ASR y comprobar la duración total (unos 40 min con pausas).

## Repositorio público

El repositorio es público (código MIT, contenido CC BY 4.0, ver `LICENSE-CONTENT.md`). Por eso:
- La portada de cada PDF de simulacro incluye, en letra pequeña: «Material no oficial, sin afiliación con Cambridge
  University Press & Assessment. Audio con voces sintéticas.» (en la portada, no en la plantilla, que no se toca).
- Los MP3 se hacen commit **solo en su versión final**: cada versión intermedia quedaría para siempre en el historial.
- Nada de datos personales en los archivos ni en los commits.

## Entrega

Los PDFs y MP3 terminados van a `sim/SIM-NN/` y se hacen commit. Roberto los sube a Drive (carpeta 07_Simulacros).
Al cerrar cada simulacro, añadir en `docs/00_Pendientes.md` una línea con lo entregado y el léxico de la práctica que
no está en ninguna teoría (para las v2 de LEX).

Si una teoría tiene que cambiar de numeración, no se hace aquí: se anota como pendiente y se respeta la v1.
