# SIM-01 · Listening · specs de las Parts 1-4
# Se monta con: python3 src/gen_SIM.py lst sim/SIM-01 --stage verify | audio | asr N | pdf
# Formato de cada spec: cabecera de src/gen_LST-P1..P4. Voces sin repetir en todo el paper; narrador: Thomas.

# ---------- Part 1 · Three extracts ----------
P1 = {
    "num": "S01",
    "subtitle": "SIM-01 · Part 1",
    "difficulty": 3,
    "wpm": 170,
    "lex": ["far from it", "toughen sb up", "have one’s priorities right", "the odd (branch)", "more often than not", "put sth right", "not be getting any younger", "physically punishing", "turn up (= find)", "fetch (a price)", "a fair bit", "word gets round", "patent medicine", "I couldn’t have put it better myself"],
    "extracts": [
        {"ctx": "You hear two friends discussing a weekend course in wild swimming.",
         "speakers": {"Woman": "Libby", "Man": "Connor"},
         "turns": [
             ("Woman", "So, how was the swimming weekend? I was half expecting you to come back with frostbite."),
             ("Man", "Far from it. I won’t pretend the first morning was pleasant. The lake was eleven degrees, and "
                     "for the first few minutes I could barely breathe. But the instructor was excellent. She wasn’t "
                     "remotely interested in toughening us up. Most of the time went on getting out safely: how to "
                     "spot a current, how to tell when your hands are going numb, when to stop."),
             ("Woman", "Not quite the heroic struggle against the elements I’d pictured, then."),
             ("Man", "No, and that’s what put a couple of the others off. They’d come for the thrill and got a talk "
                     "on hypothermia."),
             ("Woman", "Well, I’d say she had her priorities right."),
             ("Man", "So would I. And the odd thing is, knowing exactly what could go wrong made me far less anxious, "
                     "not more. By the Sunday I was the last one out of the water."),
         ],
         "items": [
             {"n": 1, "type": "Detalle",
              "stem": "What does the man say about the instructor?",
              "options": ["She concentrated on safety rather than on building endurance.",
                          "She expected beginners to cope with the cold water from the very start.",
                          "She spent too long on theory for his liking."],
              "key": "A",
              "evidence": ["She wasn’t remotely interested in toughening us up",
                           "Most of the time went on getting out safely"],
              "why": "Primero descarta la resistencia ({{She wasn’t remotely interested in toughening us up}}) y "
                     "luego dice a qué dedicó el tiempo: {{Most of the time went on getting out safely}}. La opción "
                     "lo resume en abstracto: [[safety]] frente a [[building endurance]].",
              "theory": ["5.3", "3.1"],
              "distractors": {
                  "B": {"kinds": ["4.1", "4.8"],
                        "why": "El frío aparece ({{The lake was eleven degrees}}), pero como experiencia suya; no "
                               "dice nada de lo que la instructora esperaba de los principiantes."},
                  "C": {"kinds": ["4.4"],
                        "why": "A quien no le gustó tanta teoría fue a otros: {{that’s what put a couple of the "
                               "others off}}. Él la elogia: {{the instructor was excellent}}."}}},
             {"n": 2, "type": "Sentimiento",
              "stem": "How did the man feel by the end of the course?",
              "options": ["relieved that the hardest part of the weekend was behind him",
                          "more at ease in the water than he had expected to be",
                          "uneasy about the risks he had learnt about"],
              "key": "B",
              "evidence": ["knowing exactly what could go wrong made me far less anxious, not more",
                           "By the Sunday I was the last one out of the water"],
              "why": "Lo dice al final: {{knowing exactly what could go wrong made me far less anxious, not more}}, y "
                     "lo confirma un hecho, {{By the Sunday I was the last one out of the water}}. {{the odd thing "
                     "is}} indica que no lo esperaba: de ahí [[than he had expected to be]].",
              "theory": ["3.3", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.8", "4.7"],
                        "why": "Lo duro fue la primera mañana ({{I won’t pretend the first morning was pleasant}}), "
                               "pero al final no habla de alivio: al contrario, era {{the last one out of the "
                               "water}}."},
                  "C": {"kinds": ["4.6"],
                        "why": "Invierte la relación: conocer los riesgos lo tranquilizó, {{far less anxious, not "
                               "more}}."}}},
         ]},
        {"ctx": "You hear a tree surgeon talking about his work.",
         "speakers": {"Tree surgeon": "Mitchell"},
         "turns": [
             ("Tree surgeon",
              "People tend to assume my job is mostly about cutting trees down, and I suppose that’s understandable "
              "when the first thing they see is a man with a chainsaw hanging from the top of an oak. In fact, a good "
              "deal of what I do is aimed at keeping trees standing. Many of the calls I get come from homeowners "
              "who’ve decided a tree is dangerous because it creaks in the wind or drops the odd branch, and more "
              "often than not there’s nothing wrong with it that some careful pruning won’t put right. Talking "
              "someone out of felling a perfectly healthy beech isn’t the most profitable part of the job, I’ll "
              "grant you. But I’d rather lose the fee than take down something that’s been growing for two hundred "
              "years. The work itself is physically punishing, and I’m not getting any younger. What keeps me at it, "
              "though, isn’t the climbing, much as I enjoy it. It’s walking past a tree years later and knowing it’s "
              "still there because of a decision I helped someone make."),
         ],
         "items": [
             {"n": 3, "type": "Detalle",
              "stem": "What does the tree surgeon say about many of the requests he receives?",
              "options": ["They tend to come from people who dislike the noise trees make in the wind.",
                          "They usually involve trees that are too large to prune safely.",
                          "They are often based on an exaggerated sense of danger."],
              "key": "C",
              "evidence": ["more often than not there’s nothing wrong with it"],
              "why": "Los clientes creen que el árbol es peligroso ({{homeowners who’ve decided a tree is dangerous}}) "
                     "por señales sin importancia, y casi siempre se equivocan: {{more often than not there’s nothing "
                     "wrong with it}}. [[Often]] traduce [[more often than not]]; [[exaggerated sense of danger]], el "
                     "contraste entre lo que creen y lo que hay.",
              "theory": ["5.3", "2.4"],
              "distractors": {
                  "A": {"kinds": ["4.1"],
                        "why": "Recoge {{creaks in the wind}}, pero el crujido no les molesta por el ruido: lo toman "
                               "como señal de peligro."},
                  "B": {"kinds": ["4.8"],
                        "why": "No habla del tamaño de los árboles; dice lo contrario, que la mayoría se arregla "
                               "podando: {{nothing wrong with it that some careful pruning won’t put right}}."}}},
             {"n": 4, "type": "Actitud y opinión",
              "stem": "What does the tree surgeon find most rewarding about his work?",
              "options": ["the physical challenge of climbing",
                          "knowing that he has helped to preserve trees",
                          "the chance to work on trees that are centuries old"],
              "key": "B",
              "evidence": ["knowing it’s still there because of a decision I helped someone make"],
              "why": "Descarta primero la escalada y luego da la razón: {{It’s walking past a tree years later and "
                     "knowing it’s still there because of a decision I helped someone make}}. La segunda idea es la "
                     "que manda (§3.3).",
              "theory": ["3.3", "5.3"],
              "distractors": {
                  "A": {"kinds": ["4.2"],
                        "why": "Mencionado y descartado: {{What keeps me at it, though, isn’t the climbing, much as I "
                               "enjoy it}}."},
                  "C": {"kinds": ["4.1"],
                        "why": "Recoge {{growing for two hundred years}}, que sirve para justificar que prefiera "
                               "perder un encargo, no para decir qué le satisface."}}},
         ]},
        {"ctx": "You hear two archaeologists discussing the excavation of a Victorian rubbish dump.",
         "speakers": {"Woman": "Natasha", "Man": "Brian"},
         "turns": [
             ("Woman", "I must say, I didn’t expect a rubbish dump to draw a bigger crowd on the open day than the "
                       "Roman villa."),
             ("Man", "Neither did I. Though I suspect half of them were hoping we’d turn up something valuable. A "
                     "couple of people asked me what the bottles would fetch at auction."),
             ("Woman", "Well, some of them would fetch a fair bit. Collectors pay a fortune for the oddly shaped "
                       "ones."),
             ("Man", "Which is exactly what worries me. Once word gets round, people start digging these sites up "
                     "with a spade on a Sunday afternoon, and nobody records a thing."),
             ("Woman", "True. Although I’d argue the real value isn’t in the glass at all. It’s what was in the "
                       "bottles. Half of them held patent medicines, and every one of them promised to cure "
                       "something."),
             ("Man", "Yes, that struck me too. You get a far clearer picture of what people were afraid of from what "
                     "they threw away than from anything they chose to write down."),
             ("Woman", "I couldn’t have put it better myself."),
         ],
         "items": [
             {"n": 5, "type": "Actitud y opinión",
              "stem": "What concern does the man express?",
              "options": ["Visitors were more interested in the dump than in the other parts of the site.",
                          "The bottles found at the site are worth less than people assume.",
                          "Talk of what the bottles are worth could lead to amateurs plundering sites."],
              "key": "C",
              "evidence": ["Which is exactly what worries me",
                           "people start digging these sites up with a spade on a Sunday afternoon, and nobody "
                           "records a thing"],
              "why": "{{Which is exactly what worries me}} remite a lo que pagan los coleccionistas, y la consecuencia "
                     "que teme es la excavación sin control: {{people start digging these sites up with a spade on a "
                     "Sunday afternoon, and nobody records a thing}}. [[Amateurs plundering sites]] lo parafrasea.",
              "theory": ["5.3", "3.2"],
              "distractors": {
                  "A": {"kinds": ["4.3", "4.4"],
                        "why": "Es cierto que el vertedero atrajo más público ({{draw a bigger crowd on the open day "
                               "than the Roman villa}}), pero lo dice ella, como sorpresa, y no como preocupación."},
                  "B": {"kinds": ["4.8"],
                        "why": "Él nunca dice que valgan menos; es ella quien habla del precio, y para decir que "
                               "algunas valen bastante: {{some of them would fetch a fair bit}}."}}},
             {"n": 6, "type": "Acuerdo",
              "stem": "What do the two archaeologists agree about?",
              "options": ["The rubbish reveals people’s fears more clearly than written records do.",
                          "Collectors are willing to pay too much for unusual bottles.",
                          "The open day attracted visitors for the wrong reasons."],
              "key": "A",
              "evidence": ["You get a far clearer picture of what people were afraid of from what they threw away "
                           "than from anything they chose to write down",
                           "I couldn’t have put it better myself"],
              "why": "Ella introduce la idea con los medicamentos ({{every one of them promised to cure something}}), "
                     "él la formula ({{You get a far clearer picture of what people were afraid of from what they "
                     "threw away than from anything they chose to write down}}) y ella la suscribe sin reservas: "
                     "{{I couldn’t have put it better myself}} (§3.6).",
              "theory": ["3.6", "5.3"],
              "distractors": {
                  "B": {"kinds": ["4.1", "4.4"],
                        "why": "Ella dice que los coleccionistas {{pay a fortune}}, pero sin criticarlo, y él no "
                               "opina sobre el precio: le preocupa lo que provoca."},
                  "C": {"kinds": ["4.4"],
                        "why": "Solo él lo sospecha ({{I suspect half of them were hoping we’d turn up something "
                               "valuable}}); ella no lo confirma ni lo comenta."}}},
         ]},
    ],
}

# ---------- Part 2 · Sentence completion ----------
P2 = {
    "num": "S01",
    "subtitle": "SIM-01 · Part 2",
    "difficulty": 3,
    "wpm": 170,
    "first": 7,
    "voice": "Sonia",
    "ctx": "You will hear a perfumer called Helen Marsh giving a talk about how a new perfume is created.",
    "title": "Creating a new perfume",
    "lex": ["be about as helpful as it sounds", "in a usable form", "evaporate", "blotters (smelling strips)",
            "on the shelves (a la venta)", "what I’m after", "live with sth (convivir con algo)"],
    "paragraphs": [
        "Good afternoon, everyone. People tend to imagine that a perfumer spends her days in a field of lavender, "
        "waiting for inspiration. The reality is rather more like being an architect. A new fragrance almost "
        "always starts with a document called a brief, which comes from the company that will eventually sell it. "
        "It might ask for something fresh, or something that suggests a particular place, or simply ‘a scent for a "
        "confident woman in her thirties’, which is about as helpful as it sounds. Interestingly, the most useful "
        "part of a brief is rarely the description of the smell. It’s the price, because that decides which raw "
        "materials I can afford to use.",

        "And those materials vary enormously in cost. Some of the most expensive come from flowers. Jasmine, for "
        "instance, has to be picked by hand early in the morning, before the heat of the day weakens its scent, and "
        "a huge quantity of petals produces only a tiny amount of oil. People often assume that natural ingredients "
        "are always superior, but most of a typical modern perfume is synthetic, and I don’t see that as a "
        "compromise. Synthetic molecules give us smells that nature simply doesn’t offer in a usable form. Many "
        "people think the smell of clean laundry comes from cotton, or from soap. In fact, much of it comes from a group "
        "of synthetics called musks, which are used in place of an ingredient that once came from animals.",

        "Once I know what I can spend, I start to think about structure. A perfume is built in three layers, which "
        "we call notes, and each one evaporates at a different speed. The top notes, usually citrus, things like "
        "lemon or bergamot, are what you smell in the first few minutes, and they’re gone within half an hour. Then "
        "come the heart notes, often floral, which last for several hours. And underneath everything are the base "
        "notes, woods and resins and vanilla, which can still be detected on the skin the following day. The "
        "mistake beginners make is to spend all their effort on the opening. It’s the base that people actually "
        "live with, so that’s where I begin.",

        "Then comes testing, which is where most of the time goes. Every version is tried first on thin strips of "
        "paper called blotters, and then, more importantly, on skin, because skin changes everything. The same "
        "formula can smell quite different on two people, depending on their diet, their skin type, even the "
        "temperature of the room. A fragrance can go through several hundred versions before it’s finished, and the "
        "whole process usually takes between one and three years. The longest I’ve ever worked on a single perfume "
        "is five years, and I’m still not sure it was worth it.",

        "Even then, a great many perfumes fail, and not always for the reasons you’d expect. It’s rarely because "
        "they smell unpleasant. Far more often, a perfume fails simply because it’s too similar to something "
        "already on the shelves. Our noses also tire remarkably quickly: after a few minutes of sniffing, we stop "
        "noticing a smell altogether. You’ll often see little bowls of coffee beans in perfume shops, supposedly to "
        "clear the nose, but there’s very little evidence that they help. Most perfumers I know simply smell their "
        "own skin, which gives the nose something neutral to come back to.",

        "Finally, people often ask me how we describe smells, because English, like most languages, has remarkably "
        "few words that belong to smell alone. So we borrow. From music we take notes and harmony; from touch, words "
        "like soft, sharp or velvety; and above all from colour. When I talk to a client, I’ll say a perfume needs "
        "to be greener, or warmer, and they know exactly what I mean. The one vocabulary I try to avoid is taste. "
        "Call a perfume sweet or fruity and everyone imagines a dessert, which is very rarely what I’m after.",
    ],
    "items": [
        {"n": 7, "sentence": "Helen says that the most helpful detail in a brief is usually the ___.",
         "key": "price", "evidence": "It’s the price",
         "why": "La negación descarta el candidato antes de dar la respuesta: {{the most useful part of a brief is "
                "rarely the description of the smell. It’s the price}}. En el papel, {{most helpful detail}} "
                "reformula {{most useful part}}.",
         "wrong": [{"answer": "description", "kind": "candidato",
                    "why": "Descartado: {{rarely the description of the smell}}."},
                   {"answer": "cost", "kind": "sinónimo",
                    "why": "Se oye más adelante ({{vary enormously in cost}}) y habla de las materias primas; en el "
                           "encargo, la palabra es {{price}}."}],
         "theory": ["6.3", "2.3"]},
        {"n": 8, "sentence": "Much of the clean smell many people link with freshly washed clothes comes from "
                             "synthetic ingredients called ___.",
         "key": "musks / musk", "evidence": "a group of synthetics called musks",
         "why": "Corrige una creencia y da la respuesta: {{Many people think the smell of clean laundry comes from "
                "cotton, or from soap. In fact, much of it comes from a group of synthetics called musks}}. La frase del "
                "papel admite el plural que se oye y también el singular incontable.",
         "wrong": [{"answer": "soap", "kind": "candidato",
                    "why": "Es lo que la gente cree: {{Many people think}} … {{or from soap}}."},
                   {"answer": "cotton", "kind": "candidato",
                    "why": "También forma parte de la creencia que corrige {{In fact}}."},
                   {"answer": "molecules", "kind": "candidato",
                    "why": "Se oye ({{Synthetic molecules}}), pero es una categoría general, no el nombre de esos "
                           "ingredientes."}],
         "theory": ["6.3", "3.3"]},
        {"n": 9, "sentence": "Unlike beginners, Helen begins by working on a perfume’s ___.",
         "key": "base (notes) / base note", "evidence": "It’s the base that people actually live with",
         "why": "Contrapone el error de los principiantes y lo que hace ella: {{The mistake beginners make is to "
                "spend all their effort on the opening. It’s the base that people actually live with, so that’s "
                "where I begin}}. Se acepta [[base]] o [[base notes]], que se oye antes, y también el singular [[base note]], que encaja en la "
                "frase aunque no se oiga tal cual.",
         "wrong": [{"answer": "opening", "kind": "candidato",
                    "why": "Es donde se equivocan los principiantes ({{spend all their effort on the opening}})."},
                   {"answer": "top notes", "kind": "candidato",
                    "why": "Son las notas de salida, las que se huelen al principio: equivalen a {{the opening}}."},
                   {"answer": "heart notes", "kind": "candidato",
                    "why": "Se mencionan, pero no son por donde empieza."}],
         "theory": ["6.3", "3.3"]},
        {"n": 10, "sentence": "Each early version of a perfume is tried out on strips of paper known as ___.",
         "key": "blotters", "evidence": "thin strips of paper called blotters",
         "why": "{{Every version is tried first on thin strips of paper called blotters}}. La frase del papel ya da "
                "la definición ([[strips of paper]]): solo falta el nombre, en plural.",
         "wrong": [{"answer": "skin", "kind": "candidato",
                    "why": "Es la segunda prueba, no el papel: {{and then, more importantly, on skin}}."},
                   {"answer": "blotter", "kind": "forma",
                    "why": "Se oye en plural y la frase ([[strips … known as]]) lo pide."},
                   {"answer": "blotting paper", "kind": "sinónimo", "why": "No es lo que se oye."}],
         "theory": ["6.3", "6.4"]},
        {"n": 11, "sentence": "The longest Helen has ever spent developing a single perfume is ___.",
         "key": "five years / 5 years",
         "evidence": "The longest I’ve ever worked on a single perfume is five years",
         "why": "Primero da lo habitual y después su caso extremo: {{usually takes between one and three years}} … "
                "{{The longest I’ve ever worked on a single perfume is five years}}. La cifra puede escribirse en "
                "número.",
         "wrong": [{"answer": "three years", "kind": "candidato",
                    "why": "Es el límite de lo habitual ({{between one and three years}}), no su récord."},
                   {"answer": "five", "kind": "incompleta",
                    "why": "Sin [[years]] la duración queda incompleta."}],
         "theory": ["6.3", "6.4"]},
        {"n": 12, "sentence": "Most failed perfumes are rejected for being too ___ to products already on sale.",
         "key": "similar", "evidence": "it’s too similar to something already on the shelves",
         "why": "Descarta la causa que parecería obvia y da la habitual: {{It’s rarely because they smell "
                "unpleasant. Far more often, a perfume fails simply because it’s too similar to something already on "
                "the shelves}}.",
         "wrong": [{"answer": "unpleasant", "kind": "candidato",
                    "why": "Descartado: {{It’s rarely because they smell unpleasant}}; además, no encaja con "
                           "[[too … to]]."},
                   {"answer": "close", "kind": "sinónimo", "why": "Encaja en la frase, pero no es lo que se oye."}],
         "theory": ["6.3", "2.3"]},
        {"n": 13, "sentence": "To rest their noses, most perfumers Helen knows smell their own ___.",
         "key": "skin", "evidence": "simply smell their own skin",
         "why": "Contrapone la costumbre de las tiendas y la de los perfumistas: {{You’ll often see little bowls of "
                "coffee beans in perfume shops}} … {{Most perfumers I know simply smell their own skin}}.",
         "wrong": [{"answer": "coffee beans", "kind": "candidato",
                    "why": "Es lo que ofrecen las tiendas, y la hablante duda de que sirva: {{there’s very little "
                           "evidence that they help}}."},
                   {"answer": "skins", "kind": "forma", "why": "Incontable: [[their own skin]]."}],
         "theory": ["6.3", "3.2"]},
        {"n": 14, "sentence": "Perfumers borrow more descriptive words from the vocabulary of ___ than from any "
                              "other.",
         "key": "colour / color", "evidence": "and above all from colour",
         "why": "Enumera tres préstamos y destaca el último: {{From music we take notes and harmony; from touch, "
                "words like soft, sharp or velvety; and above all from colour}}. Se acepta la grafía americana.",
         "wrong": [{"answer": "music", "kind": "candidato",
                    "why": "Es una de las fuentes, pero no la principal: {{above all}} va con [[colour]]."},
                   {"answer": "touch", "kind": "candidato", "why": "Lo mismo: una fuente más, no la principal."},
                   {"answer": "colours", "kind": "forma", "why": "Se oye en singular: {{from colour}}."}],
         "theory": ["6.3", "6.5"]},
        {"n": 15, "sentence": "Helen tries not to describe perfumes using words connected with ___.",
         "key": "taste", "evidence": "The one vocabulary I try to avoid is taste",
         "why": "{{The one vocabulary I try to avoid is taste}}, y lo explica: {{Call a perfume sweet or fruity and "
                "everyone imagines a dessert}}.",
         "wrong": [{"answer": "dessert", "kind": "candidato",
                    "why": "Es lo que imagina la gente al oír [[sweet]] o [[fruity]], no el vocabulario que evita."},
                   {"answer": "colour", "kind": "candidato",
                    "why": "Es justo el vocabulario que más usa ({{above all from colour}})."}],
         "theory": ["6.3", "3.3"]},
    ],
}

# ---------- Part 3 · Interview ----------
P3 = {
    "num": "S01",
    "subtitle": "SIM-01 · Part 3",
    "difficulty": 3,
    "wpm": 170,
    "first": 16,
    "ctx": "You will hear part of an interview with Hannah Price, who designs board games.",
    "speakers": {"Interviewer": "Ryan", "Hannah": "Emily"},
    "host": "Interviewer",
    "lex": ["carry the conversation", "no amount of X will rescue it", "go quiet", "save face", "make a mess of sth", "decide the odd battle but never the war", "knock sb out (of a game)", "the highest compliment one can pay", "be generous with (suggestions)"],
    "turns": [
        ("Interviewer",
         "My guest today is Hannah Price, whose board games are now played in more than twenty countries. Hannah, "
         "sales of board games to adults have been rising steadily for years. Why do you think that is?"),
        ("Hannah",
         "The usual answer is that people are tired of screens, and I’m sure that’s part of it, but I don’t think "
         "it’s the heart of the matter. Plenty of people who play board games spend all day on their phones and are "
         "perfectly happy to do so. What a game offers is something rather harder to find: a reason to sit round a "
         "table with other people for a couple of hours without anyone having to carry the conversation. The rules "
         "give everyone something to do with their hands and something to talk about. For a lot of adults, "
         "especially those who find socialising a bit of an effort, that structure comes as a real relief."),
        ("Interviewer",
         "So where does a new game begin? With a theme? A story?"),
        ("Hannah",
         "People are always a little disappointed when I tell them, but almost never. The theme, whether it’s "
         "pirates or gardens or whatever, usually arrives quite late, once I know what the game is actually about. "
         "What I start with is a single decision that I find interesting: a moment where you have to choose between "
         "two things you want, knowing you can’t have both. If that one choice is genuinely hard, I can build a "
         "whole game around it. If it isn’t, no amount of beautiful artwork will rescue it."),
        ("Interviewer",
         "And then the game goes out to people who test it for you. How much notice do you take of what they say?"),
        ("Hannah",
         "Of what they say? Surprisingly little. Testers are wonderfully generous with their suggestions, and most "
         "of them are wrong, not because the testers are foolish, but because they’re trying to solve the problem "
         "they can see rather than the one underneath it. What I’ve learnt to pay attention to is what they do. "
         "When someone picks up the rules for the third time, or goes quiet for ten minutes, or starts checking "
         "their phone while everyone else takes their turn, that tells me far more than any questionnaire. Games "
         "rarely fail because they’re too difficult. They fail when players stop feeling that their choices make "
         "any difference."),
        ("Interviewer",
         "Let’s talk about luck. Serious players often complain that dice spoil a good strategy game. Would you "
         "agree?"),
        ("Hannah",
         "I understand the complaint, but I’ve come to think that a certain amount of luck is essential. In a game "
         "of pure strategy, the strongest player wins nearly every time, and before long the others simply stop "
         "wanting to play with them. Luck keeps everyone in the game until the very end. It also gives the loser a "
         "way of saving face: they can always blame the dice, even if, privately, they know they made a mess of "
         "it. The trick is to let luck decide the odd battle, but never the war."),
        ("Interviewer",
         "After all these years, is there anything about the way people play your games that still surprises you?"),
        ("Hannah",
         "All the time. I’ll spend months getting the rules exactly right, and then I’ll visit a family who’ve been "
         "playing one of my games for a year and discover they’ve quietly changed half of them. They’ve added a rule "
         "so that the youngest player can never be knocked out, or they let you swap cards with whoever’s sitting "
         "opposite. When I was starting out, I found that rather hurtful, as if all my careful balancing had been "
         "for nothing. These days I take it as the highest compliment a player can pay. It means the game has "
         "stopped being mine and has become theirs."),
    ],
    "items": [
        {"n": 16, "type": "Actitud y opinión", "speaker": "Hannah",
         "stem": "What does Hannah believe is the main reason why board games have become popular with adults?",
         "options": ["They give people a welcome break from their screens.",
                     "They appeal to adults who enjoy competing with their friends.",
                     "They provide a structure that makes socialising less demanding.",
                     "They have become cheaper than most other forms of entertainment."],
         "key": "C",
         "evidence": ["a reason to sit round a table with other people for a couple of hours without anyone having "
                      "to carry the conversation",
                      "that structure comes as a real relief"],
         "why": "Hannah descarta la explicación habitual y da la suya con una señal clara ({{What a game offers is "
                "something rather harder to find}}): una excusa para reunirse {{without anyone having to carry the "
                "conversation}}. Lo remata con quién lo agradece más: {{especially those who find socialising a bit "
                "of an effort, that structure comes as a real relief}}. [[Less demanding]] parafrasea [[a bit of an "
                "effort]] y [[relief]].",
         "theory": ["7.1", "3.3"],
         "distractors": {
             "A": {"kinds": ["4.2", "4.5"],
                   "why": "Es {{The usual answer}}, y Hannah solo le concede una parte ({{I’m sure that’s part of "
                          "it}}) antes de negar que sea lo principal: {{I don’t think it’s the heart of the "
                          "matter}}. La pregunta pide [[the main reason]]."},
             "B": {"kinds": ["4.8"],
                   "why": "Nadie habla de competir con los amigos en esta respuesta; lo que destaca Hannah es "
                          "estar juntos sin esfuerzo, no ganar."},
             "D": {"kinds": ["4.8"],
                   "why": "El precio no aparece en la entrevista. El entrevistador habla de {{sales of board games "
                          "to adults}}, pero no de lo que cuestan."},
         }},
        {"n": 17, "type": "Detalle", "speaker": "Hannah",
         "stem": "According to Hannah, the starting point for a new game is usually",
         "options": ["a difficult choice that players will have to make.",
                     "a story that she would like players to experience.",
                     "an idea for how the finished game should look.",
                     "a theme that she expects to appeal to buyers."],
         "key": "A",
         "evidence": ["What I start with is a single decision that I find interesting"],
         "why": "Lo dice con una señal inequívoca: {{What I start with is a single decision that I find "
                "interesting}}, y la describe: {{you have to choose between two things you want, knowing you can’t "
                "have both}}. [[A difficult choice]] recoge [[decision]] y [[genuinely hard]].",
         "theory": ["7.2", "2.3"],
         "distractors": {
             "B": {"kinds": ["4.2", "4.4"],
                   "why": "La historia la propone el entrevistador ({{With a theme? A story?}}) y Hannah la "
                          "descarta: {{almost never}}."},
             "C": {"kinds": ["4.1"],
                   "why": "Eco de {{no amount of beautiful artwork will rescue it}}: el aspecto del juego aparece "
                          "solo para decir que no salva una mala decisión, no como punto de partida."},
             "D": {"kinds": ["4.2", "4.7"],
                   "why": "El tema llega al final, no al principio: {{usually arrives quite late, once I know what "
                          "the game is actually about}}. Además, nada se dice de lo que gusta a los compradores."},
         }},
        {"n": 18, "type": "Detalle", "speaker": "Hannah",
         "stem": "What does Hannah say about the people who test her games?",
         "options": ["Their suggestions frequently lead her to change the rules.",
                     "They tend to find her games harder than she intended.",
                     "They are reluctant to say what they really think.",
                     "Their behaviour while playing tells her more than their comments."],
         "key": "D",
         "evidence": ["What I’ve learnt to pay attention to is what they do",
                      "that tells me far more than any questionnaire"],
         "why": "Contrapone lo que dicen y lo que hacen: de lo que dicen hace {{Surprisingly little}} caso, y en "
                "cambio {{What I’ve learnt to pay attention to is what they do}}. Los ejemplos (volver a las reglas, "
                "quedarse callado, mirar el móvil) dicen más que cualquier cuestionario: {{that tells me far more than any questionnaire}}.",
         "theory": ["3.1", "7.2"],
         "distractors": {
             "A": {"kinds": ["4.6"],
                   "why": "Las sugerencias existen ({{wonderfully generous with their suggestions}}), pero Hannah "
                          "dice lo contrario de que la hagan cambiar: {{most of them are wrong}}."},
             "B": {"kinds": ["4.1", "4.2"],
                   "why": "Eco de {{too difficult}}, que Hannah usa para negarlo como causa de fracaso: {{Games "
                          "rarely fail because they’re too difficult}}. No dice que a sus probadores les parezcan "
                          "difíciles."},
             "C": {"kinds": ["4.6"],
                   "why": "Contradice lo que cuenta: los probadores son {{wonderfully generous with their "
                          "suggestions}}. El problema no es que callen, sino que proponen soluciones al problema "
                          "equivocado."},
         }},
        {"n": 19, "type": "Actitud y opinión", "speaker": "Hannah",
         "stem": "What is Hannah’s view of the role of luck in games?",
         "options": ["It should be kept to a minimum in games for serious players.",
                     "It helps to keep weaker players involved until the end.",
                     "It makes games more entertaining for people watching them.",
                     "It should be allowed to decide the result of short games only."],
         "key": "B",
         "evidence": ["Luck keeps everyone in the game until the very end"],
         "why": "Lo justifica con lo que pasa sin azar: {{the strongest player wins nearly every time}} y los "
                "demás {{stop wanting to play with them}}. Su conclusión: {{Luck keeps everyone in the game until the "
                "very end}}. [[Weaker players]] son los que perderían siempre; [[involved]] parafrasea [[in the "
                "game]].",
         "theory": ["3.3", "3.4"],
         "distractors": {
             "A": {"kinds": ["4.4"],
                   "why": "Es la queja de otros ({{Serious players often complain that dice spoil a good strategy "
                          "game}}), que Hannah entiende pero no comparte: {{I’ve come to think that a certain "
                          "amount of luck is essential}}."},
             "C": {"kinds": ["4.8"],
                   "why": "No habla de espectadores en ningún momento: todo lo que dice se refiere a quienes "
                          "juegan."},
             "D": {"kinds": ["4.1", "4.6"],
                   "why": "Eco de {{let luck decide the odd battle, but never the war}}: el azar decide momentos "
                          "concretos de cualquier partida, nunca el resultado final; la duración no se menciona."},
         }},
        {"n": 20, "type": "Sentimiento", "speaker": "Hannah",
         "stem": "How does Hannah feel now when she discovers that players have changed her rules?",
         "options": ["frustrated that her careful work has gone to waste",
                     "curious to find out whether their changes improve the game",
                     "flattered that they now treat the game as their own",
                     "worried that some of the changes are unfair to children"],
         "key": "C",
         "evidence": ["These days I take it as the highest compliment a player can pay"],
         "why": "La señal temporal separa lo que sentía de lo que siente: {{These days I take it as the highest "
                "compliment a player can pay}}, porque el juego {{has become theirs}}. [[Flattered]] es la "
                "reacción a un cumplido, y [[treat the game as their own]] parafrasea {{has become theirs}}.",
         "theory": ["3.3", "3.4"],
         "distractors": {
             "A": {"kinds": ["4.7"],
                   "why": "Es lo que sentía al principio ({{When I was starting out, I found that rather hurtful, "
                          "as if all my careful balancing had been for nothing}}), no lo que siente ahora, que es lo "
                          "que pregunta el enunciado ([[now]])."},
             "B": {"kinds": ["4.8"],
                   "why": "No dice que quiera comprobar si las reglas nuevas funcionan mejor; ni siquiera las "
                          "valora."},
             "D": {"kinds": ["4.1", "4.6"],
                   "why": "Eco de {{the youngest player}}: la regla que cita protege a los niños ({{can never be "
                          "knocked out}}), no los perjudica, y Hannah no la critica."},
         }},
    ],
}

# ---------- Part 4 · Multiple matching ----------
P4 = {
    "num": "S01",
    "subtitle": "SIM-01 · Part 4",
    "difficulty": 3,
    "wpm": 170,
    "first": 21,
    "ctx": "You will hear five short extracts in which people are talking about completing a long-distance walk.",
    "lex": ["didn’t know where to look", "come crowding in", "catch sb out", "floor sb (what floored me)",
            "bored stiff", "nothing whatsoever to get up for", "with one’s fiftieth looming", "too proud to",
            "half a step behind", "less noble"],
    "tasks": [
        {"prompt": "what finally prompted each speaker to do the walk",
         "options": ["a long-held ambition",
                     "advice from a medical professional",
                     "a promise made to someone close to them",
                     "the chance to raise money for a cause",
                     "something they had read",
                     "the loss of their job",
                     "the wish to spend time with a relative",
                     "the approach of a significant birthday"],
         "extras": {
             "A": "Speaker 1 lo menciona como antecedente ({{I’d been saying I’d walk the whole coast path for the "
                  "best part of twenty years}}) y él mismo lo rebaja: {{without ever really meaning it}}. Tampoco "
                  "el plan de Speaker 2 con su hermana ({{had always planned to do the walk together}}) es lo que "
                  "la puso en marcha.",
             "D": "Speaker 3 lo descarta: {{everyone assumed I was raising money for something}}, y a continuación "
                  "da el motivo real.",
             "G": "Speaker 2 pensaba hacer la caminata con su hermana, pero al final fue sola; Speaker 5 caminó "
                  "unos días con su hijo, pero {{that was never the point of it}}."}},
        {"prompt": "what each speaker found most difficult about the experience",
         "options": ["physical discomfort",
                     "the monotony of walking day after day",
                     "adjusting to ordinary life afterwards",
                     "being alone with their thoughts",
                     "finding their way",
                     "keeping up with a companion",
                     "accepting kindness from strangers",
                     "the persistent bad weather"],
         "extras": {
             "B": "Speaker 3 esperaba aburrirse y no fue así: {{People had warned me I’d be bored stiff by the "
                  "second week on the trail, and I never was}}.",
             "E": "Speaker 4 lo descarta: {{Getting lost was never a worry, at least}}.",
             "H": "Speaker 2 acepta la lluvia sin darle importancia: {{the rain, which barely stopped for a "
                  "fortnight, I just accepted}}."}},
    ],
    "speakers": [
        {"voice": "William",
         "text": "I’d been saying I’d walk the whole coast path for the best part of twenty years, the way you do, "
                 "without ever really meaning it. What finally got me out of the door was a routine check-up. My "
                 "doctor took my blood pressure, looked at me over her glasses and said that unless I started "
                 "moving, she’d be seeing a great deal more of me. The blisters, when they came, were nothing, "
                 "honestly. What I found genuinely hard was people’s kindness. I’ve always prided myself on "
                 "managing on my own, so when a farmer insisted on drying my boots by his fire and feeding me "
                 "supper, I didn’t know where to look.",
         "items": [
             {"n": 21, "key": "B",
              "evidence": ["What finally got me out of the door was a routine check-up"],
              "why": "La señal {{What finally got me out of the door}} introduce el desencadenante: una revisión en "
                     "la que su médica le advirtió que {{unless I started moving, she’d be seeing a great deal "
                     "more of me}}.",
              "touched": {"A": {"kinds": ["4.3"],
                                "why": "Es el antecedente, no lo que le hizo empezar: llevaba años diciéndolo "
                                       "({{for the best part of twenty years}}), {{without ever really meaning "
                                       "it}} (§8.3)."}},
              "theory": ["8.1", "8.3", "2.3"]},
             {"n": 26, "key": "G",
              "evidence": ["What I found genuinely hard was people’s kindness"],
              "why": "Lo dice con todas las letras: {{What I found genuinely hard was people’s kindness}}. Lo explica "
                     "su orgullo ({{I’ve always prided myself on managing on my own}}), y la escena del granjero lo "
                     "confirma: {{I didn’t know where to look}} = no sabía dónde meterse.",
              "touched": {"A": {"kinds": ["4.2"],
                                "why": "Las ampollas aparecen para descartarlas: {{The blisters, when they came, "
                                       "were nothing, honestly}}."}},
              "theory": ["8.1", "4.2"]}]},
        {"voice": "Molly",
         "text": "My sister and I had always planned to do the walk together once the kids were older. Then she "
                 "fell ill, and near the end she made me promise I’d go anyway, with or without her. So I did, the "
                 "following spring. People warned me about the hills, but they weren’t the problem, and the rain, "
                 "which barely stopped for a fortnight, I just accepted. You get wet, you stay wet. What caught me "
                 "out was the silence. With nobody to talk to, everything I’d been too busy to think about since "
                 "she died came crowding in, mile after mile.",
         "items": [
             {"n": 22, "key": "C",
              "evidence": ["near the end she made me promise I’d go anyway, with or without her"],
              "why": "Lo que la puso en marcha fue la promesa a su hermana enferma: {{near the end she made me "
                     "promise I’d go anyway, with or without her}}. {{So I did}} lo confirma.",
              "touched": {"G": {"kinds": ["4.3"],
                                "why": "El plan de caminar juntas es el antecedente ({{had always planned to do the "
                                       "walk together once the kids were older}}) y nunca llegó a cumplirse: fue "
                                       "sola (§8.3)."}},
              "theory": ["8.1", "8.3"]},
             {"n": 27, "key": "D",
              "evidence": ["What caught me out was the silence"],
              "why": "{{What caught me out}} = lo que la pilló desprevenida. El silencio la dejó a solas con lo que "
                     "había evitado pensar: {{everything I’d been too busy to think about since she died came "
                     "crowding in}}.",
              "touched": {"A": {"kinds": ["4.7"],
                                "why": "Le habían advertido de las cuestas, pero {{they weren’t the problem}}: lo "
                                       "esperado no fue lo difícil."},
                          "H": {"kinds": ["4.2"],
                                "why": "La lluvia no le costó: {{I just accepted}}, {{You get wet, you stay "
                                       "wet}}."}},
              "theory": ["2.3", "4.7", "8.1"]}]},
        {"voice": "Andrew",
         "text": "Oddly, the walk itself was the easy bit. What floored me was coming home. Back at a desk in a new "
                 "job, I’d catch myself staring out of the window, longing for the one simple task of putting one "
                 "foot in front of the other. People had warned me I’d be bored stiff by the second week on the "
                 "trail, and I never was. As for why I went, everyone assumed I was raising money for something. "
                 "The truth’s less noble: after twenty-two years, my company closed our office, and I found myself "
                 "with a decent redundancy payment and nothing whatsoever to get up for.",
         "items": [
             {"n": 23, "key": "F",
              "evidence": ["my company closed our office, and I found myself with a decent redundancy payment and "
                           "nothing whatsoever to get up for"],
              "why": "Tras {{As for why I went}} llega el motivo: cerraron su oficina y se quedó con una "
                     "indemnización por despido ({{a decent redundancy payment}}) y sin nada que hacer.",
              "touched": {"D": {"kinds": ["4.2"],
                                "why": "Es lo que suponía todo el mundo, y él lo corrige: {{everyone assumed I was "
                                       "raising money for something}}, {{The truth’s less noble}}."}},
              "theory": ["8.1", "4.2", "2.3"]},
             {"n": 28, "key": "C",
              "evidence": ["What floored me was coming home"],
              "why": "La respuesta de la Task Two llega antes que la de la Task One (§8.1): {{What floored me was "
                     "coming home}}. De vuelta en un trabajo de oficina, echa de menos caminar: {{longing for the "
                     "one simple task of putting one foot in front of the other}}.",
              "touched": {"B": {"kinds": ["4.7"],
                                "why": "Le avisaron de que se aburriría, pero no ocurrió: {{I’d be bored stiff by the "
                                       "second week on the trail, and I never was}}."}},
              "theory": ["8.1", "4.7"]}]},
        {"voice": "Emma",
         "text": "My friend Kate came with me, and she walks as if she’s permanently late for a train. I spent three "
                 "weeks half a step behind her, too proud to ask her to slow down, and that was far more exhausting "
                 "than the distance itself. Getting lost was never a worry, at least; the route’s beautifully "
                 "signposted. As for why I went, people assumed it was turning forty, but birthdays have never "
                 "bothered me. It was an article I came across about a woman in her late seventies who’d done the "
                 "whole route alone. I remember thinking: if she can manage it, what exactly is my excuse?",
         "items": [
             {"n": 24, "key": "E",
              "evidence": ["It was an article I came across about a woman in her late seventies who’d done the "
                           "whole route alone"],
              "why": "{{It was an article I came across}}: leyó la historia de una mujer de casi ochenta años que "
                     "había hecho la ruta sola, y se preguntó {{what exactly is my excuse?}}",
              "touched": {"H": {"kinds": ["4.2"],
                                "why": "Es lo que suponía la gente, y ella lo descarta: {{people assumed it was "
                                       "turning forty, but birthdays have never bothered me}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 29, "key": "F",
              "evidence": ["too proud to ask her to slow down, and that was far more exhausting than the distance "
                           "itself"],
              "why": "Su amiga camina muy deprisa ({{as if she’s permanently late for a train}}) y ella pasó tres "
                     "semanas {{half a step behind her}}: eso le costó {{far more exhausting than the distance "
                     "itself}}. La respuesta llega antes que la de la Task One.",
              "touched": {"E": {"kinds": ["4.2"],
                                "why": "Orientarse no fue problema: {{Getting lost was never a worry, at least}}."},
                          "A": {"kinds": ["4.5"],
                                "why": "El esfuerzo físico de la distancia aparece como término de comparación, "
                                       "para decir que fue menos duro: {{far more exhausting than the distance "
                                       "itself}}."}},
              "theory": ["8.1", "4.5"]}]},
        {"voice": "Ava",
         "text": "With my fiftieth looming, I wanted to prove to myself that I could still do something properly "
                 "difficult, before it was too late. My son came along for the first few days, which was lovely, "
                 "but that was never the point of it. I’d trained for months, so I assumed my body would cope. It "
                 "didn’t. By the fourth day my knees had swollen so badly that every descent was agony, and I "
                 "seriously thought about giving up. Oddly enough, once he’d gone home, I found I loved my own "
                 "company, which surprised everyone, including me.",
         "items": [
             {"n": 25, "key": "H",
              "evidence": ["With my fiftieth looming, I wanted to prove to myself that I could still do something "
                           "properly difficult"],
              "why": "{{With my fiftieth looming}}: se acercaba su cincuenta cumpleaños y quería demostrarse que aún "
                     "podía hacer algo difícil.",
              "touched": {"G": {"kinds": ["4.2"],
                                "why": "Su hijo la acompañó unos días, pero {{that was never the point of it}}."}},
              "theory": ["8.1", "4.2"]},
             {"n": 30, "key": "A",
              "evidence": ["By the fourth day my knees had swollen so badly that every descent was agony"],
              "why": "Esperaba que el cuerpo aguantara ({{I assumed my body would cope. It didn’t.}}) y no fue así: "
                     "{{By the fourth day my knees had swollen so badly that every descent was agony}}.",
              "touched": {"D": {"kinds": ["4.2"],
                                "why": "La soledad le gustó: {{once he’d gone home, I found I loved my own "
                                       "company}}."}},
              "theory": ["8.1", "4.7"]}]},
    ],
}
