# SIM-02 · Listening · specs de las Parts 1-4
# Se monta con: python3 src/gen_SIM.py lst sim/SIM-02 --stage verify | audio | asr N | pdf
# Formato de cada spec: cabecera de src/gen_LST-P1..P4. Voces sin repetir en todo el paper; narrador: Thomas.

# ---------- Part 1 · Three extracts ----------
P1 = {
    "num": "S02",
    "subtitle": "SIM-02 · Part 1",
    "difficulty": 3,
    "wpm": 170,
    "lex": ["won’t hear of sth", "a stickler for sth", "single sb out", "that rings a bell", "mouth the words",
            "get away with sth", "on those odds", "learn to live with sth", "flop (n./v.)", "snigger at sb",
            "do one’s homework", "grating", "I can’t argue with that"],
    "extracts": [
        {"ctx": "You hear two friends talking about a community choir that the woman has joined.",
         "speakers": {"Woman": "Emily", "Man": "Ryan"},
         "turns": [
             ("Woman", "You’ll laugh, but I’ve actually joined that choir that meets in the library on Tuesdays."),
             ("Man", "I’m not laughing, I’m impressed. You always said you couldn’t sing a note."),
             ("Woman", "I still can’t, really. That’s why I was dreading some sort of audition. But Maggie, the "
                       "woman who runs it, won’t hear of auditions. Her view is that anyone who can speak can sing, "
                       "and that what stops most people is having been told otherwise at school."),
             ("Man", "That rings a bell. I was told to just mouth the words in the school play."),
             ("Woman", "Exactly. Not that she lets us get away with anything. She’s a stickler for going over the "
                       "same few bars until we get them right. But she never singles anyone out."),
             ("Man", "So what keeps you going back? The music?"),
             ("Woman", "Partly. But mostly it’s that for two hours I can’t think about anything else. You can’t "
                       "worry about work and count beats at the same time."),
             ("Man", "I know what you mean. That’s how I feel about climbing, although your hobby is rather less "
                     "likely to land you in hospital."),
         ],
         "items": [
             {"n": 1, "type": "Detalle",
              "stem": "What does the woman say about the choir leader?",
              "options": ["She sets high standards without embarrassing individual singers.",
                          "She holds auditions so that newcomers can be placed in the right section.",
                          "She believes that music lessons in schools do more harm than good."],
              "key": "A",
              "evidence": ["She’s a stickler for going over the same few bars until we get them right",
                           "But she never singles anyone out"],
              "why": "Las dos mitades de la opción están en una misma intervención: exige ({{She’s a stickler for "
                     "going over the same few bars until we get them right}}) y no deja a nadie en evidencia "
                     "({{But she never singles anyone out}}). [[High standards]] recoge [[stickler]] y [[without "
                     "embarrassing individual singers]], [[never singles anyone out]].",
              "theory": ["5.3", "3.1"],
              "distractors": {
                  "B": {"kinds": ["4.6"],
                        "why": "Dice lo contrario: la directora {{won’t hear of auditions}}."},
                  "C": {"kinds": ["4.1", "4.5"],
                        "why": "Recoge {{at school}}, pero lo que culpa la directora es que a la gente le dijeran "
                               "que no sabía cantar ({{having been told otherwise at school}}), no las clases de "
                               "música en general."}}},
             {"n": 2, "type": "Actitud y opinión",
              "stem": "What does the woman value most about the choir?",
              "options": ["the chance to sing music she would not otherwise hear",
                          "the opportunity to make friends outside work",
                          "the way it stops her dwelling on other concerns"],
              "key": "C",
              "evidence": ["mostly it’s that for two hours I can’t think about anything else"],
              "why": "A la pregunta del amigo responde con una concesión y luego lo principal: {{Partly}} … {{But "
                     "mostly it’s that for two hours I can’t think about anything else}}, y lo explica: {{You can’t "
                     "worry about work and count beats at the same time}}. La segunda idea es la que manda (§3.3).",
              "theory": ["3.3", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.2"],
                        "why": "La música se menciona y se rebaja: {{The music?}} — {{Partly}}. No es lo que más "
                               "valora."},
                  "B": {"kinds": ["4.8", "4.1"],
                        "why": "Recoge {{work}}, pero la mujer no habla de amistades: el trabajo aparece como lo que "
                               "deja de preocuparle."}}},
         ]},
        {"ctx": "You hear a volcanologist talking about her work.",
         "speakers": {"Volcanologist": "Natasha"},
         "turns": [
             ("Volcanologist",
              "Whenever I tell people what I do, they picture me in a heat-proof suit, standing at the edge of a "
              "crater while lava spurts out behind me. I have done that, once or twice, but it’s a tiny part of the "
              "job. Most of my working life is spent in front of a screen, studying graphs of ground movement and "
              "gas readings, looking for changes so slight that you could easily mistake them for a fault in the "
              "equipment. The science, frankly, is the straightforward bit. What keeps me awake is having to tell "
              "a local mayor that there’s, say, a thirty per cent chance of an eruption in the next month. Should "
              "she evacuate twenty thousand people on those odds? If she does and nothing happens, she’ll be "
              "reluctant to do it again, and so will they. If she doesn’t, and it does erupt, the consequences "
              "hardly bear thinking about. I can give her the best numbers available, but I can’t make the "
              "decision any easier, and that’s something I’ve had to learn to live with."),
         ],
         "items": [
             {"n": 3, "type": "Detalle",
              "stem": "What does the volcanologist say about most of her working time?",
              "options": ["It is spent on visits to the craters of active volcanoes.",
                          "It is largely taken up with checking that equipment works.",
                          "It involves detecting very subtle signals in her data."],
              "key": "C",
              "evidence": ["looking for changes so slight that you could easily mistake them for a fault in the "
                           "equipment"],
              "why": "{{Most of my working life is spent in front of a screen}}, buscando {{changes so slight that "
                     "you could easily mistake them for a fault in the equipment}}. [[Very subtle signals]] "
                     "parafrasea [[changes so slight]].",
              "theory": ["5.3", "2.4"],
              "distractors": {
                  "A": {"kinds": ["4.2"],
                        "why": "Es la imagen que tiene la gente, y ella la rebaja: {{it’s a tiny part of the "
                               "job}}."},
                  "B": {"kinds": ["4.1"],
                        "why": "Eco de {{a fault in the equipment}}: los fallos de los aparatos aparecen solo como "
                               "aquello con lo que se pueden confundir los cambios."}}},
             {"n": 4, "type": "Sentimiento",
              "stem": "What does the volcanologist find hardest about her job?",
              "options": ["persuading local people to leave their homes when necessary",
                          "accepting that her forecasts cannot resolve the dilemma officials face",
                          "keeping up with the science of predicting eruptions"],
              "key": "B",
              "evidence": ["I can give her the best numbers available, but I can’t make the decision any easier"],
              "why": "Lo que le quita el sueño es la decisión de la alcaldesa ({{What keeps me awake is having to "
                     "tell a local mayor}}), y lo resume al final: {{I can give her the best numbers available, but "
                     "I can’t make the decision any easier}}. [[Accepting]] recoge [[something I’ve had to learn to "
                     "live with]].",
              "theory": ["3.3", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.4", "4.1"],
                        "why": "La que decide si se evacua es la alcaldesa ({{Should she evacuate twenty thousand "
                               "people}}); la vulcanóloga no habla de convencer a nadie."},
                  "C": {"kinds": ["4.6"],
                        "why": "Dice lo contrario: {{The science, frankly, is the straightforward bit}}."}}},
         ]},
        {"ctx": "You hear two friends discussing a podcast about failed inventions.",
         "speakers": {"Man": "Andrew", "Woman": "Sonia"},
         "turns": [
             ("Man", "Have you heard that podcast about inventions that flopped? Someone at work recommended it."),
             ("Woman", "I’ve listened to a few episodes. The one about the little electric car from the eighties "
                       "was brilliant."),
             ("Man", "I gave up after two, I’m afraid. The presenter seems to think every failure is hilarious. "
                     "There’s an awful lot of sniggering at people who lost everything."),
             ("Woman", "I’d have said she was laughing with them rather than at them. And she certainly does her "
                       "homework. She tracks down the inventors’ families, reads their letters…"),
             ("Man", "Maybe so. I just found the tone grating."),
             ("Woman", "Fair enough. What I like, though, is that it shows how often failure was simply a matter of "
                       "bad timing. Half the ideas that flopped came back twenty years later and made somebody else "
                       "a fortune."),
             ("Man", "Now that I can’t argue with. Most of what’s on my phone was somebody’s failure first."),
         ],
         "items": [
             {"n": 5, "type": "Actitud y opinión",
              "stem": "What is the man’s opinion of the presenter?",
              "options": ["She is too ready to make fun of other people’s misfortunes.",
                          "She has not looked into the inventors’ lives carefully enough.",
                          "She spends too long on each episode’s subject."],
              "key": "A",
              "evidence": ["The presenter seems to think every failure is hilarious",
                           "There’s an awful lot of sniggering at people who lost everything"],
              "why": "La crítica está en dos frases concretas: {{The presenter seems to think every failure is "
                     "hilarious}} y {{There’s an awful lot of sniggering at people who lost everything}}. [[Make "
                     "fun of]] parafrasea [[sniggering at]] y [[misfortunes]], [[people who lost everything]]. "
                     "Cuando ella lo defiende, él no cambia de opinión: {{I just found the tone grating}}.",
              "theory": ["3.4", "5.3"],
              "distractors": {
                  "B": {"kinds": ["4.4"],
                        "why": "De la investigación habla ella ({{she certainly does her homework}}), y él no la "
                               "discute: {{Maybe so}}. Su queja es el tono."},
                  "C": {"kinds": ["4.8"],
                        "why": "Nadie habla de la duración de los episodios; él lo dejó por el tono ({{I gave up "
                               "after two}})."}}},
             {"n": 6, "type": "Acuerdo",
              "stem": "What do the two friends agree about?",
              "options": ["The episode about the electric car was the best one.",
                          "The presenter treats the inventors with respect.",
                          "Many failed ideas were simply launched at the wrong time."],
              "key": "C",
              "evidence": ["it shows how often failure was simply a matter of bad timing",
                           "Now that I can’t argue with"],
              "why": "Ella propone la idea ({{it shows how often failure was simply a matter of bad timing}}), la "
                     "apoya con un dato ({{came back twenty years later}}) y él la suscribe sin reservas: {{Now that "
                     "I can’t argue with}} (§3.6). [[At the wrong time]] parafrasea [[bad timing]].",
              "theory": ["3.6", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.4"],
                        "why": "Solo lo dice ella ({{was brilliant}}); él dejó el pódcast después de dos "
                               "episodios."},
                  "B": {"kinds": ["4.4", "4.6"],
                        "why": "Es la opinión de ella ({{laughing with them rather than at them}}); él no está de "
                               "acuerdo: {{I just found the tone grating}}."}}},
         ]},
    ],
}

# ---------- Part 2 · Sentence completion ----------
P2 = {
    "num": "S02",
    "subtitle": "SIM-02 · Part 2",
    "difficulty": 3,
    "wpm": 170,
    "first": 7,
    "voice": "Mitchell",
    "ctx": "You will hear a historian called Daniel Reeve giving a talk about the nineteenth-century trade in "
           "natural ice.",
    "title": "The frozen water trade",
    "lex": ["hardly kinder", "be only too glad to", "come up with sth", "set about doing sth",
            "on the understanding that", "bring down a fever", "the decisive blow", "all but vanish",
            "melt away (fig.)"],
    "paragraphs": [
        "Good evening. If I asked you to name the most unlikely export in history, I doubt many of you would "
        "suggest frozen water. Yet for most of the nineteenth century, ice cut from the lakes and ponds of New "
        "England was shipped all over the world, and the man who started it all was a young Bostonian called "
        "Frederic Tudor. In 1806 Tudor loaded a ship with ice and sent it south to the Caribbean. Havana would "
        "later become one of his best markets, but that first cargo went to the island of Martinique, and it was "
        "a disaster. Much of the ice arrived intact, but nobody there had the faintest idea what to do with it, "
        "and most of it simply melted on the quayside.",

        "The years that followed were hardly kinder. Shipments were lost, partners lost interest, and in 1812 "
        "Tudor’s debts grew so large that he spent a short time behind bars. What saved him was partly "
        "stubbornness and partly a series of practical discoveries. The most important concerned insulation. Ice "
        "melts from the outside in, so the trick is to stop warm air reaching it. Tudor experimented with straw "
        "and with hay, both of which were heavy and tended to rot in a damp hold. The answer turned out to be "
        "sawdust, which the timber mills of Maine were only too glad to give away, since for them it was simply "
        "waste.",

        "Cutting the ice was the next problem. At first, men worked on the frozen ponds with axes and hand saws, "
        "and the blocks they produced came in every shape imaginable, which made them awkward to stack and quick "
        "to melt. In 1825 one of Tudor’s suppliers, Nathaniel Wyeth, came up with a horse-drawn plough that "
        "scored the surface in a grid, so that the ice could be broken into identical blocks. Identical blocks "
        "could be packed tightly, and that alone reduced losses dramatically.",

        "With these improvements, Tudor could think much bigger. In 1833 a cargo of around a hundred and eighty "
        "tons of his ice set off on a voyage of four months to Calcutta. Remarkably, more than half of it was still frozen when the ship arrived. The "
        "British residents of the city were so delighted that, rather than simply renting a warehouse at the "
        "docks, they raised money for a purpose-built ice house to store future shipments.",

        "You can’t sell a product that people don’t know they want, so Tudor set about creating "
        "demand. In cities from Charleston to New Orleans he offered free ice to bar owners for a whole year, on "
        "the understanding that they would sell cold drinks at the same price as warm ones. Once customers had "
        "tasted an iced drink in the heat of summer, he reasoned, they would never want to go back, and he was "
        "right. He also supplied hospitals, where ice was used to bring down fevers, but it was the bars that "
        "made his fortune.",

        "By the middle of the century the trade had grown into a huge industry. Tudor’s own favourite source was "
        "Fresh Pond, in Cambridge, Massachusetts, but ponds all over New England were harvested every winter, among them "
        "Walden Pond, where the writer Henry David Thoreau, who lived beside it, watched gangs of Irish "
        "labourers cutting the ice. Thoreau liked to imagine people in India drinking the water from his pond.",

        "So what brought the whole business to an end? Partly the fact that, as towns and factories grew up along "
        "the rivers, the ice cut from them became increasingly dirty, and by the 1880s doctors were warning that "
        "it could spread disease. That alone did serious damage to the trade’s reputation. Some people also blamed a run of unusually mild winters, which certainly caused "
        "shortages, but the decisive blow was mechanical refrigeration. Once ice could be manufactured cleanly "
        "and cheaply, in any town and in any season, nobody needed to cut it from a lake. By the 1930s the "
        "natural ice trade had all but vanished, and Tudor’s achievement had melted away, fittingly enough, from "
        "public memory.",
    ],
    "items": [
        {"n": 7, "sentence": "Tudor’s very first shipment of ice was sent to the island of ___.",
         "key": "Martinique", "evidence": "that first cargo went to the island of Martinique",
         "why": "Primero menciona un mercado posterior y después da el primero: {{Havana would later become one of "
                "his best markets, but that first cargo went to the island of Martinique}}. [[Very first "
                "shipment]] reformula [[that first cargo]].",
         "wrong": [{"answer": "Havana", "kind": "candidato",
                    "why": "Fue un buen mercado más tarde ({{would later become}}), no el primer destino; además, "
                           "es una ciudad, no una isla."},
                   {"answer": "the Caribbean", "kind": "candidato",
                    "why": "Es la región ({{sent it south to the Caribbean}}), no la isla."}],
         "theory": ["6.3", "2.3"]},
        {"n": 8, "sentence": "In 1812 Tudor was briefly imprisoned as a result of his ___.",
         "key": "debts / debt", "evidence": "Tudor’s debts grew so large that he spent a short time behind bars",
         "why": "{{in 1812 Tudor’s debts grew so large that he spent a short time behind bars}}: [[behind bars]] = "
                "en la cárcel, y [[briefly imprisoned]] lo reformula. Se acepta también el singular.",
         "wrong": [{"answer": "stubbornness", "kind": "candidato",
                    "why": "Es lo que lo salvó después ({{What saved him was partly stubbornness}}), no la causa "
                           "de la cárcel."},
                   {"answer": "partners", "kind": "candidato",
                    "why": "Se oye ({{partners lost interest}}), pero no es la causa de la cárcel."}],
         "theory": ["6.3", "6.4"]},
        {"n": 9, "sentence": "The material that Tudor found worked best as insulation was ___.",
         "key": "sawdust", "evidence": "The answer turned out to be sawdust",
         "why": "Enumera dos pruebas fallidas y da la solución: {{Tudor experimented with straw and with hay}} … "
                "{{The answer turned out to be sawdust}}.",
         "wrong": [{"answer": "straw", "kind": "candidato",
                    "why": "Probado y descartado: {{both of which were heavy and tended to rot}}."},
                   {"answer": "hay", "kind": "candidato", "why": "Lo mismo que [[straw]]."},
                   {"answer": "saw dust", "kind": "ortografía", "why": "Es una sola palabra: [[sawdust]]."}],
         "theory": ["6.3", "6.5"]},
        {"n": 10, "sentence": "Wyeth’s invention was a ___ pulled by horses that made it possible to cut "
                              "identical blocks.",
         "key": "(horse-drawn) plough / (horse-drawn) plow", "evidence": "came up with a horse-drawn plough",
         "why": "Antes se cortaba con herramientas de mano ({{with axes and hand saws}}); Wyeth {{came up with a "
                "horse-drawn plough}}. La frase del papel reformula [[horse-drawn]] con [[pulled by horses]]; si se "
                "escribe, no resta. Se acepta la grafía americana.",
         "wrong": [{"answer": "saw", "kind": "candidato",
                    "why": "Era la herramienta anterior ({{axes and hand saws}}), y no la tiraban caballos."},
                   {"answer": "grid", "kind": "candidato",
                    "why": "Es el dibujo que marcaba el arado ({{scored the surface in a grid}}), no el invento."}],
         "theory": ["6.3", "6.5"]},
        {"n": 11, "sentence": "Residents of Calcutta paid for a purpose-built ___ to keep future cargoes in.",
         "key": "ice house / icehouse / ice-house", "evidence": "a purpose-built ice house",
         "why": "Contrapone lo que no hicieron y lo que hicieron: {{rather than simply renting a warehouse at the "
                "docks, they raised money for a purpose-built ice house}}. Se acepta junto, separado o con "
                "guion.",
         "wrong": [{"answer": "warehouse", "kind": "candidato",
                    "why": "Descartado con {{rather than simply renting a warehouse}}."},
                   {"answer": "house", "kind": "incompleta", "why": "Sin [[ice]] no dice qué clase de edificio."}],
         "theory": ["6.3", "6.4"]},
        {"n": 12, "sentence": "Tudor gave free ice for a year to ___ to encourage a taste for cold drinks.",
         "key": "bar owners / bars", "evidence": "he offered free ice to bar owners for a whole year",
         "why": "{{he offered free ice to bar owners for a whole year}}, con la condición de vender las bebidas "
                "frías al mismo precio. Se acepta también [[bars]], que se oye al final del párrafo ({{it was the "
                "bars that made his fortune}}).",
         "wrong": [{"answer": "hospitals", "kind": "candidato",
                    "why": "También recibían hielo ({{He also supplied hospitals}}), pero no gratis ni para "
                           "crear afición a las bebidas frías."},
                   {"answer": "customers", "kind": "candidato",
                    "why": "Son quienes debían acostumbrarse a las bebidas frías, no quienes recibían el hielo "
                           "gratis."}],
         "theory": ["6.3", "3.3"]},
        {"n": 13, "sentence": "Thoreau saw Irish workers harvesting ice on ___.",
         "key": "Walden Pond / Walden", "evidence": "among them Walden Pond",
         "why": "Primero nombra el lago preferido de Tudor y luego el de Thoreau: {{Tudor’s own favourite source "
                "was Fresh Pond}} … {{among them Walden Pond, where the writer Henry David Thoreau}}.",
         "wrong": [{"answer": "Fresh Pond", "kind": "candidato",
                    "why": "Era la fuente preferida de Tudor, no el lago de Thoreau."},
                   {"answer": "New England", "kind": "candidato", "why": "Es la región, no el lago."}],
         "theory": ["6.3", "3.2"]},
        {"n": 14, "sentence": "By the 1880s, doctors feared that ice cut from rivers might spread ___.",
         "key": "disease / diseases", "evidence": "doctors were warning that it could spread disease",
         "why": "{{by the 1880s doctors were warning that it could spread disease}}: el hielo de los ríos venía "
                "cada vez más sucio. Se acepta también el plural.",
         "wrong": [{"answer": "dirt", "kind": "sinónimo",
                    "why": "Se oye [[dirty]], pero lo que temían los médicos es que transmitiera enfermedades."},
                   {"answer": "fevers", "kind": "candidato",
                    "why": "Se oye en otro párrafo: el hielo servía para bajarlas ({{bring down fevers}})."}],
         "theory": ["6.3", "6.4"]},
        {"n": 15, "sentence": "In the speaker’s view, what finally killed off the trade was ___.",
         "key": "(mechanical) refrigeration", "evidence": "the decisive blow was mechanical refrigeration",
         "why": "Descarta una explicación ajena y da la suya: {{Some people also blamed a run of unusually mild "
                "winters}} … {{but the decisive blow was mechanical refrigeration}}. [[Finally killed off]] "
                "reformula [[the decisive blow]].",
         "wrong": [{"answer": "mild winters", "kind": "candidato",
                    "why": "Es lo que culpaban otros ({{Some people also blamed}}); para el historiador causaron "
                           "escasez, no el final."},
                   {"answer": "manufactured ice", "kind": "sinónimo",
                    "why": "Resume la idea ({{Once ice could be manufactured cleanly}}), pero no es lo que se oye: la "
                           "palabra que da el historiador es {{mechanical refrigeration}}."},
                   {"answer": "pollution", "kind": "sinónimo",
                    "why": "El hielo sucio contribuyó ({{Partly}}), pero no fue el golpe definitivo, y la palabra "
                           "no se oye."}],
         "theory": ["6.3", "3.2"]},
    ],
}

# ---------- Part 3 · Interview ----------
P3 = {
    "num": "S02",
    "subtitle": "SIM-02 · Part 3",
    "difficulty": 3,
    "wpm": 170,
    "first": 16,
    "ctx": "You will hear part of an interview with Tom Halloran, who records the sounds of wildlife.",
    "speakers": {"Interviewer": "Libby", "Tom": "William"},
    "host": "Interviewer",
    "lex": ["a dreadful return on (time)", "the remotest glens", "a line I won’t cross", "plane and all",
            "raise one’s pitch", "fit in with sb", "I can’t say I blame them", "preach", "be lectured about sth"],
    "turns": [
        ("Interviewer",
         "My guest today is Tom Halloran, who has spent thirty years recording the sounds of the natural world "
         "for radio, film and museums. Tom, I imagine most people assume your job is all about the equipment."),
        ("Tom",
         "They do, and I understand why. The microphones are expensive, and they look impressive. But I could "
         "lend my kit to almost anyone and they’d come back with nothing usable. The real skill lies in where you "
         "put yourself and how long you’re prepared to wait. I once spent eleven nights in a hide in Scotland for "
         "forty seconds of an otter feeding her cubs. Most people would call that a dreadful return on the time. "
         "I’d call it a good week."),
        ("Interviewer",
         "Has the job become harder over the years, or is that just nostalgia talking?"),
        ("Tom",
         "Much harder, and not for the reasons people expect. The animals haven’t become any shyer. What’s changed "
         "is the background. When I started, there were places in Britain where I could go for an hour or more "
         "without hearing an engine of any kind. Now, even in the remotest glens, a plane goes over every few "
         "minutes, and a single jet can ruin a recording that’s taken all night. I’ve had to give up on some of my "
         "favourite spots altogether. These days I spend more time waiting for silence than waiting for "
         "animals."),
        ("Interviewer",
         "Couldn’t you simply remove the noise afterwards? The software must be very sophisticated by now."),
        ("Tom",
         "It is, and I do use it to take out the odd click or hum. But there’s a line I won’t cross. Some "
         "recordists will take a blackbird from one morning and a stream from another and lay them on top of each "
         "other, and the result can sound gorgeous. I just don’t think you can call it a recording of a place any "
         "more. If a museum tells its visitors that this is what a Norfolk marsh sounds like at dawn, I want that "
         "to be true, plane and all if necessary."),
        ("Interviewer",
         "Has anything you’ve recorded genuinely surprised you?"),
        ("Tom",
         "Plenty, but one thing stands out. A few years ago I was recording great tits, both in a city park and in "
         "a forest about thirty miles away, and the city birds were singing noticeably higher. Researchers have "
         "found the same thing elsewhere: birds in towns seem to raise their pitch so that they can be heard above "
         "the traffic. Once you knew to listen for it, the difference was obvious even without any equipment. We "
         "tend to think of wildlife either surviving in spite of us or disappearing because of us. Here were "
         "animals quietly changing their own voices to fit in with us, and nobody had asked them to. I found that "
         "oddly moving."),
        ("Interviewer",
         "Finally, what do you hope people take away from your recordings?"),
        ("Tom",
         "I’m wary of preaching. People switch off the moment they feel they’re being lectured about the "
         "environment, and I can’t say I blame them. What I’d really like is for someone to hear a recording of a "
         "wood at dawn and then, the next time they’re out for a walk, to stop for a minute and actually listen. "
         "If they notice what’s there, they might notice when it’s gone. And they might even mind."),
    ],
    "items": [
        {"n": 16, "type": "Actitud y opinión", "speaker": "Tom",
         "stem": "What point does Tom make about recording wildlife?",
         "options": ["Good equipment is beyond the means of most beginners.",
                     "Patience and choice of location matter more than the equipment.",
                     "The best results are usually obtained at night.",
                     "Short recordings are often more valuable than long ones."],
         "key": "B",
         "evidence": ["The real skill lies in where you put yourself and how long you’re prepared to wait"],
         "why": "Concede lo del equipo ({{They do, and I understand why}}) y da su punto con una señal clara: {{The "
                "real skill lies in where you put yourself and how long you’re prepared to wait}}. [[Choice of "
                "location]] parafrasea [[where you put yourself]]; [[patience]], [[how long you’re prepared to "
                "wait]].",
         "theory": ["7.2", "3.3"],
         "distractors": {
             "A": {"kinds": ["4.1"],
                   "why": "Eco de {{The microphones are expensive}}, pero no dice que estén fuera del alcance de "
                          "nadie: al contrario, podría prestárselos a cualquiera ({{I could lend my kit to almost "
                          "anyone}})."},
             "C": {"kinds": ["4.1"],
                   "why": "Recoge {{eleven nights in a hide}}, un ejemplo de espera, no una regla sobre la hora "
                          "del día."},
             "D": {"kinds": ["4.8"],
                   "why": "Los {{forty seconds}} ilustran cuánto cuesta conseguir poco material, no que lo breve "
                          "valga más."},
         }},
        {"n": 17, "type": "Detalle", "speaker": "Tom",
         "stem": "According to Tom, his work has become more difficult mainly because",
         "options": ["animals have become more wary of people.",
                     "the remotest places are harder to get to than before.",
                     "recordings now need to be much longer to be usable.",
                     "it is increasingly hard to escape man-made noise."],
         "key": "D",
         "evidence": ["What’s changed is the background",
                      "These days I spend more time waiting for silence than waiting for animals"],
         "why": "Descarta la explicación esperada y da la suya: {{What’s changed is the background}}. Lo concreta "
                "con los aviones ({{a single jet can ruin a recording}}) y lo resume: {{These days I spend more "
                "time waiting for silence than waiting for animals}}. [[Man-made noise]] recoge [[an engine of any "
                "kind]] y [[a plane]].",
         "theory": ["7.2", "3.3"],
         "distractors": {
             "A": {"kinds": ["4.2"],
                   "why": "Lo descarta expresamente: {{The animals haven’t become any shyer}}."},
             "B": {"kinds": ["4.1"],
                   "why": "Eco de {{the remotest glens}}: el problema allí es que pasan aviones, no que sea difícil "
                          "llegar."},
             "C": {"kinds": ["4.8"],
                   "why": "No dice que las grabaciones tengan que ser más largas; lo que se alarga es la espera "
                          "del silencio."},
         }},
        {"n": 18, "type": "Actitud y opinión", "speaker": "Tom",
         "stem": "What is Tom’s attitude to combining sounds from different recordings?",
         "options": ["He believes it gives a false impression of a place.",
                     "He thinks the results are generally of poor quality.",
                     "He accepts it provided that listeners are informed.",
                     "He considers it too time-consuming to be worthwhile."],
         "key": "A",
         "evidence": ["I just don’t think you can call it a recording of a place any more"],
         "why": "Marca el límite ({{there’s a line I won’t cross}}) y lo justifica: {{I just don’t think you can "
                "call it a recording of a place any more}}. El ejemplo del museo lo confirma: {{I want that to be "
                "true}}. [[A false impression of a place]] parafrasea las dos frases.",
         "theory": ["3.1", "3.4"],
         "distractors": {
             "B": {"kinds": ["4.6"],
                   "why": "Reconoce lo contrario: {{the result can sound gorgeous}}. Su objeción es la "
                          "veracidad, no la calidad."},
             "C": {"kinds": ["4.8"],
                   "why": "No pone ninguna condición: no lo acepta ni avisando al oyente."},
             "D": {"kinds": ["4.8"],
                   "why": "No habla del tiempo que lleva mezclar sonidos; el programa lo usa para {{take out the "
                          "odd click or hum}}."},
         }},
        {"n": 19, "type": "Sentimiento", "speaker": "Tom",
         "stem": "What did Tom find moving about his recordings of great tits?",
         "options": ["the fact that birds in the city sang more frequently",
                     "how alike the birds in the two places sounded",
                     "the way the birds had adapted to living near people",
                     "the discovery of something researchers had overlooked"],
         "key": "C",
         "evidence": ["Here were animals quietly changing their own voices to fit in with us"],
         "why": "Explica qué le emocionó: {{Here were animals quietly changing their own voices to fit in with "
                "us}}, frente a la idea habitual de que la fauna sobrevive a pesar de nosotros o desaparece. "
                "[[Adapted to living near people]] parafrasea [[changing their own voices to fit in with us]].",
         "theory": ["3.3", "3.1"],
         "distractors": {
             "A": {"kinds": ["4.6"],
                   "why": "Cantaban más agudo, no más a menudo: {{singing noticeably higher}}."},
             "B": {"kinds": ["4.6"],
                   "why": "Dice lo contrario: los pájaros de la ciudad sonaban distinto ({{noticeably "
                          "higher}})."},
             "D": {"kinds": ["4.6"],
                   "why": "Los investigadores ya lo habían visto: {{Researchers have found the same thing "
                          "elsewhere}}."},
         }},
        {"n": 20, "type": "Actitud y opinión", "speaker": "Tom",
         "stem": "What does Tom hope his recordings will do?",
         "options": ["persuade people to campaign for the environment",
                     "help people learn to identify different birds",
                     "preserve sounds that may soon disappear for good",
                     "encourage people to pay closer attention to their surroundings"],
         "key": "D",
         "evidence": ["the next time they’re out for a walk, to stop for a minute and actually listen"],
         "why": "Rechaza sermonear ({{I’m wary of preaching}}) y dice lo que quiere: {{What I’d really like}} es "
                "que el oyente, {{the next time they’re out for a walk, to stop for a minute and actually "
                "listen}}. [[Pay closer attention to their surroundings]] lo parafrasea.",
         "theory": ["3.3", "3.4"],
         "distractors": {
             "A": {"kinds": ["4.2"],
                   "why": "Lo descarta: {{I’m wary of preaching}}, porque la gente desconecta cuando la "
                          "sermonean."},
             "B": {"kinds": ["4.8"],
                   "why": "No habla de reconocer especies; quiere que la gente escuche, no que aprenda nombres."},
             "C": {"kinds": ["4.1"],
                   "why": "Eco de {{when it’s gone}}: la desaparición aparece como algo que el oyente podría "
                          "notar, no como un archivo que él quiera guardar."},
         }},
    ],
}

# ---------- Part 4 · Multiple matching ----------
P4 = {
    "num": "S02",
    "subtitle": "SIM-02 · Part 4",
    "difficulty": 3,
    "wpm": 170,
    "first": 21,
    "ctx": "You will hear five short extracts in which people are talking about giving up their car.",
    "lex": ["the car went", "pick up the odd scrape", "that was that", "be in better shape", "on the spot",
            "the regulars", "shake sb (= upset)", "with one’s shoulders up round one’s ears"],
    "tasks": [
        {"prompt": "what finally prompted each speaker to give up their car",
         "options": ["a change in their health",
                     "the cost of a repair",
                     "a move to a new home",
                     "a minor accident",
                     "a question from a child",
                     "concern about the environment",
                     "a long period without using it",
                     "pressure from their partner"],
         "extras": {
             "A": "Speaker 5 lo descarta antes de dar su motivo: {{nothing to do with my eyesight, whatever my "
                  "children say}}.",
             "F": "Dos hablantes lo niegan: Speaker 1 ({{It wasn’t a documentary about climate change that did "
                  "it}}) y Speaker 4 ({{I’d love to tell you it was an environmental decision, but it wasn’t "
                  "really}}).",
             "H": "La mujer de Speaker 3 llevaba años insistiendo ({{She’d also been telling me for years}}), "
                  "pero lo que le hizo decidirse fue la mudanza."}},
        {"prompt": "what each speaker has found to be the main benefit",
         "options": ["feeling less stressed",
                     "meeting new people",
                     "getting to know their local area",
                     "making good use of travelling time",
                     "becoming fitter",
                     "saving money",
                     "spending more time with family",
                     "a greater sense of independence"],
         "extras": {
             "F": "Speaker 1 lo rebaja: {{we’ve saved far less than people imagine}}.",
             "G": "Speaker 3 lo menciona en broma, como queja de su mujer: {{she’d rather I spent the time talking "
                  "to her}}.",
             "H": "Nadie lo menciona; al contrario, Speaker 5 depende ahora del autobús: {{I take the bus "
                  "everywhere}}."}},
    ],
    "speakers": [
        {"voice": "Connor",
         "text": "It wasn’t a documentary about climate change that did it, although I’d certainly watched a few. "
                 "In the end it was my daughter, who was seven at the time, asking me why we drove to a shop she "
                 "could see from her bedroom window. I didn’t have a good answer. So the car went, and I’ll be "
                 "honest: once you take the train fares into account, we’ve saved far less than people imagine. What I hadn’t expected was "
                 "to discover my own town. I know the back lanes now, the bakery that opens at six, the short cut "
                 "through the churchyard. You see none of that through a windscreen.",
         "items": [
             {"n": 21, "key": "E",
              "evidence": ["it was my daughter, who was seven at the time, asking me why we drove to a shop she "
                           "could see from her bedroom window"],
              "why": "Descarta un motivo y da el real: {{In the end it was my daughter, who was seven at the time, "
                     "asking me why we drove to a shop she could see from her bedroom window}}. [[A question from a child]] lo "
                     "resume; {{I didn’t have a good answer}} confirma que fue eso lo que le hizo decidir.",
              "touched": {"F": {"kinds": ["4.2"],
                                "why": "Mencionado y descartado: {{It wasn’t a documentary about climate change that "
                                       "did it}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 26, "key": "C",
              "evidence": ["What I hadn’t expected was to discover my own town"],
              "why": "{{What I hadn’t expected was to discover my own town}}, y lo concreta: {{the back lanes}}, "
                     "{{the bakery that opens at six}}, {{the short cut through the churchyard}}.",
              "touched": {"F": {"kinds": ["4.7"],
                                "why": "El ahorro fue menor de lo esperado: {{we’ve saved far less than people "
                                       "imagine}}."}},
              "theory": ["8.1", "4.7"]}]},
        {"voice": "Molly",
         "text": "My old hatchback had picked up the odd scrape over the years, nothing serious, and I’d happily "
                 "have kept it going for ever. Then the garage quoted me more to replace the gearbox than the whole "
                 "car was worth, and that was that. I live at the top of a ridiculously steep hill, so I was "
                 "dreading the walk home. Six months on, I’m in better shape than I’ve been since university. "
                 "Friends promised I’d be calmer without the traffic. I’m not, particularly. The buses run late "
                 "just as often as the roads get jammed.",
         "items": [
             {"n": 22, "key": "B",
              "evidence": ["the garage quoted me more to replace the gearbox than the whole car was worth, and that "
                           "was that"],
              "why": "El desencadenante es el presupuesto del taller: {{the garage quoted me more to replace the "
                     "gearbox than the whole car was worth, and that was that}}. [[That was that]] marca la "
                     "decisión.",
              "touched": {"D": {"kinds": ["4.2"],
                                "why": "Los golpes fueron menores y no le hicieron dejar el coche: {{the odd scrape "
                                       "over the years, nothing serious}}."}},
              "theory": ["8.1", "8.3"]},
             {"n": 27, "key": "E",
              "evidence": ["Six months on, I’m in better shape than I’ve been since university"],
              "why": "Temía la cuesta y ha resultado lo mejor: {{Six months on, I’m in better shape than I’ve been "
                     "since university}}. [[In better shape]] = [[fitter]].",
              "touched": {"A": {"kinds": ["4.7"],
                                "why": "Le prometieron más calma y no ha sido así: {{Friends promised I’d be calmer "
                                       "without the traffic. I’m not, particularly}}."}},
              "theory": ["8.1", "4.7"]}]},
        {"voice": "Brian",
         "text": "These days I take the train to work, forty minutes each way, and I’ve turned that into the most "
                 "useful part of my day: I clear my emails before I reach the office and read on the way home. My "
                 "wife says she’d rather I spent the time talking to her, but you can’t have everything. She’d also "
                 "been telling me for years that we hardly needed a car, and she was probably right, but it took "
                 "moving house to actually do something about it. Our new flat is right in the centre, and there’s "
                 "simply nowhere to park within half a mile.",
         "items": [
             {"n": 23, "key": "C",
              "evidence": ["it took moving house to actually do something about it"],
              "why": "La insistencia de su mujer es el antecedente; el desencadenante, la mudanza: {{it took moving "
                     "house to actually do something about it}}, a un piso en el centro sin aparcamiento.",
              "touched": {"H": {"kinds": ["4.3"],
                                "why": "Antecedente, no desencadenante (§8.3): {{She’d also been telling me for "
                                       "years that we hardly needed a car}}, pero no hizo nada hasta mudarse."}},
              "theory": ["8.1", "8.3"]},
             {"n": 28, "key": "D",
              "evidence": ["I’ve turned that into the most useful part of my day"],
              "why": "La respuesta de la Task Two llega antes que la de la Task One (§8.1). El tren se ha convertido en {{the most useful part of my day}}: {{I clear my emails before I "
                     "reach the office and read on the way home}}.",
              "touched": {"G": {"kinds": ["4.4"],
                                "why": "Es lo que querría su mujer, no lo que él ha ganado: {{she’d rather I spent "
                                       "the time talking to her}}."}},
              "theory": ["8.1", "3.2"]}]},
        {"voice": "Emma",
         "text": "I’d love to tell you it was an environmental decision, but it wasn’t really. I spent most of last "
                 "year working abroad, and my car sat in a friend’s garage the whole time. When I came back and "
                 "went to collect it, I realised I hadn’t missed it once, so I sold it to him on the spot. I "
                 "wouldn’t say life’s any less stressful without it. But I talk to people now. I’ve got to know "
                 "half the regulars at my bus stop, and one of them has become a really good friend.",
         "items": [
             {"n": 24, "key": "G",
              "evidence": ["I realised I hadn’t missed it once, so I sold it to him on the spot"],
              "why": "Pasó casi un año sin usarlo ({{my car sat in a friend’s garage the whole time}}) y al volver "
                     "{{I realised I hadn’t missed it once, so I sold it to him on the spot}}.",
              "touched": {"F": {"kinds": ["4.2"],
                                "why": "Mencionado y descartado: {{I’d love to tell you it was an environmental "
                                       "decision, but it wasn’t really}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 29, "key": "B",
              "evidence": ["I’ve got to know half the regulars at my bus stop"],
              "why": "{{But I talk to people now}}: {{I’ve got to know half the regulars at my bus stop}}, y una se "
                     "ha convertido en {{a really good friend}}.",
              "touched": {"A": {"kinds": ["4.2"],
                                "why": "Lo niega: {{I wouldn’t say life’s any less stressful without it}}."}},
              "theory": ["8.1", "4.2"]}]},
        {"voice": "Ava",
         "text": "What I’ve got back, more than anything, is a kind of calm. I used to arrive everywhere with my "
                 "shoulders up round my ears; now I just look out of the window. I can’t claim I’m any fitter, mind "
                 "you, since I take the bus everywhere. And no, it was nothing to do with my eyesight, whatever my "
                 "children say. I reversed into a lamp post in a supermarket car park at about two miles an hour. "
                 "Nobody was hurt and the damage was minor, but it shook me more than it should have, and I realised "
                 "I’d been dreading every journey for years.",
         "items": [
             {"n": 25, "key": "D",
              "evidence": ["I reversed into a lamp post in a supermarket car park at about two miles an hour"],
              "why": "El percance fue mínimo ({{Nobody was hurt and the damage was minor}}), pero {{it shook me more "
                     "than it should have}}: fue lo que le hizo dejar el coche.",
              "touched": {"A": {"kinds": ["4.2"],
                                "why": "Lo descarta antes de contar el accidente: {{nothing to do with my "
                                       "eyesight}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 30, "key": "A",
              "evidence": ["What I’ve got back, more than anything, is a kind of calm"],
              "why": "La respuesta de la Task Two llega antes que la de la Task One (§8.1): {{What I’ve got back, more "
                     "than anything, is a kind of calm}}, frente a antes: {{I used to arrive everywhere with my "
                     "shoulders up round my ears}}. [[Feeling less stressed]] lo resume.",
              "touched": {"E": {"kinds": ["4.2"],
                                "why": "Lo niega: {{I can’t claim I’m any fitter}}."}},
              "theory": ["8.1", "4.2"]}]},
    ],
}
