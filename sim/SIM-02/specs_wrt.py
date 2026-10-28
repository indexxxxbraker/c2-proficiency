# SIM-02 · Writing · specs de la Part 1 (essay) y de las tres tareas de la Part 2
# Se monta con: python3 src/gen_SIM.py wrt sim/SIM-02
# Formato: cabecera de src/gen_WRT-P1.py (P1) y de src/gen_WRT-P2.py (cada tarea de P2).

# ---------- Part 1 · Essay ----------
P1 = {
    "texts": [
        {"title": "Everyone’s business",
         "text": "When fewer than six in ten people vote, the result is not a neutral sample of public opinion. "
                 "Those who turn out are disproportionately older and better off, and politicians, who know exactly "
                 "who votes, shape their promises accordingly. Making attendance at the polls a legal obligation, as "
                 "Australia has done since 1924, forces governments to answer to the whole population rather than to "
                 "the sections of it that reliably turn out. Nor is the burden a heavy one: citizens already accept "
                 "jury service and filling in the census as part of citizenship, and nobody is forced to support a candidate, "
                 "since a ballot can always be left blank."},
        {"title": "The right to stay at home",
         "text": "Low turnout is usually treated as a disease to be cured, but it is better understood as a symptom. "
                 "People stay at home because they believe that voting changes nothing, and fining them leaves that "
                 "belief untouched while hiding it from view. Compulsion also swells the count with the choices of "
                 "those who know little and care less, which hardly improves the quality of democratic decisions. "
                 "In a free society, declining to take part can itself be a considered political act, and it "
                 "deserves to be respected as one. If we want more people to vote, we should give them reasons to "
                 "do so, not penalties."},
    ],
    "relation": {"type": "Mismo objetivo, distinto diagnóstico",
                 "axis": "si la baja participación es un sesgo que la ley debe corregir obligando a votar o el "
                         "síntoma de un desencanto que la obligación solo taparía.",
                 "contact": "ninguno se opone a que vote más gente: el texto 1 quiere un electorado que refleje a toda "
                            "la población ({{forces governments to answer to the whole population}}) y el texto 2, "
                            "que defiende el derecho a abstenerse, no rechaza el objetivo sino el medio ({{If we want "
                            "more people to vote}}); discrepan sobre qué revela la abstención y sobre el remedio."},
    "key_points": [
        {"id": "T1·1", "source": "politicians, who know exactly who votes, shape their promises accordingly",
         "idea": "Con baja participación votan sobre todo los mayores y los acomodados, y los políticos legislan "
                 "para ellos; obligar a votar hace que los gobiernos respondan ante toda la población.",
         "par": 2, "model": "politicians tailor their policies to them"},
        {"id": "T1·2", "source": "Nor is the burden a heavy one",
         "idea": "La obligación es una carga pequeña, como el jurado o el censo, y no fuerza a apoyar a nadie: "
                 "siempre se puede votar en blanco.",
         "par": 3, "model": "presents the duty as a minor imposition"},
        {"id": "T2·1", "source": "it is better understood as a symptom",
         "idea": "La abstención es síntoma de que la gente cree que votar no cambia nada; multar no cura esa "
                 "creencia, la esconde, y además llena las urnas de votos poco informados.",
         "par": 2, "model": "abstention reflects a widespread conviction that voting is futile"},
        {"id": "T2·2", "source": "declining to take part can itself be a considered political act",
         "idea": "En una sociedad libre, no votar puede ser una decisión política legítima; para que vote más gente "
                 "hay que darle motivos, no sanciones.",
         "par": 3, "model": "staying away can be a deliberate statement"},
    ],
    "stance": {"type": "Matizar",
               "text": "A favor del voto obligatorio, pero con condiciones propias que responden a las objeciones del "
                       "texto 2: facilidades para votar, multas pequeñas y una casilla de «ninguno de los "
                       "anteriores» para que la protesta cuente."},
    "scheme": "integrado",
    "plan": [
        {"par": 1, "content": "La pregunta de fondo: a los dos les gustaría que votara más gente, pero leen de "
                              "forma distinta la abstención", "ideas": []},
        {"par": 2, "content": "Eje 1, qué revela la abstención: sesgo (texto 1) frente a síntoma (texto 2); "
                              "evaluación y respuesta propia al temor del voto desinformado",
         "ideas": ["T1·1", "T2·1", "propia"]},
        {"par": 3, "content": "Eje 2, la libertad: carga pequeña (texto 1) frente a abstención como protesta "
                              "(texto 2); evaluación y propuesta propia", "ideas": ["T1·2", "T2·2", "propia"]},
        {"par": 4, "content": "Postura: obligación con condiciones propias; cierre en antítesis",
         "ideas": ["propia"]},
    ],
    "model": [
        "Few democratic reforms divide opinion as sharply as compulsory voting. Both writers would like more "
        "citizens to vote; where they part company is over what a low turnout actually "
        "reveals, and therefore over whether the law should intervene.",
        "On what low turnout reveals, the first writer contends that when the elderly and affluent dominate "
        "turnout, politicians tailor their policies to them, so obliging everyone to vote would make governments accountable to all. The second "
        "counters that abstention reflects a widespread conviction that voting is futile, which compulsion would "
        "merely conceal while filling ballot boxes with ill-informed choices. The first diagnosis is the better "
        "supported, since the bias it describes is well documented. The second identifies a genuine "
        "malaise, but it assumes that reluctant voters will vote carelessly, when an obligation to vote may just "
        "as plausibly prompt people to inform themselves.",
        "On the question of liberty, the first writer presents the duty as a minor imposition, comparable to jury "
        "service, and notes that nobody is compelled to endorse a candidate. The second insists that staying "
        "away can be a deliberate statement, and that people should be persuaded rather than penalised. This has "
        "real force, yet staying at home is as mute a form of protest as a blank ballot paper; a formal ‘none "
        "of the above’ option would allow dissent to be counted rather than guessed at.",
        "On balance, I believe a legal duty to vote is justified, but only if voting is made as easy as "
        "possible, through automatic registration and weekend polling, and the duty is enforced with modest "
        "fines. Compulsion can make an electorate representative; only better politics can make it "
        "engaged.",
    ],
    "own_ideas": ["La respuesta al temor del voto desinformado ({{=an obligation to vote may just as plausibly "
                  "prompt people to inform themselves}}), la casilla para el voto de protesta ({{=a formal ‘none of "
                  "the above’ option}}) y las condiciones de la postura final ({{=automatic registration and weekend "
                  "polling}}, {{=modest fines}})."],
    "comments": {
        "Content": {"text": "Las cuatro ideas clave, comprensibles sin los textos, y los dos evaluados con razones: "
                            "el diagnóstico del texto 1 como {{=the better supported}}, el del texto 2 con un reparo "
                            "concreto ({{=it assumes that reluctant voters will vote carelessly}}). La postura "
                            "matiza: acepta la obligación con condiciones propias que responden a las objeciones del "
                            "texto 2.",
                    "theory": ["3.1", "5.2", "6.2"]},
        "Communicative Achievement": {"text": "Registro neutro-formal, sin contracciones y con la primera persona "
                                              "solo en la conclusión ({{=I believe}}). Los verbos de atribución "
                                              "distinguen las voces y su fuerza: {{=contends}}, {{=counters}}, "
                                              "{{=notes}}, {{=insists}}.",
                                      "theory": ["4.3", "6.3"]},
        "Organisation": {"text": "Esquema integrado por ejes: el párrafo 2 enfrenta los dos diagnósticos y el 3 las "
                                 "dos ideas de libertad, cada uno con su evaluación. Las frases iniciales anuncian el "
                                 "eje ({{=On what low turnout reveals}}, {{=On the question of liberty}}), y la conclusión responde a la pregunta que "
                                 "abre la introducción ({{=whether the law should intervene}}).",
                         "theory": ["7.2", "7.3", "7.4"]},
        "Language": {"text": "Léxico preciso ({{=a genuine malaise}}, {{=tailor their policies}}, {{=ill-informed "
                             "choices}}) y estructuras que matizan: comparación de igualdad ({{=as mute a form of "
                             "protest as a blank ballot paper}}), aliteración en el contraste ({{=persuaded rather "
                             "than penalised}}), concesiva con [[yet]] y antítesis final ({{=Compulsion can make an "
                             "electorate representative; only better politics can make it engaged}}).",
                     "theory": ["8.1", "8.2"]},
    },
    "errors": [
        {"error": "Resumir los datos en lugar de las ideas",
         "why": "{{fewer than six in ten people}} o {{since 1924}} son apoyos; la idea es que la baja participación "
                "sesga las políticas hacia quienes votan.",
         "codes": ["C1"], "theory": ["3.1", "4.4"]},
        {"error": "Leer el texto 2 como contrario a que se vote más",
         "why": "El autor defiende el derecho a abstenerse, pero no rechaza que vote más gente ({{If we want more "
                "people to vote}}): lo que rechaza es el remedio. Presentarlo como contrario a la participación "
                "deforma la relación entre los textos.",
         "codes": ["C4", "C1"], "theory": ["3.3"]},
        {"error": "Copiar la frase más redonda",
         "why": "{{those who know little and care less}} es la expresión más vistosa del texto 2 y, copiada, no "
                "puntúa: hay que reformularla ([[ill-informed choices]]).",
         "codes": ["L4"], "theory": ["4.1", "4.2"]},
        {"error": "Opinar sin evaluar",
         "why": "Decir que uno votaría igualmente no valora los argumentos: hay que juzgar si la comparación con "
                "{{jury service and filling in the census}} se sostiene o si el voto en blanco basta como protesta.",
         "codes": ["C2"], "theory": ["5.1"]},
        {"error": "Una postura sin idea propia",
         "why": "Elegir un texto y repetir sus argumentos deja vacío el criterio C3: la postura tiene que aportar "
                "algo que no esté en ninguno de los dos (aquí, la casilla de protesta y las condiciones).",
         "codes": ["C3"], "theory": ["6.1", "6.2"]},
    ],
    "lex": ["tailor sth to sb", "a genuine malaise", "a mute form of protest", "part company over sth",
            "know little and care less", "persuaded rather than penalised"],
}

# ---------- Part 2 · tres tareas (preguntas 2-4), de géneros distintos ----------
_LETTER = {
    "genre": "letter", "register": "formal",
    "prompt": "A national newspaper recently published an article arguing that tipping in restaurants and cafés "
              "should be abolished and replaced by higher wages. You decide to write a letter to the editor "
              "responding to the article. In your letter, you should explain how tipping affects staff who rely on "
              "tips, evaluate the arguments for abolishing it and suggest what a fairer system might look "
              "like.",
    "analysis": [
        {"dato": "Contexto", "quote": "an article arguing that tipping in restaurants and cafés should be abolished",
         "note": "Respondes a un artículo concreto: hay que identificarlo al principio y dialogar con su tesis, no "
                 "escribir sobre las propinas en general."},
        {"dato": "Lector", "quote": "a letter to the editor",
         "note": "El director, y a través de él los lectores del periódico: registro formal, argumentos razonados, "
                 "nada de tono de queja personal."},
        {"dato": "Papel", "quote": "",
         "note": "El enunciado no fija quién eres; una experiencia propia (haber trabajado de camarero) da "
                 "autoridad a la carta y alimenta el primer punto."},
        {"dato": "Propósito", "quote": "evaluate the arguments for abolishing it",
         "note": "Evaluar exige conceder lo que el artículo tiene de razón antes de discrepar: una carta que solo "
                 "lo ataca falla el punto."},
        {"dato": "Puntos", "quote": "",
         "note": "Tres verbos: explicar (efectos en quien recibe la propina), evaluar (los argumentos del "
                 "artículo) y proponer (un sistema más justo)."},
    ],
    "points": [
        {"id": "P1", "quote": "explain how tipping affects staff who rely on tips",
         "asks": "Efectos concretos en los trabajadores, buenos y malos, con algún matiz (quién no recibe nada).",
         "par": 2, "model": "tips make earnings unpredictable"},
        {"id": "P2", "quote": "evaluate the arguments for abolishing it",
         "asks": "Un juicio razonado: qué argumento del artículo es sólido y cuál falla, y por qué.",
         "par": 3, "model": "is difficult to dispute"},
        {"id": "P3", "quote": "suggest what a fairer system might look like",
         "asks": "Una propuesta concreta y viable que responda a los problemas señalados antes.",
         "par": 4, "model": "A fairer approach would be"},
    ],
    "plan": [
        {"par": 1, "content": "Motivo de la carta: el artículo identificado y la experiencia que avala al autor",
         "points": []},
        {"par": 2, "content": "Efectos de la propina: ingresos irregulares y reparto desigual, pero también "
                              "reconocimiento", "points": ["P1"]},
        {"par": 3, "content": "Evaluación: el argumento del salario justo es sólido; el supuesto de que subirán "
                              "los sueldos, no", "points": ["P2"]},
        {"par": 4, "content": "Propuesta: sueldo base digno, propina voluntaria e íntegra para el personal, "
                              "repartida con transparencia", "points": ["P3"]},
        {"par": 5, "content": "Cierre: la propina es síntoma del sueldo bajo, no su causa", "points": []},
    ],
    "model": {
        "title": None,
        "salutation": "Dear Sir or Madam,",
        "paras": [
            {"heading": None,
             "text": "I am writing in response to Martin Hale’s article ‘Time to stop tipping’ (14 March), which "
                     "called for gratuities to be scrapped in favour of higher pay. Having worked as a waiter for "
                     "three years while I was a student, I read it with considerable interest and some "
                     "reservations."},
            {"heading": None,
             "text": "Mr Hale is right that tips make earnings unpredictable. On a busy Saturday I might take home "
                     "more in tips than in the rest of the week combined; on a wet Tuesday, almost nothing. Planning a "
                     "budget around such fluctuations is difficult, and staff who work quieter shifts, or who "
                     "never leave the kitchen, often see little of the money. Yet tips are not merely income. For "
                     "many of my former colleagues, they were the only tangible sign that a customer had noticed "
                     "their effort."},
            {"heading": None,
             "text": "The article’s central argument, that employers rather than customers should be responsible "
                     "for paying a decent wage, is difficult to dispute. Far less convincing is the assumption that "
                     "doing away with tips would automatically raise pay. Without legal safeguards, the likeliest "
                     "outcome is higher menu prices and unchanged wages, with the difference quietly absorbed by "
                     "the business."},
            {"heading": None,
             "text": "A fairer approach would be to guarantee a decent basic wage, to keep tipping as a voluntary "
                     "extra, and to require by law that every penny, whether left in cash, added to a card payment "
                     "or charged as a service fee, reaches the staff and is shared openly among them, kitchen "
                     "porters and cooks included. Such a system would reward good service without leaving anyone’s "
                     "rent at the mercy of the weather."},
            {"heading": None,
             "text": "Tipping, in short, is a symptom of low pay rather than its cause. Abolishing it without "
                     "addressing wages would simply remove one of the few rewards that the people who serve us "
                     "still receive."},
        ],
        "closing": "Yours faithfully,",
        "signature": "Elena Marsh",
    },
    "comments": {
        "Content": {"text": "Los tres puntos, cada uno con el desarrollo que pide su verbo: efectos con ejemplos y "
                            "un matiz sobre quién no cobra propinas ({{=who never leave the kitchen}}), una "
                            "evaluación que concede y discrepa ({{=Far less convincing is the assumption}}) y una "
                            "propuesta concreta que responde a ambos problemas.",
                    "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Carta al director reconocible: identifica el artículo desde la "
                                              "primera frase ({{=I am writing in response to}}), justifica la voz "
                                              "del autor con su experiencia y mantiene un registro formal, sin "
                                              "contracciones, con [[Dear Sir or Madam]] y [[Yours faithfully]].",
                                      "theory": ["5.1", "5.2", "5.3"]},
        "Organisation": {"text": "Un párrafo por punto, con frases iniciales que anuncian su función ({{=Mr Hale is "
                                 "right that}}, {{=A fairer approach would be}}), y un cierre que retoma la idea del "
                                 "sueldo y responde a la tesis del artículo.",
                         "theory": ["3.2", "P1-7.4"]},
        "Language": {"text": "Léxico preciso ({{=gratuities}}, {{=quietly absorbed by the business}}, {{=at the "
                             "mercy of the weather}}) y estructuras variadas: participio inicial ({{=Having worked "
                             "as a waiter}}), inversión de la comparación ({{=Far less convincing is}}) y antítesis "
                             "final ({{=a symptom of low pay rather than its cause}}).",
                     "theory": ["5.4", "P1-8.2"]},
    },
    "errors": [
        {"error": "No identificar el artículo",
         "why": "Una carta al director que no dice a qué responde pierde el contexto que da sentido a "
                "{{responding to the article}}.", "codes": ["CA1", "C3"], "theory": ["5.3"]},
        {"error": "Atacar el artículo sin evaluarlo",
         "why": "{{evaluate the arguments for abolishing it}} pide sopesar: reconocer lo que tiene de razón antes "
                "de discrepar. Una refutación sin concesiones se queda en queja.", "codes": ["C2", "CA3"],
         "theory": ["2.2", "5.4"]},
        {"error": "Hablar solo de los clientes",
         "why": "El primer punto pregunta por {{staff who rely on tips}}: centrarse en si a los clientes les "
                "molesta dejar propina no lo responde.", "codes": ["C4", "C1"], "theory": ["2.2"]},
        {"error": "Registro de conversación",
         "why": "Contracciones, preguntas retóricas en cadena o [[Mr Hale has got it all wrong!]] no encajan en "
                "una carta formal a un periódico.", "codes": ["CA2"], "theory": ["5.2", "3.1"]},
    ],
    "lex": ["gratuities", "scrap sth in favour of sth", "do away with sth", "absorb (a cost)",
            "at the mercy of sth", "kitchen porter"],
}

_ARTICLE = {
    "genre": "article", "register": "vivo",
    "prompt": "A sports magazine is running a series called ‘The sport nobody watches’. Readers are invited to send "
              "in articles about a sport they enjoy that receives little attention. Your article should describe "
              "what makes the sport appealing to those who take part, explain why it attracts so few spectators and "
              "consider whether it would benefit from greater media coverage.",
    "analysis": [
        {"dato": "Contexto", "quote": "a series called ‘The sport nobody watches’",
         "note": "El título de la serie da el ángulo: un deporte minoritario visto desde dentro, con humor sobre su "
                 "falta de público."},
        {"dato": "Lector", "quote": "A sports magazine",
         "note": "Aficionados al deporte que no conocen el tuyo: hay que explicar lo básico en dos frases y hacer "
                 "que les apetezca probarlo."},
        {"dato": "Papel", "quote": "a sport they enjoy",
         "note": "Escribes como practicante: la primera persona y la experiencia propia son el material del "
                 "artículo."},
        {"dato": "Propósito", "quote": "consider whether it would benefit from greater media coverage",
         "note": "El último punto pide sopesar ventajas e inconvenientes de salir más en los medios, no "
                 "reclamarlo sin más."},
        {"dato": "Registro", "quote": "",
         "note": "Vivo: título con gancho, apertura con una escena, frases cortas para el ritmo, humor y "
                 "contracciones ocasionales."},
    ],
    "points": [
        {"id": "P1", "quote": "describe what makes the sport appealing to those who take part",
         "asks": "Lo que engancha a los jugadores, con detalles concretos del juego, no elogios genéricos.",
         "par": 2, "model": "What makes it addictive"},
        {"id": "P2", "quote": "explain why it attracts so few spectators",
         "asks": "La causa de la falta de público, explicada con una imagen concreta.",
         "par": 3, "model": "Why, then, does almost nobody watch?"},
        {"id": "P3", "quote": "consider whether it would benefit from greater media coverage",
         "asks": "Sopesar: qué ganaría y qué podría perder el deporte con más cobertura, y una postura.",
         "par": 4, "model": "Would more coverage change that?"},
    ],
    "plan": [
        {"par": 1, "content": "Apertura con una escena en la piscina y presentación del deporte", "points": []},
        {"par": 2, "content": "Por qué engancha: el relevo constante, el trabajo en equipo y lo democrático del "
                              "juego", "points": ["P1"]},
        {"par": 3, "content": "Por qué nadie lo ve: desde el borde no se ve nada", "points": ["P2"]},
        {"par": 4, "content": "¿Más cobertura? Lo que ganaría (jugadores, dinero) y lo que perdería",
         "points": ["P3"]},
        {"par": 5, "content": "Cierre: invitación a jugar, que recoge el título", "points": []},
    ],
    "model": {
        "title": "The Best Game You’ll Never See",
        "paras": [
            {"heading": None,
             "text": "Every Thursday night, in a municipal pool that smells faintly of chlorine and chips, twelve "
                     "adults in masks, snorkels and fins spend an hour fighting over a lump of lead at the bottom of "
                     "the deep end. This is underwater hockey, and I’ve been hooked on it for six years."},
            {"heading": None,
             "text": "The rules are simple enough: two teams of six use short sticks to push a puck along the floor "
                     "of the pool into the opposing goal. What makes it addictive is that nobody can stay down for "
                     "long. A match is a constant relay of players diving, passing and surfacing for air, so "
                     "teamwork matters far more than individual brilliance. It’s also wonderfully democratic. Size "
                     "and strength count for little underwater; timing, breath control and nerve count for "
                     "everything."},
            {"heading": None,
             "text": "Why, then, does almost nobody watch? The answer is painfully literal: there’s nothing to see. "
                     "From the side of the pool, a game looks like a cluster of fins thrashing about on the surface, "
                     "while the real action unfolds, blurred and silent, two metres below. Even devoted friends "
                     "rarely come more than once."},
            {"heading": None,
             "text": "Would more coverage change that? Possibly. Underwater cameras have made recent championships "
                     "surprisingly gripping to watch online, and a little exposure might bring in new players, along "
                     "with the money to pay for pool time, which is our biggest expense. Yet I’m not convinced the "
                     "game should be reshaped for an audience. Much of its charm lies in being played purely for its "
                     "own sake, without anyone performing for the cameras or rules being bent to suit a "
                     "broadcaster’s schedule."},
            {"heading": None,
             "text": "So come and play rather than watch. You’ll swallow a fair amount of water, and you’ll almost "
                     "certainly never be famous. But you may well discover, as I did, that some of the best things "
                     "happen out of sight."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos, cada uno con detalles concretos: el atractivo para quien juega "
                            "({{=a constant relay of players diving, passing and surfacing for air}}), una causa "
                            "clara de la falta de público ({{=there’s nothing to see}}) y una valoración de la "
                            "cobertura que concede antes de discrepar ({{=Possibly}}, {{=Yet I’m not "
                            "convinced}}).", "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Article reconocible: título con gancho que juega con el de la "
                                              "serie, apertura con una escena y cierre que se dirige al lector "
                                              "({{=So come and play rather than watch}}). Registro vivo con "
                                              "control: contracciones, humor ({{=chlorine and chips}}) y frases "
                                              "cortas.", "theory": ["4.1", "4.2", "4.4"]},
        "Organisation": {"text": "Progresión de la escena al juicio: qué es, por qué engancha, por qué no se ve y "
                                 "qué haría más cobertura. Las preguntas al principio de los párrafos 3 y 4 "
                                 "anuncian su función ({{=Why, then, does almost nobody watch?}}), y el cierre "
                                 "recoge el título ({{=happen out of sight}}).",
                         "theory": ["4.3", "P1-7.4"]},
        "Language": {"text": "Léxico preciso y visual ({{=fins thrashing about on the surface}}, {{=blurred and "
                             "silent}}, {{=rules being bent}}) y estructuras que dan ritmo: paralelismo con "
                             "antítesis ({{=Size and strength count for little underwater; timing, breath control "
                             "and nerve count for everything}}) y concesiva con [[yet]].",
                     "theory": ["4.5", "P1-8.2"]},
    },
    "errors": [
        {"error": "Explicar el reglamento entero",
         "why": "El primer punto pide {{what makes the sport appealing}}: dos frases de reglas bastan; el resto "
                "del espacio es para lo que se siente jugando.", "codes": ["C2", "C4"], "theory": ["2.2"]},
        {"error": "Contestar el último punto con un sí entusiasta",
         "why": "{{consider whether}} pide sopesar: qué ganaría el deporte y qué podría perder con más "
                "cobertura.", "codes": ["C2", "CA3"], "theory": ["2.2", "4.5"]},
        {"error": "Escribirlo como un report",
         "why": "Encabezados, recomendaciones numeradas y tono impersonal convierten el texto en otro género y "
                "pierden al lector de una revista.", "codes": ["CA1", "CA2"], "theory": ["4.1", "4.2"]},
        {"error": "Un título que solo nombra el deporte",
         "why": "[[Underwater Hockey]] informa, pero no engancha: en un article el título forma parte del "
                "efecto sobre el lector.", "codes": ["CA5"], "theory": ["4.4"]},
    ],
    "lex": ["be hooked on sth", "count for little / for everything", "thrash about", "painfully literal",
            "bend the rules", "for its own sake"],
}

_REPORT = {
    "genre": "report", "register": "neutro",
    "prompt": "Your town has been twinned with a town abroad for many years, and last summer you took part in an "
              "exchange visit there. The twinning association has asked you to write a report for its committee. "
              "Your report should outline the main activities of the visit, assess what participants gained from "
              "it and recommend ways of attracting more young people to future exchanges.",
    "analysis": [
        {"dato": "Contexto", "quote": "The twinning association has asked you to write a report",
         "note": "La asociación quiere decidir cómo mejorar los intercambios: el report tiene que dar hechos, un "
                 "juicio y propuestas que pueda aplicar."},
        {"dato": "Lector", "quote": "its committee",
         "note": "Un comité de voluntarios que conoce el hermanamiento: registro neutro, claro y sin "
                 "contracciones, con encabezados."},
        {"dato": "Papel", "quote": "you took part in an exchange visit",
         "note": "Hablas como participante: puedes usar tu experiencia, pero conviene apoyarla en la opinión del "
                 "grupo (un cuestionario)."},
        {"dato": "Propósito", "quote": "recommend ways of attracting more young people",
         "note": "La última sección decide el valor del report: propuestas concretas para un problema que el "
                 "apartado anterior ha detectado."},
        {"dato": "Puntos", "quote": "",
         "note": "Tres verbos (outline, assess, recommend): resumir, valorar y proponer, cada uno en su sección."},
    ],
    "points": [
        {"id": "P1", "quote": "outline the main activities of the visit",
         "asks": "Un resumen breve de lo que se hizo, destacando lo más valorado. [[Outline]] pide brevedad.",
         "par": 2, "model": "The week combined official and informal events"},
        {"id": "P2", "quote": "assess what participants gained from it",
         "asks": "Un juicio con datos: qué ganaron los participantes y qué falló, como base de las propuestas.",
         "par": 3, "model": "staying in private homes had given them an insight"},
        {"id": "P3", "quote": "recommend ways of attracting more young people to future exchanges",
         "asks": "Propuestas concretas y viables para atraer a jóvenes, ligadas al problema detectado.",
         "par": 4, "model": "To attract younger people"},
    ],
    "plan": [
        {"par": 1, "content": "Propósito del report y fuente (cuestionario al grupo)", "points": []},
        {"par": 2, "content": "Actividades: actos oficiales e informales; lo más valorado", "points": ["P1"]},
        {"par": 3, "content": "Lo que ganaron los participantes y el problema: un grupo de edad muy alta",
         "points": ["P2"]},
        {"par": 4, "content": "Tres recomendaciones para atraer a jóvenes", "points": ["P3"]},
        {"par": 5, "content": "Conclusión: valoración global", "points": []},
    ],
    "model": {
        "title": "The Summer Exchange with Belcourt: A Report for the Committee",
        "paras": [
            {"heading": "Introduction",
             "text": "This report reviews last summer’s exchange visit to our twin town, Belcourt, and suggests how "
                     "future exchanges might appeal to a wider age range. It draws on my own experience and on a "
                     "short questionnaire completed by eighteen of the twenty-four people in the group."},
            {"heading": "The programme",
             "text": "The week combined official and informal events. Alongside the civic reception at the town "
                     "hall, the programme included a tour of the local cheese cooperative, a day’s walking in the "
                     "hills and a joint concert given by the two towns’ choirs. Most memorable, according to the "
                     "questionnaire, were the evenings spent with host families."},
            {"heading": "Benefits and one weakness",
             "text": "Almost every respondent felt that staying in private homes had given them an insight into "
                     "daily life that no hotel could offer. Several said the week had revived their French, and "
                     "three participants have since arranged private visits to their hosts. One weakness was mentioned "
                     "repeatedly, however: with an average age of over sixty, the group hardly reflected the town, "
                     "and the few teenagers present found the formal events tedious."},
            {"heading": "Recommendations",
             "text": "To attract younger people, the association could, first, work with schools and sports clubs to "
                     "organise exchanges built around shared interests, such as a football tournament or a music "
                     "workshop. Second, part of each programme might be planned by young participants themselves. "
                     "Finally, the exchange should be promoted on social media rather than only in the quarterly "
                     "newsletter, which few residents under fifty read."},
            {"heading": "Conclusion",
             "text": "Overall, the visit was a considerable success. With a programme designed partly by and for "
                     "younger residents, future exchanges could ensure that the link between the two towns outlives "
                     "the association’s present members."},
        ]},
    "comments": {
        "Content": {"text": "Los tres puntos en su sección: un resumen breve de las actividades, una valoración con "
                            "datos que detecta el problema ({{=the group hardly reflected the town}}) y tres "
                            "recomendaciones que responden a él ({{=built around shared interests}}).",
                    "theory": ["2.2", "8.1"]},
        "Communicative Achievement": {"text": "Report neutro: claro y sin contracciones, con las fuentes citadas "
                                              "al principio ({{=It draws on my own experience}}) y la opinión del "
                                              "grupo por delante de la propia ({{=according to the "
                                              "questionnaire}}). El comité puede actuar con lo que lee.",
                                      "theory": ["6.1", "6.2"]},
        "Organisation": {"text": "Título informativo, encabezados con contenido y una sección por punto. Las "
                                 "recomendaciones se enumeran ({{=first}}, {{=Second}}, {{=Finally}}) y salen del "
                                 "problema descrito en la sección anterior.", "theory": ["6.3", "3.2"]},
        "Language": {"text": "Léxico propio del género ({{=respondent}}, {{=One weakness was mentioned "
                             "repeatedly}}) con algo de color en el registro neutro ({{=revived their French}}), "
                             "inversión para destacar ({{=Most memorable, according to the questionnaire, were}}) y "
                             "un cierre con [[outlive]].", "theory": ["6.4", "P1-8.2"]},
    },
    "errors": [
        {"error": "Un diario de viaje",
         "why": "{{outline the main activities}} pide un resumen; contar el viaje día a día deja sin espacio la "
                "valoración y las propuestas.", "codes": ["C2", "CA1"], "theory": ["2.2", "6.3"]},
        {"error": "Recomendaciones sin relación con el análisis",
         "why": "Si la sección anterior no ha dicho por qué faltan jóvenes, las propuestas para {{attracting more "
                "young people}} quedan en el aire.", "codes": ["O2", "C2"], "theory": ["6.3"]},
        {"error": "Solo la opinión propia",
         "why": "{{assess what participants gained}} habla de todos: un report convence más si se apoya en datos "
                "del grupo y no solo en la experiencia de quien escribe.", "codes": ["C4", "CA3"],
         "theory": ["6.2"]},
        {"error": "Encabezados vacíos",
         "why": "[[Part 1]], [[Part 2]] no orientan al comité; cada encabezado tiene que decir de qué trata la "
                "sección.", "codes": ["O1"], "theory": ["6.1", "3.2"]},
    ],
    "lex": ["twin town", "civic reception", "revive one’s French", "outlive sth", "hardly reflect sth"],
}

P2 = [_LETTER, _ARTICLE, _REPORT]
