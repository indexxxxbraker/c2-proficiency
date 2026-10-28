# SIM-01 · Speaking · spec del test completo (formato de src/gen_SPK.py)
# Se monta con: python3 src/gen_SIM.py spk sim/SIM-01   (necesita red: Wikimedia Commons y edge-tts)
# Fotos: cada 'file' es el título del archivo en Commons (dominio público, CC0 o CC BY sin SA); gen_SPK vuelve a
# comprobar la licencia al descargarla. what/spec describen la foto real: revisarlos si se cambia alguna.

SPEC = {
    "num": "S01", "level": 3,
    "subtitle": "SIM-01 · Part 2: comunicarse · Part 3: el hogar",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "Do you like to have music on while you’re working or studying?",
         "model": "It depends entirely on what I’m doing. If it’s something routine, like sorting out emails, I’ll "
                  "happily have something on in the background. But the moment I need to concentrate on reading "
                  "or writing, I find lyrics really distracting, so it’s either silence or something instrumental "
                  "that I know so well I barely notice it."},
        {"q": "How do you usually celebrate your birthday?",
         "model": "Fairly quietly these days, to be honest. When I was younger I used to organise big parties, but "
                  "they always seemed to involve more stress than fun. Now I prefer a long dinner out with a handful of "
                  "close friends – somewhere nobody has to cook or clear up afterwards, which is a present in "
                  "itself."},
        {"q": "Do you think you’re a good judge of character?",
         "model": "I’d like to think so, but I’m not sure the evidence backs me up. I tend to warm to people very "
                  "quickly, which means I’ve occasionally trusted someone I really shouldn’t have. On the other "
                  "hand, my first impressions of people I don’t take to are almost always right – so perhaps I’m "
                  "only half a good judge."},
    ]},
    "p2": {
        "title": "Exhibition – Keeping in touch",
        "intro": "different ways in which people communicate",
        "q1_pics": ["C", "D"],
        "q1": "how the people in these pictures might be feeling about the way they are communicating",
        "context": "I’d like you to imagine that a communications museum is putting on an exhibition called "
                   "‘Keeping in touch’. These pictures are being considered for a poster advertising the "
                   "exhibition.",
        "task": "Talk together about the different ways of communicating that these pictures show. Then decide "
                "which picture would make the most effective poster.",
        "partner_voice": "Libby",
        "photos": [
            {"letter": "A", "file": "File:Telephone switchboard 6 Oct 1907 Salt Lake City.jpg",
             "what": "Una fotografía de 1907: en una sala amplia, una larga fila de operadoras, sentadas de espaldas, "
                     "trabaja ante una centralita telefónica que ocupa toda la pared.",
             "spec": "Que el trabajo exigía rapidez y mucha concentración; que oían a medias conversaciones ajenas; "
                     "que era uno de los pocos empleos de oficina abiertos a las mujeres de la época; que trabajaban "
                     "en silencio y bajo vigilancia.",
             "offers": "Muestra que hablar a distancia necesitaba intermediarios humanos: la tecnología no siempre "
                       "elimina a las personas, a veces solo las esconde.",
             "decision": "A favor: llama la atención y plantea cuánto hemos cambiado. En contra: puede dar al cartel "
                         "un aire de lección de historia."},
            {"letter": "B", "file": "File:Postman on Wandle Rd, SW17 (5479444030).jpg",
             "what": "Un cartero de Royal Mail, con un fajo de cartas en la mano, empuja un carrito rojo de reparto "
                     "por la acera de una calle de casas adosadas.",
             "spec": "Que lleva años haciendo la misma ruta y conoce a los vecinos; que hoy reparte más facturas, "
                     "folletos y paquetes que cartas personales.",
             "offers": "La comunicación lenta y física: una carta exige esfuerzo y se guarda; también, el valor de "
                       "alguien que recorre el barrio cada día.",
             "decision": "A favor: cercana y reconocible. En contra: puede leerse como pura nostalgia, o como algo "
                         "demasiado cotidiano para un cartel."},
            {"letter": "C", "file": "File:Sign language, 2014 (01).jpg",
             "what": "Dos mujeres, sentadas a una mesa, conversan en lengua de signos: una le cuenta algo con las "
                     "manos y la otra la escucha sonriendo, a punto de responder.",
             "spec": "Que son amigas y quizá hacía tiempo que no se veían; que la conversación es animada y ninguna "
                     "de las dos aparta la vista de la otra.",
             "offers": "Recuerda que comunicarse no depende de la voz ni de la tecnología: exige atención plena y "
                       "mirar al otro.",
             "decision": "A favor: original, amplía la idea de comunicación. En contra: quizá haya que explicarla, "
                         "y no debe usarse como simple curiosidad."},
            {"letter": "D", "file": "File:Beautiful senior couple working on laptop in the garden.jpg",
             "what": "Una pareja de cierta edad, abrazada, sonríe ante la pantalla de un portátil: todo indica que "
                     "hablan por videollamada con alguien a quien quieren.",
             "spec": "Que al otro lado están los hijos o los nietos, que viven lejos; que la llamada es un momento "
                     "esperado de la semana; que quizá les costó acostumbrarse a la tecnología.",
             "offers": "Cercanía a pesar de la distancia, pero también sus límites: verse no es lo mismo que estar "
                       "juntos.",
             "decision": "A favor: actual, emotiva y fácil de entender. En contra: es la opción más previsible."},
            {"letter": "E", "file": "File:\"Comadres\" talking (50222476403).jpg",
             "what": "Fotografía en blanco y negro: dos mujeres mayores charlan en un mercado al aire libre; una de "
                     "ellas subraya lo que dice señalando con el dedo.",
             "spec": "Que se conocen de toda la vida y coinciden cada semana en el mercado; que se están poniendo al "
                     "día de las novedades del barrio, y que la charla les importa más que la compra.",
             "offers": "La comunicación sin motivo ni aparato: hablar por hablar, que es lo que mantiene unida una "
                       "calle, un barrio o un pueblo.",
             "decision": "A favor: cálida, universal, sin tecnología de por medio; el gesto da vida a la foto. En "
                         "contra: puede parecer nostálgica y dejar fuera a los visitantes jóvenes."},
        ],
        "phase1_lines": [
            "The two women signing look completely absorbed in each other – there’s nothing between them, not "
            "even a screen.",
            "I’d imagine the couple are thrilled to see whoever’s on the other end, even if it’s no substitute "
            "for a hug.",
        ],
        "decision": "La D convence por cercanía; la A, por la curiosidad que despierta; la C, por recordar que "
                    "comunicarse no es solo tecnología. Una salida negociada: la D en el cartel y la A dentro, a la "
                    "entrada, para que el visitante vea el contraste.",
        "language": ["What the poster needs, above all, is …", "This one raises a question rather than answering it.",
                     "A and E make a striking pair: …", "If it came down to a choice between …"],
        "partner": [
            {"text": "I find the video call quite moving, actually. They’re clearly delighted, and they’re huddled "
                     "together in front of the screen, as if they’re trying to close the distance.",
             "provokes": "Una observación fina: recógela con sus palabras y llévala a la otra foto.",
             "react": "‘Trying to close the distance’ – that’s exactly it. And the two women signing don’t have any "
                      "distance to close, which is probably why they look so relaxed.",
             "theory": ["6.2"]},
            {"text": "My vote would be for the switchboard operators. Old photographs always draw people in, and this "
                     "one shows that a phone call once depended on a whole roomful of people.",
             "provokes": "Una propuesta razonable: concede lo que tiene de bueno antes de objetar.",
             "react": "You’ve got a point about old photographs – people do stop and look. My only worry is that it "
                      "might make the exhibition look like a history lesson rather than something to do with "
                      "visitors’ own lives.",
             "theory": ["6.3"]},
            {"text": "Honestly, the two women at the market say it all. Nobody stops to chat like that any more – most "
                     "people don’t even know who lives next door these days.",
             "provokes": "Una generalización exagerada: matízala sin desautorizar a tu compañera.",
             "react": "I think that’s putting it a bit strongly. Plenty of people still stop for a chat at the market "
                      "or the school gate – it’s just that some of the gossip has moved to group chats.",
             "theory": ["6.4", "6.3"]},
            {"text": "You’ve been very quiet about the postman. What do you make of him? Do you think anyone still "
                     "gets excited about a letter?",
             "provokes": "Te cede el turno con una pregunta: respóndela y amplía el alcance más allá de la foto.",
             "react": "I think they do, actually – precisely because letters are so rare now. A letter takes effort, and I think "
                      "people can tell. Mind you, most of what he’s delivering is probably bills.",
             "theory": ["6.5"]},
            {"text": "We’re running out of time, so why don’t we settle on the video call? It’s modern and cheerful, "
                     "and almost everyone can relate to it.",
             "provokes": "Una propuesta de cierre: acepta, negocia o deja constancia del desacuerdo, pero decidid.",
             "react": "I could live with that, although it is a bit predictable. How about the video call on the "
                      "poster and the switchboard just inside the entrance, so that people can see how far we’ve come?",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "home and belonging",
        "cards": [
            {"q": "What makes a place feel like home?",
             "ideas": ["people", "routine", "memories"],
             "plan": {
                 "Operación": "[[What makes]]: identificar factores y jerarquizarlos (§3.1).",
                 "Postura": "Lo que hace hogar un sitio no es el edificio, sino las personas y los hábitos.",
                 "Línea 1": "Las personas: alguien que nota si vuelves ([[people]]).",
                 "Línea 2": "La rutina, infravalorada: pequeños hábitos que adaptan el sitio a ti ([[routine]]).",
                 "Contrapunto": "Los recuerdos explican el apego en retrospectiva, no que un sitio sea hogar ahora "
                                "([[memories]]).",
                 "Cierre": "El hogar se construye, y por eso puede construirse más de una vez (idea propia)."},
             "model": [
                 "That’s something I’ve thought about quite a lot, because I’ve moved several times in the last few "
                 "years. And what I’ve noticed is that a place can be perfectly comfortable without ever feeling "
                 "like home. So for me, the answer has much less to do with the building than with what happens "
                 "inside it and around it.",
                 "The most obvious factor is people. A flat you share with friends can feel like home within a "
                 "week, whereas a beautiful house in a street where you don’t know a soul can feel like a hotel for years. I "
                 "suppose home is partly the place where someone would notice if you didn’t come home.",
                 "Then there’s routine, which I think is underrated. It’s the small, repetitive things – knowing "
                 "which stair creaks, having a favourite chair, the café where they start making your coffee as "
                 "soon as you walk in. None of that is remarkable in itself, but taken together it gives you the "
                 "sense that the place has adjusted to you, and you to it.",
                 "Memories obviously play a part too, though I’d add a note of caution here. A place can be full of "
                 "memories and still not feel like home any more – plenty of people go back to the house they grew "
                 "up in and feel like visitors. Memories, then, may explain why a place seems "
                 "special in retrospect, rather than what makes it home now.",
                 "So, all in all, I’d say home is less a location than a relationship. You don’t so much find it as "
                 "build it, slowly, out of people and habits – and that, to me, is rather reassuring, because it "
                 "means you can do it more than once.",
             ],
             "comments": [
                 "Apertura personal que sitúa la respuesta y adelanta la postura: no es el edificio, sino lo que pasa "
                 "en él (§3.3). [[has much less to do with … than with …]] (§4.6).",
                 "Primera idea de la tarjeta ([[people]]) con un contraste concreto, [[whereas]], y una definición "
                 "propia que cierra el párrafo (§3.4).",
                 "Segunda idea ([[routine]]), jerarquizada con [[which I think is underrated]] (§3.3); detalles "
                 "concretos y una síntesis que los recoge: [[taken together]] (§4.5).",
                 "Contrapunto con la tercera idea ([[memories]]): concede y matiza. [[I’d add a note of caution "
                 "here]] (§4.2), un caso que lo demuestra y la distinción [[in retrospect, rather than … now]] (§4.6).",
                 "Cierre que responde a la pregunta con una fórmula propia: [[less a location than a "
                 "relationship]], [[You don’t so much … as …]] (§4.6), y una idea que va más allá de la tarjeta "
                 "(§3.4).",
             ],
             "follow_up": {"q": "Can a person feel at home in more than one place at the same time?",
                           "ideas": "Sí, si el hogar depende de personas y hábitos, como decía el long turn: quien "
                                    "vive entre dos ciudades puede sentirse en casa en las dos, aunque de forma "
                                    "distinta; el riesgo es no sentirse del todo en ninguna. Enlaza sin repetir: "
                                    "[[That follows on from what I was saying about routine …]]"}},
            {"q": "Is it important for people to put down roots?",
             "ideas": ["community", "opportunity", "identity"],
             "plan": {
                 "Operación": "[[Is it important]]: graduar y decir para quién y cuándo (§3.1).",
                 "Postura": "Importante para casi todos en algún momento, pero no para todos ni siempre.",
                 "Línea 1": "La comunidad: una red de apoyo que tarda años en formarse y no se traslada "
                            "([[community]]).",
                 "Línea 2": "Las oportunidades: quedarse puede cerrar puertas, e irse enseña lo que uno quiere "
                            "([[opportunity]]).",
                 "Contrapunto": "La identidad: hay quien la construye con los sitios por los que pasa "
                                "([[identity]]).",
                 "Cierre": "Las raíces importan, pero pueden ser personas y no un lugar (idea propia)."},
             "model": [
                 "I’d say it’s important for most people at some point in their lives, but I’m not convinced it’s "
                 "important for everyone, or at every stage. It rather depends on what you’re hoping to get out of "
                 "life, and on when you ask the question.",
                 "The strongest argument for putting down roots is community. If you stay in one place long enough, "
                 "you build up a network of people who know you – neighbours who’ll keep an eye on your house, "
                 "friends you can ring at two in the morning when something goes wrong. That kind of support takes "
                 "years to develop, and it simply can’t be packed up and taken with you when you move. People who "
                 "never stay anywhere for long often find they have plenty of acquaintances but very few people "
                 "they could really rely on.",
                 "On the other hand, there’s the question of opportunity. Staying put can mean turning down a better "
                 "job, a different kind of education, or simply the chance to see how other people live. For a lot "
                 "of young people especially, moving away is how they find out what they actually want – and some "
                 "of them only appreciate where they’re from once they’ve left.",
                 "Identity is where it gets more complicated. Some people feel that knowing exactly where they "
                 "belong gives them a kind of anchor. Others, though, build their sense of who they are out of the "
                 "places they’ve passed through, and I don’t think they’re any less rooted for it – their roots are "
                 "just a different shape.",
                 "So, on balance, I’d say roots matter, but they don’t have to be planted in one spot. What really "
                 "counts is having somewhere, or someone, to come back to.",
             ],
             "comments": [
                 "Responde de inmediato y gradúa (§3.1): [[for most people at some point]], [[or at every "
                 "stage]]; la postura ya incluye la condición de la que depende (§3.3).",
                 "Primera idea ([[community]]), desarrollada con ejemplos concretos y una consecuencia: lo que no se "
                 "puede llevar consigo (§3.4). [[The strongest argument for … is]] (§4.2).",
                 "Segunda idea ([[opportunity]]), en sentido contrario: [[On the other hand]] (§4.3); enumeración en "
                 "tres tiempos y una observación final que matiza (§4.6).",
                 "Tercera idea ([[identity]]) como contrapunto: [[is where it gets more complicated]] (§4.2); "
                 "contraste [[Some people … Others, though, …]] y una imagen que reformula la pregunta "
                 "([[their roots are just a different shape]]) (§4.5).",
                 "Cierre que vuelve a la pregunta con una idea propia: las raíces pueden ser personas. [[on "
                 "balance]] (§4.2), [[What really counts is]] (§4.6).",
             ],
             "follow_up": {"q": "Is it harder to put down roots in a big city than in a small town?",
                           "ideas": "No necesariamente: en un pueblo la comunidad ya existe, pero cuesta entrar en "
                                    "ella; en la ciudad hay que construirla, aunque hay más gente afín. Lo decisivo "
                                    "es quedarse el tiempo suficiente, que enlaza con la idea de comunidad del long "
                                    "turn."}},
        ],
        "discussion": [
            {"q": "Why do you think it’s become so hard for young people to leave home?",
             "theory": ["6.7"],
             "ideas": "La vivienda cara y el empleo inestable, pero también la comodidad y una relación con los "
                      "padres más fácil que antes; no siempre es un fracaso.",
             "lang": "It’s partly economic, of course, but I suspect parents and children simply get on better than "
                     "they used to."},
            {"q": "How much does the place where you grow up shape the person you become?", "theory": ["4.6"],
             "ideas": "Mucho en el acento, las costumbres y las expectativas; menos en el carácter. A veces lo que "
                      "más marca es el deseo de irse.",
             "lang": "More than we like to admit – even people who spend their lives trying to get away from a place are "
                     "shaped by it."},
            {"q": "Should governments do more to help people stay in the towns and villages they come from?",
             "theory": ["3.5", "6.3"],
             "ideas": "Servicios, transporte y buena conexión a internet, sí; subvencionar que la gente se quede sin "
                      "más, no: casi todos se van buscando oportunidades.",
             "lang": "They can make staying a realistic option, but they can’t – and shouldn’t – make it the only "
                     "one."},
            {"q": "Some people say home is a feeling rather than a place. What’s your view?",
             "theory": ["6.7", "6.3"],
             "ideas": "En parte; pero el lugar importa, porque los sentimientos se apoyan en olores, calles y "
                      "objetos concretos.",
             "lang": "I’d go along with that to some extent, but feelings need somewhere to attach themselves to."},
            {"q": "Can people really feel they belong to an online community?",
             "theory": ["4.3"],
             "ideas": "La pertenencia puede ser real (apoyo, intereses compartidos), pero es más frágil: es fácil "
                      "marcharse sin consecuencias.",
             "lang": "The sense of belonging can be perfectly genuine; what’s missing is any obligation to stay when "
                     "things get awkward."},
            {"q": "Why do people often feel more attached to their home town once they’ve moved away?",
             "theory": ["4.6"],
             "ideas": "La distancia idealiza y la identidad se nota por contraste; además, a menudo se echa de menos "
                      "una etapa de la vida más que el lugar.",
             "lang": "I think it’s often less the town they miss than the person they were when they lived there."},
        ],
    },
    "lex": ["a good judge of character", "the evidence backs me up", "a present in itself", "draw people in", "close the distance", "that’s putting it a bit strongly", "I could live with that", "put down roots", "stay put", "keep an eye on", "not know a soul", "in retrospect", "pack sth up", "an anchor (figurado)"],
}
