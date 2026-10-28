# spk_specs.py · Contenido de SPK_Practica_01 a 06 (proyecto C2 Proficiency, modulo 09 SPK)
#
# Este archivo es la fuente de las seis hojas de Speaking: preguntas, fotos, intervenciones del companero sintetico,
# tarjetas, long turns modelo, comentarios y soluciones. El PDF y el MP3 de cada hoja se generan a partir de aqui con
# gen_SPK.py (que necesita c2_plantilla.py y lst_audio.py en la misma carpeta).
#
# CORREGIR UNA HOJA
#   1. Editar el texto en el SPEC correspondiente (SPEC01 ... SPEC06). El formato de cada campo esta documentado en
#      la cabecera de gen_SPK.py; marcado en los campos en espanol: [[ingles]] · [[!negrita]] · [[/cursiva]].
#   2. Regenerar solo esa hoja:   python3 gen_SPK.py spk_specs.py carpeta_salida 03
#      (sin numero, genera las seis). Hace falta internet: las fotos se descargan de Wikimedia Commons y se vuelve
#      a comprobar su licencia; las voces se sintetizan con edge-tts. Unos 2-4 minutos por hoja.
#   3. La verificacion es automatica y bloquea la salida si algo falla: 250-320 palabras por long turn, 60/180 s en
#      las fases de la Part 2, reconocimiento de voz de cada linea del MP3, licencias, ortografia britanica,
#      referencias a SPK_Teoria_v1 y restos de marcado en el PDF.
#   4. Si cambia el texto que se oye (preguntas, companero, instrucciones), cambia el MP3: hay que sustituir los dos
#      archivos, PDF y MP3, aunque el error solo estuviera en uno.
#   5. Una correccion sustituye a la hoja publicada con el mismo nombre (sin versiones: SPK_Practica_03 sigue
#      siendo SPK_Practica_03).

SPEC01 = {
    "num": "01", "level": 1,
    "subtitle": "Hoja 01 · Part 2: implicarse en la comunidad · Part 3: aprender · dificultad 1 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "How do you usually spend your weekends?",
         "model": "It depends a lot on the time of year, to be honest. During term I tend to spend Saturday "
                  "catching up on work, but I always keep Sunday free — usually for a long walk or lunch with "
                  "friends. I suppose I’ve learnt that if I don’t protect one day, the whole week starts to blur."},
        {"q": "Is there anything you would like to learn to do in the next few years?",
         "model": "I’d love to learn to sail properly. I’ve been out on boats a few times, but always as a "
                  "passenger, and there’s something appealing about a skill where the weather has the final say. "
                  "Whether I’ll actually find the time is another matter."},
        {"q": "How important is it for you to live near your family?",
         "model": "More important than I used to think. When I was younger I couldn’t wait to move away, but "
                  "living on my own made me realise how much I rely on being able to drop in on my parents "
                  "without planning it weeks in advance."},
    ]},
    "p2": {
        "title": "Council leaflet – Get involved",
        "intro": "people taking part in activities in their local community",
        "q1_pics": ["A", "C"],
        "q1": "what the people might be getting out of these activities",
        "context": "I'd like you to imagine that a town council is producing a leaflet to encourage residents to "
                   "take a more active part in their local community. These pictures will be used in the leaflet.",
        "task": "Talk together about what each of these activities might offer the people who take part. Then "
                "decide which picture would work best on the cover of the leaflet.",
        "partner_voice": "Ryan",
        "photos": [
            {"letter": "A", "file": "File:Reading Repair Cafe - DIY workshop.jpg",
             "what": "Un repair café: vecinos de varias edades arreglando aparatos en una mesa común.",
             "spec": "Que van tanto por la compañía como por el aparato; que alguno es jubilado y comparte un oficio; "
                     "que les une no tirar cosas.",
             "offers": "Una habilidad práctica, ahorro y menos residuos, pero sobre todo conversación: es una excusa "
                       "para encontrarse.",
             "decision": "A favor: gente corriente, sociable y algo inesperado. En contra: quizá haya que explicar "
                         "qué es un repair café."},
            {"letter": "B", "file": "File:Alameda Food Bank Thanksgiving volunteers 111119-G-FY356-017.jpg",
             "what": "Una adolescente clasifica donaciones de comida en un almacén.",
             "spec": "—",
             "offers": "Sentido de utilidad inmediata: ayudar a quien lo necesita.",
             "decision": "A favor: el valor social es evidente. En contra: puede sonar a obligación seria, y una "
                         "portada triste no anima a nadie."},
            {"letter": "C", "file": "File:A girl scout volunteer shows her pride in planting this tree.jpg",
             "what": "Una chica sonríe junto al árbol que acaba de plantar; al fondo, más voluntarios.",
             "spec": "Que está orgullosa de algo que la sobrevivirá; que quizá vino con su grupo y no por iniciativa "
                     "propia; que lo importante es el resultado visible.",
             "offers": "Dejar algo que dura, estar al aire libre, un resultado que se ve.",
             "decision": "A favor: alegre, sencilla, se entiende sin texto. En contra: es la imagen más previsible."},
            {"letter": "D", "file": "File:Beach Clean-up Day in Ha Long Bay (31433196023).jpg",
             "what": "Un grupo con chaquetas iguales recoge basura en una playa.",
             "spec": "—",
             "offers": "Trabajo en equipo y un antes y un después muy visible.",
             "decision": "A favor: muestra gente trabajando junta. En contra: no todos los pueblos tienen playa y el "
                         "uniforme parece de empresa."},
        ],
        "phase1_lines": [
            "What strikes me about the girl is how proud she looks — I’d hazard a guess it’s the first tree she’s "
            "ever planted.",
            "I get the impression the people in the repair café are there as much for the company as for the "
            "toasters.",
        ],
        "decision": "La A, si el criterio es que el lector piense «yo podría hacer eso» y vea que implicarse es "
                    "sociable; la C, si se prefiere una portada que se entienda de un vistazo. Una salida negociada: "
                    "una en la portada y la otra dentro.",
        "language": ["It depends what the leaflet is trying to achieve.", "This one would make people think, ‘I "
                     "could do that’.", "B and D both show …, whereas …", "If we had to settle on one, …"],
        "partner": [
            {"text": "For me, the girl planting the tree looks genuinely proud of herself. I suspect it’s less about "
                     "the environment than the feeling of having made something that will outlast her. The repair "
                     "café’s different, though. I’d say most of those people are there for the company.",
             "provokes": "Una idea interesante que conviene recoger con sus palabras y llevar más lejos.",
             "react": "That’s a nice way of putting it — ‘something that will outlast her’. And I suppose the repair "
                      "café is the same idea in a way: fixing a toaster is really an excuse to talk.",
             "theory": ["6.2"]},
            {"text": "I think the food bank picture is the obvious one for the cover. It shows people helping those "
                     "who really need it, and surely that’s what community is all about.",
             "provokes": "Una propuesta razonable: concede antes de objetar.",
             "react": "I’ll grant that it’s the most worthy of the four, but a leaflet like this needs to make "
                      "people think ‘I could do that’, and a food bank might feel like quite a commitment.",
             "theory": ["6.3"]},
            {"text": "Honestly, if everyone spent one Saturday a month on a beach like that, we’d solve half the "
                     "world’s problems within a year. That’s the picture that could change everything!",
             "provokes": "Una exageración entusiasta: modérala sin desanimar.",
             "react": "Let’s not get carried away — it’s a council leaflet, not a manifesto. Though I’ll give them "
                      "that: the people on that beach do look as if they’re enjoying themselves.",
             "theory": ["6.4", "6.3"]},
            {"text": "So, if I’ve understood you, you’re saying volunteering is really just a hobby for people with "
                     "too much time on their hands?",
             "provokes": "Una lectura deformada de lo que has dicho: recházala y aclara.",
             "react": "Nothing of the sort! My point was that people get something out of it themselves — and "
                      "that’s exactly what the leaflet should show.",
             "theory": ["6.3", "6.4"]},
            {"text": "Right, we need to decide. Shall we just go with the girl and the tree? It’s cheerful, and "
                     "everyone likes trees.",
             "provokes": "Una propuesta de cierre: acepta, negocia o cierra el desacuerdo, pero decidid.",
             "react": "I’ll drink to that — although if we want people to see that it’s sociable, the repair café "
                      "might do the job better. Could we put one on the cover and the other inside?",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "learning",
        "cards": [
            {"q": "What makes some things easier to learn than others?",
             "ideas": ["motivation", "feedback", "age"],
             "plan": {
                 "Operación": "[[What makes]]: causas, jerarquizadas (§3.1).",
                 "Postura": "La facilidad depende menos de la materia que de las condiciones en que se aprende.",
                 "Línea 1": "La rapidez con que sabes si lo haces bien ([[feedback]]).",
                 "Línea 2": "Las ganas: lo que te importa se aprende antes ([[motivation]]). Menos evidente y más "
                            "importante.",
                 "Contrapunto": "La edad influye, pero la exageramos porque nos sirve de excusa ([[age]]).",
                 "Cierre": "La dificultad no está fijada del todo: se puede crear el feedback y la razón para "
                           "insistir (idea propia)."},
             "model": [
                 "Well, the obvious answer is that some things are simply harder than others — quantum physics is "
                 "harder than making toast. But I don’t think that’s the interesting part of the question. The "
                 "way I see it, how easy something is to learn depends less on the thing itself than on the "
                 "conditions you learn it in.",
                 "Take feedback, for a start. When you’re learning to ride a bike, you know within a second whether "
                 "you’ve got it right, because you fall off. Compare that with learning to write well, or to invest "
                 "sensibly, where you might not find out for months — or years — whether what you did was any "
                 "good. The faster and clearer the feedback, the quicker we learn, and I’d say that explains a "
                 "great deal.",
                 "Then there’s motivation, which is probably the more important factor. Children pick up the rules "
                 "of a game in minutes but struggle with fractions for weeks, and it’s not because games are "
                 "simpler. It’s because they want to play. If something matters to you, you put up with the "
                 "frustration that learning always involves.",
                 "Admittedly, age plays a part as well. Most adults will never lose their accent in a foreign "
                 "language, and some physical skills really are easier to acquire when you’re young. But I think we "
                 "tend to exaggerate this, partly because it gives us a convenient excuse. It’s much easier to say ‘I’m "
                 "too old for this’ than ‘I don’t really want to’.",
                 "So, to come back to the question, I’d say difficulty isn’t entirely fixed. If you can find a way "
                 "of getting quick feedback and a reason to care, even quite demanding things become a lot more "
                 "manageable.",
             ],
             "comments": [
                 "Descarta la respuesta fácil con humor y adelanta la postura. [[Well]] (§4.3), [[The way I see "
                 "it]] (§4.2), [[depends less on … than on …]] (§4.6).",
                 "Primera línea: afirma, ilustra con dos casos opuestos y saca la regla (§3.4). [[Take …, for a "
                 "start]] (§4.2), correlativa [[The faster …, the quicker …]] (§4.6).",
                 "Segunda línea, jerarquizada (§3.3): [[probably the more important factor]]. Escindida [[It’s "
                 "not because …; it’s because …]] (§4.6) y caso cotidiano.",
                 "Contrapunto con la tercera idea de la tarjeta: concede y limita. [[Admittedly]] (§4.3), "
                 "[[we tend to exaggerate this]].",
                 "Cierre que vuelve a la pregunta con una idea propia: la dificultad se puede modificar. [[to come "
                 "back to the question]] (§4.2).",
             ],
             "follow_up": {"q": "Is it better to learn something on your own or with a teacher?",
                           "ideas": "Depende de la fase: al principio, un profesor da el feedback rápido del que "
                                    "hablaba la tarjeta; más adelante, aprender solo obliga a ser autónomo. "
                                    "Enlaza con el long turn sin repetirlo: [[That ties in with what I said about "
                                    "feedback …]]"}},
            {"q": "How important is it for people to go on learning throughout their lives?",
             "ideas": ["work", "health", "curiosity"],
             "plan": {
                 "Operación": "[[How important]]: graduar y decir de qué depende (§3.1).",
                 "Postura": "Muy importante, pero no en el sentido de cursos y títulos.",
                 "Línea 1": "La razón económica: los trabajos cambian y lo aprendido caduca ([[work]]).",
                 "Línea 2": "La mente: mantenerse ágil y, sobre todo, no volverse rígido ([[health]], [[curiosity]]).",
                 "Contrapunto": "La presión por mejorar sin descanso agota; estar satisfecho no es fracasar.",
                 "Cierre": "Importa como actitud, no como obligación (idea propia)."},
             "model": [
                 "I’d say it’s very important — though perhaps not in the way the question is usually meant. When "
                 "people talk about lifelong learning, they tend to mean courses and qualifications, and I think "
                 "that’s only a small part of it. Learning, to my mind, is a much broader habit than that.",
                 "The most obvious argument is the economic one. Very few people now do the same job for forty "
                 "years, and even if they do, the job itself changes beyond recognition. Someone who stopped "
                 "learning at twenty-two would be struggling by thirty-five, simply because the tools and the "
                 "expectations would have moved on without them. So in that sense, it isn’t really optional any "
                 "more.",
                 "But I think the more interesting argument has to do with the mind rather than the job. As far as "
                 "I know, there’s quite a lot of evidence that people who keep learning — a language, an "
                 "instrument, whatever it happens to be — stay mentally sharper for longer. And it’s not just a "
                 "question of memory. Learning something new forces you to be a beginner again, which is "
                 "uncomfortable, but it also stops you from becoming rigid in your views.",
                 "That said, I’m a bit wary of turning this into an obligation. There’s a certain kind of pressure "
                 "these days to be constantly improving yourself, and it can be exhausting. Someone who’s content "
                 "with the life they have isn’t necessarily failing at anything, and not everyone wants to spend "
                 "their evenings acquiring new skills.",
                 "So, all things considered, I’d say it matters enormously — but as an attitude rather than a duty. "
                 "Curiosity is worth keeping; a constant sense that you’re falling behind probably isn’t.",
             ],
             "comments": [
                 "Responde en la primera frase y redefine la pregunta: la postura ya está dentro (§3.2).",
                 "Primera línea, desarrollada con una hipótesis concreta. [[The most obvious argument is]] (§4.2), "
                 "condicional [[would be struggling … would have moved on]] (§4.6).",
                 "Segunda línea, de otra naturaleza y jerarquizada. Atenuación [[As far as I know]] para un dato "
                 "que no se puede comprobar (§4.6); [[it’s not just a question of …]] (§4.2).",
                 "Contrapunto que matiza la propia postura. [[That said]] (§4.2), [[I’m a bit wary of]].",
                 "Cierre con una oposición nítida. [[all things considered]] (§4.2), [[as an attitude rather than a "
                 "duty]], elipsis final [[probably isn’t]] (§4.5).",
             ],
             "follow_up": {"q": "Do you think older people are given enough opportunities to learn new things?",
                           "ideas": "Ofertas hay (universidades de mayores, cursos municipales), pero la "
                                    "tecnología se diseña pensando en los jóvenes y el prejuicio de que «ya no "
                                    "están para eso» pesa más que la falta de cursos."}},
        ],
        "discussion": [
            {"q": "Do you think schools today prepare young people well for adult life?", "theory": ['6.7'],
             "ideas": "Bien en contenidos, peor en lo práctico (finanzas personales, gestionar el tiempo) y en "
                      "tolerar el error.",
             "lang": "They’re good at teaching facts, but rather less good at teaching people what to do when "
                     "they don’t know the answer."},
            {"q": "Some people say we learn more from our failures than from our successes. How far do you agree?", "theory": ['6.7', '6.3'],
             "ideas": "Solo si el fracaso se analiza; si no, solo deja miedo. El éxito también enseña, pero invita "
                      "menos a pensar.",
             "lang": "Up to a point — failure only teaches you something if you’re prepared to look at it honestly."},
            {"q": "Can you really learn something properly from a screen?", "theory": ['4.3'],
             "ideas": "Conocimientos, sí; destrezas físicas y criterio, peor. Lo que falta es el feedback de otra "
                      "persona y la presión de estar presente.",
             "lang": "It depends what you mean by ‘properly’. You can learn the facts, but judgement is another "
                     "matter."},
            {"q": "How has the internet changed what people need to know?", "theory": ['4.3'],
             "ideas": "Menos memorizar datos y más saber evaluar fuentes; paradoja: cuanto más accesible es la "
                      "información, más hace falta saber para distinguirla.",
             "lang": "If anything, it’s made knowledge more important, not less — you need to know enough to "
                     "spot nonsense."},
            {"q": "Why do you think some people stop wanting to learn new things as they get older?", "theory": ['4.6'],
             "ideas": "Miedo a hacer el ridículo como principiante, falta de tiempo, una identidad ya cerrada; no es "
                      "tanto la capacidad como el orgullo.",
             "lang": "I suspect it’s less a question of ability than of pride: nobody enjoys being a beginner at "
                     "fifty."},
            {"q": "Is there anything that can’t be taught?", "theory": ['4.6'],
             "ideas": "Se pueden enseñar técnicas, no el deseo de usarlas: la curiosidad, el gusto o la empatía se "
                      "contagian más que se enseñan.",
             "lang": "You can teach someone how to do almost anything, but not, I think, to want to do it."},
        ],
    },
    "lex": ["outlast", "put up with", "beyond recognition", "be wary of", "drop in on", "have the final say",
            "a convenient excuse", "lifelong learning", "spot nonsense", "a manifesto"],
}

SPEC02 = {
    "num": "02", "level": 2,
    "subtitle": "Hoja 02 · Part 2: la vida local · Part 3: el tiempo libre y el trabajo · dificultad 2 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "What kind of things do you like to read in your spare time?",
         "model": "Mostly non-fiction, oddly enough — history and popular science. I read so much for my degree "
                  "that novels tend to feel like more work, whereas a good history book is pure escape. I do try "
                  "to read one novel a month, though, just so I don’t forget how."},
        {"q": "Do you prefer to plan your free time or to see what happens?",
         "model": "I’m a planner by nature, I’m afraid. If I leave a Saturday completely open, I usually end up "
                  "wasting it. Mind you, some of the best evenings I can remember were the ones nobody had "
                  "planned, so I’m trying to leave a bit more to chance."},
        {"q": "Which place that you have visited would you most like to go back to?",
         "model": "Probably Lisbon. I was only there for a long weekend, so it’s all a bit of a blur, but I "
                  "remember thinking it was the first city I’d visited where I could genuinely imagine living. "
                  "I’d like to go back and find out whether that was just the sunshine talking."},
    ]},
    "p2": {
        "title": "Travel brochure – Local life",
        "intro": "everyday life in different places",
        "q1_pics": ["A", "D"],
        "q1": "what these pictures suggest about everyday life in the places where they were taken",
        "context": "I'd like you to imagine that a travel company is producing a brochure for people who want to "
                   "experience local life rather than famous tourist sights.",
        "task": "Talk together about how well each of these pictures reflects that idea. Then decide which two "
                "pictures should be used in the brochure.",
        "partner_voice": "Connor",
        "photos": [
            {"letter": "A", "file": "File:Fishermen mending their nets, Essaouira, 2008.jpg",
             "what": "Pescadores sentados en el suelo de un puerto, cosiendo redes.",
             "spec": "Que es trabajo de todos los días, no un espectáculo; que lo hacen juntos y charlando; que el "
                     "oficio pasa de unos a otros.",
             "offers": "Autenticidad: un oficio real que no se representa para nadie.",
             "decision": "A favor: lo más genuino de las cinco. En contra: el visitante solo puede mirar; ¿qué "
                         "experiencia le ofrece?"},
            {"letter": "B", "file": "File:Market vendor with fresh vegetables.jpg",
             "what": "Una vendedora en su puesto de verduras en un mercado al aire libre.",
             "spec": "—",
             "offers": "La vida cotidiana que todo el mundo comparte: comprar, comer, regatear.",
             "decision": "A favor: el visitante puede participar, no solo mirar. En contra: casi demasiado común."},
            {"letter": "C", "file": "File:Children Ceremonial dance, Koo Festival.jpg",
             "what": "Niños con trajes a juego bailan en una fiesta; detrás, el público.",
             "spec": "—",
             "offers": "Color, energía y cultura propia.",
             "decision": "A favor: la más llamativa. En contra: es un día de fiesta, no la vida diaria; puede vender "
                         "folclore como si fuera lo cotidiano."},
            {"letter": "D", "file": "File:Singer street music in Olinda.jpg",
             "what": "Un músico canta y toca en una calle; detrás, un hombre en silla de ruedas y una paseante.",
             "spec": "Que es un sitio habitual para él; que el hombre de detrás es un vecino, no un turista; que la "
                     "calle es también lugar de reunión.",
             "offers": "La calle como espacio de encuentro, con música que no está en ningún programa.",
             "decision": "A favor: espontánea y cercana. En contra: ambigua; puede leerse como un espectáculo "
                         "para turistas."},
            {"letter": "E", "file": "File:Visitors of the Louvre taking photographs of Mona Lisa (1325512 1920).jpg",
             "what": "Una multitud fotografía la Mona Lisa con el móvil.",
             "spec": "—",
             "offers": "Justo lo contrario de lo que promete el folleto: el turismo de monumento y multitud.",
             "decision": "Solo serviría como contraste («lo que no verás»), y es arriesgado abrir un folleto con lo "
                         "que no se ofrece."},
        ],
        "phase1_lines": [
            "Picture A looks as though it could have been taken on any day of the week — there’s nothing staged "
            "about it.",
            "I’d hazard a guess the man in the wheelchair is a regular, which makes me think the musician plays "
            "there for the neighbours rather than for visitors.",
        ],
        "decision": "B y A si el criterio es la vida diaria auténtica; B y D si se quiere algo en lo que el "
                    "visitante pueda participar. C es la tentación (la más vistosa) y E solo serviría como "
                    "contraste.",
        "language": ["It depends whether the brochure is selling things to watch or things to do.",
                     "It’s striking, but it’s a festival, not everyday life.", "A and B have that in common, "
                     "whereas …", "So we’re agreed on B; it’s the second one we need to settle."],
        "partner": [
            {"text": "I think picture A says far more about everyday life. Mending nets isn’t a show — it’s just work "
                     "that has to be done. The musician I’m less sure about. He might well be playing for the "
                     "tourists rather than for the locals.",
             "provokes": "Una lectura discutible de la foto D: recógela y especula con otro detalle.",
             "react": "You may be right, although the man in the wheelchair behind him doesn’t look like a tourist. "
                      "I’d hazard a guess this is a regular spot.",
             "theory": ["6.2", "5.2"]},
            {"text": "What about the dancers, though? It’s colourful, it’s full of energy — that’s exactly what "
                     "people imagine when they think of local culture.",
             "provokes": "Una foto atractiva pero discutible para el criterio: concede su mérito y objeta.",
             "react": "I’ll give them that — it’s by far the most striking. But it’s a festival, not everyday life, "
                      "so it might give visitors the wrong idea.",
             "theory": ["6.3"]},
            {"text": "You know what I’d do? I’d put the Mona Lisa crowd on the very first page, with a big red cross "
                     "through it. It would say everything about the trip in one picture!",
             "provokes": "Una idea ingeniosa pero exagerada: concede lo que tiene de bueno y modérala.",
             "react": "I’ll grant you that it would make the point — but let’s not get carried away. A brochure "
                      "that opens with what you won’t see is a risky way to sell a holiday.",
             "theory": ["6.3", "6.4"]},
            {"text": "So, if I’ve understood you correctly, you think tourists shouldn’t bother visiting famous "
                     "places at all? Not even once?",
             "provokes": "Una generalización que no has hecho: recházala y vuelve al criterio de la tarea.",
             "react": "Nothing of the sort. I’m only saying that this brochure is aimed at people who want "
                      "something else.",
             "theory": ["6.3", "6.4"]},
            {"text": "OK, I think we’re nearly out of time. I’d go for the market and the dancers. Shall we agree on "
                     "that?",
             "provokes": "Una propuesta a medias aceptable: acepta una parte y negocia o cierra la otra.",
             "react": "The market, yes — I’ll drink to that. The dancers I’m less sure about, so we may have to "
                      "differ on the second one, but if we had to settle, I’d go for the fishermen.",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "time",
        "cards": [
            {"q": "How has technology changed the way people use their free time?",
             "ideas": ["communication", "entertainment", "rest"],
             "plan": {
                 "Operación": "[[How has … changed]]: efectos de distinto signo (§3.1).",
                 "Postura": "Más que cambiar lo que hacemos, ha cambiado la textura del tiempo libre: llega en "
                            "fragmentos y siempre hay algo con qué llenarlos.",
                 "Línea 1": "El entretenimiento infinito: nunca hay un momento vacío ([[entertainment]], "
                            "[[rest]]).",
                 "Línea 2": "La comunicación, con dos caras: cercanía y disponibilidad permanente "
                            "([[communication]]).",
                 "Contrapunto": "También abre posibilidades: aprender, encontrar aficiones minoritarias.",
                 "Cierre": "No ha reducido el tiempo libre: lo ha llenado; el reto es dejar parte vacía (idea "
                           "propia)."},
             "model": [
                 "I think the biggest change isn’t so much in what we do with our free time as in its texture, if "
                 "that makes sense. Free time used to come in blocks — an evening, a Sunday afternoon — and now it "
                 "tends to come in fragments, because there’s always something to fill even the smallest gap.",
                 "Take entertainment, for a start. A generation ago, if there was nothing good on television, you "
                 "got bored and went for a walk, or read a book, or rang a friend. Now the supply is effectively "
                 "infinite. You can watch, listen to or scroll through something at any moment, and the result, "
                 "I’d say, is that we rarely experience a moment that’s genuinely empty. And boredom, which used to push "
                 "people into doing something creative, has almost disappeared.",
                 "Communication has changed things too, though in a more mixed way. On the one hand, it’s never "
                 "been easier to keep in touch with friends who live in another city or another country. On the "
                 "other, being permanently reachable means that free time is never entirely free. There’s always a "
                 "message to answer or a group chat to keep up with, and that can start to feel like a second "
                 "job.",
                 "Admittedly, it would be unfair to make it all sound negative. People now learn the guitar from "
                 "online videos or find others who share some obscure hobby, which simply wasn’t possible before. In that sense, "
                 "technology has widened our options enormously.",
                 "So, on balance, I’d say technology hasn’t really reduced our free time; it has filled it. And "
                 "perhaps the real challenge now is to leave some of it deliberately empty.",
             ],
             "comments": [
                 "Redefine la pregunta con una imagen propia (bloques frente a fragmentos) que sostiene todo el "
                 "long turn. [[isn’t so much … as …]] (§4.6), [[if that makes sense]] (§4.4).",
                 "Primera línea con un contraste antes y ahora (§3.5, perspectiva del tiempo). [[Take …, for a "
                 "start]] (§4.2), [[effectively infinite]], inciso [[I’d say]] (§4.6).",
                 "Segunda línea, con efectos de signo opuesto. [[On the one hand … On the other …]] y juego de "
                 "palabras [[free time is never entirely free]] (§4.1: detalle y flexibilidad).",
                 "Contrapunto que corrige el tono del propio discurso. [[Admittedly]] (§4.3), [[some obscure "
                 "hobby]].",
                 "Cierre con la idea propia en forma de paradoja. [[on balance]] (§4.2), [[hasn’t … reduced …; it "
                 "has filled it]] (§4.5, elipsis).",
             ],
             "follow_up": {"q": "Do you think people today are worse at doing nothing than they used to be?",
                           "ideas": "Probablemente sí: el aburrimiento se ha vuelto evitable, así que no se practica. "
                                    "Retoma la idea del long turn sin repetirla: [[It comes back to that idea of "
                                    "empty time …]]"}},
            {"q": "Why do some people find it hard to switch off from work?",
             "ideas": ["ambition", "technology", "expectations"],
             "plan": {
                 "Operación": "[[Why]]: causas, jerarquizadas (§3.1).",
                 "Postura": "Porque el trabajo ha perdido sus paredes: el límite ya no viene dado, hay que "
                            "construirlo.",
                 "Línea 1": "La tecnología lo hace posible: el mismo móvil para todo ([[technology]]).",
                 "Línea 2": "Las expectativas lo explican: la cultura del compromiso y la identidad ligada al "
                            "trabajo ([[expectations]], [[ambition]]). Más importante.",
                 "Contrapunto": "No siempre es un problema: a quien le apasiona su trabajo le cuesta desconectar "
                                "y no sufre.",
                 "Cierre": "El interruptor ya no viene de serie; hay que instalarlo y eso exige disciplina (idea "
                           "propia)."},
             "model": [
                 "I suppose the simplest answer is that work used to have walls and now it doesn’t. When my "
                 "grandparents finished a shift, the work stayed in the factory or the office. Today, for a lot of "
                 "people, it follows them home in their pocket.",
                 "That’s the technological side of it, and I think it’s the most obvious factor. If your emails "
                 "arrive on the same device you use to talk to your friends, there’s no clear moment when work "
                 "ends. You check your phone for something else entirely, and suddenly you’re thinking about a "
                 "meeting you’ve got on Monday. The boundary simply isn’t there any more.",
                 "But technology only makes it possible; it doesn’t explain why people actually do it. For that, I "
                 "think you have to look at expectations — both other people’s and our own. In a lot of workplaces "
                 "there’s an unspoken assumption that the committed employee is the one who answers at ten at "
                 "night. And for many people, their job has become a large part of who they are, so stepping away "
                 "from it can feel almost like losing a bit of themselves.",
                 "Mind you, I’m not sure it’s always a problem. Some people find it hard to switch off because they "
                 "genuinely love what they do, and for them the line between work and pleasure is quite blurred, "
                 "in a good way. Telling them to switch off would be a bit like telling a musician to stop humming.",
                 "So, to come back to the question, I’d say people find it hard because the off switch is no longer "
                 "built into the day. If you want one, you have to build it yourself — and that takes a surprising "
                 "amount of discipline.",
             ],
             "comments": [
                 "Apertura con una metáfora que adelanta la postura y un contraste con el pasado (§3.5).",
                 "Primera línea, presentada como la más obvia, con un caso cotidiano que la hace visible (§3.4).",
                 "Segunda línea, jerarquizada: separa lo que hace posible algo de lo que lo explica. [[only makes it "
                 "possible; it doesn’t explain why]] (§4.6), [[an unspoken assumption]], [[stepping away from "
                 "it]].",
                 "Contrapunto que limita la propia tesis. [[Mind you]] (§4.3), [[in a good way]].",
                 "Cierre que retoma la metáfora del principio (patrón organizativo, §4.1). [[to come back to the "
                 "question]] (§4.2).",
             ],
             "follow_up": {"q": "Should employers be allowed to contact their staff outside working hours?",
                           "ideas": "Matiza: en emergencias, sí; como costumbre, no. Algunos países ya regulan el "
                                    "derecho a desconectar; la norma ayuda porque quita la presión individual."}},
        ],
        "discussion": [
            {"q": "Do you think people today have less free time than their grandparents did?", "theory": ['4.6'],
             "ideas": "Quizá más horas libres sobre el papel, pero más fragmentadas y menos libres de verdad; "
                      "depende mucho del trabajo y del país.",
             "lang": "On paper, probably not — but I suspect it feels less free, which may matter more."},
            {"q": "Is being busy a sign of success?", "theory": ['4.3'],
             "ideas": "Se ha convertido en símbolo de estatus, pero el verdadero lujo es disponer de tu tiempo.",
             "lang": "It’s become a kind of status symbol, but if anything, the real luxury is having time to spare."},
            {"q": "Some people say that boredom is good for us. What do you think?", "theory": ['6.7', '6.3'],
             "ideas": "Sí, en dosis: obliga a pensar y a inventar; pero el aburrimiento crónico no tiene nada de "
                      "creativo.",
             "lang": "Up to a point. A bit of boredom forces you to think; a lot of it just wears you down."},
            {"q": "Would a four-day working week be a good idea?", "theory": ['3.5'],
             "ideas": "Funciona donde se mide el resultado y no las horas; en sectores con atención al público es "
                      "más difícil. Distingue entre trabajos.",
             "lang": "It would work in some jobs far better than in others, so I’d be wary of a one-size-fits-all "
                     "rule."},
            {"q": "Why does time seem to pass more quickly as we get older?", "theory": ['3.4'],
             "ideas": "Hay menos primeras veces: la rutina deja pocos recuerdos, y en retrospectiva el tiempo sin "
                      "recuerdos parece corto.",
             "lang": "I think it’s because there are fewer firsts — routine doesn’t leave many memories behind."},
            {"q": "Is it ever possible to waste time usefully?", "theory": ['3.5'],
             "ideas": "Sí: muchas ideas llegan cuando no se busca nada; el problema es que no se puede programar "
                      "la inspiración.",
             "lang": "I’d say some of the most useful time I’ve spent was time I thought I was wasting."},
        ],
    },
    "lex": ["texture (of time)", "effectively infinite", "permanently reachable", "keep up with", "an obscure "
            "hobby", "switch off", "an unspoken assumption", "step away from", "blurred", "a status symbol",
            "wear sb down", "one-size-fits-all", "time to spare"],
}

SPEC03 = {
    "num": "03", "level": 3,
    "subtitle": "Hoja 03 · Part 2: un siglo de trabajo · Part 3: la influencia de los demás · dificultad 3 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "What do you usually do to relax after a busy day?",
         "model": "Something physical, as a rule. If I’ve spent the whole day at a desk, sitting on a sofa doesn’t "
                  "really feel like rest, so I’ll go for a run or at least a long walk. It sounds counter-intuitive, "
                  "but I come back far less tired than when I left."},
        {"q": "Who has had the most influence on the person you are today?",
         "model": "Probably a teacher I had at fourteen, more than anyone in my family. She was the first person "
                  "who treated my questions as interesting rather than annoying, and I think that changed the way "
                  "I approached learning altogether. I doubt she has any idea."},
        {"q": "Do you see yourself living in the same place in ten years’ time?",
         "model": "Honestly, I’d be surprised. Not because I don’t like it here, but because the kind of work I’m "
                  "interested in tends to be concentrated in a few big cities. Mind you, people who say that often "
                  "end up coming back, so I wouldn’t bet on it either way."},
    ]},
    "p2": {
        "title": "Exhibition – A century of work",
        "intro": "different places of work",
        "q1_pics": ["A", "B"],
        "q1": "what it might have been like to work in these places",
        "context": "I'd like you to imagine that a museum is planning an exhibition about how work has changed over "
                   "the last hundred years. These pictures will be used in the exhibition.",
        "task": "Talk together about what each picture shows about the way work has changed. Then decide which "
                "picture should be used on the poster advertising the exhibition.",
        "partner_voice": "Thomas",
        "photos": [
            {"letter": "A", "file": "File:Collins konfektionsfabrik 1920a.jpg",
             "what": "Una fábrica de ropa hacia 1920: filas de mujeres cosiendo; al fondo, un hombre de pie.",
             "spec": "Que trabajaban muchas horas, quizá en silencio; que el hombre del fondo es un encargado; que el "
                     "trabajo era repetitivo pero se hacía junto a compañeras.",
             "offers": "El trabajo industrial clásico: horario fijo, tarea repetida, vigilancia directa.",
             "decision": "A favor: el punto de partida del siglo, inconfundible. En contra: en blanco y negro y "
                         "sola, solo habla del pasado."},
            {"letter": "B", "file": "File:Call center (8301477546).jpg", "artist": "Carlos Ebert",
             "what": "Un centro de llamadas: filas de cubículos con trabajadores con auriculares.",
             "spec": "Que es la fábrica de la era de la información: guion, pantalla, tiempo medido; que se habla "
                     "todo el día, pero no con quien está al lado.",
             "offers": "La continuidad: cambian las herramientas, no tanto la organización del trabajo.",
             "decision": "A favor: la idea más interesante para una exposición, por el parecido con la A. En contra: "
                         "es una lectura que el público quizá no haga sin ayuda."},
            {"letter": "C", "file": "File:Business woman at home in her bedroom working on her laptop. "
                                    "(51236863108).jpg",
             "what": "Una mujer trabaja con el portátil en una mesa junto a la ventana de su casa.",
             "spec": "—",
             "offers": "Autonomía y ningún desplazamiento, a cambio de aislamiento y de que casa y trabajo se mezclen.",
             "decision": "A favor: el cambio más reciente y el que más afecta al visitante. En contra: no se ve el "
                         "trabajo, solo un portátil."},
            {"letter": "D", "file": "File:Factory Automation Robotics Palettizing Bread.jpg",
             "what": "Robots industriales apilan cajas de pan en una fábrica sin nadie a la vista.",
             "spec": "—",
             "offers": "La automatización: más producción con menos personas; la pregunta es adónde han ido.",
             "decision": "A favor: llamativa, y la ausencia de personas es el mensaje. En contra: una exposición sobre "
                         "el trabajo humano sin humanos en el cartel."},
            {"letter": "E", "file": "File:Local shoe makers-producers.jpeg",
             "what": "Zapateros trabajando en un taller pequeño y abarrotado.",
             "spec": "—",
             "offers": "El oficio completo, de principio a fin, que convive con todo lo demás.",
             "decision": "A favor: recuerda que no todo ha cambiado. En contra: puede leerse como algo del pasado "
                         "o de otro lugar, no como presente."},
        ],
        "phase1_lines": [
            "I imagine the women in picture A worked very long hours, and the man at the back is presumably there to "
            "make sure nobody stops.",
            "What strikes me about the call centre is that everyone is talking all day, but not to the person next "
            "to them.",
        ],
        "decision": "A y D juntas (antes y ahora) si el criterio es que el cartel cuente el siglo de un vistazo; B si "
                    "se quiere provocar con la idea de que el trabajo ha cambiado menos de lo que creemos. C tiene "
                    "el problema de que no se ve el trabajo.",
        "language": ["It depends whether the poster should show change or continuity.",
                     "The call centre is really the factory floor of our time.",
                     "If we put A and D side by side, the poster tells the whole story.",
                     "That’s a neat idea, but would visitors get it?"],
        "partner": [
            {"text": "Picture A must have been exhausting — rows of women sewing for hours, probably in silence. "
                     "Although, when you look at the call centre, I’m not sure that much has changed. It’s the same "
                     "rows, only with headsets instead of needles.",
             "provokes": "Una comparación aguda: recógela con sus palabras y llévala más lejos.",
             "react": "That’s a striking way of putting it — headsets instead of needles. And I suppose the man at "
                      "the back of picture A has simply been replaced by software that times every call.",
             "theory": ["6.2"]},
            {"text": "For the poster, I’d go for the robots, without a doubt. That’s where work is heading, and a "
                     "museum ought to show the future, not just the past.",
             "provokes": "Una propuesta defendible: concede su fuerza y objeta con el criterio de la tarea.",
             "react": "I’ll grant that it’s the most eye-catching, but the exhibition is about the last hundred "
                      "years, and a poster with no people on it might send the wrong message.",
             "theory": ["6.3", "5.3"]},
            {"text": "Mind you, the woman working from home is the real revolution. No commute, no boss looking over "
                     "her shoulder — I’d say she’s got the perfect life!",
             "provokes": "Un entusiasmo exagerado: modéralo y aporta la otra cara.",
             "react": "Let’s not get carried away — plenty of people who work from home say they miss having "
                      "colleagues, and the working day has a way of never quite ending.",
             "theory": ["6.4"]},
            {"text": "I have to say, I think you’re being a bit romantic about the old days. Factory work a hundred "
                     "years ago was no picnic.",
             "provokes": "Una crítica a tu postura: reconoce lo que tenga de cierto antes de responder, o recházala "
                         "si no es lo que has dicho.",
             "react": "I won’t deny it — I may be romanticising it a little. But my point was only that some "
                      "things, like working side by side, seem to have got lost along the way.",
             "theory": ["6.3"]},
            {"text": "Right, we’ve got about thirty seconds left, I’d say — no, I tell a lie, less than that. Shall "
                     "we put the factory and the robots side by side? Then and now.",
             "provokes": "Una propuesta de cierre (y un ejemplo de [[I tell a lie]], §4.4): decidid ya.",
             "react": "I’ll drink to that — then and now says it all. Although if there’s room, I’d sneak the call "
                      "centre in between, just to make people think.",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "influence",
        "cards": [
            {"q": "To what extent are people’s opinions shaped by those around them?",
             "ideas": ["family", "friends", "social media"],
             "plan": {
                 "Operación": "[[To what extent]]: una medida, con el dónde sí y el dónde no (§3.1).",
                 "Postura": "Mucho más de lo que admitimos, pero moldear no es determinar.",
                 "Línea 1": "La familia llega primero: heredamos los supuestos antes de poder razonar ([[family]]).",
                 "Línea 2": "Los amigos no convencen: hacen que discrepar cueste; las redes añaden la cifra de la "
                            "aprobación ([[friends]], [[social media]]).",
                 "Contrapunto": "Las opiniones nacidas de la experiencia directa resisten la presión.",
                 "Cierre": "La libertad que queda está en elegir de quién te rodeas (idea propia)."},
             "model": [
                 "I’d say to a much greater extent than most of us would like to admit. We tend to think of our "
                 "opinions as conclusions we’ve reached on our own, but if you look at where they actually come "
                 "from, other people are almost always involved somewhere — a parent, a friend, a voice in a feed.",
                 "The most obvious influence is the family, simply because it gets there first. Long before we’re "
                 "able to weigh up an argument, we’ve absorbed a whole set of assumptions — about money, about "
                 "politics, about what counts as a sensible career. Even people who reject their parents’ views "
                 "are, in a sense, still defined by them, because they’re reacting against them.",
                 "Friends work in a subtler way. It isn’t so much that they persuade us as that disagreeing with "
                 "them has a cost. If everyone around you thinks a certain way, voicing the opposite view means "
                 "risking a bit of friction, and most of us, most of the time, would rather not. Social media adds "
                 "something new to this: it doesn’t only show us what people believe; it shows us how many of them "
                 "approve. And that number, whether we like it or not, tells us what is acceptable to say.",
                 "Admittedly, there are limits to all this. Opinions that come from direct experience — say, of "
                 "illness, or of living in another country — are remarkably hard to shift, whatever the people "
                 "around you think. Someone who has been unemployed, for instance, rarely needs persuading about how hard "
                 "it is to find work.",
                 "So, to come back to the question, I’d say our opinions are shaped by others to a considerable "
                 "extent, but not determined by them. And perhaps the freedom we do have lies mainly in choosing "
                 "whose company we keep.",
             ],
             "comments": [
                 "Responde la medida en la primera frase y explica por qué la pregunta engaña (§3.2).",
                 "Primera línea: afirma, razona y matiza con una paradoja (quien rechaza a sus padres sigue definido "
                 "por ellos). [[simply because it gets there first]], [[in a sense]] (§4.3).",
                 "Segunda línea, distinta en mecanismo, que funde dos ideas de la tarjeta. [[It isn’t so much that "
                 "… as that …]] (§4.6), [[most of us, most of the time]].",
                 "Contrapunto: el dónde no de la pregunta [[To what extent]]. [[Admittedly]] (§4.3).",
                 "Cierre que distingue dos verbos ([[shaped]] / [[determined]]) y añade una idea propia (§4.1).",
             ],
             "follow_up": {"q": "Do you think people are more easily influenced now than they were in the past?",
                           "ideas": "No necesariamente más, pero por más fuentes y más rápido; antes la influencia "
                                    "era local y lenta. Recoge una idea del long turn sin repetirla."}},
            {"q": "Why are some people more willing to take advice than others?",
             "ideas": ["experience", "pride", "trust"],
             "plan": {
                 "Operación": "[[Why]]: causas, jerarquizadas (§3.1).",
                 "Postura": "Depende menos del consejo que de lo que aceptarlo parece decir de uno.",
                 "Línea 1": "El orgullo: aceptar un consejo es admitir que no sabías; paradoja: los más competentes "
                            "piden más consejo ([[pride]]).",
                 "Línea 2": "La confianza en quien aconseja, alimentada por la experiencia previa ([[trust]], "
                            "[[experience]]). Más importante.",
                 "Contrapunto": "No aceptarlo no siempre es vanidad: hay consejos genéricos o malos.",
                 "Cierre": "Quien acepta consejos no es el débil, sino el que se siente seguro (idea propia)."},
             "model": [
                 "I think the honest answer is that it has less to do with the advice itself than with what "
                 "accepting it seems to say about you. Taking someone’s advice means admitting, at least "
                 "implicitly, that they knew something you didn’t, and some people find that much harder than "
                 "others.",
                 "Pride is the obvious factor here. For someone who’s insecure about their position — a new "
                 "manager, say, or a teenager — accepting advice can feel like a public admission of weakness. "
                 "Interestingly, it’s often the most competent people who ask for advice most readily, precisely "
                 "because they’ve got nothing to prove.",
                 "The second factor is trust, and I’d say it’s probably the more important one. We don’t really "
                 "evaluate advice on its merits; we evaluate the person giving it. If I suspect that someone has "
                 "an interest in what I decide — a salesperson, for instance — I’ll discount whatever they tell me, "
                 "however sensible it is. And experience feeds into this: if you’ve followed bad advice in the past "
                 "and paid for it, you become wary. Oddly enough, we often find it easier to take advice from a stranger "
                 "than from a brother or sister, perhaps because there’s no history between us.",
                 "That said, I don’t think unwillingness is always a sign of vanity. A lot of advice is generic, and "
                 "some of it is simply wrong. A certain amount of scepticism is perfectly healthy, and some of the best "
                 "decisions people make are the ones they made against everyone’s advice.",
                 "So, all things considered, I’d say people who take advice easily aren’t the weak ones, as we "
                 "sometimes assume. If anything, they tend to be the ones who feel secure enough to admit what they "
                 "don’t know.",
             ],
             "comments": [
                 "Redefine la pregunta: el problema no es el consejo, sino lo que significa aceptarlo. [[has less to "
                 "do with … than with …]] (§4.6).",
                 "Primera línea con dos casos breves y una paradoja que da detalle (§3.4). [[Interestingly]], "
                 "[[precisely because]].",
                 "Segunda línea, jerarquizada, con un caso y una consecuencia; funde dos ideas de la tarjeta. "
                 "[[We don’t really evaluate … ; we evaluate …]] (§4.6), [[however sensible it is]].",
                 "Contrapunto que defiende a quien no acepta consejos. [[That said]] (§4.2), [[a certain amount of "
                 "scepticism]].",
                 "Cierre que invierte un prejuicio. [[If anything]] (§4.3).",
             ],
             "follow_up": {"q": "Who do you usually turn to when you need advice, and why?",
                           "ideas": "Pregunta personal: responde en la primera frase, da una razón ligada al long turn "
                                    "(confianza, falta de interés propio) y añade un matiz: depende del tema."}},
        ],
        "discussion": [
            {"q": "Who has more influence on young people today: their parents or the people they follow online?",
             "theory": ["6.7", "4.3"],
             "ideas": "Los padres en lo profundo (valores, hábitos); internet en lo visible (gustos, aspiraciones). "
                      "Distingue tipos de influencia.",
             "lang": "It depends what kind of influence we mean: parents shape values, but online figures shape "
                     "what people want."},
            {"q": "Is it possible to think completely independently?",
             "theory": ["4.6"],
             "ideas": "Del todo, no: pensamos con conceptos y lenguaje heredados; sí se puede pensar con más "
                      "independencia, sabiendo de dónde vienen nuestras ideas.",
             "lang": "Completely, no — we think with words and ideas we didn’t invent. But we can be aware of where "
                     "they come from."},
            {"q": "Should advertising aimed at children be banned?",
             "theory": ["3.5"],
             "ideas": "Argumento a favor: los niños no distinguen persuasión de información. En contra: dónde está el "
                      "límite (patrocinio, influencers). Una postura graduada.",
             "lang": "There’s a strong case for restricting it, though I’m not sure an outright ban would be "
                     "workable."},
            {"q": "Why do people follow trends even when they don’t particularly like them?",
             "theory": ["3.4"],
             "ideas": "Pertenencia y miedo a quedarse fuera; además, el gusto se forma por exposición: acaba gustando "
                      "lo que se ve a menudo.",
             "lang": "Partly to belong, I suppose — and partly because we end up liking what we see often enough."},
            {"q": "Every generation seems to think the next one is worse. Why might that be?",
             "theory": ["6.7", "4.3"],
             "ideas": "Nostalgia selectiva (recordamos lo bueno de nuestra juventud) y la sensación de perder el "
                      "control del mundo que conocíamos.",
             "lang": "I think it says more about the older generation than the younger one — it’s nostalgia, really."},
            {"q": "Can one person really change the way a whole society thinks?",
             "theory": ["4.6"],
             "ideas": "Una persona puede dar forma a un cambio que ya estaba en marcha; rara vez lo crea de la nada. "
                      "Ejemplos sin nombres concretos si no se está seguro.",
             "lang": "One person can give a change its voice, but I suspect the change is usually already under way."},
        ],
    },
    "lex": ["no picnic", "romanticise", "look over sb’s shoulder", "weigh up", "voice a view", "friction",
            "hard to shift", "whose company we keep", "a public admission", "nothing to prove", "discount (advice)",
            "an outright ban", "under way", "counter-intuitive"],
}

SPEC04 = {
    "num": "04", "level": 4,
    "subtitle": "Hoja 04 · Part 2: personas y naturaleza · Part 3: el progreso · dificultad 4 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "How long have you lived in the place where you live now?",
         "model": "About ten years — no, I tell a lie, it must be twelve now, because we moved just before I started "
                  "secondary school. Long enough, anyway, to have seen most of the shops on my street change hands "
                  "at least once."},
        {"q": "Is there a piece of technology you couldn’t live without?",
         "model": "I’d like to say no, but it would be my phone, obviously — not for the phone itself, but because "
                  "it has quietly absorbed everything else: my maps, my music, my bank. Which is slightly alarming "
                  "when you think about it."},
        {"q": "Would you describe yourself as an optimist or a pessimist?",
         "model": "A cautious optimist, I suppose. I generally expect things to work out, but I like to know what I’d "
                  "do if they didn’t. A friend of mine calls that pessimism with good manners, and she may have a "
                  "point."},
    ]},
    "p2": {
        "title": "Documentary – Sharing the planet",
        "intro": "people and nature in different situations",
        "q1_pics": ["A", "E"],
        "q1": "what these pictures suggest about the relationship between people and wild animals",
        "context": "I'd like you to imagine that a television company is making a documentary about whether people "
                   "and nature can share the same space. These pictures are being considered for the opening "
                   "sequence.",
        "task": "Talk together about what each picture says about the relationship between people and the natural "
                "world. Then decide which picture would make the most powerful opening image.",
        "partner_voice": "Natasha",
        "photos": [
            {"letter": "A", "file": "File:Urban Fox (5338896611).jpg",
             "what": "Un zorro cruza el umbral de una casa en plena ciudad.",
             "spec": "Que viene a menudo y encuentra comida en la basura; que se mueve como si la calle fuera suya; "
                     "que los vecinos lo toleran, o no lo saben.",
             "offers": "La naturaleza que se adapta a nosotros sin pedir permiso.",
             "decision": "A favor: inesperada e íntima; plantea la pregunta del documental. En contra: es un solo "
                         "animal y un caso más bien anecdótico."},
            {"letter": "B", "file": "File:Rooftop garden NYC.jpg",
             "what": "Vista aérea de una azotea ajardinada entre edificios de Nueva York.",
             "spec": "—",
             "offers": "Naturaleza en la ciudad, pero diseñada y privada: ¿convivencia o decoración?",
             "decision": "A favor: optimista y muy visual. En contra: es naturaleza domesticada, no compartida."},
            {"letter": "C", "file": "File:Barn wind turbines 0504.jpg",
             "what": "Un granero viejo con aerogeneradores al fondo, en el campo.",
             "spec": "—",
             "offers": "Energía limpia que transforma el paisaje: el campo como espacio de producción.",
             "decision": "A favor: pasado y futuro en un plano. En contra: habla más de energía que de convivencia "
                         "con la naturaleza."},
            {"letter": "D", "file": "File:Beekeeper.jpg",
             "what": "Un apicultor abre las colmenas rodeado de abejas.",
             "spec": "—",
             "offers": "Una relación de beneficio mutuo (polinización, miel) o de explotación, según se mire.",
             "decision": "A favor: muestra cooperación concreta. En contra: es una actividad económica más que un "
                         "espacio compartido."},
            {"letter": "E", "file": "File:Bear jam (35342243771).jpg",
             "what": "Coches parados en una carretera de Yellowstone mientras unos osos pasan junto al arcén.",
             "spec": "Que la gente quiere ver lo salvaje, pero sin bajarse del coche; que el animal se ha convertido "
                     "en espectáculo; un zoo al revés.",
             "offers": "La naturaleza como espectáculo, vista desde la máquina.",
             "decision": "A favor: irónica y potente; resume la pregunta del documental. En contra: puede leerse "
                         "como una simple anécdota turística."},
        ],
        "phase1_lines": [
            "The fox looks as though it’s done this a hundred times — I suspect it knows the bins better than the "
            "people do.",
            "What strikes me about picture E is that everyone wants to see a wild animal, but nobody seems prepared "
            "to get out of the car.",
        ],
        "decision": "E si el documental quiere abrir con una pregunta incómoda (miramos la naturaleza desde la "
                    "máquina); A si prefiere abrir con la idea de que la naturaleza ya vive entre nosotros. B y C "
                    "hablan más de diseño y de energía que de compartir espacio.",
        "language": ["It depends whether the opening should reassure people or unsettle them.",
                     "It’s nature, but it’s been tamed.", "A and E are almost mirror images: …",
                     "If we had to settle on one, I’d go for the one that raises a question."],
        "partner": [
            {"text": "The fox looks completely at home, doesn’t it? I’d guess it’s been visiting that house for years. "
                     "Whereas in the other one, people are queuing in their cars just to catch a glimpse of a wild "
                     "animal. It’s almost like a zoo in reverse.",
             "provokes": "Una imagen brillante ([[a zoo in reverse]]): recógela y desarróllala.",
             "react": "A zoo in reverse — I like that. And it works both ways: in picture A, the animal comes to us "
                      "on its own terms, whereas in E we go to it and stay safely behind glass.",
             "theory": ["6.2", "5.2"]},
            {"text": "For the opening, I’d go for the wind turbines next to the old barn. It shows the past and the "
                     "future side by side, and that’s really what the documentary is about.",
             "provokes": "Una propuesta atractiva que se aleja un poco de la tarea: concede y reconduce al criterio.",
             "react": "I’ll grant that it’s a lovely image, but is the documentary really about energy? I thought it "
                      "was about whether we can share space with other living things.",
             "theory": ["6.3", "6.4"]},
            {"text": "Honestly, the rooftop garden is the answer to everything. If every building had one, our cities "
                     "would be as green as the countryside within ten years!",
             "provokes": "Una exageración: modérala con humor y un dato de sentido común.",
             "react": "Let’s not get carried away. A few plants on a roof are lovely, but they’re hardly a forest — "
                      "and most of the people in that city will never set foot on one.",
             "theory": ["6.4"]},
            {"text": "But surely the beekeeper isn’t sharing anything with nature. He’s just using the bees to make "
                     "money, isn’t he?",
             "provokes": "Un argumento con parte de razón: concédela y matiza.",
             "react": "I won’t deny he makes a living out of them, but the bees get something too — and without "
                      "people like him, a lot of crops would never be pollinated.",
             "theory": ["6.3"]},
            {"text": "Right, we really need to make a decision. I’m still going for the wind farm. What about you?",
             "provokes": "Una postura firme al cierre: negocia o cierra el desacuerdo de forma explícita.",
             "react": "We may have to differ on that one. For me, the bear jam is the strongest opening, because it "
                      "asks the question the whole documentary is about. Could we agree on that, with the turbines "
                      "later on?",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "progress",
        "cards": [
            {"q": "Is technological progress always a good thing?",
             "ideas": ["health", "work", "relationships"],
             "plan": {
                 "Operación": "[[Is … always]]: un juicio; el [[always]] pide matizar (§3.1).",
                 "Postura": "No siempre: poder hacer más no equivale a vivir mejor.",
                 "Línea 1": "La salud: el caso más claro a favor, pero con dilemas nuevos ([[health]]).",
                 "Línea 2": "El trabajo y las relaciones: ganancias que traen costes ocultos ([[work]], "
                            "[[relationships]]).",
                 "Contrapunto": "Rechazar la tecnología también tiene víctimas.",
                 "Cierre": "El progreso es bueno cuando decidimos para qué sirve (idea propia)."},
             "model": [
                 "The short answer, I think, is no — but not because technology is somehow bad. It’s because the "
                 "word ‘progress’ hides an assumption: that being able to do more automatically means living "
                 "better. And those two things don’t always go together. A new technology gives us options; whether our "
                 "lives improve depends on what we do with them.",
                 "Health is the strongest case for progress, and I wouldn’t want to argue with it. Vaccines, "
                 "anaesthetics, antibiotics — it’s hard to imagine anyone seriously wishing them away. But even here "
                 "there are dilemmas we didn’t have before. We can now keep people alive far longer than we can keep "
                 "them well, and that raises questions that medicine on its own can’t answer.",
                 "Work is a more mixed picture. Technology has taken a great deal of drudgery out of people’s jobs, "
                 "which is clearly a gain. At the same time, the tools that make us more efficient also make us "
                 "easier to monitor and harder to switch off, so the time we save tends to be reclaimed in other ways. "
                 "As for relationships, we’re in contact with more "
                 "people than ever, yet I’m not convinced the contact is any deeper. If anything, it may have become "
                 "easier to keep people at a comfortable distance.",
                 "Admittedly, the alternative isn’t very attractive either. Refusing new technology has its own "
                 "victims, and they’re usually the people who would have benefited most from it — the sick, the isolated, "
                 "the very poor.",
                 "So, all things considered, I’d say progress is a good thing when we decide what it’s for. The "
                 "problem isn’t the technology itself; it’s the assumption that it will make those decisions for "
                 "us.",
             ],
             "comments": [
                 "Responde en la primera frase y desmonta el supuesto que esconde la pregunta. Escindida [[It’s "
                 "because …]] (§4.6).",
                 "Primera línea: concede el caso más fuerte y aun así encuentra un dilema (detalle, §4.1). "
                 "[[I wouldn’t want to argue with it]], [[far longer than we can keep them well]].",
                 "Segunda línea, con dos ideas de la tarjeta de signo mixto. [[At the same time]], [[As for]] "
                 "(§4.2), [[If anything]] (§4.3).",
                 "Contrapunto contra la propia postura: rechazar el progreso también tiene costes. [[Admittedly]] "
                 "(§4.3).",
                 "Cierre que traslada el problema de la tecnología a quien decide. Escindida final [[The problem "
                 "isn’t …; it’s …]] (§4.6).",
             ],
             "follow_up": {"q": "Do you think we rely too much on technology to solve our problems?",
                           "ideas": "Enlaza con el cierre del long turn: confiamos en que la tecnología decida por "
                                    "nosotros; algunos problemas son políticos o sociales y no técnicos."}},
            {"q": "Who benefits most from progress?",
             "ideas": ["the wealthy", "the young", "future generations"],
             "plan": {
                 "Operación": "[[Who]]: comparar ganadores (y perdedores) a distintos plazos (§3.1, §3.5).",
                 "Postura": "Depende del plazo: a corto, los que ya van por delante; a largo, casi todos, y sobre "
                            "todo quienes aún no han nacido.",
                 "Línea 1": "Los ricos y los formados: acceden antes y convierten la ventaja en más ventaja "
                            "([[the wealthy]]).",
                 "Línea 2": "Los jóvenes: no tienen nada que desaprender; los mayores pierden el valor de su "
                            "experiencia ([[the young]]).",
                 "Contrapunto": "A largo plazo, los lujos se vuelven necesidades, pero también se heredan los "
                                "costes ([[future generations]]).",
                 "Cierre": "Por eso cuesta defender el progreso: los que más ganan no votan (idea propia)."},
             "model": [
                 "I think the answer depends almost entirely on the time scale you choose. In the short term, "
                 "progress tends to benefit the people who are already ahead; in the long term, it benefits almost "
                 "everyone — and, oddly enough, the biggest winners are people who haven’t been born yet.",
                 "In the short term, it’s hard to argue with the idea that the wealthy gain most. New technologies "
                 "are expensive at first, so the people who can afford them get them early, and they can often turn "
                 "that head start into further advantage. The same is true of education: the better educated you "
                 "are, the faster you can make use of something new. By the time a new technology reaches everyone, the "
                 "people who had it first have often moved on to the next one.",
                 "The young are in a similar position, though for different reasons. They don’t need to unlearn "
                 "anything. For an older worker, a new technology can mean that thirty years of experience suddenly "
                 "count for very little, whereas a twenty-year-old simply picks it up. It isn’t that older people can’t "
                 "adapt; it’s that adapting costs them more.",
                 "But if you take the longer view, the picture changes. Mobile phones started out as a status symbol "
                 "for a few executives; now they’re used by farmers and fishermen all over the world. Things that "
                 "begin as luxuries tend to end up as necessities, and the people who inherit them get them almost "
                 "for free — along with the costs, of course, such as the damage to the environment.",
                 "So, all things considered, I’d say progress benefits the future most and the present unevenly. "
                 "And perhaps that’s exactly why it’s so hard to argue for: the people who stand to gain most aren’t "
                 "around to vote for it.",
             ],
             "comments": [
                 "Responde con la variable que lo decide todo (el plazo) y anticipa la sorpresa final (§3.2, §3.5).",
                 "Primera línea, a corto plazo, con un mecanismo claro. [[it’s hard to argue with the idea that]], "
                 "correlativa [[the better educated …, the faster …]] (§4.6).",
                 "Segunda línea, paralela pero con otra razón; los perdedores aparecen en el contraste. [[though for "
                 "different reasons]], [[whereas]].",
                 "Giro a largo plazo con un caso que todos reconocen; el contrapunto va dentro ([[along with the "
                 "costs, of course]]). [[But if you take the longer view]] (§4.2).",
                 "Cierre con una idea propia que explica una paradoja política. [[stand to gain]] (§4.6).",
             ],
             "follow_up": {"q": "Is it fair that some people get the benefits of new technology long before others?",
                           "ideas": "Parece injusto, pero el precio alto de los primeros usuarios financia que luego "
                                    "baje para todos; la cuestión es cuánto dura el desfase en salud o educación."}},
        ],
        "discussion": [
            {"q": "In what ways is life better today than it was fifty years ago?",
             "theory": ["3.5"],
             "ideas": "Salud, esperanza de vida, acceso a información y a viajar; matiza con lo que se ha perdido "
                      "(estabilidad laboral, vivienda asequible en muchos sitios).",
             "lang": "In most measurable ways, it clearly is — though some of the things that are harder to measure "
                     "may have got worse."},
            {"q": "Do you think people today are happier than previous generations?",
             "theory": ["4.6"],
             "ideas": "Más comodidad no implica más felicidad: las expectativas suben con las posibilidades; la "
                      "comparación constante resta.",
             "lang": "I suspect we’re more comfortable rather than happier, partly because our expectations rise "
                     "with everything we gain."},
            {"q": "Is it possible to stop progress once it has started?",
             "theory": ["4.3"],
             "ideas": "Detenerlo, rara vez; orientarlo y ralentizarlo, sí (regulación, moratorias, prohibiciones "
                      "internacionales).",
             "lang": "Stop it, probably not. Steer it, yes — and if anything, that’s the more useful question."},
            {"q": "Some people say that every solution creates a new problem. How much truth is there in this?",
             "theory": ["6.7", "6.3"],
             "ideas": "Bastante: los antibióticos y las resistencias, el coche y la contaminación; pero los nuevos "
                      "problemas suelen ser menores que los que se resolvieron.",
             "lang": "There’s a good deal of truth in it, but the new problems are usually smaller than the ones they "
                     "replaced."},
            {"q": "Who should decide which scientific research is allowed?",
             "theory": ["3.5"],
             "ideas": "Ni solo los científicos (interés propio) ni solo los políticos (falta de conocimiento): "
                      "organismos mixtos, con la sociedad informada.",
             "lang": "I wouldn’t want to leave it entirely to scientists, or entirely to politicians, for that "
                     "matter."},
            {"q": "What do you think future generations will see as the biggest mistake of our time?",
             "theory": ["4.4"],
             "ideas": "Es especulativa: gana tiempo con contenido y elige un candidato (el clima, la atención, la "
                      "desigualdad) con una razón.",
             "lang": "That’s a difficult one to call, but my guess would be the way we treated the environment as "
                     "someone else’s problem."},
        ],
    },
    "lex": ["change hands", "absorb (functions)", "pessimism with good manners", "on its own terms",
            "a zoo in reverse", "set foot on", "make a living out of", "drudgery", "wish sth away",
            "keep sb at a distance", "a head start", "unlearn", "count for very little", "stand to gain",
            "steer (progress)", "difficult to call"],
}

SPEC05 = {
    "num": "05", "level": 5,
    "subtitle": "Hoja 05 · Part 2: los rituales cotidianos · Part 3: la verdad · dificultad 5 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "What kind of routine do you have in the mornings?",
         "model": "A fairly rigid one, I’m afraid. Coffee first, then twenty minutes reading the news, and only then "
                  "anything resembling work. I didn’t plan it that way, but I’ve noticed that on days when the "
                  "routine breaks down, the whole day tends to go with it."},
        {"q": "Is there a tradition in your family that you particularly enjoy?",
         "model": "We have a long lunch on the first Sunday of every month, which started when my grandparents "
                  "were alive and somehow outlived them. Nobody ever suggests it — it just happens — and I think "
                  "that’s exactly why it matters."},
        {"q": "How do you feel about being photographed?",
         "model": "Not very comfortable, to be honest. I never quite recognise myself in photos, and I’m always "
                  "aware of the camera. Mind you, I’m glad other people insist on taking them, because they’re "
                  "often the only record I have of things I’d otherwise forget."},
    ]},
    "p2": {
        "title": "Exhibition – The rituals we live by",
        "intro": "people taking part in different kinds of ritual",
        "q1_pics": ["A", "D"],
        "q1": "what these routines might mean to the people involved",
        "context": "I'd like you to imagine that a museum is putting together an exhibition about the rituals that "
                   "shape everyday life. These pictures are being considered for the exhibition.",
        "task": "Talk together about what each picture suggests about why people need rituals. Then decide which "
                "picture should be left out of the exhibition.",
        "partner_voice": "Emily",
        "photos": [
            {"letter": "A", "file": "File:Morning routine (50571166888).jpg", "artist": "Gauthier Delecroix",
             "what": "Un hombre practica taichí a contraluz en un paseo casi vacío, de mañana.",
             "spec": "Que lo hace cada día a la misma hora; que el gesto repetido le da calma, o una identidad; que "
                     "no le importa, o incluso busca, estar solo.",
             "offers": "Un ritual íntimo y elegido: orden y calma al empezar el día.",
             "decision": "A favor: bella y pura. En contra: muy individual; puede leerse como simple ejercicio."},
            {"letter": "B", "file": "File:Festival in Japan - Laughing Over Tea - open-air tea ceremony in Japan "
                                    "(1914 by Elstner Hilton).jpg", "artist": "Elstner Hilton (1914), vía A. Davey",
             "what": "Una ceremonia del té al aire libre en una foto antigua: mujeres en kimono sirven y ríen.",
             "spec": "—",
             "offers": "El ritual heredado: repetir gestos que unen con el pasado y con los demás.",
             "decision": "A favor: el ritual por excelencia. En contra: lejano en el tiempo y en el espacio para el "
                         "visitante."},
            {"letter": "C", "file": "File:Sposi che ballano con gli invitati durante la festa.jpg",
             "what": "Una novia ríe y baila rodeada de invitados en una boda.",
             "spec": "—",
             "offers": "El rito de paso: un cambio de vida que se celebra ante la comunidad.",
             "decision": "A favor: alegría y comunidad. En contra: la imagen más previsible."},
            {"letter": "D", "file": "File:NYCS smartphones vc.jpg", "artist": "Billie Grace Ward",
             "what": "Pasajeros en un andén de metro, cada uno mirando su móvil.",
             "spec": "Que lo hacen sin pensar, cada día, en los mismos huecos de espera; que es un hábito más que un "
                     "ritual; que estando juntos nadie se mira.",
             "offers": "La pregunta de fondo: ¿un hábito colectivo es un ritual?",
             "decision": "A favor: la más provocadora; obliga a definir qué es un ritual. En contra: puede parecer "
                         "que no encaja."},
            {"letter": "E", "file": "File:Tourist holding a selfie stick (27082979383).jpg",
             "artist": "Stephanie Kraus",
             "what": "Una turista se hace una foto con un palo de selfi.",
             "spec": "—",
             "offers": "Un ritual moderno: documentar la experiencia, ¿o sustituirla?",
             "decision": "A favor: actual y reconocible. En contra: el tópico más fácil de criticar."},
        ],
        "phase1_lines": [
            "I’d hazard a guess the man in picture A has been doing this every morning for years — the "
            "repetition is probably the whole point.",
            "The people on the platform are doing the same thing every day too, but I doubt it means anything to "
            "them. Or perhaps that’s exactly what a modern ritual looks like.",
        ],
        "decision": "Dejar fuera la E si el criterio es evitar el tópico, porque la D ya representa los rituales "
                    "modernos con más ambigüedad; dejar fuera la D si se define el ritual como algo con significado "
                    "consciente. Lo que no conviene es descartar la D sin discutirla: es la que da sentido a la "
                    "exposición.",
        "language": ["It depends how we define a ritual in the first place.", "There’s a fine line between a ritual "
                     "and a habit.", "It earns its place because it makes people think.",
                     "If one has to go, I’d rather lose the obvious one."],
        "partner": [
            {"text": "The man doing tai chi looks completely absorbed, as though the rest of the city doesn’t exist. "
                     "Whereas the people on the platform are all staring at their phones. I’m not sure you’d call "
                     "that a ritual. It’s more of a habit, surely?",
             "provokes": "Una distinción interesante (ritual o hábito): recógela y llévala más lejos.",
             "react": "That’s the interesting question, isn’t it — where a habit ends and a ritual begins. I’d say "
                      "it’s a matter of meaning: the man has chosen his; the commuters have simply drifted into "
                      "theirs.",
             "theory": ["6.2", "6.5"]},
            {"text": "For me, the wedding is the one picture that has to stay. It’s the only one where people are "
                     "genuinely celebrating something together.",
             "provokes": "Una postura razonable: concede su mérito y añade un matiz.",
             "react": "I’ll grant you that it’s the most joyful. Though the tea ceremony is just as communal, in a "
                      "quieter way — it’s simply a celebration of something less dramatic.",
             "theory": ["6.3"]},
            {"text": "And honestly, that selfie is the saddest thing I’ve ever seen. It’s proof that our whole "
                     "generation has completely lost the ability to live in the moment.",
             "provokes": "Una generalización exagerada: modérala sin desdeñar la idea.",
             "react": "Let’s not get carried away. People have always wanted proof that they were there — "
                      "postcards, holiday slides. The stick is new; the instinct isn’t.",
             "theory": ["6.4"]},
            {"text": "You don’t seem to think traditions like the tea ceremony matter very much, do you? I get the "
                     "feeling you’d happily leave it out.",
             "provokes": "Una atribución que probablemente no has hecho: recházala y aclara tu postura.",
             "react": "Nothing of the sort — if anything, I think it’s the clearest example of what a ritual is. I "
                      "was only wondering whether visitors would relate to it.",
             "theory": ["6.3", "4.3"]},
            {"text": "OK, decision time. I’d leave out the commuters. If you ask me, they’re not really doing a "
                     "ritual at all. Agreed?",
             "provokes": "Una propuesta discutible al cierre: negocia o cierra el desacuerdo, pero decidid.",
             "react": "We may have to differ on that. For me, the commuters are what makes the exhibition "
                      "interesting. I’d rather lose the selfie — it says the same thing, only more obviously. "
                      "Could you live with that?",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "truth",
        "cards": [
            {"q": "Is it ever right to tell a lie?",
             "ideas": ["kindness", "trust", "consequences"],
             "plan": {
                 "Operación": "[[Is it ever right]]: un juicio con su criterio (§3.1).",
                 "Postura": "Sí, a veces, pero mucho menos de lo que nos decimos.",
                 "Línea 1": "La amabilidad: la mentira que protege al otro y no al mentiroso; ese es el criterio "
                            "([[kindness]]).",
                 "Línea 2": "Cada mentira gasta confianza, y más en las instituciones ([[trust]], "
                            "[[consequences]]).",
                 "Contrapunto": "Incluso la mentira amable decide por el otro: puede ser paternalista.",
                 "Cierre": "Si una mentira sale fácil, probablemente es la equivocada (idea propia)."},
             "model": [
                 "I’d say yes, occasionally — but far less often than we tell ourselves. Most of us lie several "
                 "times a day without really thinking about it — to be polite, to avoid an argument, or simply to get "
                 "out of a conversation — and I suspect that if we had to justify each lie, very few would survive "
                 "the test.",
                 "The strongest case for lying is kindness. If a friend asks whether you enjoyed a dinner they spent "
                 "all day cooking, the truthful answer may be ‘not really’, but saying so would hurt them and help "
                 "nobody. In cases like that, the lie protects the other person rather than the liar, and that seems "
                 "to me to be the crucial test. A lie that only saves you from embarrassment is a different matter "
                 "altogether.",
                 "The problem is that every lie, however small, draws on a kind of shared account of trust. Each "
                 "time one is discovered, the account goes down, and it isn’t easily topped up again. That’s true "
                 "of friendships, but it’s even more true of institutions. When a government or a company is caught "
                 "lying ‘for our own good’, people don’t just doubt that particular statement; they start to doubt "
                 "everything that follows.",
                 "Admittedly, even kind lies have a cost that’s easy to overlook. When you decide that someone is "
                 "better off not knowing something, you’re also deciding for them, and that can be rather "
                 "patronising, however kindly it’s meant.",
                 "So, all things considered, I’d say lying can be right, but only rarely, and only when it’s done for "
                 "someone else’s sake. And perhaps a useful rule of thumb is this: if a lie comes easily, it’s "
                 "probably the wrong one.",
             ],
             "comments": [
                 "Responde en la primera frase y gradúa con un giro autocrítico ([[than we tell ourselves]]) que "
                 "anuncia el criterio (§3.2).",
                 "Primera línea con un caso cotidiano y el criterio explícito ([[the crucial test]]); contraste final "
                 "con la mentira egoísta (§3.4). [[a different matter altogether]].",
                 "Segunda línea con una metáfora sostenida ([[a shared account of trust]], [[topped up]]) y un salto "
                 "de escala: de la amistad a las instituciones (§3.5, §4.1).",
                 "Contrapunto contra la propia postura: la mentira amable es paternalista. [[Admittedly]] (§4.3).",
                 "Cierre con una regla propia, presentada con atenuación ([[perhaps a useful rule of thumb]]) "
                 "(§4.6).",
             ],
             "follow_up": {"q": "Do you think people today are more or less honest than they used to be?",
                           "ideas": "Probablemente igual de honestos, pero más expuestos: hoy las mentiras se "
                                    "descubren antes y quedan registradas. Retoma la imagen de la confianza como "
                                    "cuenta sin repetirla."}},
            {"q": "How far can we rely on our own memories?",
             "ideas": ["emotion", "time", "other people"],
             "plan": {
                 "Operación": "[[How far]]: una medida, con el dónde sí y el dónde no (§3.1).",
                 "Postura": "Para lo esencial, bastante; para los detalles, mucho menos de lo que creemos: la memoria "
                            "reconstruye, no graba.",
                 "Línea 1": "La emoción da seguridad, no exactitud; el tiempo rellena huecos ([[emotion]], "
                            "[[time]]).",
                 "Línea 2": "Los demás: los relatos familiares y las fotos sustituyen al recuerdo ([[other "
                            "people]]).",
                 "Contrapunto": "Que la memoria no sea fiel tiene ventajas: hace la vida más llevadera.",
                 "Cierre": "La memoria sirve como guía del significado, no como prueba (idea propia)."},
             "model": [
                 "Less than we’d like to think, I suspect, though more than the sceptics claim. As far as I "
                 "understand it, memory works less like a recording than like a reconstruction: each time we "
                 "remember something, we rebuild it, and each rebuilding changes it slightly.",
                 "For the broad outline of our lives, I think we can rely on it reasonably well. I know where I grew "
                 "up and which school I went to, and nobody needs to check that. Those are things I use constantly, so "
                 "they’re checked against reality all the time. The trouble starts with details — "
                 "who said what, in which order, and how we felt at the time.",
                 "Emotion is a particularly misleading guide. We tend to assume that a memory which feels vivid must "
                 "be accurate, but the research seems to suggest the opposite: strong emotions make us more "
                 "confident about our memories, not more accurate. And time makes things worse, because the gaps "
                 "get filled with whatever seems most plausible, usually in a way that flatters us.",
                 "Other people play a surprisingly large part too. Families retell the same stories so often that "
                 "it becomes impossible to say whether you remember an event or just the version you’ve heard at "
                 "every birthday since. I’ve got a vivid memory of my third birthday, for instance, which I’m "
                 "fairly sure comes from a photograph.",
                 "Admittedly, this unreliability isn’t entirely a bad thing. If we remembered everything exactly as "
                 "it happened, every embarrassment included, life might be rather harder to bear. So, to come back "
                 "to the question, I’d say we can trust our memories to tell us what matters to us, but not "
                 "necessarily what happened. They’re better as a guide to meaning than as evidence.",
             ],
             "comments": [
                 "Responde la medida con dos extremos y da el principio que explicará todo: [[less like a recording "
                 "than like a reconstruction]] (§4.6). [[As far as I understand it]]: atenuación (§4.6).",
                 "El dónde sí, breve, con un caso concreto, y el paso al dónde no: [[The trouble starts with]].",
                 "Primera línea del dónde no: funde dos ideas de la tarjeta. [[the research seems to suggest]], "
                 "contraste [[more confident …, not more accurate]] (§4.6).",
                 "Segunda línea con un ejemplo personal que la hace visible (§3.4). [[Other people play a "
                 "surprisingly large part too]].",
                 "Contrapunto y cierre fundidos: concede una ventaja y responde a la pregunta con una distinción "
                 "propia. [[Admittedly]] (§4.3), [[to come back to the question]] (§4.2).",
             ],
             "follow_up": {"q": "Why do two people often remember the same event so differently?",
                           "ideas": "Cada uno se fija en cosas distintas y reconstruye desde su propio interés; luego "
                                    "cada versión se refuerza al contarla. Enlaza con [[reconstruction]] sin "
                                    "repetir el long turn."}},
        ],
        "discussion": [
            {"q": "Is honesty always the best policy in close relationships?", "theory": ["6.7", "4.6"],
             "ideas": "Honestidad sobre lo importante, tacto sobre lo trivial; la sinceridad brutal a veces es "
                      "egoísmo disfrazado.",
             "lang": "On the things that matter, yes. On the trivial things, a little tact is arguably a form of "
                     "honesty too."},
            {"q": "Can fiction tell us truths that facts can’t?", "theory": ["4.6"],
             "ideas": "Sí: los hechos dicen qué pasó; la ficción, cómo se vive. Una novela sobre la guerra puede "
                      "enseñar más del miedo que un informe.",
             "lang": "Facts tell you what happened; fiction tells you what it felt like — and that’s a kind of "
                     "truth as well."},
            {"q": "Should journalists ever keep information from the public?", "theory": ["3.5"],
             "ideas": "En casos muy concretos (seguridad de personas, víctimas), sí; pero el criterio no puede ser "
                      "proteger al poder.",
             "lang": "Occasionally, I think — but the test should be whether it protects people, not whether it "
                     "protects the powerful."},
            {"q": "Is there such a thing as an objective truth?", "theory": ["4.4"],
             "ideas": "Para hechos medibles, sí; para valores y significados, la cuestión es más abierta. Gana tiempo "
                      "con contenido y distingue tipos de verdad.",
             "lang": "That’s a big question. I’d say there is for facts — the boiling point of water isn’t a matter "
                     "of opinion — but much less so for values."},
            {"q": "Is it possible to live entirely without secrets?", "theory": ["4.3"],
             "ideas": "Difícilmente, y quizá no sea deseable: la intimidad necesita cosas que no se comparten; un "
                      "secreto no es lo mismo que una mentira.",
             "lang": "I doubt it, and if anything, I’m not sure it would be healthy. Privacy isn’t the same as "
                     "dishonesty."},
            {"q": "Some people say that the truth always comes out in the end. How much truth is there in this?",
             "theory": ["6.7", "6.3"],
             "ideas": "Más hoy que antes, por los registros digitales; pero muchas verdades no salen nunca, y la frase "
                      "consuela más de lo que describe.",
             "lang": "It’s a comforting idea, but I suspect it’s more of a hope than a description."},
        ],
    },
    "lex": ["a fine line", "earn its place", "drift into", "outlive", "a shared account of trust", "top up",
            "patronising", "a rule of thumb", "for sb’s sake", "a different matter altogether", "harder to bear",
            "tact"],
}

SPEC06 = {
    "num": "06", "level": 6,
    "subtitle": "Hoja 06 · Part 2: el azar y la elección · Part 3: el azar · dificultad 6 de 6",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "Do you consider yourself a lucky person?",
         "model": "In the things that matter most, yes — I was born somewhere peaceful, into a family that valued "
                  "education, and I chose neither of those. In the small things, though, I’m spectacularly unlucky: "
                  "if one train is cancelled all week, it’s mine."},
        {"q": "How do you usually make important decisions?",
         "model": "Slowly, I’m afraid. I tend to make a list of pros and cons and then, rather annoyingly, ignore it "
                  "and go with my instinct. I’ve come to think the list is useful mainly because it tells me what "
                  "my instinct actually is."},
        {"q": "What would you do with a completely free year?",
         "model": "I’d probably spend the first month sleeping and the next eleven feeling guilty about it. "
                  "Seriously, though, I’d like to learn a language from scratch somewhere I couldn’t get by in "
                  "English, partly to see how much of my personality survives in another language."},
    ]},
    "p2": {
        "title": "Book cover – The role of chance",
        "intro": "situations involving chance and choice",
        "q1_pics": ["A", "E"],
        "q1": "why people might choose to leave things to chance in these situations",
        "context": "I'd like you to imagine that a publisher is bringing out a book about the part that chance plays "
                   "in our lives. These pictures are being considered for the cover.",
        "task": "Talk together about what each picture suggests about the relationship between chance and choice. "
                "Then decide which picture would make the most thought-provoking cover.",
        "partner_voice": "Mitchell",
        "photos": [
            {"letter": "A", "file": "File:Faireys Play Soccer- a Women's Football Match Between Fairey and Av Roe, "
                                    "Fallowfield, Manchester, Lancashire, England, UK, 1944 D23521.jpg",
             "what": "Un árbitro lanza una moneda ante dos capitanas antes de un partido de fútbol femenino de los "
                     "años cuarenta.",
             "spec": "Que recurren al azar porque es justo: nadie puede quejarse del resultado; que es un rito "
                     "previo al partido; que ninguna de las dos controla nada.",
             "offers": "El azar como mecanismo de justicia: se usa precisamente porque nadie lo controla.",
             "decision": "A favor: idea clara y poco obvia. En contra: foto antigua y discreta para una portada."},
            {"letter": "B", "file": "File:CSIRO ScienceImage 3567 Examining an agar dish for bacterial colonies as "
                                    "part of the bioremediation project.jpg", "artist": "David McClenaghan, CSIRO",
             "what": "Un científico examina colonias de bacterias en una placa de Petri.",
             "spec": "—",
             "offers": "La casualidad en el descubrimiento (la penicilina): el azar que solo aprovecha quien está "
                       "preparado.",
             "decision": "A favor: la idea más rica. En contra: sin explicación, el lector ve ciencia, no azar."},
            {"letter": "C", "file": "File:Downtown Raleigh Lightning Strike (216140693).jpeg",
             "what": "Un rayo cae sobre una ciudad de noche.",
             "spec": "—",
             "offers": "El azar puro, el que nadie decide: la naturaleza como lotería.",
             "decision": "A favor: espectacular. En contra: más dramática que reflexiva; sugiere que todo es azar."},
            {"letter": "D", "file": "File:Fork in the road.jpg",
             "what": "Vista aérea de una carretera que se bifurca, con un coche acercándose al cruce.",
             "spec": "—",
             "offers": "La elección: decidir sin saber adónde lleva cada camino.",
             "decision": "A favor: equilibra azar y elección. En contra: metáfora muy gastada."},
            {"letter": "E", "file": "File:Scenes of open gambling in Reno, Nevada casinos- roulette wheel at left; "
                                    "bar at right LCCN2003677179.jpg",
             "what": "Una sala de juego antigua: hombres alrededor de una ruleta.",
             "spec": "Que creen que pueden ganar a la suerte; que el casino es el único que controla las "
                     "probabilidades; que hay algo de rito y de autoengaño.",
             "offers": "El azar como espectáculo y como negocio: la ilusión de control.",
             "decision": "A favor: mucha historia. En contra: reduce el azar al juego."},
        ],
        "phase1_lines": [
            "In picture A, I imagine they toss a coin precisely because nobody can argue with it — it’s chance used "
            "as a kind of fairness.",
            "The men round the roulette wheel, on the other hand, presumably think they can beat the odds, which "
            "is a very different relationship with chance.",
        ],
        "decision": "B si se busca una portada que haga pensar (azar y preparación); D si el libro equilibra azar y "
                    "elección; A como opción original. C es la tentación: espectacular, pero da a entender que todo "
                    "es azar.",
        "language": ["It depends whether the book argues that chance can be tamed or not.",
                     "It’s striking, but it rather gives the game away.",
                     "It works on two levels: …", "Thought-provoking, yes — but would anyone pick it up?"],
        "partner": [
            {"text": "The coin toss is interesting, isn’t it? Nobody’s gambling anything there. They use chance "
                     "precisely because it’s fair. The casino’s the opposite. Those men think they can beat the odds, "
                     "which is exactly why they’ll lose.",
             "provokes": "Un contraste muy útil (azar justo frente a azar engañoso): recógelo y amplía el alcance.",
             "react": "That’s a neat distinction — chance as a referee and chance as a temptation. And you could say "
                      "the same about lotteries for school places: we accept them because nobody controls them.",
             "theory": ["6.2", "6.5"]},
            {"text": "For the cover, I’d go for the scientist. So many great discoveries happened by accident, and "
                     "that’s really the most fascinating side of chance.",
             "provokes": "Una buena propuesta con un punto débil: concede y señala el problema.",
             "react": "I’ll give you that — it’s the richest idea of the five. But would a reader see chance in "
                      "it without an explanation? To most people, it just looks like science.",
             "theory": ["6.3"]},
            {"text": "Actually, forget the others. The lightning says it all. Life is completely random, and nothing "
                     "we decide makes the slightest difference.",
             "provokes": "Una postura extrema y fatalista: modérala y discrepa con argumentos.",
             "react": "Let’s not get carried away — if nothing we decided made any difference, there’d be no point "
                      "in writing the book, let alone choosing a cover for it.",
             "theory": ["6.4", "6.3"]},
            {"text": "I suppose you’re one of those people who believes everyone makes their own luck? That hard "
                     "work is all it takes?",
             "provokes": "Una etiqueta que te atribuye una postura: matiza lo que tenga de cierto o recházala.",
             "react": "I won’t deny there’s some truth in it — preparation matters. But nothing of the sort if you "
                      "mean that people born into poverty simply didn’t try hard enough.",
             "theory": ["6.3"]},
            {"text": "We’re running out of time. I’d still choose the fork in the road. It’s the only picture where a "
                     "choice is actually being made. What do you say?",
             "provokes": "Una propuesta razonada al cierre: acéptala, negóciala o cierra el desacuerdo.",
             "react": "I’ll drink to that, as long as the book really is about choice as well as chance. If it’s "
                      "mainly about chance, we may have to differ, and I’d go for the scientist.",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "chance",
        "cards": [
            {"q": "How far are people’s lives shaped by chance rather than choice?",
             "ideas": ["birth", "luck", "decisions"],
             "plan": {
                 "Operación": "[[How far … rather than …]]: una medida comparativa (§3.1).",
                 "Postura": "Mucho más de lo que creemos, sobre todo cuando nos va bien; ayuda separar el punto de "
                            "partida del camino.",
                 "Línea 1": "El punto de partida es casi todo azar: país, época, familia, salud ([[birth]]).",
                 "Línea 2": "El camino es una mezcla, y la suerte se acumula: una pequeña ventaja abre otras "
                            "([[luck]]).",
                 "Contrapunto": "Las decisiones cuentan: con el mismo punto de partida, la gente acaba en lugares "
                                "distintos ([[decisions]]).",
                 "Cierre": "Nos atribuimos los éxitos y culpamos al azar de los fracasos; debería ser al revés "
                           "(idea propia)."},
             "model": [
                 "I think the honest answer is far more than most of us like to believe, particularly when things "
                 "are going well. It helps, though, to separate where we start from the route we take, because "
                 "chance plays a rather different role in each.",
                 "Where we start is almost entirely a matter of chance. Nobody chooses the country they’re born in, "
                 "the century, their parents or their health, and yet those four things probably decide more about "
                 "a life than any decision we make later on. In that sense, birth is the biggest lottery of all, "
                 "and the prizes are distributed very unevenly. And none of them is earned.",
                 "The route is more of a mixture. Chance keeps intervening — a conversation with a stranger, a "
                 "teacher who happens to notice you, graduating just as the economy collapses. And what makes these "
                 "accidents so powerful is that they compound. A small piece of luck at eighteen can open a door "
                 "that leads to another, and another, until it looks, from the outside, like a carefully planned "
                 "career. Very few people who succeed would describe it that way, of course.",
                 "Admittedly, choices clearly matter. Two people with almost identical starting points can end up in "
                 "very different places, and that isn’t all down to luck. How we respond to an opportunity, or to a "
                 "setback, is at least partly up to us. Some people make the most of a small piece of luck; others "
                 "waste a large one.",
                 "So, all things considered, I’d say chance deals the cards and choice decides how we play them. "
                 "The danger is that we tend to credit our choices when things go well and blame chance when they "
                 "don’t. If anything, it should probably be the other way round.",
             ],
             "comments": [
                 "Responde la medida en la primera frase y anuncia la distinción que organiza todo el long turn "
                 "([[where we start]] / [[the route we take]]) (§3.2, §4.2).",
                 "Primera línea: una enumeración que convence por acumulación y una metáfora ([[the biggest lottery "
                 "of all]]). [[In that sense]] (§4.3).",
                 "Segunda línea con tres casos rápidos y un mecanismo ([[they compound]]) que da detalle (§3.4, "
                 "§4.1).",
                 "Contrapunto que devuelve su peso a la elección. [[Admittedly]] (§4.3), [[isn’t all down to "
                 "luck]].",
                 "Cierre con una imagen propia y una inversión final. [[If anything]] (§4.3).",
             ],
             "follow_up": {"q": "Is it fair that some people are born with far more advantages than others?",
                           "ideas": "No es justo ni injusto en sí (nadie lo ha decidido); la cuestión de justicia es "
                                    "qué hace la sociedad con esas diferencias. Distingue para no repetir el long "
                                    "turn."}},
            {"q": "Why do people find uncertainty so difficult to live with?",
             "ideas": ["control", "fear", "planning"],
             "plan": {
                 "Operación": "[[Why]]: causas, jerarquizadas (§3.1).",
                 "Postura": "Porque una mala certeza se lleva mejor que una pregunta abierta.",
                 "Línea 1": "Cómo estamos hechos: la incertidumbre nos mantiene en alerta ([[fear]]).",
                 "Línea 2": "La cultura del control: si todo se puede planificar, lo imprevisible parece un fracaso "
                            "([[control]], [[planning]]). Más importante.",
                 "Contrapunto": "Hay quien vive bien en la incertidumbre; y en ella está también la esperanza.",
                 "Cierre": "No se puede eliminar; lo útil es aprender a tolerarla (idea propia)."},
             "model": [
                 "I suspect it’s because, for most of us, a bad certainty is easier to deal with than an open "
                 "question. If you know something unpleasant is going to happen, you can at least prepare for it; "
                 "if you don’t know, you’re stuck in a kind of permanent alert.",
                 "Part of that, I think, is simply how we’re built. For most of human history, an unknown noise in "
                 "the dark was worth treating as a threat, and our minds still seem to work on that principle. It’s "
                 "often said that people waiting for medical results feel worse than people who’ve already had bad "
                 "news, and whether or not that’s strictly true, it certainly matches most people’s experience.",
                 "But there’s a cultural side to it as well, and it may be the more important one. We’re constantly "
                 "told that almost everything can be planned, measured or insured against. So when something "
                 "genuinely can’t be predicted, it doesn’t just feel uncomfortable; it feels like a failure, as if "
                 "we ought to have been able to control it. Planning, which is meant to reassure us, can even make "
                 "this worse, because every plan creates a new way of failing.",
                 "Mind you, not everyone experiences it in the same way. Some people seem to thrive on uncertainty: "
                 "they start businesses, move abroad on a whim, and find a completely predictable life far more "
                 "frightening. And uncertainty is also, after all, where hope comes from. If the future were fixed, "
                 "there’d be nothing to look forward to.",
                 "So, to come back to the question, I’d say we find it hard because we’re wired for vigilance and "
                 "taught to expect control. Since we can’t get rid of uncertainty, perhaps the more useful skill is "
                 "learning to tolerate it.",
             ],
             "comments": [
                 "Responde con una paradoja ([[a bad certainty is easier … than an open question]]) y la explica en "
                 "la frase siguiente (§3.2, §4.6).",
                 "Primera línea: un mecanismo (evolución) y un ejemplo presentado con cautela: [[It’s often said "
                 "that …, and whether or not that’s strictly true, …]] (§4.6, atenuación).",
                 "Segunda línea, jerarquizada ([[it may be the more important one]]), con un contraste [[it doesn’t "
                 "just feel …; it feels …]] (§4.6).",
                 "Contrapunto doble: hay quien prospera en la incertidumbre y además es fuente de esperanza. [[Mind "
                 "you]] (§4.3), condicional [[If the future were fixed]].",
                 "Cierre que resume las dos causas en una frase simétrica ([[wired for … and taught to …]]) y propone "
                 "una idea propia (§4.1).",
             ],
             "follow_up": {"q": "Do you think it’s possible to plan too much?",
                           "ideas": "Sí: cuando el plan sustituye a la atención y deja de adaptarse; un buen plan "
                                    "incluye margen para lo imprevisto. Enlaza con la idea de tolerar la "
                                    "incertidumbre."}},
        ],
        "discussion": [
            {"q": "Should important decisions ever be left to chance?", "theory": ["3.5"],
             "ideas": "A veces sí, precisamente por justicia: sorteos de plazas escolares, jurados, desempates. El "
                      "azar es aceptable cuando no hay un criterio mejor.",
             "lang": "Sometimes, yes — when there’s no fairer way to choose, a lottery at least has the virtue of "
                     "being impartial."},
            {"q": "Some people say that we make our own luck. How much truth is there in this?",
             "theory": ["6.7", "6.3"],
             "ideas": "Parte de verdad (la preparación aprovecha las oportunidades), pero la frase olvida el punto de "
                      "partida y puede culpar a quien no tuvo suerte.",
             "lang": "Some — preparation certainly helps you spot opportunities. But it’s a saying that tends to be "
                     "used by people who started with a head start."},
            {"q": "Why do you think people believe in fate?", "theory": ["3.4"],
             "ideas": "Da sentido y consuelo: si algo estaba escrito, no es culpa nuestra ni fue en vano; además el "
                      "cerebro busca patrones.",
             "lang": "I suppose it’s comforting: if something was meant to happen, then it wasn’t pointless — or "
                     "our fault."},
            {"q": "How important have accidents been in the history of science?", "theory": ["4.4"],
             "ideas": "Mucho, pero el accidente solo sirve a quien sabe verlo; ejemplos si se conocen (penicilina, "
                      "rayos X) y, si no, razonar en general.",
             "lang": "Very, I think — although an accident only becomes a discovery if someone is prepared enough "
                     "to notice it."},
            {"q": "Can we ever really predict the future?", "theory": ["4.3"],
             "ideas": "Tendencias, sí (demografía, clima); sucesos concretos, no. Las predicciones más seguras son las "
                      "aburridas.",
             "lang": "Trends, to some extent. Events, hardly ever — and if anything, the most confident predictions "
                     "tend to be the least reliable."},
            {"q": "If you could know exactly how your life would turn out, would you want to?", "theory": ["4.4"],
             "ideas": "Hipotética: gana tiempo con contenido y razona; la mayoría diría que no, porque quitaría la "
                      "esperanza y el sentido de decidir.",
             "lang": "That’s a fascinating question. I think I’d say no: knowing the ending would take away the "
                     "point of most of the decisions along the way."},
        ],
    },
    "lex": ["give the game away", "beat the odds", "a head start", "deal the cards", "compound (effects)",
            "down to luck", "on a whim", "thrive on", "wired for", "impartial", "from scratch", "get by",
            "spectacularly unlucky"],
}

SPECS = [SPEC01, SPEC02, SPEC03, SPEC04, SPEC05, SPEC06]
