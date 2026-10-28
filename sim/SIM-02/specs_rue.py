# SIM-02 · Reading and Use of English · specs de las Parts 1-7
# Se monta con: python3 src/gen_SIM.py rue sim/SIM-02
# Formato de cada spec: cabecera del generador correspondiente (src/gen_UOE-P1..P4, src/gen_RDG-P5..P7).

# ---------- Part 1 · Multiple-choice cloze ----------
P1 = {
    "title": "Listening to the heart",
    "example": {"opts": ["pointed", "showed", "hinted", "led"], "key": "A"},
    "text": [
        "In 1816 the physician René Laennec, then working at a Paris hospital, was asked to examine a young woman "
        "whose symptoms {0} to heart disease. Until then, a doctor who wished to listen to a patient’s heart had had to make {1} with "
        "the naked ear, pressed directly against the chest. The conventions of the day, however, {2} out that "
        "method, and her plumpness meant that tapping on her chest would {3} little useful information.",
        "Laennec then recalled having seen children in the street send signals to one another along a {4} of "
        "timber, one scratching at one end while another listened at the other. He rolled a few sheets of paper "
        "into a tight cylinder, placed one end on the woman’s chest and was astonished to hear her heartbeat more "
        "clearly than ever before.",
        "His later instruments {5} of little more than a hollow wooden tube, and the name he coined for them, "
        "‘stethoscope’, is {6} from the Greek words for ‘chest’ and ‘to examine’. Within a generation the device "
        "had become {7} and parcel of medical practice. Laennec himself, however, did not live long enough to {8} "
        "the full rewards of his invention: in 1826, aged only forty-five, he died of tuberculosis, a disease he "
        "had done more than anyone to help doctors identify.",
    ],
    "items": [
        {"n": 1, "opts": ["good", "do", "way", "use"], "key": "B", "theory": ["4.2"],
         "why": "[[make do with sth]]: arreglárselas con algo insuficiente a falta de algo mejor. Antes del "
                "estetoscopio, el médico solo tenía su oído.",
         "wrong": {"A": "[[make good]] es cumplir una promesa ([[make good on]]) o reparar un daño; *[[make good "
                        "with the naked ear]] no significa nada.",
                   "C": "[[make way]] es dejar paso ([[make way for sth]]); con [[with]] no forma expresión.",
                   "D": "[[make use]] va con [[of]] ([[make use of the naked ear]]), no con [[with]]."}},
        {"n": 2, "opts": ["ruled", "counted", "struck", "shut"], "key": "A", "theory": ["7.1"],
         "why": "[[rule sth out]]: descartar algo, hacerlo imposible. Las convenciones de la época impedían que "
                "un médico apoyara la cabeza en el pecho de una mujer joven.",
         "wrong": {"B": "[[count sb out]] es no contar con alguien ([[count me out]]); se dice de personas que "
                        "quedan fuera de un plan, no de un método que se descarta.",
                   "C": "[[strike sth out]] es tachar algo escrito; [[struck out]] no significa «hacer imposible».",
                   "D": "[[shut sth out]] es impedir que entre algo (la luz, el ruido) o dejar fuera a alguien; "
                        "no se dice de un procedimiento."}},
        {"n": 3, "opts": ["earn", "breed", "gain", "yield"], "key": "D", "theory": ["3.1", "5.1"],
         "why": "[[yield]]: producir un resultado, datos o información ([[the search yielded little]]). El sujeto "
                "es el procedimiento ([[tapping on her chest]]), que no iba a dar información útil.",
         "wrong": {"A": "[[earn]] es ganar algo con esfuerzo o mérito (dinero, respeto); no se «gana» información "
                        "así.",
                   "B": "[[breed]] es engendrar, casi siempre algo negativo ([[breed resentment]]); no va con "
                        "[[information]].",
                   "C": "Con [[gain]] el sujeto es quien obtiene algo ([[doctors gain information]]); un "
                        "procedimiento no «gana» información."}},
        {"n": 4, "opts": ["stretch", "span", "length", "reach"], "key": "C", "theory": ["3.4", "5.1"],
         "why": "[[a length of timber / rope / pipe]]: un trozo largo de un material. Los niños se transmitían "
                "señales a lo largo de un madero.",
         "wrong": {"A": "[[a stretch of]] va con extensiones de terreno, agua o tiempo ([[a stretch of coast]]), "
                        "no con un objeto.",
                   "B": "[[span]] es la luz de un puente o un lapso ([[a span of time]]); [[a span of timber]] no "
                        "se dice.",
                   "D": "[[reach]] es el alcance o un tramo de río ([[the upper reaches]]); no un trozo de "
                        "material."}},
        {"n": 5, "opts": ["consisted", "comprised", "composed", "contained"], "key": "A", "theory": ["6.1", "6.3"],
         "why": "[[consist of]]: constar de. Es el único de los cuatro que se construye en activa con [[of]]: "
                "[[his instruments consisted of a tube]].",
         "wrong": {"B": "[[comprise]] es transitivo, sin preposición ([[comprised a tube]]); [[comprised of]] solo "
                        "aparece en pasiva ([[were comprised of]]), y aquí falta el auxiliar.",
                   "C": "[[composed of]] exige pasiva ([[were composed of]]); *[[his instruments composed of]] "
                        "no es gramatical.",
                   "D": "[[contain]] es transitivo ([[contained a tube]]); *[[contained of]] no existe."}},
        {"n": 6, "opts": ["stemmed", "originated", "derived", "arisen"], "key": "C", "theory": ["6.3"],
         "why": "Delante del hueco hay [[is]]: hace falta un participio que admita pasiva. [[be derived from]]: "
                "proceder de, tratándose de palabras ([[the name is derived from Greek]]).",
         "wrong": {"A": "[[stem from]] es intransitivo: [[the name stems from]], nunca *[[is stemmed from]].",
                   "B": "[[originate]] también es intransitivo: [[it originated in / from]], no *[[is originated "
                        "from]].",
                   "D": "[[arise]] es intransitivo y su participio no va con [[is]] (*[[is arisen]]); además se "
                        "dice de problemas o situaciones, no de nombres."}},
        {"n": 7, "opts": ["piece", "part", "bit", "share"], "key": "B", "theory": ["4.1"],
         "why": "[[part and parcel of sth]]: parte esencial e inseparable de algo. Es un binomio fijo: ninguna de "
                "sus dos palabras se cambia.",
         "wrong": {"A": "*[[piece and parcel]] no existe; [[piece]] forma otros pares ([[all of a piece]]).",
                   "C": "*[[bit and parcel]] tampoco existe ([[bit]]).",
                   "D": "[[share]] no forma pareja con [[parcel]] (*[[share and parcel]])."}},
        {"n": 8, "opts": ["harvest", "gather", "glean", "reap"], "key": "D", "theory": ["3.1"],
         "why": "[[reap the rewards / benefits]]: recoger el fruto de algo. Laennec murió joven, antes de que su "
                "invento se impusiera del todo.",
         "wrong": {"A": "[[harvest]] es cosechar en sentido literal (o reunir datos); no forma collocation con "
                        "[[rewards]].",
                   "B": "[[gather]] es reunir o juntar ([[gather information]]); *[[gather the rewards]] no se "
                        "dice.",
                   "C": "[[glean]] es ir sacando información poco a poco ([[glean details]]); no va con "
                        "[[rewards]]."}},
    ],
}

# ---------- Part 2 · Open cloze ----------
P2 = {
    "title": "The puzzle of the yawn",
    "example": "EVEN",
    "text": [
        "We begin yawning before we are {0} born – foetuses have been observed doing it in the womb – and yet it "
        "remains {9} of the least understood things the human body does. We carry {10} yawning several times a "
        "day for the rest of our lives, but scientists still cannot agree on {11} it is actually for.",
        "For many years the most popular explanation was that a yawn draws extra oxygen into the blood. Plausible "
        "{12} it sounds, the theory has not survived testing: volunteers given air rich in oxygen to breathe "
        "yawned no less often than those who were not. A more recent suggestion is that yawning helps to cool the "
        "brain, {13} would explain why people seem to yawn less on very hot days.",
        "Stranger still is the fact that yawning is contagious. Seeing, hearing or even reading about someone else "
        "yawning is often enough to make us do the {14}. Some researchers have linked this to empathy, pointing "
        "out that we are more susceptible to the yawns of family and friends than to {15} of strangers. Others "
        "remain unconvinced. {16} the explanation turns out to be, you have probably yawned at least once while "
        "reading this.",
    ],
    "items": [
        {"n": 9, "key": ["ONE"], "type": "[[one of]] + superlativo", "theory": ["3", "4"],
         "why": "Detrás del hueco va [[of the least understood things]]: [[one of the …]], «una de las cosas "
                "menos comprendidas». El sujeto es singular ([[it remains]]), así que solo cabe [[one]].",
         "wrong": "[[!some]] o [[!any]] (no concuerdan con el sujeto singular [[it]]); [[!among]] (*[[remains "
                  "among of]])."},
        {"n": 10, "key": ["ON"], "type": "Partícula de phrasal verb", "theory": ["6.2"],
         "why": "[[carry on doing sth]]: seguir haciendo algo. El gerundio [[yawning]] detrás confirma la "
                "partícula.",
         "wrong": "[[!out]] ([[carry out]] es llevar a cabo y va con un sustantivo: [[carry out a test]]); "
                  "[[!over]] ([[carry over]] es trasladar algo a otro periodo)."},
        {"n": 11, "key": ["WHAT"], "type": "Relativo nominal", "theory": ["8"],
         "why": "[[agree on]] necesita un objeto, y el hueco es a la vez ese objeto y el complemento de [[for]] "
                "al final: [[what it is for]], «para qué sirve».",
         "wrong": "[[!why]] o [[!how]] (dejarían [[for]] sin complemento: *[[why it is actually for]]); "
                  "[[!which]] (necesita antecedente)."},
        {"n": 12, "key": ["AS", "THOUGH"], "type": "Concesiva con adjetivo antepuesto", "theory": ["9.2"],
         "why": "Adjetivo + [[as / though]] + sujeto + verbo: [[Plausible as it sounds]] = «por muy plausible que "
                "parezca». Las dos conjunciones valen en esta estructura.",
         "wrong": "[[!although]] (no admite el adjetivo delante: *[[Plausible although it sounds]]); [[!so]] o "
                  "[[!if]] (no forman la concesiva)."},
        {"n": 13, "key": ["WHICH"], "type": "Relativo de oración", "theory": ["8"],
         "why": "Tras la coma, el relativo remite a toda la oración anterior (que el bostezo enfríe el cerebro) y "
                "es sujeto de [[would explain]]: solo [[which]].",
         "wrong": "[[!that]] (no va tras coma en una explicativa); [[!this]] o [[!it]] (convertirían la frase en "
                  "dos oraciones unidas solo por una coma); [[!what]] (no tiene valor de relativo de oración)."},
        {"n": 14, "key": ["SAME"], "type": "Sustitución: [[do the same]]", "theory": ["4", "6.3"],
         "why": "[[do the same]]: hacer lo mismo, es decir, bostezar también. El artículo [[the]] delante solo "
                "deja [[same]].",
         "wrong": "[[!opposite]] (dice lo contrario de [[contagious]]); [[!likewise]] (es adverbio y no va tras "
                  "[[the]]); [[!thing]] (*[[do the thing]] no significa «hacer lo mismo»)."},
        {"n": 15, "key": ["THOSE"], "type": "Sustitución de un sustantivo plural", "theory": ["4"],
         "why": "El hueco sustituye a [[the yawns]], en plural, delante de [[of]]: [[those of strangers]] = los "
                "bostezos de los desconocidos.",
         "wrong": "[[!that]] (singular: no concuerda con [[yawns]]); [[!ones]] (*[[to ones of strangers]] exige "
                  "[[the ones]], dos palabras); [[!them]] (no admite [[of]] detrás)."},
        {"n": 16, "key": ["WHATEVER"], "type": "Relativo concesivo", "theory": ["8", "9.2"],
         "why": "[[turns out to be]] necesita un complemento, y el hueco lo aporta: [[Whatever the explanation "
                "turns out to be]] = «sea cual sea la explicación». La oración principal va tras la coma.",
         "wrong": "[[!however]] ([[be]] se quedaría sin complemento); [[!whichever]] (exige un sustantivo detrás: "
                  "[[whichever explanation]]); [[!whether]] (pide [[or not]] y otra estructura)."},
    ],
}

# ---------- Part 3 · Word formation ----------
P3 = {
    "changes": "hasta tres cambios por hueco",
    "title": "Thinking inside the box",
    "example": "REVOLUTION", "example_stem": "REVOLVE",
    "text": [
        "In April 1956 a converted oil tanker, the Ideal X, sailed from Newark to Houston with fifty-eight metal "
        "boxes lashed to its deck. Few people paid much attention, yet the voyage marked the beginning of a "
        "{0|REVOLVE} in the way goods are moved around the world.",
        "Until then, cargo had been {17|LABOUR} loaded by hand, item by item, in a process that could keep a ship "
        "in port for a week or more. Theft was common, and the sheer {18|EFFICIENT} of the system added enormously "
        "to the price of goods. Malcolm McLean, the American haulage magnate behind the Ideal X, had spent years "
        "watching his lorries queue at the docks, and his solution was {19|DECEPTIVE} simple: instead of "
        "unloading the goods, why not lift the whole box from lorry to ship?",
        "The savings were enormous. By McLean’s own reckoning, loading the Ideal X cost less than a thirtieth of "
        "what it would have cost by conventional means. Once container sizes had been standardised in the late "
        "1960s, the same box could travel by road, rail and sea without being opened, and a period of "
        "{20|PRECEDENT} growth in world trade followed, bringing with it a new {21|DEPEND} between distant "
        "economies.",
        "Not everyone gained. As cranes did in hours what gangs of dockers had once done in days, thousands of "
        "men lost their livelihoods. Ports had to {22|MODERN} or decline, and old waterfronts in cities such as "
        "London and New York fell into {23|USE}. The humble container seldom attracts the {24|ADMIRE} lavished on "
        "the jet engine or the microchip, yet it has done as much as either to shape the modern world.",
    ],
    "items": [
        {"n": 17, "stem": "LABOUR", "key": ["LABORIOUSLY"], "type": "Adverbio · -ious + -ly",
         "theory": ["4.5", "8.5"],
         "why": "[[had been]] + hueco + [[loaded]]: un adverbio que modifica al participio. La carga se subía a "
                "mano, pieza a pieza, con mucho esfuerzo.",
         "changes": "[[labour]] → [[laborious]] ([[-ious]]; la [[u]] de la raíz se pierde) → [[laboriously]] "
                    "([[-ly]]). Dos cambios.",
         "wrong": "*[[!LABOURIOUSLY]] (conserva la [[u]] que se pierde); [[!LABORIOUS]] (adjetivo: no puede "
                  "modificar a [[loaded]])."},
        {"n": 18, "stem": "EFFICIENT", "key": ["INEFFICIENCY"], "type": "Sustantivo · prefijo in- y -cy",
         "theory": ["6.1", "4.1"],
         "why": "[[the sheer]] + hueco + [[of the system]]: sustantivo. Lo que encarecía las mercancías era la "
                "ineficacia del sistema, no su eficacia.",
         "changes": "[[efficient]] → [[efficiency]] ([[-cy]]) → [[inefficiency]] ([[in-]]). Dos cambios.",
         "wrong": "[[!EFFICIENCY]] (dice lo contrario: la eficacia no encarece nada); [[!INEFFICIENT]] "
                  "(adjetivo); [[!INEFFICIENCIES]] (el plural no casa con [[sheer]], que intensifica sustantivos "
                  "incontables o abstractos: [[the sheer size]], [[the sheer inefficiency]]); *[[!UNEFFICIENCY]] "
                  "(el prefijo es [[in-]])."},
        {"n": 19, "stem": "DECEPTIVE", "key": ["DECEPTIVELY"], "type": "Adverbio de grado · -ly",
         "theory": ["4.5"],
         "why": "[[was]] + hueco + [[simple]]: un adverbio que modifica al adjetivo. [[deceptively simple]]: "
                "sencillo en apariencia, aunque esconda más de lo que parece. Es una collocation muy frecuente.",
         "changes": "[[deceptive]] → [[deceptively]] ([[-ly]]). Un cambio.",
         "wrong": "[[!DECEPTIVE]] (adjetivo: *[[deceptive simple]]); *[[!DECEPTIONALLY]] (no existe)."},
        {"n": 20, "stem": "PRECEDENT", "key": ["UNPRECEDENTED"], "type": "Adjetivo · un- y -ed",
         "theory": ["6.1", "4.2"],
         "why": "[[a period of]] + hueco + [[growth]]: adjetivo. Un crecimiento sin precedentes del comercio "
                "mundial.",
         "changes": "[[precedent]] → [[precedented]] ([[-ed]]) → [[unprecedented]] ([[un-]]). Dos cambios.",
         "wrong": "[[!PRECEDENTED]] (casi no se usa sin el prefijo y dice lo contrario); *[[!INPRECEDENTED]] (el "
                  "prefijo es [[un-]]); [[!PRECEDING]] («anterior», de [[precede]], no de [[precedent]])."},
        {"n": 21, "stem": "DEPEND", "key": ["INTERDEPENDENCE", "INTERDEPENDENCY"],
         "type": "Sustantivo · prefijo inter- y -ence", "theory": ["6.4", "4.1", "8.4"],
         "why": "[[a new]] + hueco + [[between distant economies]]: sustantivo singular. [[between]] indica que "
                "la dependencia es mutua: hace falta el prefijo [[inter-]]. [[Interdependency]] es una variante "
                "registrada, menos frecuente.",
         "changes": "[[depend]] → [[dependence]] ([[-ence]]) → [[interdependence]] ([[inter-]]). Dos cambios.",
         "wrong": "[[!DEPENDENCE]] o [[!DEPENDENCY]] (van con [[on]], en una sola dirección; [[between]] pide "
                  "reciprocidad); "
                  "[[!INDEPENDENCE]] (dice lo contrario); *[[!INTERDEPENDANCE]] (la terminación es "
                  "[[-ence]])."},
        {"n": 22, "stem": "MODERN", "key": ["MODERNISE", "MODERNIZE"], "type": "Verbo · -ise",
         "theory": ["4.3"],
         "why": "[[had to]] + hueco + [[or decline]]: un verbo en infinitivo, coordinado con [[decline]]. Los "
                "puertos tenían que modernizarse o hundirse. La grafía con [[-ize]] también es correcta.",
         "changes": "[[modern]] → [[modernise]] ([[-ise]]). Un cambio.",
         "wrong": "[[!MODERNISED]] o [[!MODERNISING]] (tras [[had to]] va el infinitivo); "
                  "[[!MODERNITY]] (sustantivo)."},
        {"n": 23, "stem": "USE", "key": ["DISUSE"], "type": "Sustantivo · prefijo dis-",
         "theory": ["6.2", "6.4"],
         "why": "[[fall into disuse]]: dejar de usarse, quedar abandonado. Expresión fija con el sustantivo "
                "precedido de [[dis-]].",
         "changes": "[[use]] → [[disuse]] ([[dis-]]). Un cambio.",
         "wrong": "[[!MISUSE]] (uso indebido: no forma la expresión); [[!USELESSNESS]] (*[[fall into "
                  "uselessness]]); [[!UNUSE]] (no existe)."},
        {"n": 24, "stem": "ADMIRE", "key": ["ADMIRATION"], "type": "Sustantivo · -ation",
         "theory": ["4.1", "8.2"],
         "why": "[[attracts the]] + hueco + [[lavished on]]: sustantivo. La admiración que se dedica al motor a "
                "reacción o al microchip.",
         "changes": "[[admire]] → [[admiration]] ([[-ation]]; la [[e]] final se pierde). Un cambio.",
         "wrong": "[[!ADMIRERS]] (personas: no se «prodigan» sobre un invento); *[[!ADMIREATION]] (conserva la "
                  "[[e]] que se pierde)."},
    ],
}

# ---------- Part 4 · Key word transformations ----------
P4 = {
    "example": {"s1": "The concert was cancelled because the singer was ill.", "keyword": "CALLED",
                "s2": "The concert {G} because the singer was ill.", "answer": "WAS CALLED OFF"},
    "items": [
        {"n": 25, "s1": "People say that old Mr Hollis grew the largest pumpkin ever seen in the county.",
         "keyword": "REPUTED", "s2": "Old Mr Hollis {G} the largest pumpkin ever seen in the county.",
         "key": ["IS REPUTED TO HAVE GROWN", "IS REPUTED TO BE THE {MAN|ONE|PERSON} WHO GREW"],
         "halves": ("is reputed", "to have grown"),
         "theory": ["3.3"],
         "why": "[[People say that …]] → pasiva impersonal con el sujeto personal: [[he is reputed to …]]. Lo "
                "que se dice está en presente ([[is]]); lo que hizo, en pasado, así que va el infinitivo "
                "perfecto: [[to have grown]]. También conserva el sentido [[is reputed to be the man who grew]] "
                "(ocho palabras).",
         "wrong": [("IS REPUTED TO GROW", "el infinitivo simple hablaría de algo habitual, no de un hecho "
                                         "pasado"),
                   ("WAS REPUTED TO HAVE GROWN", "[[People say]] está en presente: lo dicen ahora"),
                   ("IS REPUTED FOR HAVING GROWN", "[[reputed]] va con infinitivo; [[be renowned for]] sí "
                                                   "lleva [[for]], pero no es la palabra clave")]},
        {"n": 26, "s1": "Nobody realised that the portrait was a fake until an expert examined it.",
         "keyword": "LIGHT", "s2": "Only when an expert examined the portrait {G} that it was a fake.",
         "key": ["DID IT {_|FINALLY} COME TO LIGHT", "WAS IT {_|FINALLY} BROUGHT TO LIGHT"],
         "halves": ("did it", "come to light"),
         "theory": ["3.1", "5.2"],
         "why": "[[come to light]]: salir a la luz, descubrirse. Tras [[Only when …]] la oración principal lleva "
                "inversión: [[did it come to light that …]]. La pasiva de [[bring to light]] también conserva el "
                "sentido ([[was it brought to light]]), aunque es menos natural. [[Finally]] solo explicita lo que "
                "ya dice [[until]] y se acepta.",
         "wrong": [("IT CAME TO LIGHT", "falta la inversión que exige [[Only when]] al principio"),
                   ("DID IT BRING TO LIGHT", "[[bring to light]] es transitivo: con el [[it]] impersonal hace "
                                             "falta [[come to light]] o la pasiva"),
                   ("DID IT COME INTO LIGHT", "la expresión fija es [[come to light]]")]},
        {"n": 27, "s1": "If she hadn’t injured her ankle, Anna would probably have won the race.",
         "keyword": "STOOD", "s2": "Anna would {G} of winning the race if she hadn’t injured her ankle.",
         "key": ["HAVE STOOD {A GOOD|A VERY GOOD|A REAL|A STRONG|A DECENT|A FAIR|AN EXCELLENT|EVERY} CHANCE"],
         "halves": ("have stood", "a good chance"),
         "theory": ["5.1", "3.2"],
         "why": "[[would probably have won]] → [[would have stood a good chance of winning]]: [[stand a chance "
                "(of doing sth)]], tener posibilidades. Tras [[would]] va el infinitivo perfecto ([[have stood]]). "
                "Valen los adjetivos que expresan una probabilidad clara: [[good]], [[very good]], [[real]], "
                "[[strong]], [[decent]], [[fair]], [[excellent]], y también [[every chance]] («todas las "
                "posibilidades»).",
         "wrong": [("HAVE HAD A GOOD CHANCE", "no usa la palabra clave"),
                   ("HAVE STOOD GOOD CHANCES", "[[stand a chance]] va en singular y con [[a]]"),
                   ("HAVE STOOD A CHANCE", "sin adjetivo, [[stand a chance]] es «tener alguna posibilidad»: se "
                                           "pierde el [[probably]] de la frase 1"),
                   ("STOOD A GOOD CHANCE", "tras [[would]] hace falta [[have]] + participio")]},
        {"n": 28, "s1": "The ferry left late because of the fog, not because of the strike.",
         "keyword": "BLAME", "s2": "It was the fog, not the strike, {G} the ferry’s late departure.",
         "key": ["{THAT|WHICH} WAS {_|REALLY} TO BLAME FOR", "{THAT|WHICH} WAS THE ONE TO BLAME FOR",
                 "{THAT|WHICH} DESERVED THE BLAME FOR"],
         "halves": ("that was", "to blame for"),
         "theory": ["3.4", "5.2"],
         "why": "Cleft sentence: [[It was X that …]] destaca la causa. [[be to blame for sth]]: ser el culpable, "
                "la causa de algo malo; la preposición es [[for]]. Con un sujeto no humano también vale "
                "[[which]], y conservan el sentido [[was the one to blame for]] y [[deserved the blame for]].",
         "wrong": [("THAT WAS BLAMED FOR", "pasiva: diría que alguien culpó a la niebla, no que fuera la causa"),
                   ("THAT WAS TO BLAME OF", "la preposición es [[for]]"),
                   ("WAS TO BLAME FOR", "la cleft necesita [[that]] o [[which]] delante del verbo")]},
        {"n": 29, "s1": "The restaurant’s food was nothing like the sophisticated cooking its website had "
                        "promised.",
         "keyword": "CRY", "s2": "The restaurant’s food was {G} the sophisticated cooking its website had promised.",
         "key": ["A {_|VERY} FAR CRY FROM"],
         "halves": ("a far cry", "from"),
         "theory": ["5.2"],
         "why": "[[be a far cry from sth]]: no parecerse en nada a algo, quedar muy lejos de ello. Equivale a "
                "[[nothing like]]. Expresión fija: artículo, adjetivo y preposición no cambian; se admite el "
                "intensificador ([[a very far cry from]]).",
         "wrong": [("FAR CRY FROM", "falta el artículo [[a]]"),
                   ("A FAR CRY TO", "la preposición es [[from]]"),
                   ("A LONG CRY FROM", "la expresión es [[a far cry]]; [[a long way from]] sería otra")]},
        {"n": 30, "s1": "It took the former champion months to accept that she had lost to an amateur.",
         "keyword": "TERMS", "s2": "It was months before the former champion {G} losing to an amateur.",
         "key": ["{_|FINALLY|FULLY} CAME TO TERMS WITH", "HAD {_|FINALLY|FULLY} COME TO TERMS WITH",
                 "{COULD|WAS ABLE TO|MANAGED TO} COME TO TERMS WITH"],
         "halves": ("came to terms", "with"),
         "theory": ["5.2", "5.3"],
         "why": "[[come to terms with sth]]: asumir algo doloroso, aceptarlo. Tras [[It was months before]] va "
                "el pasado ([[came]]), y también caben [[had come]], [[could / was able to / managed to come]] y "
                "los adverbios [[finally]] o [[fully]], que no cambian el sentido. El gerundio [[losing]] es el "
                "complemento de [[with]].",
         "wrong": [("CAME TO TERMS OF", "la preposición es [[with]]"),
                   ("CAME IN TERMS WITH", "la expresión es [[come to terms]]"),
                   ("ACCEPTED THE TERMS OF", "cambia el sentido: aceptar las condiciones de algo")]},
    ],
}

# ---------- Part 5 · Multiple choice ----------
P5 = {
    "intro": "a newspaper column about lawns",
    "title": "Letting it grow",
    "standfirst": "After forty years of mowing, our columnist has all but put the mower away. He is still not "
                  "entirely sure how he feels about it.",
    "text": [
        "My father mowed the lawn every Saturday morning from April to October, and he did it in stripes. The "
        "stripes mattered. They ran parallel to the back of the house, each exactly the width of the mower, and "
        "any wavering from the line was treated as a minor moral failing, somewhere between forgetting a birthday "
        "and leaving the cap off the toothpaste. I inherited both the mower and the routine, and for most of my "
        "adult life I assumed, without ever quite putting it into words, that a well-kept lawn was simply "
        "something a responsible person owed the rest of the street.",

        "It is worth remembering how recent, and how odd, that assumption is. For most of history, an expanse of "
        "closely cropped grass that produced neither food nor fodder was a luxury only the very rich could "
        "contemplate. The lawns of eighteenth-century country houses were kept short by teams of men with "
        "scythes, sometimes helped by sheep, and landscape gardeners such as Capability Brown made fortunes "
        "sweeping away formal flowerbeds so that the grass could run uninterrupted to the door. The real "
        "function of all that grass was to announce that the owner had land to spare and labour to waste. A "
        "lawn, in other words, was not so much a garden as a boast.",

        "What turned that boast into a suburban duty was a piece of engineering. In 1830 Edwin Budding, an "
        "engineer from Gloucestershire, having watched a machine in a cloth mill trim the surface of fabric with "
        "a rotating blade, patented a device that did the same job for grass. He is said to have tested it at "
        "night, to spare himself the ridicule of his neighbours. Within a few decades, the lawnmower had put the aristocrat’s indulgence within reach of the bank clerk, and what had once been a "
        "mark of privilege became, with remarkable speed, a mark of respectability. It is from that moment, I "
        "suspect, that my father’s stripes ultimately descend.",

        "My own conversion owes less to history than to arithmetic. A few years ago a conservation charity asked "
        "thousands of householders to leave their lawns unmown for a month and then count the flowers that came "
        "up. Lawns cut only every four weeks or so, it turned out, produced far more flowers, and far more "
        "nectar, than those mown every week, while patches left to grow longer supported a wider range of plants "
        "still. I read the report twice, partly out of interest and partly in the hope of finding a flaw in it. I "
        "did not find one. I had always regarded the lawn as a small contribution to the order of things. It had "
        "never occurred to me that, from the point of view of a bee, it might have more in common with a car "
        "park.",

        "So, two springs ago, I stopped. I would like to report that the result was a meadow. It was not, at "
        "least not at first. It was a shaggy, faintly shameful rectangle that drew pointed remarks from the "
        "postman and a note from next door asking, with elaborate politeness, whether I had been unwell. The first "
        "summer brought dandelions in quantities I would once have found alarming, and a good deal of something "
        "that the internet assured me was harmless and my mother assured me was not. Nor, I "
        "confess, am I wholly at ease with some of my new allies in what has become known as the ‘no mow’ "
        "movement. There is a strand of it that seems less interested in insects than in being seen to care "
        "about them, and a lawn left long chiefly so that its owner can mention it at dinner parties is, it seems "
        "to me, just my father’s stripes in a different costume.",

        "And yet something has shifted. By the second summer the grass was threaded with clover and self-heal "
        "and a small blue flower I had to look up, and on warm afternoons the whole thing hummed. I have kept a "
        "mown path through the middle, partly for access and partly, I admit, to reassure the street that the "
        "neglect is deliberate. It seems to have worked. The neighbours have stopped enquiring after my health, "
        "and last month one of them asked instead which part of her own lawn I thought she might leave alone.",

        "I still own the mower, and I still use it, though far less often and never in stripes. My father would "
        "have been appalled, I suspect, and then curious, and then, had the bees been out, quietly persuaded. "
        "That, at any rate, is what I tell myself on Saturday mornings, when the old habit stirs and I make a cup "
        "of tea instead.",
    ],
    "lex": ["a minor moral failing", "closely cropped grass", "neither food nor fodder", "land to spare",
            "not so much X as Y", "put sth within reach of sb", "a mark of respectability", "owe less to X than to Y",
            "shaggy", "a pointed remark", "with elaborate politeness", "a strand of (a movement)",
            "in a different costume", "be threaded with", "enquire after sb’s health", "the old habit stirs"],
    "items": [
        {"n": 31, "type": "Opinión y actitud", "para": [1],
         "stem": "How does the writer present his father’s approach to mowing the lawn?",
         "options": ["as a way of passing on a sense of duty to his son",
                     "as a source of anxiety about what the neighbours might think",
                     "as a ritual he valued more for the routine than for the result",
                     "as investing a trivial task with a certain moral seriousness"],
         "key": "D",
         "own": "Con ironía: el padre convertía el césped en una cuestión casi moral; torcer una raya era una "
                "pequeña falta, como olvidar un cumpleaños.",
         "why": "Lo dice la comparación del primer párrafo: {{any wavering from the line was treated as a minor "
                "moral failing, somewhere between forgetting a birthday and leaving the cap off the toothpaste}}. "
                "[[Minor moral failing]] junta lo pequeño y lo moral; los ejemplos domésticos dejan ver la ironía "
                "del autor (§4.3). [[Trivial task]] y [[moral seriousness]] parafrasean las dos mitades.",
         "theory": ["4.3", "6.1"],
         "distractors": {
             "A": {"kinds": ["7.7"],
                   "why": "El autor heredó la costumbre ({{I inherited both the mower and the routine}}), pero no "
                          "dice que el padre quisiera enseñarle nada: lo que heredó lo asumió él solo."},
             "B": {"kinds": ["7.4", "7.1"],
                   "why": "Toma {{the rest of the street}}, pero esa idea es del autor adulto ({{I assumed, "
                          "without ever quite putting it into words}}), no una inquietud del padre."},
             "C": {"kinds": ["7.7"],
                   "why": "Que le gustara más la rutina que el resultado no aparece en el texto; al contrario, "
                          "el resultado importaba: {{The stripes mattered}}."},
         }},
        {"n": 32, "type": "Detalle", "para": [2],
         "stem": "What point does the writer make about the lawns of eighteenth-century country houses?",
         "options": ["They demanded more skill to maintain than modern lawns do.",
                     "They were laid out to show off the architecture of the house.",
                     "Their very uselessness was the point.",
                     "They were admired chiefly by those who could not afford them."],
         "key": "C",
         "own": "Que servían para presumir: un terreno que no daba nada demostraba que el dueño podía "
                "permitirse desperdiciar tierra y trabajo.",
         "why": "El césped era un lujo precisamente porque no producía nada: {{closely cropped grass that "
                "produced neither food nor fodder was a luxury only the very rich could contemplate}}. Su "
                "función, dice el autor, era {{to announce that the owner had land to spare and labour to "
                "waste}}. [[Uselessness]] resume [[neither food nor fodder]], y [[was the point]], [[The real "
                "function]] (§6.2).",
         "theory": ["6.2", "3.2"],
         "distractors": {
             "A": {"kinds": ["7.1", "7.7"],
                   "why": "Se apoya en {{teams of men with scythes}}, pero el texto no compara la destreza que "
                          "exigían con la de hoy: los segadores aparecen como prueba del trabajo derrochado."},
             "B": {"kinds": ["7.2"],
                   "why": "Es cierto que el césped llegaba hasta la casa ({{so that the grass could run "
                          "uninterrupted to the door}}), pero el autor no dice que fuera para lucir el "
                          "edificio: su función era otra, {{The real function of all that grass}}."},
             "D": {"kinds": ["7.7"],
                   "why": "El texto dice quién podía permitírselos ({{only the very rich}}), no quién los "
                          "admiraba."},
         }},
        {"n": 33, "type": "Detalle", "para": [3],
         "stem": "According to the third paragraph, the invention of the lawnmower led to",
         "options": ["a symbol of wealth becoming something expected of ordinary households.",
                     "a sharp decline in the number of labourers employed to look after large estates.",
                     "lawns being valued for their appearance rather than for what they cost to keep.",
                     "a fashion for mechanical devices among the newly prosperous middle classes."],
         "key": "A",
         "own": "A que lo que era un lujo de aristócratas pasara a ser una obligación de cualquier familia "
                "respetable de las afueras.",
         "why": "El párrafo describe el paso del lujo al deber: {{What turned that boast into a suburban duty was "
                "a piece of engineering}}, y {{what had once been a mark of privilege became, with remarkable "
                "speed, a mark of respectability}}. [[Symbol of wealth]] recoge [[mark of privilege]]; "
                "[[something expected of ordinary households]], [[suburban duty]] y [[respectability]].",
         "theory": ["6.1", "6.2"],
         "distractors": {
             "B": {"kinds": ["7.7"],
                   "why": "Suena lógico (la máquina sustituye a los {{teams of men with scythes}} del párrafo "
                          "anterior), pero el texto no habla de los jornaleros de las fincas después de 1830."},
             "C": {"kinds": ["7.5"],
                   "why": "El cambio que cuenta el texto es de quién tiene césped y qué significa ({{put the "
                          "aristocrat’s indulgence within reach of the bank clerk}}), no un paso del coste a la "
                          "belleza."},
             "D": {"kinds": ["7.1"],
                   "why": "Recoge {{a piece of engineering}} y {{patented a device}}, pero no hay ninguna moda de "
                          "aparatos: lo que se extiende es el césped."},
         }},
        {"n": 34, "type": "Opinión y actitud", "para": [4],
         "stem": "How did the writer react to the findings of the charity’s survey?",
         "options": ["He welcomed them as a scientific excuse for doing less work in the garden.",
                     "He was made to see his lawn from another creature’s perspective.",
                     "He doubted that householders could have counted the flowers accurately.",
                     "He was surprised by how many people had been willing to take part."],
         "key": "B",
         "own": "Le hicieron ver su césped desde otro punto de vista: para él era orden; para una abeja, casi "
                "un aparcamiento.",
         "why": "La reacción está en las dos últimas frases: {{I had always regarded the lawn as a small "
                "contribution to the order of things}}, pero {{It had never occurred to me that, from the point "
                "of view of a bee, it might have more in common with a car park}}. [[Another creature’s "
                "perspective]] parafrasea [[from the point of view of a bee]]; lo que ve desde ahí contrasta con "
                "su idea del orden.",
         "theory": ["4.2", "6.2"],
         "distractors": {
             "A": {"kinds": ["7.7"],
                   "why": "El autor no habla de ahorrarse trabajo; lo que le hace cambiar es el dato: {{produced "
                          "far more flowers, and far more nectar}}."},
             "C": {"kinds": ["7.5"],
                   "why": "Buscó un fallo, pero no lo encontró: {{partly in the hope of finding a flaw in it. I "
                          "did not find one}}. La opción convierte esa búsqueda en desconfianza."},
             "D": {"kinds": ["7.1"],
                   "why": "Recoge {{thousands of householders}}, pero el autor no comenta la participación: le "
                          "interesa el resultado."},
         }},
        {"n": 35, "type": "Opinión y actitud", "para": [5],
         "stem": "What criticism does the writer make of some members of the ‘no mow’ movement?",
         "options": ["They are too quick to condemn people who prefer a tidy garden.",
                     "They overstate the benefits of long grass for wildlife.",
                     "Their concern for insects is partly a form of display.",
                     "They have made unmown lawns fashionable among the wealthy."],
         "key": "C",
         "own": "Que algunos lo hacen para que se vea: les importan menos los insectos que quedar bien.",
         "why": "La crítica es explícita: {{There is a strand of it that seems less interested in insects than in "
                "being seen to care about them}}. La comparación con el padre lo remata: un césped largo para "
                "presumir en las cenas es {{just my father’s stripes in a different costume}}, es decir, otra "
                "forma de exhibición (§4.2).",
         "theory": ["4.2", "4.3"],
         "distractors": {
             "A": {"kinds": ["7.7"],
                   "why": "El texto no dice que critiquen a quienes cortan el césped; quien recibe comentarios es "
                          "el propio autor ({{drew pointed remarks from the postman}})."},
             "B": {"kinds": ["7.7", "7.5"],
                   "why": "El autor no discute los beneficios para los insectos; los acepta en el párrafo "
                          "anterior ({{I did not find one}}). Lo que critica son los motivos de algunos, no sus "
                          "datos."},
             "D": {"kinds": ["7.1", "7.3"],
                   "why": "Se apoya en {{mention it at dinner parties}}, pero no habla de una moda entre los "
                          "ricos: las cenas son el escaparate, no una clase social."},
         }},
        {"n": 36, "type": "Global", "para": "global",
         "stem": "Which of the following best describes the writer’s attitude to his decision to stop mowing?",
         "options": ["He is pleased with its effects but reluctant to make grand claims for it.",
                     "He sees it as a long-overdue rejection of his father’s values.",
                     "He regrets the friction that it caused with the people who live next door.",
                     "He expects that most other gardeners will soon be following his example."],
         "key": "A",
         "own": "Contento, pero sin triunfalismo: el jardín ha mejorado y los vecinos se interesan, aunque "
                "sigue usando la cortadora y desconfía de quienes presumen de ello.",
         "why": "Los efectos le gustan ({{And yet something has shifted}}, {{on warm afternoons the whole thing "
                "hummed}}), pero rebaja cada logro: {{I would like to report that the result was a meadow. It "
                "was not}}, {{I still own the mower, and I still use it}}, y cierra con una duda irónica: "
                "{{That, at any rate, is what I tell myself}}. Su reparo ante quienes presumen ({{Nor, I "
                "confess, am I wholly at ease}}) confirma que no quiere hacer de ello una causa.",
         "theory": ["5.4", "4.3"],
         "distractors": {
             "B": {"kinds": ["7.5"],
                   "why": "El final lo contradice: el padre, cree el autor, habría acabado convencido ({{and "
                          "then, had the bees been out, quietly persuaded}}). No es un rechazo de sus valores."},
             "C": {"kinds": ["7.6"],
                   "why": "Hubo roces ({{a note from next door asking, with elaborate politeness, whether I had "
                          "been unwell}}), pero el autor no se arrepiente y el conflicto se resuelve: {{The "
                          "neighbours have stopped enquiring after my health}}."},
             "D": {"kinds": ["7.3"],
                   "why": "Solo una vecina pide consejo ({{which part of her own lawn I thought she might leave "
                          "alone}}); generalizarlo a la mayoría de los jardineros va mucho más allá del texto."},
         }},
    ],
}

# ---------- Part 6 · Gapped text ----------
P6 = {
    "intro": "an extract from a magazine article about sheepdog trials",
    "title": "A language of whistles",
    "standfirst": "Our writer spends a day at a sheepdog trial in the Welsh hills and discovers that the most "
                  "important member of each team never says a word.",
    "text": [
        "From the bottom of the field, the course looked like nowhere in particular: a steep slope of rough "
        "grass, a few hurdles, a small pen made of gates and a row of muddy pick-up trucks parked along a "
        "dry-stone wall. Somewhere near the top, so far away that I had to be told where to look, five sheep were "
        "grazing with every appearance of unconcern. Within a few minutes, I was promised, they would be the most "
        "closely watched animals in the valley.",
        37,
        "What matters, rather, is control. Each handler has fifteen minutes to send a dog up the hill, bring the "
        "sheep down through a series of gates, separate two of them from the group and finally shut all five in "
        "the pen. For most of the run the handler must stay beside a post at the bottom of the field, so every "
        "instruction has to travel several hundred metres up the hillside as a whistle. The judge starts with a "
        "hundred points and takes them away: for every sheep that strays off line, every hesitation, every sign "
        "of panic.",
        38,
        "For a long moment nothing happened. Her handler, an elderly man in a flat cap, whistled once and then "
        "again, more sharply. The dog did not move. ‘She can’t hear him,’ Pritchard murmured. ‘Wind’s taking it.’ "
        "Where we were standing I could feel no wind at all, but up on the ridge, apparently, it was strong "
        "enough to carry a whistle away entirely. Eventually the dog seemed to make up her own mind and the sheep "
        "began to drift downhill, but by then, as Pritchard put it, the run was ‘in bits’.",
        39,
        "Pritchard learnt his from his father, whose own whistle, made of horn, he still uses: a small, worn "
        "crescent, no bigger than a thumbnail, which he took out of his pocket to show me. "
        "Younger handlers, he said, mostly buy plastic or steel ones online, ‘and there’s nothing wrong with "
        "that’. It was clear, all the same, that he would sooner have parted with his dog.",
        40,
        "That, I gradually came to understand, is the strangest thing about the partnership. The dog is reading "
        "the handler at least as closely as the handler is reading the sheep, and nerves travel. Several runs "
        "that morning came apart not on the hill but at the shed, the moment when the dog has to slip into the "
        "group and cut two sheep away from the rest. Done well, it takes a second. Done badly, it can use up all "
        "the remaining minutes and still not happen.",
        41,
        "By the time Nell’s turn came, a little after three, the wind had dropped. Pritchard walked to the post "
        "without a word to anyone, sent her off with a single long note and then stood perfectly still, hands in "
        "his pockets, for what felt like several minutes. Her outrun was wide and calm, and she brought the sheep "
        "down the hill in a line so straight it might have been ruled. By the second gate I had more or less "
        "stopped breathing.",
        42,
        "Her score, when it was read out, put her second. The winner, to nobody’s great surprise, was the young "
        "handler I had watched before lunch, and Pritchard was the first to go over and shake her hand. If he "
        "was disappointed, he hid it well. ‘The old ewe beat us,’ he said, scratching Nell behind the ear. "
        "‘She’ll have learnt something from that. I know I have.’",
        43,
        "Perhaps that is the point. A trial is less a contest of speed than of patience and trust between two "
        "creatures who cannot share a word of language but have learnt, over years, to share a great deal else. "
        "Pritchard, I suspect, would find that rather fanciful. ‘It’s just work,’ he would say, ‘done properly.’ "
        "But work done properly is a rarer sight than it ought to be, and I could happily have watched it all "
        "week.",
    ],
    "paragraphs": {
        "A": "I saw it done well only once that morning. A young handler, barely out of school, waited with her dog "
             "crouched at her feet while the sheep milled about, until a gap no wider than a hand opened in the "
             "group. A single word, and the dog was through it. The judge, Pritchard told me, would hardly have "
             "needed to pick up his pencil.",
        "B": "The first dog of the morning, a lean black-and-white bitch, set off on what Pritchard called the "
             "outrun, sweeping wide in a great pear-shaped arc so as to come up behind the sheep without alarming "
             "them. It was beautifully done. Then, just short of the top, she stopped, dropped flat in the grass "
             "and stayed there.",
        "C": "As I drove back down the valley that evening, it struck me that I had spent seven hours watching what "
             "was, on the face of it, a very slow way of moving five sheep a few hundred metres. I could not "
             "remember when I had last paid such close attention to anything for so long.",
        "D": "His dog, a four-year-old called Nell, was not due to run until mid-afternoon, and he spent most of "
             "the morning on the bank above the course, saying very little. I asked whether he was nervous. He "
             "gave the question some thought. ‘Not for me,’ he said eventually. ‘For her. She knows when I’m "
             "wound up, and it goes straight down the whistle.’",
        "E": "The man doing the promising was Alun Pritchard, a hill farmer who has been competing at trials for "
             "the best part of thirty years and judging them for ten. He had agreed to explain what I was about "
             "to see on one condition: that I stopped calling it a race. ‘Speed’s got nothing to do with it,’ he "
             "said. ‘Any fool can make sheep run.’",
        "F": "Even the shed, which I had been dreading on her behalf, worked at the first attempt. It was the pen "
             "that nearly undid them. One ewe, older and warier than the rest, turned and stamped at the dog, and "
             "for almost a minute the two stood nose to nose while the clock ran on. When the ewe at last gave "
             "way, the gate closed with eleven seconds to spare.",
        "G": "Whistles, it turns out, are something of a private language. Every handler develops a set of his or "
             "her own, and two dogs working the same field may respond to quite different calls. There are "
             "signals for left and right, for stop, walk on and steady, and a good handler can vary each one, a "
             "little softer or a little sharper, to say how urgently it is meant.",
        "H": "Sheepdog trials have a longer history than most people imagine. The first recorded one was held at "
             "Bala, in north Wales, in 1873, and drew a crowd of around three hundred. A century later, "
             "television brought the sport to millions, when ‘One Man and His Dog’ began a run on the BBC that "
             "would last for more than twenty years.",
    },
    "lex": ["with every appearance of unconcern", "the best part of (thirty years)", "any fool can …",
            "stray off line", "make up one’s own mind", "in bits (informal)", "would sooner have …",
            "part with sth", "nerves travel", "come apart (fig.)", "mill about", "be wound up (informal)",
            "on sb’s behalf", "undo sb (fig.)", "nose to nose", "with eleven seconds to spare",
            "on the face of it", "fanciful"],
    "items": [
        {"n": 37, "key": "E", "theory": ["4.1", "4.4"],
         "before": "El párrafo anterior termina con una promesa anónima: {{Within a few minutes, I was promised}}. "
                   "E identifica a quien la hizo con un sustantivo que la recoge: {{The man doing the "
                   "promising was Alun Pritchard}} (§4.4).",
         "after": "E termina negando que sea una carrera ({{‘Speed’s got nothing to do with it,’}}), y el párrafo "
                  "siguiente da la alternativa con [[rather]]: {{What matters, rather, is control}}. Además, E "
                  "presenta a Pritchard con nombre completo y el texto lo nombra después solo por el apellido: "
                  "{{as Pritchard put it}}."},
        {"n": 38, "key": "B", "theory": ["3.1", "4.1"],
         "before": "El párrafo anterior explica las reglas en general ({{Each handler has fifteen minutes to send "
                   "a dog up the hill}}); B pasa de la explicación al relato con el primer perro del día: {{The "
                   "first dog of the morning}}.",
         "after": "B deja a la perra inmóvil ({{she stopped, dropped flat in the grass and stayed there}}), y el "
                  "párrafo siguiente continúa la escena: {{For a long moment nothing happened. Her handler}}. "
                  "[[Her]] remite a la perra de B.",
         "trap": {"letter": "D",
                  "why": "{{His dog, a four-year-old called Nell}} también presenta una perra, pero su turno es "
                         "{{not due to run until mid-afternoon}} y el texto que sigue describe al dueño de la perra "
                         "como {{an elderly man in a flat cap}}, que no es Pritchard. Además, {{His}} no tiene "
                         "antecedente tras la explicación de las reglas."}},
        {"n": 39, "key": "G", "theory": ["4.4", "3.4"],
         "before": "El párrafo anterior acaba con el silbido que se lleva el viento ({{strong enough to carry a "
                   "whistle away entirely}}); G retoma la palabra para generalizar: {{Whistles, it turns out, "
                   "are something of a private language}} (§4.4, cadena léxica).",
         "after": "G dice que cada pastor tiene su propio juego de silbidos ({{Every handler develops a set of his "
                  "or her own}}), y el párrafo siguiente lo presupone con un posesivo: {{Pritchard learnt his "
                  "from his father}}. Sin G, [[his]] no tiene a qué referirse.",
         "trap": {"letter": "H",
                  "why": "Podría parecer una digresión histórica tras el primer recorrido, pero no menciona los "
                         "silbidos, así que {{Pritchard learnt his from his father}} se queda sin referente."}},
        {"n": 40, "key": "D", "theory": ["4.1", "3.1"],
         "before": "El párrafo anterior termina con el perro de Pritchard: {{he would sooner have parted with his "
                   "dog}}. D lo presenta de inmediato: {{His dog, a four-year-old called Nell}}.",
         "after": "D acaba con la explicación de Pritchard sobre los nervios ({{She knows when I’m wound up, and "
                  "it goes straight down the whistle}}), y el párrafo siguiente la recoge con un demostrativo: "
                  "{{That, I gradually came to understand, is the strangest thing about the partnership}}. "
                  "También anuncia el turno de Nell, que llega después: {{By the time Nell’s turn came}}.",
         "trap": {"letter": "A",
                  "why": "{{I saw it done well only once that morning}} parece seguir a la mañana de "
                         "competición, pero [[it]] no tiene antecedente: el [[shed]] aún no se ha explicado. Y "
                         "A no dice nada que pueda ser {{the strangest thing about the partnership}}."}},
        {"n": 41, "key": "A", "theory": ["4.1", "4.4"],
         "before": "El párrafo anterior contrasta el [[shed]] bien y mal hecho ({{Done well, it takes a second}}); "
                   "A recoge esa misma idea con [[it]]: {{I saw it done well only once that morning}}.",
         "after": "A presenta a la joven del único [[shed]] perfecto ({{A young handler, barely out of school}}), "
                  "y el texto la retoma más adelante como ganadora: {{the young handler I had watched before "
                  "lunch}}. Además, A cierra la mañana y el párrafo siguiente salta a la tarde: {{a little "
                  "after three}}.",
         "trap": {"letter": "F",
                  "why": "{{Even the shed, which I had been dreading on her behalf}} encaja con el tema del "
                         "párrafo anterior, pero se refiere a Nell ({{on her behalf}}), cuyo turno todavía no ha "
                         "llegado: el párrafo siguiente empieza {{By the time Nell’s turn came}}."}},
        {"n": 42, "key": "F", "theory": ["3.1", "4.1"],
         "before": "El párrafo anterior sigue el recorrido de Nell hasta {{By the second gate}}; F continúa con las "
                   "dos fases que faltan, el [[shed]] y el corral: {{Even the shed, which I had been dreading on "
                   "her behalf}}.",
         "after": "F cuenta el pulso con una oveja vieja ({{One ewe, older and warier than the rest}}), y el "
                  "párrafo siguiente lo recuerda al dar la puntuación: {{‘The old ewe beat us,’}}. Sin F, la "
                  "frase de Pritchard no tiene referente.",
         "trap": {"letter": "C",
                  "why": "Un final de jornada podría seguir a la carrera de Nell, pero el párrafo siguiente "
                         "todavía está en el campo ({{Her score, when it was read out}}) y {{The old ewe}} no "
                         "aparece en C."}},
        {"n": 43, "key": "C", "theory": ["3.2", "4.1"],
         "before": "El párrafo anterior cierra la competición con la puntuación y el ganador ({{Her score, when it "
                   "was read out, put her second}}); C sale del campo: {{As I drove back down the valley that "
                   "evening}}.",
         "after": "C termina con la sorpresa del autor ({{I could not remember when I had last paid such close "
                  "attention to anything for so long}}), y el último párrafo la interpreta: {{Perhaps that is the "
                  "point}}. La lentitud que señala C ({{a very slow way of moving five sheep}}) es la que "
                  "{{less a contest of speed than of patience and trust}} explica.",
         "trap": {"letter": "H",
                  "why": "Un apunte histórico podría servir de cierre, pero {{Perhaps that is the point}} pide "
                         "una reflexión del autor a la que responder, y H solo da fechas y cifras."}},
    ],
    "extra": {
        "letter": "H", "theory": ["5.1", "5.2"],
        "rules_out": [
            {"gaps": [37],
             "why": "Tras {{I was promised}} hace falta saber quién lo promete, y {{What matters, rather, is "
                    "control}} necesita delante algo que se descarte (la velocidad). H no aporta ninguna de las "
                    "dos cosas: {{Sheepdog trials have a longer history than most people imagine}}."},
            {"gaps": [38, 41, 42],
             "why": "Esos huecos están en mitad del relato de la jornada: el texto que sigue presupone una perra "
                    "concreta ({{Her handler, an elderly man in a flat cap}}), una mañana ya avanzada ({{the "
                    "young handler I had watched before lunch}}) o el pulso con una oveja ({{The old ewe beat "
                    "us}}). H habla de {{Bala, in north Wales, in 1873}}."},
            {"gaps": [39],
             "why": "{{Pritchard learnt his from his father}} necesita delante algo que sea [[his]]: los "
                    "silbidos. H no los menciona."},
            {"gaps": [40],
             "why": "{{That, I gradually came to understand, is the strangest thing about the partnership}} "
                    "remite a algo sobre el perro y el pastor; H habla de la historia y de la televisión ({{‘One "
                    "Man and His Dog’}})."},
            {"gaps": [43],
             "why": "Por delante podría pasar como apunte final, pero {{Perhaps that is the point}} pide algo que "
                    "interpretar, y H no contiene ninguna reflexión del autor."},
        ],
    },
}

# ---------- Part 7 · Multiple matching ----------
P7 = {
    "intro": "an article in which four people talk about judging competitions",
    "units": "judges",
    "lead": "Which judge",
    "title": "In the judge’s chair",
    "standfirst": "Four people who judge very different kinds of competition explain what the job involves.",
    "compound": 3,
    "sections": [
        {"label": "A", "name": "Fiona Grant, figure-skating judge",
         "text": "People imagine that the hardest part of judging is spotting the mistakes. It isn’t: after twenty "
                 "years of practice, and with a replay screen in front of you, the mistakes more or less announce "
                 "themselves. The hard part is everything that goes on in your own head. When a seventeen-year-old "
                 "falls on her opening jump and spends the rest of the programme fighting back tears, every human "
                 "instinct tells you to reward her courage. You can’t. You mark what she did on the ice, not what "
                 "it cost her, and you go home feeling slightly ashamed of how easily you managed it. The sport has "
                 "had to work hard at its reputation. After a vote-trading scandal at the 2002 Winter Olympics, the "
                 "old system of marks out of six was scrapped in favour of one in which every element is scored "
                 "separately, and I think we are a good deal more honest for it. What I still find difficult is "
                 "the abuse. Within minutes of a result, a skater’s fans will have posted the judges’ names "
                 "online, and some of what they write is vile."},
        {"label": "B", "name": "Derek Holt, vegetable judge at agricultural shows",
         "text": "I’ve judged vegetables at shows for twenty-six years, and I still get butterflies when I walk "
                 "into the marquee. Outsiders laugh, but the standards are exacting. A prize-winning plate of "
                 "onions has to match for size, shape and colour, with the necks neatly tied and not a blemish "
                 "between them, and the difference between first and third can come down to a millimetre. Some "
                 "exhibitors spend an entire summer nursing a single leek, so the least you owe them is a proper "
                 "look. I won’t judge in my own county any more: I know too many of the growers, and the ones who lose always "
                 "assume that’s why. Even so, I get accused of having favourites about once a season, usually by "
                 "someone who has driven a long way with a car boot full of leeks. My answer is to stay behind "
                 "once the cards are out and tell anyone who asks exactly why they didn’t win. Most of them take "
                 "it well. A few have come back the following year and beaten everyone, which pleases me more "
                 "than anything I grow myself."},
        {"label": "C", "name": "Ruth Okafor, pianist",
         "text": "I sit on the juries of three or four international piano competitions a year, and I have come to "
                 "distrust the whole business a little. Ten jurors from ten countries, each with a different idea "
                 "of how Chopin should sound, are not going to agree on who is the most interesting young pianist "
                 "in the room. What they can agree on is who made the fewest mistakes, and so, again and again, the "
                 "prizes go to the safe, polished player whom nobody loves and nobody can object to. Early in my "
                 "career as a juror I helped to vote out, in the second round, a young man whose playing struck me "
                 "as wilful and undisciplined. He is now one of the finest pianists of his generation, and I wince "
                 "whenever I see his name on a poster. These days I try to listen for the player I will still want "
                 "to hear in ten years’ time. I don’t always persuade my colleagues, but I no longer keep quiet "
                 "when I disagree with them."},
        {"label": "D", "name": "Patrick Doyle, wine judge",
         "text": "At a big competition I might taste a hundred and twenty wines in a day, and the only thing I know "
                 "about each is what’s in the glass. The bottles are hidden, the labels are gone and the order is "
                 "shuffled, partly so that no wine is always tasted at the end of a long morning, when everyone’s "
                 "palate is tired and every red starts to taste the same. It’s humbling. A few years ago I gave a "
                 "perfectly ordinary score to a wine I had praised extravagantly in my newspaper column only weeks "
                 "before, and I only found out when the results were published. My editor was delighted; I was "
                 "less so. People assume the job is all pleasure, but by mid-afternoon it’s closer to hard labour: "
                 "rinse, sniff, sip, spit, write, a hundred times over. What makes up for it is the hour at the end "
                 "of the day, when the panel sits down together and fights over the medals. I’ve learnt more from "
                 "those arguments than from any course."},
    ],
    "lex": ["announce themselves (fig.)", "fight back tears", "a vote-trading scandal", "scrap sth in favour of sth",
            "get butterflies", "not a blemish between them", "come down to (a millimetre)", "have favourites",
            "struck me as wilful", "wince", "keep quiet", "praise sth extravagantly", "make up for sth"],
    "items": [
        {"n": 44, "prompt": "is troubled by the hostility of spectators?", "key": "A",
         "theory": ["3.3", "4.3"],
         "elements": ["{{What I still find difficult is the abuse}}: los aficionados publican los nombres de los "
                      "jueces y {{some of what they write is vile}}."],
         "trap": {"letter": "B", "kinds": ["7.4"],
                  "why": "También recibe acusaciones ({{I get accused of having favourites}}), pero de los "
                         "concursantes que pierden, no del público: {{usually by someone who has driven a long "
                         "way with a car boot full of leeks}}."}},
        {"n": 45, "prompt": "takes steps to avoid any suspicion of bias?", "key": "B",
         "theory": ["3.3"],
         "elements": ["{{I won’t judge in my own county any more: I know too many of the growers}}, y explica el "
                      "motivo: {{the ones who lose always assume that’s why}}."],
         "trap": {"letter": "D", "kinds": ["7.4"],
                  "why": "La cata es a ciegas ({{The bottles are hidden, the labels are gone}}), pero es una "
                         "norma del concurso, no una decisión suya."}},
        {"n": 46, "prompt": "was unaware of an inconsistency in their own judgements until it became public?",
         "key": "D", "theory": ["4.1", "3.3"],
         "elements": ["Incoherencia: {{I gave a perfectly ordinary score to a wine I had praised extravagantly in "
                      "my newspaper column only weeks before}}.",
                      "Se enteró al publicarse: {{I only found out when the results were published}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "También se equivocó al juzgar ({{I helped to vote out, in the second round, a young "
                         "man}}), pero no hay contradicción entre dos juicios suyos ni nada que se hiciera "
                         "público."}},
        {"n": 47, "prompt": "believes that group decisions tend to favour inoffensive candidates?", "key": "C",
         "theory": ["3.3", "3.4"],
         "elements": ["Como los jurados solo coinciden en los errores, {{the prizes go to the safe, polished player "
                      "whom nobody loves and nobody can object to}}."],
         "trap": {"letter": "D", "kinds": ["7.2"],
                  "why": "El jurado también decide en grupo ({{the panel sits down together and fights over the "
                         "medals}}), pero no dice a quién favorecen esas decisiones."}},
        {"n": 48, "prompt": "says that identifying errors is the least demanding part of the role?", "key": "A",
         "theory": ["3.3", "3.4"],
         "elements": ["{{People imagine that the hardest part of judging is spotting the mistakes. It isn’t}}: los "
                      "errores {{more or less announce themselves}}."],
         "trap": {"letter": "C", "kinds": ["7.1"],
                  "why": "Habla de errores ({{who made the fewest mistakes}}), pero como lo único en que coinciden "
                         "los jurados, no como la parte fácil del trabajo."}},
        {"n": 49, "prompt": "makes a point of explaining decisions to those affected by them?", "key": "B",
         "theory": ["3.3"],
         "elements": ["{{My answer is to stay behind once the cards are out and tell anyone who asks exactly why "
                      "they didn’t win}}."],
         "trap": {"letter": "D", "kinds": ["7.4"],
                  "why": "También discute las decisiones, pero con los otros jueces ({{when the panel sits down "
                         "together}}), no con los concursantes."}},
        {"n": 50, "prompt": "feels uneasy about how readily they can suppress their natural feelings?",
         "key": "A", "theory": ["4.1", "3.4"],
         "elements": ["Reprime lo que siente: {{every human instinct tells you to reward her courage. You "
                      "can’t}}.",
                      "Le incomoda la facilidad: {{you go home feeling slightly ashamed of how easily you managed "
                      "it}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "También siente malestar ({{I wince whenever I see his name on a poster}}), pero por una "
                         "decisión equivocada, no por reprimir sus sentimientos."}},
        {"n": 51, "prompt": "regrets having underestimated someone’s potential early in their judging career?",
         "key": "C", "theory": ["4.1", "3.3"],
         "elements": ["Error al principio: {{Early in my career as a juror I helped to vote out, in the second "
                      "round, a young man}}.",
                      "Pesar: {{He is now one of the finest pianists of his generation, and I wince}}."],
         "trap": {"letter": "D", "kinds": ["7.6"],
                  "why": "También se equivocó ({{I gave a perfectly ordinary score}}), pero hace unos años, no al "
                         "principio de su carrera, y con un vino, no con el futuro de una persona."}},
        {"n": 52, "prompt": "values the disagreements they have with fellow judges?", "key": "D",
         "theory": ["3.3", "4.4"],
         "elements": ["Las discusiones del final compensan el día ({{fights over the medals}}) y le enseñan: "
                      "{{I’ve learnt more from those arguments than from any course}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "Discrepa de sus colegas y ya no se calla ({{I no longer keep quiet when I disagree with "
                         "them}}), pero no dice que valore esas discusiones: desconfía del jurado como sistema."}},
        {"n": 53, "prompt": "explains how a practical arrangement prevents tiredness from distorting results?",
         "key": "D", "theory": ["3.3"],
         "elements": ["{{the order is shuffled, partly so that no wine is always tasted at the end of a long "
                      "morning, when everyone’s palate is tired}}."],
         "trap": {"letter": "A", "kinds": ["7.5"],
                  "why": "También cuenta un cambio en el sistema de puntuación ({{the old system of marks out of "
                         "six was scrapped}}), pero responde a un escándalo de votos, no al cansancio."}},
    ],
}
