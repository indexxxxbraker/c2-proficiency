# SIM-02 · Speaking · spec del test completo (formato de src/gen_SPK.py)
# Se monta con: python3 src/gen_SIM.py spk sim/SIM-02   (necesita red: Wikimedia Commons y edge-tts)
# Fotos: cada 'file' es el título del archivo en Commons (dominio público, CC0 o CC BY sin SA); gen_SPK vuelve a
# comprobar la licencia al descargarla. what/spec describen la foto real: revisarlos si se cambia alguna.

SPEC = {
    "num": "S02", "level": 3,
    "subtitle": "SIM-02 · Part 2: cómo comemos · Part 3: éxito y ambición",
    "p1": {"questions": [
        {"q": "Where do you live?", "model": None},
        {"q": "And are you working or studying at the moment?", "model": None},
        {"q": "Are you someone who enjoys trying new things?",
         "model": "More so than I used to be. As a teenager I was quite cautious – I’d order the same dish every time "
                  "we went out. These days I try to say yes to things I’d once have turned down, within reason. Most of "
                  "them turn out to be perfectly pleasant, and every now and then one becomes a real passion."},
        {"q": "Is there a building in your town or city that you particularly like?",
         "model": "Yes, the old railway station. It’s nothing special from the outside, just brick and iron, but "
                  "inside there’s an enormous glass roof, and on a sunny morning the whole hall is flooded with light. "
                  "What I like most, I think, is that it’s still used for what it was built for, rather than being "
                  "turned into a shopping centre."},
        {"q": "Do you prefer big get-togethers or seeing friends in small groups?",
         "model": "Small groups, on the whole. In a big crowd the conversation tends to break up into lots of little "
                  "ones, and I end up drifting between them without really talking to anyone. With four or five "
                  "people you can actually follow a thread, and even disagree properly. That said, I do enjoy the "
                  "odd big celebration, as long as there’s a quiet corner somewhere."},
    ]},
    "p2": {
        "title": "Magazine cover – The way we eat",
        "intro": "different situations in which people eat",
        "q1_pics": ["A", "D"],
        "q1": "how the people in these pictures might be feeling about the meal they are having",
        "context": "I’d like you to imagine that a food magazine is publishing a special issue called ‘The way we "
                   "eat’. These pictures are being considered for the cover.",
        "task": "Talk together about the different attitudes to eating that these pictures show. Then decide which "
                "picture would make the most effective cover.",
        "partner_voice": "Ryan",
        "photos": [
            {"letter": "A", "file": "File:The Grimm family eating Sunday dinner 8d18337v.jpg",
             "what": "Fotografía de 1943: en una cocina modesta, una madre sentada a la mesa sirve la comida del "
                     "domingo a una de sus hijas pequeñas; alrededor, niñas y jóvenes de varias edades, entre platos, "
                     "tazas y fuentes.",
             "spec": "Que es el único momento de la semana en que comen todos juntos; que la madre trabaja fuera y "
                     "apenas se sienta; que la comida es sencilla, pero el domingo la convierte en un "
                     "acontecimiento.",
             "offers": "La comida como ritual familiar y como esfuerzo de quien la prepara: quien cocina rara vez "
                       "es quien más disfruta de la mesa.",
             "decision": "A favor: cálida y con historia, invita a comparar con hoy. En contra: puede leerse como "
                         "nostalgia de un pasado idealizado."},
            {"letter": "B",
             "file": "File:High school students eat lunch at a public school cafeteria in North Carolina 02.jpg",
             "what": "El comedor de un instituto: en primer plano, un chico con sudadera naranja bebe de un cartón de "
                     "leche ante una bandeja amarilla; detrás, mesas llenas de estudiantes que comen y charlan bajo el "
                     "lema del equipo del centro.",
             "spec": "Que tienen poco tiempo y comen deprisa; que el comedor es sobre todo un lugar social, donde "
                     "importa con quién te sientas; que la comida no les entusiasma.",
             "offers": "Comer como acto social entre iguales: la mesa decide grupos, amistades y también "
                       "exclusiones.",
             "decision": "A favor: animada y actual, atrae a lectores jóvenes. En contra: la comida apenas se ve y "
                         "puede parecer un reportaje sobre la escuela."},
            {"letter": "C", "file": "File:Motorbike food stall, Hua Hin (8288362869).jpg",
             "what": "Un mercado nocturno en Tailandia: una vendedora, con gorra y polo amarillo, conduce una moto "
                     "que arrastra un carrito lleno de tarros de frutos secos y dulces, entre mesas de restaurante con "
                     "mantel y gente que pasea.",
             "spec": "Que va de un sitio a otro según la hora; que tiene clientes fijos que la buscan; que vende cada "
                     "noche lo mismo, y que la gente come de pie o andando.",
             "offers": "Comer en la calle, rápido, barato y entre desconocidos: la comida como parte de la vida "
                       "pública de una ciudad.",
             "decision": "A favor: colorida y llamativa en un quiosco. En contra: puede parecer un anuncio de viajes "
                         "más que una reflexión sobre cómo comemos."},
            {"letter": "D", "file": "File:BC - Picnic (26933173737).jpg",
             "what": "Un pícnic en un parque soleado: dos mujeres jóvenes sonríen a la cámara sentadas sobre una manta "
                     "de cuadros de colores; una sostiene a un bebé de pie y una niña se ha tumbado a su lado; junto a "
                     "ellas, un cuenco de comida y un móvil; al fondo, mesas, una barbacoa y un parque infantil.",
             "spec": "Que han aprovechado el primer día de sol; que la comida es lo de menos; que los niños no paran "
                     "quietos y nadie mira el reloj, aunque el móvil está a mano.",
             "offers": "Comer como excusa para estar juntos al aire libre, sin horarios ni mesa ni ceremonia.",
             "decision": "A favor: alegre y luminosa, transmite placer. En contra: es la opción más previsible, casi "
                         "de catálogo."},
            {"letter": "E", "file": "File:IMac at Lunch time.jpg",
             "what": "Un plato de pasta con tomate, con tenedor y cuchillo, sobre un escritorio de oficina junto al "
                     "teclado de un ordenador encendido, entre notas adhesivas, papeles y una botella de agua; no hay "
                     "nadie.",
             "spec": "Que quien come ahí lo hace solo y sin dejar de trabajar; que la pausa para comer ha "
                     "desaparecido; que ni siquiera recordará qué ha comido.",
             "offers": "El reverso del tema: comer solo, deprisa y sin prestar atención; plantea qué se pierde.",
             "decision": "A favor: provoca, es la más original y abre debate. En contra: es la menos apetecible para "
                         "una revista de cocina."},
        ],
        "phase1_lines": [
            "The mother in the old photograph is so busy serving everyone that I doubt she gets to eat much herself.",
            "The picnic looks far more relaxed – nobody seems to care what time it is, or whether the baby eats a "
            "thing.",
        ],
        "decision": "La D convence por alegre; la E, por provocadora; la A, por el contraste con el pasado. Una salida "
                    "negociada: la E en la portada, con un titular que la explique, y la D en las páginas interiores.",
        "language": ["What a cover needs to do, first and foremost, is …",
                     "This one makes you stop and think rather than just feel hungry.",
                     "A and E couldn’t be more different: …",
                     "If it came down to comfort versus provocation, …"],
        "partner": [
            {"text": "I think the children in the old photo look rather solemn, actually. Maybe Sunday dinner was "
                     "more of a duty than a pleasure in those days.",
             "provokes": "Una lectura distinta de la foto: concede lo que tiene de razonable y matízala con lo que "
                         "se ve.",
             "react": "They’re certainly on their best behaviour. But the mother is busy making sure everyone’s "
                      "served, and I suspect that for her, getting everyone round the table at once was the whole "
                      "point.",
             "theory": ["6.2", "6.3"]},
            {"text": "For me, the desk is the most honest picture. Most people I know eat lunch in front of a screen "
                     "every single day, so it’s the one readers would recognise.",
             "provokes": "Una propuesta sólida: recógela con sus palabras y añade una objeción.",
             "react": "You’re right that it’s familiar – painfully so. My worry is that it isn’t exactly appetising "
                      "for a food magazine. Readers might recognise themselves and then leave it on the shelf.",
             "theory": ["6.3"]},
            {"text": "The market is the only one that shows food being sold rather than eaten, though. All the "
                     "others are about the meal itself.",
             "provokes": "Una observación que cambia el criterio: valórala y llévala a la decisión.",
             "react": "That’s a good distinction, and the market certainly has the most colour. But I’m not sure the "
                      "special issue is about shopping – ‘The way we eat’ suggests it’s about how we eat, not where "
                      "we buy our food.",
             "theory": ["6.2", "6.4"]},
            {"text": "Honestly, nobody sits down to a proper family meal any more. Everyone’s either eating on the "
                     "go or staring at their phones.",
             "provokes": "Una generalización exagerada: matízala sin desautorizar a tu compañero.",
             "react": "That may be true on weekdays, but plenty of families still make an effort at weekends – and "
                      "the picnic’s a good example: there’s a phone lying right next to them, and nobody’s looking "
                      "at it.",
             "theory": ["6.4", "6.3"]},
            {"text": "We’re nearly out of time. Shall we go for the picnic? It’s cheerful, and it would really stand "
                     "out on the shelves.",
             "provokes": "Una propuesta de cierre: acepta, negocia o deja constancia del desacuerdo, pero decidid.",
             "react": "I could go along with that, although it’s a bit safe. I know I said the desk wasn’t very "
                      "appetising, but with a cover line like ‘Is this lunch?’ that becomes the point – and we could "
                      "keep the picnic for the inside pages.",
             "theory": ["6.6", "6.3"]},
        ],
    },
    "p3": {
        "theme": "success and ambition",
        "cards": [
            {"q": "What does it mean to be successful?",
             "ideas": ["money", "recognition", "satisfaction"],
             "plan": {
                 "Operación": "[[What does it mean]]: definir, distinguir y jerarquizar (§3.1).",
                 "Postura": "El éxito tiene una cara externa y otra interna; a la larga cuenta la interna.",
                 "Línea 1": "El dinero: la definición más común y en parte razonable, porque da seguridad y "
                            "opciones; pero [[enough]] nunca llega ([[money]]).",
                 "Línea 2": "El reconocimiento: importa más de lo que admitimos, pero deja el éxito en manos de otros "
                            "([[recognition]]).",
                 "Contrapunto": "La satisfacción: la definición más sólida, aunque puede servir de excusa "
                                "([[satisfaction]]).",
                 "Cierre": "Éxito es poder mirar atrás sin desear haber vivido la vida de otro (idea propia)."},
             "model": [
                 "It’s a question people answer very differently depending on who you ask. Ask a bank manager and "
                 "success means one thing; ask your grandmother and it means something else entirely. For me, "
                 "there’s an outward side to success and an inward side, and in the long run it’s the inward one "
                 "that matters.",
                 "The most common answer is probably money, and I don’t want to be snobbish about that. Having enough "
                 "money gives you security and, above all, choices – you can leave a job you hate, or help someone "
                 "you care about. The problem is that ‘enough’ keeps moving. People who measure success in money "
                 "rarely reach a point where they feel they’ve arrived.",
                 "Then there’s recognition, which I suspect matters to far more people than would ever admit it. "
                 "Being respected by your colleagues, or simply having your work noticed, is a powerful motivator. "
                 "But it puts your sense of success in other people’s hands, and other people can be fickle, or "
                 "simply not be paying attention.",
                 "Which brings me to satisfaction – doing something you believe is worth doing, and doing it well. "
                 "That seems to me the most solid definition, although I’d add a word of caution: it can become an "
                 "excuse. It’s easy to tell yourself you’re fulfilled when really you’ve just stopped trying.",
                 "So, if I had to put it in a sentence, I’d say success is being able to look back on your life "
                 "without wishing you’d lived someone else’s. That doesn’t rule out money or praise, but it does "
                 "put them in their place.",
             ],
             "comments": [
                 "Apertura que muestra que la pregunta no tiene una sola respuesta, con un contraste concreto (el "
                 "director del banco y la abuela), y adelanta la postura: [[an outward side … and an inward side]] "
                 "(§3.3).",
                 "Primera idea de la tarjeta ([[money]]): concede antes de criticar ([[I don’t want to be snobbish "
                 "about that]], §4.3) y remata con una observación propia: [[‘enough’ keeps moving]] (§3.4).",
                 "Segunda idea ([[recognition]]), con una valoración ([[which I suspect matters to far more people "
                 "than would ever admit it]]) y su límite: depende de otros (§3.4, §4.6).",
                 "Tercera idea como contrapunto ([[satisfaction]]): la mejor, pero con una advertencia que matiza "
                 "([[I’d add a word of caution]], §4.2) y un ejemplo de cómo puede engañar.",
                 "Cierre que responde a la pregunta con una definición propia ([[if I had to put it in a "
                 "sentence]]) y sitúa las otras ideas: [[put them in their place]] (§3.3, §4.6).",
             ],
             "follow_up": {"q": "Do you think people’s idea of success changes as they get older?",
                           "ideas": "Sí: de lo externo (sueldo, estatus) a lo interno (tiempo, relaciones, sentido), "
                                    "aunque no siempre por sabiduría, a veces por resignación. Enlaza con el long "
                                    "turn sin repetirlo: [[That ties in with what I was saying about ‘enough’ …]]"}},
            {"q": "Is ambition always a good thing?",
             "ideas": ["motivation", "pressure", "other people"],
             "plan": {
                 "Operación": "[[Is … always]]: graduar y buscar los casos en que no (§3.1).",
                 "Postura": "Casi siempre útil, pero dañina cuando se convierte en un fin o la pagan otros.",
                 "Línea 1": "La motivación: sin ambición no se termina nada difícil ([[motivation]]).",
                 "Línea 2": "La presión: cuando cada meta se sustituye por otra, la ambición es una cinta de correr "
                            "([[pressure]]).",
                 "Contrapunto": "Los demás: dañina si se persigue a su costa; generosa si es ambición por otros "
                                "([[other people]]).",
                 "Cierre": "Buena sirvienta, mala ama: hay que preguntarse para qué es (idea propia)."},
             "model": [
                 "Not always, no – although I’d say it’s a good thing far more often than people tend to think. "
                 "‘Ambitious’ has become almost an insult in some circles, and I think that’s a shame. The real "
                 "question is what the ambition is for, and who ends up paying for it.",
                 "Its most obvious benefit is motivation. Without some ambition, very little gets done: nobody trains "
                 "for a marathon or rewrites a novel for the fifth time out of mere contentment. Ambition gives you a "
                 "reason to put up with the boring, difficult middle part of any worthwhile project. And it isn’t only "
                 "about grand plans: small ambitions, like learning to play one piece properly, make ordinary life "
                 "more interesting.",
                 "The downside is pressure, especially when ambition stops being a means and becomes an end in "
                 "itself. I know people who have achieved almost everything they set out to do and still feel like "
                 "failures, because every goal they reach is immediately replaced by a bigger one. At that point "
                 "it’s less a drive than a treadmill.",
                 "And then there are other people. Ambition becomes genuinely harmful when it’s pursued at someone "
                 "else’s expense – a colleague whose work you take credit for, or a family that never sees you. On "
                 "the other hand, ambition can be generous, too: a teacher who is ambitious for her pupils is about "
                 "the best kind of teacher there is.",
                 "So, on balance, I’d say ambition makes a good servant but a poor master. It’s well worth having, as "
                 "long as you keep asking yourself what it’s for.",
             ],
             "comments": [
                 "Responde de inmediato y gradúa ([[Not always, no – although …]], §3.1); la última frase anuncia las "
                 "dos preguntas que ordenan el resto: para qué y a costa de quién (§3.3).",
                 "Primera idea ([[motivation]]) con dos ejemplos concretos, una formulación propia ([[the boring, "
                 "difficult middle part]]) y una ampliación a las ambiciones pequeñas (§3.4).",
                 "Segunda idea ([[pressure]]) en sentido contrario: [[The downside is]] (§4.2); un caso observado y "
                 "una imagen que lo resume: [[less a drive than a treadmill]] (§4.6).",
                 "Tercera idea ([[other people]]) como contrapunto doble: dañina o generosa, con [[On the other "
                 "hand]] (§4.3) y un ejemplo positivo que amplía la pregunta (§3.4).",
                 "Cierre con una fórmula propia ([[a good servant but a poor master]]) que recoge la pregunta inicial "
                 "sobre para qué sirve la ambición (§3.3, §4.5).",
             ],
             "follow_up": {"q": "Should parents encourage their children to be ambitious?",
                           "ideas": "Sí, en el sentido de animarlos a intentar cosas difíciles; no, si la ambición es "
                                    "la de los padres. Enlaza con el long turn: la pregunta es para qué y para quién "
                                    "es la ambición."}},
        ],
        "discussion": [
            {"q": "Why do some people care so much more about status than others?", "theory": ["6.7"],
             "ideas": "Inseguridad, educación y un entorno competitivo; también la cultura: en unos sitios el estatus "
                      "se exhibe y en otros se disimula.",
             "lang": "I suspect it often has less to do with vanity than with insecurity – status is a way of "
                     "reassuring yourself."},
            {"q": "Should schools reward effort as much as achievement?", "theory": ["6.3"],
             "ideas": "Sí en los primeros años, porque el esfuerzo se aprende; pero los resultados también importan, "
                      "y la vida adulta no premia solo el intento.",
             "lang": "Rewarding effort makes sense up to a point, but sooner or later the world only marks you on "
                     "results."},
            {"q": "Is it possible to be too competitive?", "theory": ["4.6"],
             "ideas": "Sí, cuando ganar importa más que hacer bien las cosas o se sacrifica a los demás; la competencia "
                      "sana empuja y la obsesiva aísla.",
             "lang": "Yes – competition is healthy as long as you’re competing against yourself rather than against "
                     "the people around you."},
            {"q": "Does social media make people feel less successful than they really are?",
             "theory": ["6.3", "4.3"],
             "ideas": "Sí, porque comparamos nuestra vida entera con los mejores momentos de los demás; pero también da "
                      "modelos, contactos y oportunidades.",
             "lang": "The trouble is that we’re comparing our everyday lives with other people’s highlights."},
            {"q": "Are some kinds of success valued too highly in society today?", "theory": ["3.5", "6.3"],
             "ideas": "La fama y el dinero rápido, frente a trabajos discretos y esenciales como los cuidados o la "
                      "enseñanza.",
             "lang": "We tend to celebrate the most visible kinds of success and overlook the people who keep "
                     "everything running."},
            {"q": "Would you rather be admired or liked?", "theory": ["6.7", "4.6"],
             "ideas": "Admirado por lo que haces, querido por cómo eres; a la larga pesa más lo segundo; también se "
                      "puede discutir que sea un dilema real.",
             "lang": "I’d rather be liked, if only because admiration tends to keep people at a slight distance."},
        ],
    },
    "lex": ["say yes to things", "within reason", "be flooded with light", "follow a thread", "the odd (big "
            "celebration)", "on one’s best behaviour", "painfully so", "go along with sth", "a cover line",
            "out of mere contentment", "put up with", "an end in itself", "less a drive than a treadmill",
            "at sb’s expense", "a good servant but a poor master", "fickle", "put sth in its place"],
}
