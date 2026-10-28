# SIM-01 · Writing · specs de la Part 1 (essay) y de las tres tareas de la Part 2
# Se monta con: python3 src/gen_SIM.py wrt sim/SIM-01
# Formato: cabecera de src/gen_WRT-P1.py (P1) y de src/gen_WRT-P2.py (cada tarea de P2).

# ---------- Part 1 · Essay ----------
P1 = {
    "texts": [
        {"title": "Time to send them home",
         "text": "Many of the most celebrated objects in Western museums were acquired in ways that would now be "
                 "called looting: seized during military campaigns, removed under colonial rule or bought from people "
                 "in no position to refuse. Keeping them on display, however carefully they are labelled, prolongs "
                 "the original injustice. The familiar objection that their countries of origin lack the means to "
                 "care for them no longer holds, if it ever did, and it carries an unpleasant echo of the attitudes "
                 "that justified their removal. These objects belong to living cultures, and only by returning them "
                 "can museums begin to repair the damage."},
        {"title": "The case for sharing",
         "text": "Nobody today defends the methods by which some museum collections were assembled, and where an "
                 "object was plainly stolen, the case for sending it back is strong. Wholesale restitution, however, "
                 "would come at a price. Great museums allow millions of visitors to see the art of many "
                 "civilisations side by side and to understand how cultures have borrowed from one another. "
                 "Dividing those collections along national lines would narrow that view, and it risks encouraging "
                 "the idea that culture is the property of nations. Long-term loans, joint research and shared "
                 "ownership offer a way of acknowledging the past without impoverishing the future."},
    ],
    "relation": {"type": "Mismo diagnóstico, distinta solución",
                 "axis": "si la injusticia con que se reunieron las colecciones obliga a devolver los objetos o si "
                         "basta con compartirlos.",
                 "contact": "los dos aceptan que hubo expolio: el texto 1 lo llama así ({{would now be called "
                            "looting}}) y el texto 2 lo concede ({{Nobody today defends the methods}}); la "
                            "diferencia está en el remedio."},
    "key_points": [
        {"id": "T1·1", "source": "Keeping them on display, however carefully they are labelled, prolongs the "
                                 "original injustice",
         "idea": "Muchas piezas se obtuvieron por la fuerza o con abuso, y exponerlas, aunque se explique su "
                 "origen, perpetúa la injusticia.",
         "par": 2, "model": "perpetuates the wrong done to those from whom they were taken"},
        {"id": "T1·2", "source": "The familiar objection that their countries of origin lack the means to care for "
                                 "them no longer holds",
         "idea": "Decir que los países de origen no pueden conservarlas es falso y paternalista; las piezas "
                 "pertenecen a culturas vivas y hay que devolverlas.",
         "par": 2, "model": "both outdated and condescending"},
        {"id": "T2·1", "source": "Wholesale restitution, however, would come at a price",
         "idea": "Lo robado sin discusión debe volver, pero devolverlo todo privaría al público de ver y comparar "
                 "las culturas juntas en un mismo lugar.",
         "par": 3, "model": "would deny millions the chance to see how civilisations have influenced one another"},
        {"id": "T2·2", "source": "Long-term loans, joint research and shared ownership offer a way of "
                                 "acknowledging the past",
         "idea": "Mejor préstamos, investigación conjunta y propiedad compartida; repartir las colecciones por "
                 "países alimenta la idea de que la cultura es de las naciones.",
         "par": 3, "model": "favours loans and shared stewardship instead"},
    ],
    "stance": {"type": "Superar",
               "text": "Ni devolverlo todo ni conservarlo todo: cada reclamación se juzga por separado, dando peso a "
                       "lo que quieran las comunidades de origen; lo que sigue vivo vuelve, y lo demás puede "
                       "compartirse."},
    "scheme": "bloques",
    "plan": [
        {"par": 1, "content": "La pregunta de fondo y en qué coinciden y discrepan los dos textos", "ideas": []},
        {"par": 2, "content": "Texto 1: resumen y evaluación (argumento sólido; el valor vivo de los objetos, con "
                              "un ejemplo propio)", "ideas": ["T1·1", "T1·2", "propia"]},
        {"par": 3, "content": "Texto 2: resumen y evaluación (supuesto discutible; respuesta propia a su temor)",
         "ideas": ["T2·1", "T2·2", "propia"]},
        {"par": 4, "content": "Postura: criterio caso por caso según la comunidad de origen", "ideas": ["propia"]},
    ],
    "model": [
        "Few cultural questions provoke more heated argument than whether museums should return "
        "objects taken from the peoples who made them. Both writers accept that at least some of this material was "
        "obtained unjustly; where they differ is over what that admission requires of museums today.",
        "The first writer contends that exhibiting looted artefacts, however candid the accompanying captions, "
        "perpetuates the wrong done to those from whom they were taken, and dismisses the claim that the nations "
        "concerned could not look after them as both outdated and condescending. This is a compelling argument, "
        "strongest in its reminder that such objects often retain a living significance: a "
        "ceremonial mask still worn at festivals is not simply an exhibit.",
        "The second writer, while conceding that anything stolen outright should be handed back, warns that "
        "breaking up major collections would deny millions the chance to see how civilisations have "
        "influenced one another, and favours loans and shared stewardship instead. This has some merit, "
        "but returned objects could still travel on loan, and the argument rests on a questionable assumption: "
        "that the benefit to visitors in London or Paris outweighs the claims of those whose heritage is at "
        "stake. Nor is the fear of a proprietorial view of culture entirely convincing: objects can "
        "return to the communities that made them, not to governments.",
        "On balance, I am not persuaded that either writer’s solution is right in every case. Each claim should be "
        "judged on its merits, with particular weight given to the wishes of the communities concerned. Where an "
        "object is still used or revered, it belongs at home; where it is not, the partnerships the second writer "
        "proposes may serve everyone.",
    ],
    "own_ideas": ["El ejemplo que concreta la idea de cultura viva ({{=a ceremonial mask still worn at "
                  "festivals}}), la respuesta a la pérdida de acceso ({{=returned objects could still travel on "
                  "loan}}), el supuesto que el texto 2 no dice ({{=the benefit to visitors in London or Paris "
                  "outweighs the claims}}), la distinción entre comunidades y Estados ({{=not to "
                  "governments}}) y el criterio final ({{=with particular weight given to the wishes of the "
                  "communities concerned}})."],
    "comments": {
        "Content": {"text": "Las cuatro ideas clave, comprensibles sin los textos, y los dos evaluados con razones: "
                            "el primero como {{=a compelling argument}}, el segundo con dos reparos concretos ({{="
                            "rests on a questionable assumption}}). La postura final no elige un texto: propone un "
                            "criterio que integra lo mejor de los dos.",
                    "theory": ["3.1", "5.2", "6.2"]},
        "Communicative Achievement": {"text": "Registro neutro-formal y sin primera persona hasta la conclusión "
                                              "({{=I am not persuaded}}), donde la postura la justifica. Los "
                                              "verbos de atribución distinguen las voces: {{=contends}}, "
                                              "{{=dismisses}}, {{=warns}}, {{=favours}}.",
                                      "theory": ["4.3", "6.3"]},
        "Organisation": {"text": "Esquema por bloques: un párrafo por texto, cada uno con resumen y evaluación, y "
                                 "una conclusión que responde a la pregunta de la introducción. La concesión abre "
                                 "el párrafo 3 ({{=while conceding that}}) y enlaza con la idea final del texto 1.",
                         "theory": ["7.1", "7.3", "7.4"]},
        "Language": {"text": "Léxico preciso ({{=shared stewardship}}, {{=a proprietorial view of culture}}, "
                             "{{=whose heritage is at stake}}) y estructuras variadas: inversión tras negación "
                             "({{=Nor is the fear}}), concesiva con [[however]] + adjetivo ({{=however candid the "
                             "accompanying captions}}) y paralelismo en la conclusión ({{=Where an object is "
                             "still used or revered}} … {{=where it is not}}).",
                     "theory": ["8.1", "8.2"]},
    },
    "errors": [
        {"error": "Resumir la lista de ejemplos del texto 1",
         "why": "Enumerar {{seized during military campaigns}} y lo demás gasta palabras en apoyos; la idea es que "
                "la exposición prolonga una injusticia.",
         "codes": ["C1"], "theory": ["3.1", "4.4"]},
        {"error": "Presentar el texto 2 como una defensa del expolio",
         "why": "El autor concede que {{where an object was plainly stolen, the case for sending it back is "
                "strong}}. Leerlo como lo contrario del texto 1 es una mala interpretación y deforma la relación "
                "entre los textos.",
         "codes": ["C4", "C1"], "theory": ["3.3"]},
        {"error": "Copiar las frases que mejor suenan",
         "why": "{{acknowledging the past without impoverishing the future}} es la frase más citable del texto 2 "
                "y, copiada, no puntúa: hay que reformularla.",
         "codes": ["L4"], "theory": ["4.1", "4.2"]},
        {"error": "Opinar sin evaluar",
         "why": "Decir que uno prefiere ver las piezas en su país no valora los argumentos: hay que juzgar si "
                "{{The familiar objection}} está bien rebatida o si el temor del texto 2 se sostiene.",
         "codes": ["C2"], "theory": ["5.1"]},
        {"error": "Una conclusión que repite la introducción",
         "why": "Sin un criterio propio, la postura queda en «hay argumentos en los dos sentidos», que no es "
                "postura.",
         "codes": ["C3", "O4"], "theory": ["6.2", "7.3"]},
    ],
    "lex": ["shared stewardship", "a proprietorial view of sth", "stolen outright", "whose heritage is at stake", "wholesale restitution"],
}

# ---------- Part 2 · tres tareas (preguntas 2-4), de géneros distintos ----------
_ARTICLE = {
    "genre": "article", "register": "neutro",
    "prompt": "An environmental magazine is running a series called ‘The right to quiet’. Readers have been invited "
              "to send in articles describing the sounds of a place they know well, explaining how noise affects the "
              "quality of life there and considering whether silence deserves the same protection as clean air or "
              "water.",
    "analysis": [
        {"dato": "Contexto", "quote": "a series called ‘The right to quiet’",
         "note": "El título de la serie ya insinúa una tesis (el silencio como derecho): el artículo tiene que "
                 "llegar a esa pregunta, no quedarse en la descripción."},
        {"dato": "Lector", "quote": "An environmental magazine",
         "note": "Lectores interesados en el medio ambiente, no especialistas en acústica: registro neutro, ideas "
                 "claras y ejemplos concretos."},
        {"dato": "Papel", "quote": "a place they know well",
         "note": "Escribes como vecino o usuario habitual de un lugar: la primera persona es natural, pero el caso "
                 "tiene que servir a una idea general."},
        {"dato": "Propósito", "quote": "considering whether silence deserves the same protection",
         "note": "El último punto pide sopesar, no proclamar: hay que reconocer el límite de la comparación con el "
                 "aire y el agua antes de concluir."},
        {"dato": "Registro", "quote": "",
         "note": "Neutro: frases variadas y algo de color en la descripción, sin coloquialismos ni tono de "
                 "panfleto."},
    ],
    "points": [
        {"id": "P1", "quote": "describing the sounds of a place they know well",
         "asks": "Una descripción sensorial concreta, ordenada (aquí, a lo largo del día), que haga oír el lugar.",
         "par": 2, "model": "By nine, the noise has layers"},
        {"id": "P2", "quote": "explaining how noise affects the quality of life there",
         "asks": "Efectos sobre las personas de ese lugar, con algún matiz (quién lo sufre más), no generalidades "
                 "sobre el ruido.",
         "par": 3, "model": "its cumulative effect is hard to overstate"},
        {"id": "P3", "quote": "considering whether silence deserves the same protection as clean air or water",
         "asks": "Valorar la comparación: en qué se parece y en qué no, y qué protección sería razonable.",
         "par": 4, "model": "the comparison is apt"},
    ],
    "plan": [
        {"par": 1, "content": "Apertura que engancha: el único momento de silencio del día en la calle", "points": []},
        {"par": 2, "content": "Los sonidos de la calle de la mañana a la noche, por capas", "points": ["P1"]},
        {"par": 3, "content": "Efectos acumulados: sueño, ánimo, cansancio; quién se va y quién lo sufre más",
         "points": ["P2"]},
        {"par": 4, "content": "¿Proteger el silencio como el aire? Sí en un sentido, no en otro; medidas concretas",
         "points": ["P3"]},
        {"par": 5, "content": "Cierre breve con humor que recoge un detalle del párrafo 2", "points": []},
    ],
    "model": {
        "title": "Notes from a Noisy Street",
        "paras": [
            {"heading": None,
             "text": "At around four in the morning, the street where I live falls almost silent. For perhaps an "
                     "hour, the only sounds are the hum of a refrigerated lorry outside the supermarket and "
                     "footsteps on their way home. Then the first delivery vans arrive, and the day begins its "
                     "long crescendo."},
            {"heading": None,
             "text": "By nine, the noise has layers. Buses idle at the stop beneath my window, a café drags its "
                     "metal tables across the pavement, and the building site on the corner contributes a "
                     "pneumatic drill that seems to start whenever I sit down to work. Evenings bring their own "
                     "soundtrack: conversations spilling out of bars, scooters whining through the traffic, and a "
                     "neighbour practising the trumpet with more enthusiasm than skill."},
            {"heading": None,
             "text": "None of this is unusual in a city centre, and much of it is the sound of a place that "
                     "is alive. Yet its cumulative effect is hard to overstate. Neighbours describe broken sleep, "
                     "frayed tempers and a low-level fatigue that is easy to dismiss precisely because it has no "
                     "single cause. Several families with young children have moved away in recent years, and older "
                     "residents, who spend most of the day at home, seem to bear the brunt of it."},
            {"heading": None,
             "text": "Should quiet, then, be protected in the way we now protect clean air? In one sense the "
                     "comparison is apt: noise, like dirty air or water, is a cost imposed on people who never "
                     "agreed to pay it. But quiet is harder to define: one person’s lively street is another’s "
                     "sleepless night, and a city that outlawed every "
                     "disturbance would be a dead one. What we can do is treat quiet as a shared resource rather "
                     "than a private luxury, by limiting night-time deliveries and building work, and by designing "
                     "streets that absorb sound instead of amplifying it."},
            {"heading": None,
             "text": "The trumpet, I suspect, is beyond the reach of any law. The rest is not."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos, cada uno con el desarrollo que pide su verbo: una descripción por "
                            "capas ({{=By nine, the noise has layers}}), efectos concretos y quién los sufre "
                            "({{=older residents, who spend most of the day at home}}) y una valoración de la "
                            "comparación que concede antes de proponer ({{=In one sense the comparison is "
                            "apt}}).", "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Article reconocible: título sugerente, apertura que engancha con "
                                              "una escena ({{=At around four in the morning}}) y cierre breve que "
                                              "no resume como un essay. Registro neutro con toques de humor "
                                              "({{=with more enthusiasm than skill}}).",
                                      "theory": ["4.1", "4.2", "4.4"]},
        "Organisation": {"text": "Progresión del lugar a la idea: escena, sonidos, efectos, propuesta. Las "
                                 "frases iniciales anuncian la función de cada párrafo ({{=Should quiet, then, be "
                                 "protected}}), y el cierre retoma un detalle del párrafo 2 ({{=The trumpet}}).",
                         "theory": ["4.3", "P1-7.4"]},
        "Language": {"text": "Léxico preciso y variado para el sonido ({{=long crescendo}}, {{=drags its metal "
                             "tables}}, {{=spilling out of bars}}) y estructuras que matizan: concesiva con [[yet]], "
                             "comparación con [[like]] y antítesis ({{=a shared resource rather than a private "
                             "luxury}}).", "theory": ["4.5", "P1-8.2"]},
    },
    "errors": [
        {"error": "Describir el ruido en general",
         "why": "El primer punto pide {{the sounds of a place they know well}}: una lista de ruidos urbanos sin "
                "lugar concreto no lo cumple.", "codes": ["C2"], "theory": ["2.2"]},
        {"error": "Contestar el último punto con un sí o un no",
         "why": "{{considering whether}} pide sopesar: reconocer lo que la comparación con el aire tiene de "
                "acertado y lo que no.", "codes": ["C2", "CA3"], "theory": ["2.2", "4.5"]},
        {"error": "Escribirlo como un essay",
         "why": "Sin título, con una introducción que anuncia el plan y una conclusión que resume, el texto "
                "deja de ser un article.", "codes": ["CA1", "CA5"], "theory": ["4.1", "4.4"]},
        {"error": "Tono de panfleto",
         "why": "Exclamaciones y exigencias ([[We must ban noise now!]]) no convencen a lectores que ya "
                "simpatizan con el tema y rompen el registro.", "codes": ["CA2"], "theory": ["4.2", "3.1"]},
    ],
    "lex": ["a long crescendo", "frayed tempers", "low-level fatigue", "beyond the reach of any law"],
}

_REPORT = {
    "genre": "report", "register": "formal",
    "prompt": "A year ago your town introduced a public bicycle-hire scheme, and the council is now asking local "
              "groups for feedback. As secretary of your residents’ association, you have been asked to write a "
              "report for the council. Your report should outline how the scheme has been used in your area, "
              "assess its main successes and shortcomings, and recommend changes for its second year.",
    "analysis": [
        {"dato": "Contexto", "quote": "the council is now asking local groups for feedback",
         "note": "El ayuntamiento decidirá con lo que lea: el report tiene que dar datos, juicio y propuestas "
                 "aplicables."},
        {"dato": "Papel", "quote": "As secretary of your residents’ association",
         "note": "Hablas en nombre de un grupo: conviene citar de dónde salen los datos (una encuesta a los "
                 "socios) y usar [[the association]] más que [[I]]."},
        {"dato": "Lector", "quote": "a report for the council",
         "note": "Una institución: registro formal, sin contracciones, frases impersonales y encabezados."},
        {"dato": "Propósito", "quote": "recommend changes for its second year",
         "note": "Todo desemboca en recomendaciones concretas que respondan a los problemas detectados."},
        {"dato": "Puntos", "quote": "",
         "note": "Tres verbos distintos (outline, assess, recommend): describir, valorar y proponer, cada uno en "
                 "su sección."},
    ],
    "points": [
        {"id": "P1", "quote": "outline how the scheme has been used in your area",
         "asks": "Hechos resumidos: quién lo usa, para qué y cuándo. [[Outline]] pide brevedad.",
         "par": 2, "model": "Take-up has been considerably higher"},
        {"id": "P2", "quote": "assess its main successes and shortcomings",
         "asks": "Un juicio equilibrado: lo que funciona y lo que no, con razones.",
         "par": 3, "model": "The scheme’s principal achievement"},
        {"id": "P3", "quote": "recommend changes for its second year",
         "asks": "Propuestas concretas y viables, cada una ligada a un problema del apartado anterior.",
         "par": 4, "model": "the association recommends three measures"},
    ],
    "plan": [
        {"par": 1, "content": "Propósito del report y fuentes (encuesta y observación)", "points": []},
        {"par": 2, "content": "Uso: trayectos, horarios y usuarios nuevos", "points": ["P1"]},
        {"par": 3, "content": "Logros (nuevos ciclistas, precio, app) y tres problemas", "points": ["P2"]},
        {"par": 4, "content": "Tres recomendaciones, cada una para un problema", "points": ["P3"]},
        {"par": 5, "content": "Conclusión: valoración global", "points": []},
    ],
    "model": {
        "title": "The Bicycle-Hire Scheme in Riverside: First-Year Review",
        "paras": [
            {"heading": "Introduction",
             "text": "This report, prepared on behalf of the Riverside Residents’ Association, assesses the first "
                     "year of the council’s bicycle-hire scheme in our district and proposes changes for the "
                     "coming year. It draws on a survey completed by 140 members and on observations at the "
                     "district’s four docking stations."},
            {"heading": "Use of the scheme",
             "text": "Take-up has been considerably higher than many expected. Most journeys are short trips to the "
                     "railway station between seven and nine in the morning, while weekend use is dominated by "
                     "families riding along the river path. Notably, a third of respondents had not cycled for years "
                     "before the scheme was launched."},
            {"heading": "Successes and shortcomings",
             "text": "The scheme’s principal achievement is that it has made cycling an everyday option for people "
                     "who would never have bought a bicycle. Members also praised the modest annual fee and the "
                     "booking app, which most found straightforward. Three shortcomings, however, were raised "
                     "repeatedly. The stations in the residential streets are often empty by eight o’clock, while "
                     "the one at the railway has no free docks, leaving later commuters stranded. The bicycles are "
                     "too heavy for many older residents, particularly on the hill up to the hospital, and the "
                     "hospital itself, one of the district’s busiest destinations, has no station of its own."},
            {"heading": "Recommendations",
             "text": "In view of these findings, the association recommends three measures. First, bicycles should be "
                     "moved back from the railway overnight, so that the residential stations are full, and the "
                     "railway docks free, at the start of the morning rush. Second, a number of electrically assisted "
                     "bicycles should be introduced, at least on routes with steep gradients. Finally, a fifth "
                     "station should be installed beside the hospital, where it would serve staff and visitors alike."},
            {"heading": "Conclusion",
             "text": "Overall, the scheme has been a clear success in Riverside. With relatively minor adjustments, "
                     "it could reach a considerably wider section of the community."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos en su sección: uso con datos verosímiles ({{=a third of respondents "
                            "had not cycled for years}}), un juicio con logros y problemas, y tres recomendaciones "
                            "que responden a esos problemas ({{=so that the residential stations are full}}).",
                    "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Formal e impersonal: el sujeto es la asociación ({{=the association "
                                              "recommends}}), las fuentes se citan al principio ({{=It draws on a "
                                              "survey}}) y el lector puede actuar con lo que lee.",
                                      "theory": ["6.1", "6.2"]},
        "Organisation": {"text": "Título informativo, encabezados con contenido y una sección por punto. Las "
                                 "recomendaciones se enumeran ({{=First}}, {{=Second}}, {{=Finally}}) y cada una "
                                 "se corresponde con un problema anterior.", "theory": ["6.3", "3.2"]},
        "Language": {"text": "Léxico propio del género ({{=Take-up}}, {{=principal achievement}}, {{=In view of "
                             "these findings}}) y pasivas que dan objetividad ({{=should be moved back "
                             "from the railway overnight}}), sin caer en la jerga.", "theory": ["6.4", "P1-8.2"]},
    },
    "errors": [
        {"error": "Recomendaciones que no responden a nada",
         "why": "Proponer, por ejemplo, más carriles bici cuando el apartado anterior no ha hablado de seguridad "
                "rompe la lógica del report: cada propuesta tiene que resolver un problema detectado.",
         "codes": ["C2", "O2"], "theory": ["6.3"]},
        {"error": "Extenderse en el primer punto",
         "why": "{{outline}} pide un resumen; describir cada estación y cada tipo de usuario deja sin espacio la "
                "valoración y las propuestas.", "codes": ["C2"], "theory": ["2.2"]},
        {"error": "Hablar en nombre propio",
         "why": "Escribes {{As secretary of your residents’ association}}: las opiniones son las de los socios, "
                "no las tuyas, y tiene que notarse de dónde salen.", "codes": ["CA3", "C4"], "theory": ["6.2"]},
        {"error": "Contracciones y tono de conversación",
         "why": "El lector es el ayuntamiento: [[it’s been great]] o [[loads of people]] fallan el registro.",
         "codes": ["CA2"], "theory": ["3.1", "6.4"]},
    ],
    "lex": ["take-up", "docking station", "leave sb stranded", "the morning rush"],
}

_REVIEW = {
    "genre": "review", "register": "vivo",
    "prompt": "An arts website has invited readers to send in reviews of a live comedy show they have seen recently. "
              "Your review should describe the performer’s style, evaluate how well the humour worked with the "
              "audience on the night and consider whether there are any subjects that comedians should leave "
              "alone.",
    "analysis": [
        {"dato": "Contexto", "quote": "An arts website",
         "note": "Lectores aficionados a los espectáculos que deciden si ir: quieren saber cómo es el cómico y si "
                 "merece la pena."},
        {"dato": "Papel", "quote": "a live comedy show they have seen recently",
         "note": "Escribes como espectador que estuvo allí: [[on the night]] invita a contar lo que pasó en la "
                 "sala, no solo a juzgar el texto."},
        {"dato": "Propósito", "quote": "consider whether there are any subjects that comedians should leave alone",
         "note": "El tercer punto abre una cuestión general; lo natural en una review es enlazarla con el "
                 "espectáculo concreto."},
        {"dato": "Registro", "quote": "",
         "note": "Vivo: se admiten contracciones, frases cortas para el ritmo e ironía, siempre con control."},
        {"dato": "Puntos", "quote": "",
         "note": "Describir, evaluar y considerar: descripción, juicio con ejemplos y reflexión; al final, la "
                 "recomendación propia del género."},
    ],
    "points": [
        {"id": "P1", "quote": "describe the performer’s style",
         "asks": "Cómo trabaja el cómico (ritmo, tono, presencia), con un ejemplo concreto.",
         "par": 2, "model": "Doran’s great gift is timing"},
        {"id": "P2", "quote": "evaluate how well the humour worked with the audience on the night",
         "asks": "Un juicio sobre lo que funcionó y lo que no con ese público, apoyado en lo que pasó en la sala.",
         "par": 3, "model": "Not everything landed"},
        {"id": "P3", "quote": "consider whether there are any subjects that comedians should leave alone",
         "asks": "Una reflexión matizada, mejor si sale del propio espectáculo, con una postura clara.",
         "par": 4, "model": "whether some subjects should be off limits"},
    ],
    "plan": [
        {"par": 1, "content": "La obra identificada: quién, qué espectáculo y de qué trata; frase que engancha",
         "points": []},
        {"par": 2, "content": "El estilo: ritmo y voz, con un número concreto como ejemplo", "points": ["P1"]},
        {"par": 3, "content": "La noche: lo que no funcionó con parte del público y cómo lo resolvió",
         "points": ["P2"]},
        {"par": 4, "content": "¿Temas prohibidos? Lo que importa es hacia quién apunta el chiste", "points": ["P3"]},
        {"par": 5, "content": "Veredicto y recomendación", "points": []},
    ],
    "model": {
        "title": "Small Mercies: Maeve Doran at the Corn Exchange",
        "paras": [
            {"heading": None,
             "text": "Maeve Doran doesn’t tell jokes so much as tell on herself. For seventy minutes, perched on a "
                     "bar stool with a glass of water she never touches, she works through a year in which her "
                     "father moved in, her marriage wobbled, her aunt died and her teenage son started a podcast about her. It "
                     "sounds bleak. It isn’t."},
            {"heading": None,
             "text": "Doran’s great gift is timing. She delivers her best lines almost as afterthoughts, in a flat, "
                     "conversational voice, and lets the silence do the rest. A long routine about teaching her "
                     "father to use a smartphone builds so patiently that by the time the payoff arrives – he has "
                     "been texting her husband for tips on handling her – the audience is already laughing in anticipation."},
            {"heading": None,
             "text": "Not everything landed. On the night I went, the crowd was a mixture of students and "
                     "pensioners, and a section on dating apps left the older half politely baffled. To her "
                     "credit, Doran noticed, abandoned the material with a rueful shrug and won the room back with "
                     "a story about her aunt’s disastrous funeral that had people of every age wiping their eyes."},
            {"heading": None,
             "text": "That funeral routine raises the question of whether some subjects should be off limits. "
                     "Doran’s implicit answer is that none are, provided the joke is aimed upwards or inwards "
                     "rather than at people who can’t answer back. Her material on grief works because she is its "
                     "main target; a comic mocking a stranger’s bereavement would be another matter entirely. "
                     "Taste, in other words, lies less in the topic than in the angle."},
            {"heading": None,
             "text": "Small Mercies is touring until March. If you think you’ve had your fill of confessional "
                     "comedy, go anyway: this is what it looks like when it’s done properly."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos, con ejemplos de la función: el estilo ilustrado con un número "
                            "({{=A long routine about teaching her father}}), lo que pasó en la sala ({{=left the "
                            "older half politely baffled}}) y una postura sobre los temas que sale del propio "
                            "espectáculo ({{=Taste, in other words, lies less in the topic than in the angle}}).",
                    "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Review reconocible: título con obra y lugar, espectáculo "
                                              "identificado desde la primera frase, evaluación y veredicto final "
                                              "({{=go anyway}}). Registro vivo con control: contracciones y frases "
                                              "cortas para el ritmo ({{=It sounds bleak. It isn’t.}}).",
                                      "theory": ["7.1", "7.2"]},
        "Organisation": {"text": "De la descripción al juicio y del juicio a la idea general; el párrafo 4 se "
                                 "engancha al 3 con {{=That funeral routine}}, y el cierre responde a la apertura "
                                 "con la recomendación.", "theory": ["7.3", "P1-7.4"]},
        "Language": {"text": "Léxico preciso del género ({{=routine}}, {{=payoff}}, {{=won the room back}}), "
                             "juego de palabras inicial ({{=tell on herself}}) y antítesis final; concesiva con "
                             "[[to her credit]] y condicional con [[provided]].", "theory": ["7.4", "P1-8.2"]},
    },
    "errors": [
        {"error": "Contar el espectáculo chiste a chiste",
         "why": "Resumir los números agota las palabras sin juzgar nada: {{describe the performer’s style}} pide "
                "cómo trabaja, no qué dice.", "codes": ["C2", "CA3"], "theory": ["7.3"]},
        {"error": "Olvidar [[on the night]]",
         "why": "{{evaluate how well the humour worked with the audience on the night}} pide hablar de la reacción "
                "del público concreto; una valoración general del humor deja el punto a medias.",
         "codes": ["C1"], "theory": ["2.2"]},
        {"error": "Convertir el tercer punto en un essay",
         "why": "Una disertación abstracta sobre la libertad de expresión, sin relación con el espectáculo, "
                "rompe el género y desequilibra el texto.", "codes": ["CA1", "C4"], "theory": ["7.3", "8.1"]},
        {"error": "Terminar sin veredicto",
         "why": "El lector de una review quiere saber si debe ir: sin recomendación, falla el efecto del género.",
         "codes": ["CA5", "O4"], "theory": ["7.1"]},
    ],
    "lex": ["tell on sb", "a rueful shrug", "win the room back", "have had one's fill of"],
}

P2 = [_ARTICLE, _REPORT, _REVIEW]
