# C2 Proficiency · material de preparación autónoma

*Self-study materials for the Cambridge C2 Proficiency exam: theory, practice sheets and full mock exams, with explanations in Spanish.*

Material completo para preparar por tu cuenta el **Cambridge C2 Proficiency** (antes CPE): teoría de cada parte del
examen, hojas de práctica con soluciones explicadas, audios de Listening y Speaking, y simulacros completos.
Las explicaciones están en español; todo el inglés, en inglés británico.

## Motivación

Creé este repositorio para preparar el C2 de forma independiente, sin academia, durante el curso 2026–2027.
Partiendo de un nivel C1, la idea era tener **todo el material listo antes de empezar a estudiar**, organizado
por partes del examen y con un criterio común, en lugar de ir acumulando apuntes y ejercicios sueltos.

Lo hago público porque puede servir a cualquiera que esté en la misma situación: alguien con un buen nivel de inglés
que quiere preparar el C2 por su cuenta y necesita material estructurado, con soluciones razonadas y no solo claves.

## Cómo se ha hecho

Todo el material lo ha escrito **Claude** (Anthropic), a través de Claude Code y claude.ai, bajo mi dirección:
yo he decidido la estructura, el alcance de cada parte y las reglas de calidad, y he revisado el resultado.

- El formato de cada tarea (número de ítems, extensión de los textos, tiempos, criterios de corrección) sigue el
  **handbook público de Cambridge** para el C2 Proficiency. Todos los textos, ítems y modelos son **originales**:
  no se reproduce ningún examen oficial.
- Los PDFs se generan con scripts en Python (ReportLab) a partir de especificaciones, con una plantilla visual común.
- Cada hoja pasa por varias comprobaciones antes de darse por buena: scripts que verifican el formato (recuento de
  palabras, numeración, palabra clave), **resolución a ciegas por un agente independiente** que no ve la clave, y,
  en Listening, transcripción automática del audio para detectar palabras que la voz sintética pronuncia mal.

Aun así puede haber errores. Si encuentras uno, abre un *issue*.

## Qué contiene

| Paper | Partes | Material |
|---|---|---|
| Reading and Use of English | 1–7 | Teoría de cada parte, hojas de práctica, léxico C2 (idioms, phrasal verbs, collocations, confusables, lenguaje argumentativo) |
| Writing | 1 (essay) y 2 (article, letter, report, review) | Teoría por género, rúbrica de autocorrección, modelos comentados criterio por criterio |
| Listening | 1–4 | Teoría y práctica con audio (PDF + MP3, con el guion y las pausas del examen) |
| Speaking | 1–3 | Teoría, rúbrica y tests completos con fotos y audio de examinador para practicar solo |
| Simulacros | Todo el examen | Exámenes completos, un PDF por paper, con hoja de respuestas y soluciones |

Estado actual: **16 teorías, 116 hojas de práctica y 22 audios** en `material/` (índice en
[`material/README.md`](material/README.md)), y los simulacros en `sim/` a medida que se terminan.

## Cómo usarlo

**Para estudiar:** abre los PDFs. Cada hoja tiene el ejercicio en formato de examen, una hoja de respuestas para
corregirte y, tras un salto de página, las soluciones: por qué la respuesta es la correcta, por qué fallan los
distractores y qué apartado de la teoría lo explica. En Listening, pon el MP3 sin pausarlo, como en el examen real.

**Para generar material nuevo:**

```bash
pip install -r requirements.txt          # y ffmpeg si vas a generar audio
python3 src/gen_UOE-P3.py --demo salida/  # hoja de ejemplo de Use of English Part 3
```

Cada generador documenta en su cabecera el formato de la especificación que recibe.

```
material/ teorías y hojas de práctica por paper (UOE, RDG, WRT, LST, SPK, LEX)
src/    generadores (uno por parte del examen), plantilla visual y motor de audio
fonts/  fuentes de la plantilla (Carlito, Caladea, Poppins)
sim/    simulacros completos
docs/   estado del proyecto y listas de trabajo
```

## Avisos

- **Material no oficial.** Este proyecto no está afiliado, patrocinado ni revisado por Cambridge University Press &
  Assessment. *Cambridge English* y *C2 Proficiency* son marcas de sus respectivos titulares y se citan solo para
  identificar el examen.
- **Audio sintético.** Las voces se generan con el servicio de lectura en voz alta de Microsoft a través de `edge-tts`.
  No transmiten la entonación como una persona, por eso ninguna respuesta depende solo del tono. El audio se ofrece
  para estudio personal y sin fines comerciales. Para acostumbrarte al audio real, completa la preparación con los
  tests oficiales.
- **Contenido generado con IA.** Está revisado con las comprobaciones descritas arriba, pero no sustituye al material
  oficial para calibrar tu nivel antes del examen.

## Licencias

- Código (`src/`): [MIT](LICENSE).
- Contenido educativo (textos, ejercicios, soluciones, PDFs): [CC BY 4.0](LICENSE-CONTENT.md), con las excepciones
  que se indican allí (audio y fotografías).
- Fuentes (`fonts/`): SIL Open Font License 1.1.
