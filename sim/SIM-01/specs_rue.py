# SIM-01 · Reading and Use of English · specs de las Parts 1-7
# Se monta con: python3 src/gen_SIM.py rue sim/SIM-01
# Formato de cada spec: cabecera del generador correspondiente (src/gen_UOE-P1..P4, src/gen_RDG-P5..P7).

# ---------- Part 1 · Multiple-choice cloze ----------
P1 = {
    "title": "The potato’s unlikely champion",
    "example": {"opts": ["overcome", "overtake", "overdo", "overrun"], "key": "A"},
    "text": [
        "Few foods have had to {0} as much prejudice as the potato. In eighteenth-century France it was widely "
        "thought fit only for animals, and to many people, eating it {1} of desperation. Rumours that it caused "
        "leprosy were {2}, and polite society {3} the plant short shrift.",
        "Antoine-Augustin Parmentier knew better. An army pharmacist who had been taken prisoner during the Seven "
        "Years’ War, he had lived on little else in captivity, and he came home convinced that the potato could help "
        "{4} famine in years of poor harvests.",
        "He set out to {5} over his compatriots with considerable flair, serving elaborate potato dinners to "
        "distinguished guests and presenting the king with a bouquet of potato flowers. According to one "
        "much-repeated story, he even had a field of potatoes guarded by soldiers during the day but left unwatched "
        "at night, so that curious locals would steal the plants. Whatever the truth of the tale, his efforts "
        "eventually {6} fruit. Within a generation the potato had {7} on, and today Parmentier is {8} with turning "
        "a despised crop into a national staple.",
    ],
    "items": [
        {"n": 1, "opts": ["hinted", "smacked", "echoed", "bordered"], "key": "B", "theory": ["6.1"],
         "why": "[[smack of sth]]: dar la impresión de algo malo, «oler a» ([[it smacked of desperation]]). Es el "
                "único de los cuatro que se construye con [[of]] en este sentido.",
         "wrong": {"A": "[[hint]] va con [[at]] ([[it hinted at desperation]]); *[[hinted of]] no existe.",
                   "C": "[[echo]] es transitivo ([[it echoed an earlier crisis]]); *[[echoed of]] no existe.",
                   "D": "[[border]] en sentido figurado va con [[on]] ([[it bordered on desperation]]); con "
                        "[[of]] no funciona."}},
        {"n": 2, "opts": ["replete", "profuse", "rife", "prolific"], "key": "C", "theory": ["5.1", "3.2"],
         "why": "[[rife]]: muy extendido, y casi siempre de algo malo ([[rumours were rife]], [[corruption is "
                "rife]]). Funciona como predicativo, sin complemento.",
         "wrong": {"A": "[[replete]] exige complemento ([[replete with]]: repleto de); solo, al final de la "
                        "oración, queda cojo.",
                   "B": "[[profuse]]: abundante en lo que se da o se vierte ([[profuse apologies]], [[profuse "
                        "bleeding]]); no se dice de rumores que circulan.",
                   "D": "[[prolific]]: muy productivo, que produce mucho ([[a prolific writer]]); los rumores "
                        "no producen nada."}},
        {"n": 3, "opts": ["paid", "dealt", "showed", "gave"], "key": "D", "theory": ["4.2"],
         "why": "[[give sb/sth short shrift]]: despachar algo con desdén, no prestarle ninguna atención. Expresión "
                "fija; [[gave]] es el pasado.",
         "wrong": {"A": "*[[pay short shrift]] es un cruce frecuente con [[pay scant attention]], pero no es la "
                        "expresión ([[paid]]).",
                   "B": "[[deal]] forma otras combinaciones ([[deal a blow]]); *[[dealt short shrift]] no existe.",
                   "C": "*[[show short shrift]] tampoco existe ([[showed]])."}},
        {"n": 4, "opts": ["avert", "evade", "elude", "deter"], "key": "A", "theory": ["5.1"],
         "why": "[[avert]]: impedir a tiempo que ocurra algo malo ([[avert famine, a crisis, a disaster]]). La "
                "patata podía evitar el hambre en los años de malas cosechas.",
         "wrong": {"B": "[[evade]]: eludir con habilidad o con trampa algo que te persigue o te obliga ([[evade "
                        "tax, capture, a question]]); no se evita así una hambruna.",
                   "C": "[[elude]]: escaparse de alguien ([[elude the police]]) o no ser alcanzado ([[success "
                        "eluded him]]); no significa impedir.",
                   "D": "[[deter]]: disuadir a alguien ([[deter sb from doing sth]]); su objeto es una persona, "
                        "no un hecho."}},
        {"n": 5, "opts": ["hand", "win", "take", "turn"], "key": "B", "theory": ["7.1"],
         "why": "[[win sb over]]: ganarse a alguien, convencerlo de algo de lo que desconfiaba. Encaja con la "
                "campaña que se describe a continuación (cenas, flores para el rey).",
         "wrong": {"A": "[[hand sb over]]: entregar a alguien (a la policía, a otra autoridad).",
                   "C": "[[take over]]: hacerse con el control; con personas como objeto no significa convencer.",
                   "D": "[[turn sb over]]: entregar a alguien a la justicia ([[turn sb over to the police]])."}},
        {"n": 6, "opts": ["carried", "brought", "bore", "held"], "key": "C", "theory": ["4.2"],
         "why": "[[bear fruit]]: dar fruto, tener éxito al cabo del tiempo ([[his efforts bore fruit]]). Expresión "
                "fija; [[bore]] es el pasado de [[bear]].",
         "wrong": {"A": "*[[carried fruit]] no forma la expresión; [[carry]] es «llevar» en sentido literal.",
                   "B": "*[[brought fruit]] tampoco; [[bring results]] sí existe, pero no con [[fruit]].",
                   "D": "*[[held fruit]] no existe ([[held]])."}},
        {"n": 7, "opts": ["caught", "looked", "turned", "set"], "key": "A", "theory": ["7.1"],
         "why": "[[catch on]]: hacerse popular, extenderse. En una generación la patata se impuso.",
         "wrong": {"B": "[[look on]]: mirar sin intervenir; no tiene sentido con [[the potato]] como sujeto.",
                   "C": "[[turn on]]: encender, o volverse contra alguien ([[turn on sb]]).",
                   "D": "[[set on]]: atacar ([[the dogs set on him]]); intransitivo y con este sujeto no "
                        "significa nada."}},
        {"n": 8, "opts": ["attributed", "acknowledged", "recognised", "credited"], "key": "D", "theory": ["6.1"],
         "why": "[[be credited with sth / with doing sth]]: atribuirle a alguien un mérito. La preposición "
                "[[with]] y el gerundio [[turning]] solo encajan con [[credited]].",
         "wrong": {"A": "[[attribute]] va con [[to]] y con la cosa como sujeto pasivo ([[the change is attributed "
                        "to Parmentier]]); *[[attributed with]] es un error frecuente.",
                   "B": "[[acknowledged]] va con [[as]] ([[acknowledged as the pioneer]]), no con [[with]] + "
                        "gerundio.",
                   "C": "[[recognised]] también va con [[as]] o [[for]] ([[recognised for his work]]); con "
                        "[[with]] no funciona."}},
    ],
}

# ---------- Part 2 · Open cloze ----------
P2 = {
    "title": "The psychology of waiting",
    "example": "WITH",
    "text": [
        "Some years ago, the managers of a busy American airport were faced {0} a curious problem. Passengers "
        "were complaining bitterly about the time it took for their luggage to reach them, so the airport took on "
        "extra baggage handlers and cut the average wait to eight minutes, comfortably within the industry norm. "
        "{9} so, the complaints kept coming. It took some time for the managers to work out {10} was really going "
        "on: passengers reached the baggage hall within a minute of leaving the plane and then found {11} standing "
        "by the carousel for seven more. The solution the managers came {12} with was ingenious. Arriving flights "
        "were moved to gates further from the main terminal, so that the walk took six times as long, and the "
        "complaints all but disappeared.",
        "The episode illustrates a principle that researchers have long understood: what matters is not so much "
        "the length of a wait {13} how it feels. Time spent doing something passes more quickly than time spent "
        "doing nothing. It is {14} this reason that so many lifts have mirrors beside them, and that restaurants "
        "hand menus to diners who are still waiting for a table. Uncertainty makes matters worse, too: a wait of "
        "unknown length seems longer than one {15} end is in sight. And there is {16} quite as infuriating as "
        "watching someone who arrived after you being served first.",
    ],
    "items": [
        {"n": 9, "key": ["EVEN"], "type": "Conector compuesto [[even so]]", "theory": ["7.2"],
         "why": "Detrás del hueco va [[so]] y una coma: [[even so]] = aun así. Han reducido la espera por debajo "
                "de lo normal y, pese a ello, siguen las quejas.",
         "wrong": "[[!and]] ([[and so]] introduce una consecuencia, y aquí hay contraste); [[!just]] o [[!ever]] "
                  "(no forman conector con [[so]])."},
        {"n": 10, "key": ["WHAT"], "type": "Relativo nominal", "theory": ["8"],
         "why": "[[work out]] necesita objeto, y el hueco es a la vez ese objeto y el sujeto de [[was really going "
                "on]]: [[what]] = «lo que». Los dos puntos dan después la respuesta.",
         "wrong": "[[!that]] o [[!which]] (necesitan un antecedente que no hay); [[!it]] (*[[work out it was "
                  "going on]] no tiene sentido)."},
        {"n": 11, "key": ["THEMSELVES"], "type": "Reflexivo en [[find oneself + -ing]]", "theory": ["4", "6.3"],
         "why": "[[find oneself doing sth]]: verse en una situación sin haberla buscado. El reflexivo concuerda con "
                "el sujeto plural [[passengers]].",
         "wrong": "[[!them]] (con [[find]], el pronombre que remite al sujeto tiene que ser reflexivo: [[found "
                  "them standing]] hablaría de otras personas); [[!it]] (no tiene antecedente)."},
        {"n": 12, "key": ["UP"], "type": "Partícula de phrasal verb", "theory": ["6.2"],
         "why": "[[come up with]]: idear, dar con una solución. El [[with]] ya está detrás del hueco.",
         "wrong": "[[!out]] ([[come out with]] = soltar un comentario o lanzar un producto); [[!across]] ([[come "
                  "across]] no lleva [[with]])."},
        {"n": 13, "key": ["AS"], "type": "Correlativo [[not so much … as]]", "theory": ["10", "7.2"],
         "why": "[[not so much X as Y]]: no tanto X como Y. El [[not so much]] anterior anuncia el [[as]].",
         "wrong": "[[!but]] (*[[not so much X but Y]] es un cruce frecuente con [[not X but Y]], pero no es "
                  "correcto); [[!than]] (no hay comparativo)."},
        {"n": 14, "key": ["FOR"], "type": "Cleft con frase preposicional", "theory": ["10", "6.3"],
         "why": "[[It is … that]] destaca una frase preposicional: [[for this reason]], «por esta razón». La "
                "razón es la frase anterior: el tiempo ocupado pasa más deprisa.",
         "wrong": "[[!by]] o [[!with]] (no forman expresión con [[reason]]); [[!due]] (pediría [[to]]: [[due to "
                  "this]]); [[!because]] (*[[because this reason]])."},
        {"n": 15, "key": ["WHOSE"], "type": "Relativo posesivo", "theory": ["8"],
         "why": "[[one]] sustituye a [[a wait]], y detrás del hueco va un sustantivo sin determinante ([[end]]): "
                "relativo posesivo, «una espera cuyo final está a la vista».",
         "wrong": "[[!where]] o [[!when]] (exigirían [[the end]]); [[!which]] o [[!that]] (*[[which end is in "
                  "sight]])."},
        {"n": 16, "key": ["NOTHING", "LITTLE"], "type": "Cuantificador negativo", "theory": ["3"],
         "why": "[[there is nothing quite as … as]]: no hay nada tan exasperante como… [[Little]] («poca cosa») "
                "también es gramatical y conserva el sentido, aunque con [[quite]] suena menos natural.",
         "wrong": "[[!no]] (*[[there is no quite as]]: [[no]] necesita un sustantivo); [[!anything]] (sin "
                  "negación delante no funciona); [[!something]] (dice lo contrario: que hay algo así de "
                  "irritante, sin el valor de superlativo)."},
    ],
}

# ---------- Part 3 · Word formation ----------
P3 = {
    "changes": "hasta tres cambios por hueco",
    "title": "The man who braved the rain",
    "example": "DISBELIEF", "example_stem": "BELIEVE",
    "text": [
        "When the merchant Jonas Hanway began to carry an umbrella through the streets of London in the 1750s, he "
        "was greeted with open {0|BELIEVE}. Umbrellas were familiar enough as accessories for women, but a man who "
        "sheltered under one risked having his {17|MASCULINE} called into question.",
        "Hanway, a tireless {18|PHILANTHROPY} who campaigned on behalf of the city’s poor, was not easily "
        "deterred. He had seen umbrellas in everyday use on his travels in Persia, and he could see no reason why a "
        "sensible man should arrive at his destination soaked to the skin. His {19|CONVENTION} habit did not endear "
        "him to the coachmen of London, who relied on wet weather for much of their trade and are said to have "
        "jeered at him in the street.",
        "Hanway’s {20|PERSIST} eventually paid off. {21|STAND} the mockery he endured, other men gradually "
        "followed his lead, and by the time of his death in 1786 the umbrella was well on its way to becoming "
        "{22|COMMON} among respectable Londoners. The appeal of staying dry, it seems, had proved {23|RESIST}. "
        "Today Hanway is remembered less for his charitable work than as the {24|RUN} of every commuter who has "
        "ever unfurled an umbrella on a wet Monday morning.",
    ],
    "items": [
        {"n": 17, "stem": "MASCULINE", "key": ["MASCULINITY", "MASCULINENESS"], "type": "Sustantivo · -ity",
         "theory": ["4.1", "8.2"],
         "why": "[[his]] + hueco + [[called into question]]: sustantivo. Lo que se ponía en duda era su "
                "hombría. [[Masculineness]] figura en algún diccionario como derivado, pero la forma normal es "
                "[[masculinity]].",
         "changes": "[[masculine]] → [[masculinity]]: [[-ity]], y la [[e]] final se pierde. Un cambio.",
         "wrong": "[[!MASCULINE]] (es la palabra base y es adjetivo); [[!MASCULINISM]] (ideología, no "
                  "cualidad); *[[!MASCULINEITY]] (conserva una [[e]] que se pierde)."},
        {"n": 18, "stem": "PHILANTHROPY", "key": ["PHILANTHROPIST"], "type": "Sustantivo de persona",
         "theory": ["4.4", "8.3"],
         "why": "[[a tireless]] + hueco + [[who campaigned]]: un sustantivo de persona en singular. Hanway era un "
                "filántropo.",
         "changes": "[[philanthropy]] → [[philanthropist]]: la [[y]] final se sustituye por [[-ist]]. Un cambio.",
         "wrong": "[[!PHILANTHROPIC]] (adjetivo); [[!PHILANTHROPISTS]] (plural tras [[a]])."},
        {"n": 19, "stem": "CONVENTION", "key": ["UNCONVENTIONAL"], "type": "Adjetivo · prefijo un-",
         "theory": ["4.2", "6.1"],
         "why": "[[His]] + hueco + [[habit]]: adjetivo. El párrafo anterior explica que un hombre con paraguas "
                "rompía las normas: hábito poco convencional.",
         "changes": "[[convention]] → [[conventional]] ([[-al]]) → [[unconventional]] ([[un-]]). Dos cambios.",
         "wrong": "[[!CONVENTIONAL]] (dice lo contrario de lo que cuenta el texto); *[[!INCONVENTIONAL]] (el "
                  "prefijo es [[un-]])."},
        {"n": 20, "stem": "PERSIST", "key": ["PERSISTENCE", "PERSISTENCY"], "type": "Sustantivo · -ence",
         "theory": ["4.1", "8.4"],
         "why": "[[Hanway’s]] + hueco + [[eventually paid off]]: sustantivo. Su insistencia acabó dando resultado. "
                "[[Persistency]] es una variante registrada, mucho menos frecuente.",
         "changes": "[[persist]] → [[persistence]]: [[-ence]] (no [[-ance]]). Un cambio.",
         "wrong": "*[[!PERSISTANCE]] (grafía con [[a]]); [[!PERSISTENT]] (adjetivo)."},
        {"n": 21, "stem": "STAND", "key": ["NOTWITHSTANDING"], "type": "Preposición compuesta",
         "theory": ["7.3", "2.2"],
         "why": "Hueco + [[the mockery he endured]] + coma + oración principal: hace falta una preposición "
                "concesiva, «pese a». [[Notwithstanding]] se forma sobre [[withstand]].",
         "changes": "[[stand]] → [[withstand]] ([[with-]]) → [[notwithstanding]] ([[not-]] y [[-ing]]). Tres "
                    "cambios.",
         "wrong": "[[!WITHSTANDING]] (participio de [[withstand]], «resistir»: haría a [[other men]] resistir "
                  "las burlas que sufrió Hanway, que no tiene sentido); [[!OUTSTANDING]] (adjetivo, «excelente» "
                  "o «pendiente»)."},
        {"n": 22, "stem": "COMMON", "key": ["COMMONPLACE"], "type": "Adjetivo · compuesto",
         "theory": ["7.2"],
         "why": "[[becoming]] + hueco + [[among respectable Londoners]]: adjetivo predicativo. El paraguas se "
                "estaba volviendo algo habitual.",
         "changes": "[[common]] + [[place]] → [[commonplace]], en una sola palabra. Un cambio.",
         "wrong": "[[!COMMONER]] (comparativo o sustantivo, «plebeyo»); [[!UNCOMMON]] (lo contrario); "
                  "[[!COMMONALITY]] (sustantivo)."},
        {"n": 23, "stem": "RESIST", "key": ["IRRESISTIBLE"], "type": "Adjetivo · prefijo ir- y -ible",
         "theory": ["6.1", "8.4"],
         "why": "[[had proved]] + hueco: adjetivo. Las ventajas de ir seco resultaron imposibles de resistir; "
                "por eso los demás imitaron a Hanway.",
         "changes": "[[resist]] → [[resistible]] ([[-ible]]) → [[irresistible]] ([[ir-]]). Dos cambios.",
         "wrong": "*[[!IRRESISTABLE]] (la terminación es [[-ible]]); [[!RESISTANT]] (no encaja con el sujeto "
                  "[[the appeal]]); *[[!UNRESISTIBLE]] (el prefijo es [[ir-]])."},
        {"n": 24, "stem": "RUN", "key": ["FORERUNNER"], "type": "Sustantivo · prefijo fore-",
         "theory": ["6.4", "4.4", "8.1"],
         "why": "[[as the]] + hueco + [[of every commuter]]: sustantivo singular. Hanway es el precursor de todos "
                "los que hoy abren un paraguas.",
         "changes": "[[run]] → [[runner]] ([[-er]], con doble [[n]]) → [[forerunner]] ([[fore-]]). Dos cambios.",
         "wrong": "[[!RUNNER]] (corredor); *[[!FORERUNER]] (sin duplicar la [[n]]); [[!FORERUNNERS]] (plural "
                  "tras [[the]] y con [[every commuter]])."},
    ],
}

# ---------- Part 4 · Key word transformations ----------
P4 = {
    "example": {"s1": "Jack started learning the cello three years ago.", "keyword": "BEEN",
                "s2": "Jack {G} for three years.", "answer": "HAS BEEN LEARNING THE CELLO"},
    "items": [
        {"n": 25, "s1": "Demand for tickets was so great that the festival’s website crashed within minutes.",
         "keyword": "SUCH", "s2": "{G} that the festival’s website crashed within minutes.",
         "key": ["SUCH WAS {THE|_} DEMAND FOR TICKETS", "{THE|_} DEMAND FOR TICKETS WAS SUCH",
                 "THERE WAS SUCH {GREAT|HIGH|_} DEMAND FOR TICKETS", "THERE WAS SUCH A {GREAT|HIGH|_} DEMAND FOR "
                 "TICKETS", "TICKETS WERE IN SUCH {GREAT|HIGH|_} DEMAND"],
         "halves": ("Such was", "the demand for tickets"),
         "theory": ["3.1", "3.7"],
         "why": "[[so great that]] → [[such was … that]]: con [[such]] al principio, el verbo va delante del "
                "sujeto. También valen la forma sin inversión, con [[such]] detrás del verbo ([[the demand for "
                "tickets was such that]]), y las construcciones con [[such (a) + sustantivo]]: [[there was such "
                "(great) demand]], [[tickets were in such demand]].",
         "wrong": [("SUCH WAS THE DEMAND", "falta [[for tickets]]: la segunda mitad no puntúa"),
                   ("SUCH THE DEMAND FOR TICKETS WAS", "sin inversión, [[such]] no puede ir delante"),
                   ("SO GREAT WAS THE DEMAND FOR TICKETS", "")]},
        {"n": 26, "s1": "I’m sure Helen didn’t intend her remarks to offend anyone.",
         "keyword": "MEANT", "s2": "Helen can’t {G} offence with her remarks.",
         "key": ["{POSSIBLY|_} HAVE MEANT TO {CAUSE|GIVE} {ANY|ANYONE|_}"],
         "halves": ("have meant", "to cause / give (any)"),
         "theory": ["3.5", "5.1"],
         "why": "[[I’m sure … didn’t]] sobre el pasado → [[can’t have]] + participio. [[Offence]] pide su verbo: "
                "[[cause / give (any) offence]] o [[cause / give anyone offence]].",
         "wrong": [("MEANT TO CAUSE ANY", "[[can’t]] + pasado no existe: hace falta [[have meant]]"),
                   ("HAVE MEANT CAUSING ANY", "[[mean + -ing]] significa «implicar», no «tener intención»"),
                   ("HAVE MEANT TO MAKE ANY", "*[[make offence]] no es collocation"),
                   ("HAVE MEANT ANYONE TO TAKE", "[[take offence]] va con [[at]]: *[[take offence with her "
                                                 "remarks]] no es correcto")]},
        {"n": 27, "s1": "As the negotiations dragged on, the two sides became increasingly reluctant to compromise.",
         "keyword": "MORE", "s2": "The longer the negotiations dragged on, {G} to compromise.",
         "key": ["THE MORE {RELUCTANT|UNWILLING} {THE TWO SIDES|BOTH SIDES|THE SIDES} {BECAME|GREW|GOT|WERE}",
                 "THE MORE {RELUCTANT|UNWILLING} WERE {THE TWO SIDES|BOTH SIDES}"],
         "halves": ("the more reluctant", "the two sides became"),
         "theory": ["3.7"],
         "why": "[[increasingly]] → comparativo correlativo: [[the longer …, the more …]]. Detrás de [[the more "
                "reluctant]] van el sujeto y el verbo; con [[were]] también cabe la inversión, más formal "
                "([[the more reluctant were the two sides]]).",
         "wrong": [("THE MORE THE TWO SIDES BECAME RELUCTANT", "el adjetivo tiene que ir pegado a [[the more]]"),
                   ("THE MORE RELUCTANT THEY BECAME", "[[they]] remitiría a [[the negotiations]]: falta el "
                                                      "sujeto real"),
                   ("MORE RELUCTANT THE TWO SIDES BECAME", "falta el [[the]] del segundo término")]},
        {"n": 28, "s1": "Even after reading the instructions twice, Paul still had no idea how to assemble the "
                        "wardrobe.",
         "keyword": "WISER", "s2": "Paul read the instructions twice, but {G} as to how to assemble the wardrobe.",
         "key": ["{_|HE} {WAS STILL|WAS|REMAINED|ENDED UP} NONE THE WISER", "{_|HE} {WAS STILL|WAS} NOT ANY THE WISER",
                 "{_|HE} {STILL|_} WASN’T ANY THE WISER", "{_|HE} {WAS STILL|WAS|REMAINED} NO WISER",
                 "{_|HE} {WAS STILL|WAS} NOT ANY WISER", "{_|HE} {STILL|_} WASN’T ANY WISER"],
         "halves": ("(he) was (still)", "none the wiser"),
         "theory": ["5.2"],
         "why": "[[be none the wiser]]: seguir sin entender, no saber más que antes. Tras [[but]], el sujeto "
                "puede repetirse ([[he]]) u omitirse, porque es el mismo. También valen las variantes [[not any "
                "the wiser]] y [[no wiser]], menos idiomáticas pero con el mismo sentido.",
         "wrong": [("WAS NOT MUCH THE WISER", "[[not much the wiser]] supone que entendió algo más: cambia el sentido"),
                   ("HE WAS NOT THE WISER", "la expresión exige [[none]], [[not any]] o [[no]]"),
                   ("HE WAS NONE WISER", "falta [[the]]: la forma es [[none the wiser]]")]},
        {"n": 29, "s1": "Tom didn’t tell anyone about his plans because he was worried that his colleagues "
                        "would laugh at him.",
         "keyword": "FEAR", "s2": "Tom said nothing about his plans {G} by his colleagues.",
         "key": ["{FOR|OUT OF|THROUGH} FEAR OF BEING {LAUGHED AT|MOCKED|RIDICULED|MADE FUN OF}",
                 "FOR FEAR {THAT|_} HE {WOULD|MIGHT|SHOULD} BE {LAUGHED AT|MOCKED|RIDICULED}",
                 "FOR FEAR HE {WOULD|MIGHT|SHOULD} BE MADE FUN OF"],
         "halves": ("for fear of", "being laughed at"),
         "theory": ["5.4", "3.3"],
         "why": "[[for fear of + -ing]]: por miedo a. Como detrás viene [[by his colleagues]], el gerundio va en "
                "pasiva: [[being laughed at]], con la preposición de [[laugh at]] al final. También valen los "
                "sinónimos ([[mocked]], [[ridiculed]], [[made fun of]]) y [[for fear (that) he would be laughed "
                "at]].",
         "wrong": [("FOR FEAR OF BEING LAUGHED", "falta [[at]]: [[laugh at]] la conserva en pasiva"),
                   ("FOR FEAR OF LAUGHING AT", "voz activa: no encaja con [[by his colleagues]]"),
                   ("IN FEAR OF BEING LAUGHED AT", "[[in fear of]] es «temiendo, amenazado por» "
                                                   "([[live in fear of]]); para el motivo se usa [[for fear of]]")]},
        {"n": 30, "s1": "Our head teacher always takes the trouble to learn the name of every new pupil.",
         "keyword": "POINT", "s2": "Our head teacher always {G} the name of every new pupil.",
         "key": ["MAKES A POINT OF {LEARNING|MEMORISING|MEMORIZING|GETTING TO KNOW}",
                 "MAKES IT A POINT TO {LEARN|MEMORISE|MEMORIZE|GET TO KNOW}"],
         "halves": ("makes a point", "of learning"),
         "theory": ["5.2", "5.1"],
         "why": "[[make a point of doing sth]]: hacer algo a propósito, con especial empeño, porque se considera "
                "importante; equivale a [[take the trouble to]]. La variante [[make it a point to do sth]] también "
                "existe.",
         "wrong": [("MAKES A POINT TO LEARN", "con [[a point]] va [[of + -ing]]; [[to]] exige [[make it a point]]"),
                   ("IS MAKING A POINT OF LEARNING", "[[always]] + presente simple: es un hábito"),
                   ("MAKES THE POINT OF LEARNING", "[[make the point that]] es «señalar, argumentar»")],
         "lex": ["make a point of doing sth"]},
    ],
}

# ---------- Part 5 · Multiple choice ----------
P5 = {
    "intro": "an article about the history of sleep",
    "title": "The hour between sleeps",
    "standfirst": "Our ancestors, it seems, routinely woke in the middle of the night. What, if anything, should we "
                  "make of that?",
    "text": [
        "For most of my adult life, waking at three in the morning has felt like a small emergency. The routine "
        "will be familiar to many readers: the glance at the clock, the hurried calculation of how many hours "
        "remain before the alarm goes off, the creeping conviction that the coming day is already ruined. "
        "Sleeplessness of this kind, which arrives not at bedtime but in the dead of night, is generally treated as a "
        "malfunction, to be corrected with pills, apps or a stern regime of ‘sleep hygiene’. It had simply never "
        "occurred to me that it might once have been regarded as nothing of the sort.",

        "That it may have been is largely the discovery of a historian. While researching what the night was like "
        "in early modern Britain, A. Roger Ekirch kept coming across references to something called ‘first "
        "sleep’. They turned up in diaries and letters, in prayer books and medical treatises, and in the "
        "statements of witnesses in court, who would mention quite casually that they had seen or heard something "
        "after their first sleep. What struck Ekirch was less the phrase itself than the fact that nobody ever "
        "paused to explain it. A term that needs no gloss is one that everybody already understands, and the "
        "conclusion he eventually drew was that sleeping in two instalments, with a spell of wakefulness in "
        "between, had once been entirely unremarkable.",

        "That spell, which might last an hour or more, seems to have been put to every conceivable use. People "
        "prayed, and some devotional books supplied prayers composed for the occasion. They got up to tend the "
        "fire or see to the animals; they talked, made love, or lay quietly turning over the dreams from which "
        "they had just surfaced. Some, inevitably, made use of the darkness for less innocent purposes. What they "
        "did not do, as far as the records show, was fret about being awake. Only gradually, as artificial "
        "lighting spread and bedtimes drifted later, did the two sleeps merge into one, and by the early twentieth "
        "century the very idea of a first sleep had all but vanished from ordinary speech.",

        "Historians’ hunches seldom find support in a laboratory, but this one did. In the early 1990s the "
        "psychiatrist Thomas Wehr, working at the National Institute of Mental Health in the United States, asked "
        "a group of volunteers to spend fourteen hours of every twenty-four in darkness, roughly the length of a "
        "winter night before the arrival of cheap lighting. After some weeks, their sleep began to divide: a first "
        "stretch of several hours, a period of calm wakefulness, and then a second stretch that lasted until "
        "morning. The convergence of the archive and the sleep laboratory is genuinely striking, and it is not "
        "hard to see why the story has travelled so far.",

        "Travelled it certainly has, and not always in the best of company. A modest industry has grown up around "
        "the notion that we are all sleeping ‘wrongly’, and that by recovering the rhythm of our ancestors we "
        "might recover their supposed serenity too. There is already no shortage of advice on retraining the body "
        "into two tidy sleeps, and it can surely be only a matter of time before someone opens a retreat that charges "
        "handsomely for the privilege of being woken at midnight. The reasoning behind all this is seductive and, "
        "I think, muddled. That people once slept in a particular way tells us how they lived, not how we ought "
        "to; our ancestors also ate badly, died young and treated most illnesses with remedies that did more harm "
        "than good. Nor is the evidence quite as tidy as the marketing suggests. Researchers who recorded the "
        "sleep of three present-day societies without electricity, in Africa and South America, found little "
        "sign of a regular break in the night.",

        "And yet I would not want to dismiss the history altogether, because its real value lies somewhere the "
        "wellness industry has little reason to look. Much of the misery of waking at night comes not from the "
        "waking itself but from the panic that follows it: the conviction that something has gone wrong, and the "
        "frantic effort to put it right, which more or less guarantees that it will not be put right. Knowing "
        "that a wakeful spell in the small hours was, for centuries, simply part of the night does nothing to "
        "change the body. It can, however, change what we make of it, and that is a point some sleep specialists "
        "have been quick to take up.",

        "I have not, I should add, rediscovered some lost rhythm. I still wake at three, and I still occasionally "
        "lie there doing sums. But I no longer reach for my phone or curse the dark, and on a good night I let my "
        "thoughts wander wherever they please, which is, I suspect, much what my great-great-grandparents did. "
        "Whether that amounts to progress or regression, I am happy to leave undecided.",
    ],
    "lex": ["in the dead of night", "a creeping conviction", "a stern regime", "sleep in two instalments",
            "a spell of wakefulness", "fret about", "turn sth over (in one's mind)", "surface (from a dream)",
            "a hunch", "convergence", "not always in the best of company", "charge handsomely", "muddled",
            "lie there doing sums", "in the small hours", "curse the dark"],
    "items": [
        {"n": 31, "type": "Implicación", "para": [1],
         "stem": "In the first paragraph, the writer admits to having",
         "options": ["assumed without question that waking in the night was a disorder.",
                     "kept quiet about a problem that is in fact widely shared.",
                     "relied on pills and apps to get back to sleep.",
                     "become resigned to waking in the night."],
         "key": "A",
         "own": "Hasta hace poco, el autor daba por hecho que despertarse de madrugada era una avería que había que "
                "arreglar; nunca se le había ocurrido otra cosa.",
         "why": "{{For most of my adult life}}, despertarse a las tres {{has felt like a small emergency}}, y la "
                "última frase revela la suposición que el autor nunca había puesto en duda: {{It had simply never "
                "occurred to me that it might once have been regarded as nothing of the sort}}. [[Nothing of the "
                "sort]] remite a {{a malfunction}}: compartía la idea general sin cuestionarla. [[Without "
                "question]] parafrasea [[never occurred to me]], y [[disorder]], [[malfunction]] (§6.1).",
         "theory": ["3.2", "6.1"],
         "distractors": {
             "B": {"kinds": ["7.7", "7.1"],
                   "why": "Recoge {{will be familiar to many readers}} (el problema es común), pero el autor no "
                          "dice en ninguna línea que lo haya ocultado: lo cuenta con toda naturalidad."},
             "C": {"kinds": ["7.1", "7.7"],
                   "why": "{{pills, apps or a stern regime of ‘sleep hygiene’}} son los remedios que se suelen "
                          "aplicar ({{is generally treated as a malfunction}}), no algo que el autor diga haber "
                          "usado."},
             "D": {"kinds": ["7.5"],
                   "why": "Lo contradice el tono de todo el párrafo: para el autor era {{a small emergency}}, con "
                          "{{the hurried calculation}} y {{the creeping conviction that the coming day is already "
                          "ruined}}. Eso es alarma, no resignación."},
         }},
        {"n": 32, "type": "Detalle", "para": [2],
         "stem": "According to the second paragraph, what led Ekirch to conclude that sleeping in two parts had "
                 "once been normal?",
         "options": ["the frequency with which the phrase ‘first sleep’ appeared in legal records",
                     "the accounts witnesses gave of what they had done during the night",
                     "the fact that the phrase was never thought to need explaining",
                     "the detailed descriptions of the interval found in personal diaries"],
         "key": "C",
         "own": "Que nadie explicara nunca qué era el [[first sleep]]: si nadie lo explica, es que todo el mundo "
                "lo entendía.",
         "why": "El párrafo separa la expresión de lo que la hace reveladora: {{What struck Ekirch was less the "
                "phrase itself than the fact that nobody ever paused to explain it}}. La frase siguiente da el "
                "razonamiento ({{A term that needs no gloss is one that everybody already understands}}) y de ahí "
                "sale la conclusión: {{had once been entirely unremarkable}}. [[Never thought to need explaining]] "
                "parafrasea [[nobody ever paused to explain it]] sin repetir sus palabras.",
         "theory": ["2.2", "6.1"],
         "distractors": {
             "A": {"kinds": ["7.3", "7.1"],
                   "why": "Los juicios son solo una de las fuentes ({{and in the statements of witnesses in "
                          "court}}), y el texto no habla de frecuencia. Además, la frase clave le quita peso a la "
                          "expresión en sí: {{less the phrase itself than}}."},
             "B": {"kinds": ["7.1"],
                   "why": "Toma {{witnesses}} y {{seen or heard something}}, pero lo que importa de esos "
                          "testimonios es que mencionan el primer sueño {{quite casually}}, no lo que los testigos "
                          "hacían por la noche."},
             "D": {"kinds": ["7.7"],
                   "why": "Los diarios aparecen en la lista de fuentes ({{They turned up in diaries and letters}}), "
                          "pero ninguna fuente describe el intervalo con detalle; al contrario, {{nobody ever "
                          "paused to explain it}}."},
         }},
        {"n": 33, "type": "Implicación", "para": [3],
         "stem": "What is implied by the sentence ‘What they did not do, as far as the records show, was fret "
                 "about being awake’?",
         "options": ["The records give only a partial picture of how the interval was spent.",
                     "Being awake in the night was not regarded as a cause for concern.",
                     "People were kept too busy during the interval to feel anxious.",
                     "Worrying about sleep is a problem that did not exist before modern times."],
         "key": "B",
         "own": "Que despertarse a media noche no preocupaba a nadie: era lo normal.",
         "why": "Tras la lista de actividades, la frase cierra el contraste con el primer párrafo: la gente de "
                "entonces no hacía lo que hace el autor ({{fret about being awake}}). El resto del párrafo lo "
                "confirma: el intervalo era parte de la noche hasta que {{the two sleeps merge into one}}. "
                "[[Not regarded as a cause for concern]] es la paráfrasis de [[did not … fret]].",
         "theory": ["3.1", "3.2"],
         "distractors": {
             "A": {"kinds": ["7.1"],
                   "why": "Se apoya en el inciso {{as far as the records show}}, que es una cautela del autor, no "
                          "lo que la frase quiere decir. El texto no insinúa que falten datos sobre el intervalo."},
             "C": {"kinds": ["7.5"],
                   "why": "Añade una relación de causa que el texto no establece. El párrafo enumera lo que se "
                          "hacía ({{They got up to tend the fire or see to the animals}}) e incluye actividades "
                          "tranquilas ({{lay quietly turning over the dreams}}): no dice que la gente no se "
                          "preocupara por estar ocupada."},
             "D": {"kinds": ["7.3"],
                   "why": "Generaliza demasiado: el texto habla solo de no inquietarse por estar despierto en ese "
                          "intervalo, y lo matiza con {{as far as the records show}}. No dice nada de cualquier "
                          "preocupación por el sueño antes de la época moderna (§6.4)."},
         }},
        {"n": 34, "type": "Opinión y actitud", "para": [4],
         "stem": "How does the writer present Wehr’s experiment in the fourth paragraph?",
         "options": ["as more convincing than the historical evidence it seemed to support",
                     "as proof that artificial light is to blame for poor sleep today",
                     "as a deliberate attempt to test the historian’s findings",
                     "as an unexpected confirmation from a very different kind of research"],
         "key": "D",
         "own": "Como un respaldo inesperado: un laboratorio confirma lo que el historiador había deducido de los "
                "archivos, y al autor le parece muy llamativo.",
         "why": "La primera frase anuncia la sorpresa ({{Historians’ hunches seldom find support in a laboratory, "
                "but this one did}}) y la última la valora: {{The convergence of the archive and the sleep "
                "laboratory is genuinely striking}}. [[Seldom]] hace inesperada la confirmación; el contraste "
                "[[archive]] / [[laboratory]] es la [[very different kind of research]].",
         "theory": ["4.2", "6.2"],
         "distractors": {
             "A": {"kinds": ["7.7"],
                   "why": "El autor no compara la fuerza de las dos pruebas: habla de {{convergence}}, es decir, de "
                          "que coinciden, no de que una pese más que la otra."},
             "B": {"kinds": ["7.3", "7.5"],
                   "why": "El experimento muestra que con {{fourteen hours of every twenty-four in darkness}} el "
                          "sueño se divide; no demuestra que la luz artificial cause problemas de sueño hoy. "
                          "[[Proof]] y [[to blame]] van mucho más allá del texto."},
             "C": {"kinds": ["7.7"],
                   "why": "Nada indica que Wehr quisiera comprobar las conclusiones de Ekirch: el texto solo dice "
                          "que la intuición del historiador encontró apoyo ({{but this one did}}), no que el "
                          "experimento se diseñara para eso."},
         }},
        {"n": 35, "type": "Propósito", "para": [5],
         "stem": "The writer mentions that ‘our ancestors also ate badly, died young’ and relied on harmful "
                 "remedies in order to",
         "options": ["illustrate how much healthier modern habits have become.",
                     "question the idea that what was once usual must be good for us.",
                     "explain why the practice of two sleeps eventually died out.",
                     "ridicule the customers of the sleep industry for their credulity."],
         "key": "B",
         "own": "Para mostrar que «antes se hacía así» no significa «es lo mejor»: también hacían cosas que nadie "
                "querría imitar.",
         "why": "El ejemplo apoya la frase que lo introduce: {{That people once slept in a particular way tells "
                "us how they lived, not how we ought to}}. Es la razón por la que el autor llama al razonamiento "
                "de la industria {{seductive and, I think, muddled}}: lo antiguo no es bueno por ser antiguo. "
                "[[Question the idea]] recoge la función del fragmento (§5.1).",
         "theory": ["5.1", "5.2"],
         "distractors": {
             "A": {"kinds": ["7.2"],
                   "why": "Se deduce que hoy vivimos mejor, pero esa no es la función de la frase: el autor no "
                          "compara hábitos de salud, sino que desmonta el argumento de que lo de entonces era "
                          "mejor ({{not how we ought to}})."},
             "C": {"kinds": ["7.8"],
                   "why": "Por qué desapareció el doble sueño se explica en el tercer párrafo: {{as artificial "
                          "lighting spread and bedtimes drifted later}}. Este pasaje no trata de eso."},
             "D": {"kinds": ["7.4", "7.3"],
                   "why": "La ironía del párrafo apunta a la industria y a su razonamiento ({{The reasoning behind "
                          "all this is seductive and, I think, muddled}}), no a sus clientes, de los que el texto "
                          "no dice nada; y [[ridicule]] exagera el tono de [[muddled]]."},
         }},
        {"n": 36, "type": "Global", "para": "global",
         "stem": "What does the writer conclude about the history of segmented sleep?",
         "options": ["It offers a pattern of sleep that many people today would do well to adopt.",
                     "It is of limited interest because the evidence for it is uncertain.",
                     "It can ease the distress of waking at night even if it changes nothing physically.",
                     "It shows that modern insomnia is caused by the habits of industrial societies."],
         "key": "C",
         "own": "Que no sirve como receta para dormir de otra manera, pero quita angustia: cambia cómo vivimos el "
                "despertar, no el cuerpo.",
         "why": "El autor sitúa el valor de la historia lejos de la industria del bienestar ({{its real value "
                "lies somewhere the wellness industry has little reason to look}}): saber que el despertar era "
                "normal {{does nothing to change the body}}, pero {{It can, however, change what we make of it}}. "
                "El último párrafo lo confirma con su caso: no ha recuperado ningún ritmo ({{I still wake at "
                "three}}), pero ya no se angustia ({{I no longer reach for my phone or curse the dark}}).",
         "theory": ["5.4", "4.3"],
         "distractors": {
             "A": {"kinds": ["7.4"],
                   "why": "Es la idea de la industria del bienestar ({{by recovering the rhythm of our ancestors "
                          "we might recover their supposed serenity too}}), que el autor rechaza; él mismo dice "
                          "{{I have not, I should add, rediscovered some lost rhythm}}."},
             "B": {"kinds": ["7.6"],
                   "why": "La mitad sobre las pruebas tiene apoyo ({{Nor is the evidence quite as tidy as the "
                          "marketing suggests}}), pero el autor no le resta interés a la historia: {{I would not "
                          "want to dismiss the history altogether}}, y el paralelo con el laboratorio le parece "
                          "{{genuinely striking}}."},
             "D": {"kinds": ["7.5", "7.7"],
                   "why": "El texto relaciona la luz artificial con la desaparición del doble sueño ({{as "
                          "artificial lighting spread}}), no con el insomnio actual. Lo que, según el autor, "
                          "empeora el despertar nocturno es {{the panic that follows it}}."},
         }},
    ],
}

# ---------- Part 6 · Gapped text ----------
P6 = {
    "intro": "an extract from a magazine article about bird ringing",
    "title": "A ring for every traveller",
    "standfirst": "Our writer spends an autumn morning with the volunteers of a coastal bird observatory and comes "
                  "away looking at small birds rather differently.",
    "text": [
        "It was still dark when I pulled into the car park behind the dunes, and the only sound was the sea. The "
        "observatory turned out to be a low brick building that had once housed the coastguard. "
        "Inside, a gas heater was hissing, a kettle was coming to the boil and four people in "
        "layers of fleece were pulling on waterproofs with the unhurried air of those who have done this hundreds "
        "of times. The wind had dropped overnight, which, I was told, was exactly what everyone had been hoping for.",
        37,
        "We set off in single file along a track through the scrub, Darby leading with a head torch that she "
        "switched off as soon as the sky began to pale. The nets, ten in all, had been put up the previous evening "
        "and furled overnight, and each now had to be opened, a fiddly business of unhooking loops and adjusting "
        "guy ropes. By the time the last was ready, it was light enough to make out birds moving in the bushes, "
        "and the first round of checks began.",
        38,
        "Back in the ringing room, the bags were hung in a row on hooks along one wall, each of them twitching "
        "faintly. What followed had the brisk precision of a production line. Each bird was taken out, identified "
        "and, where its plumage allowed, aged and sexed. Its wing was laid flat along a small steel rule and "
        "measured to the nearest millimetre; then it was slipped head first into a plastic tube on a set of "
        "electronic scales and weighed. A volunteer at the desk wrote everything down in a ledger.",
        39,
        "That number is the whole point of the exercise. A ringed bird that is never encountered again tells "
        "researchers almost nothing, and the overwhelming majority are never encountered again. Every year, "
        "however, a small fraction are caught by another ringer or found dead by a member of the public, and each "
        "of those encounters is reported to the British Trust for Ornithology, which runs the national scheme. "
        "Pieced together over decades, the reports show where birds go, how long they live and, increasingly, "
        "which species are quietly disappearing.",
        40,
        "Darby’s own favourite is altogether more modest. Pinned above the desk is a letter, yellowing now, from "
        "a man in western France who found one of the observatory’s blackcaps sheltering in his garden one October "
        "and sent in the number on its ring, with an apology for his English. ‘It found its own way there, at "
        "night, without a map,’ she said. ‘And a complete stranger took the trouble to write. Both of those things "
        "still amaze me.’",
        41,
        "Then, a little after nine, everything changed. Goldcrests began to come in off the sea in their dozens, "
        "so exhausted by the crossing that some dropped into the first bushes they reached, and the nets were "
        "soon full of them. Britain’s smallest bird, a goldcrest weighs about as much as a "
        "twenty-pence coin, and many of these had probably left Scandinavia the night before. Darby ringed "
        "one in front of me, placed it in my palm and went to fetch more bags. Through its feathers I could feel "
        "a heartbeat so rapid that it was less a beat than a hum.",
        42,
        "The last bird of the morning turned out to be the most remarkable. A blackbird came out of the final net "
        "already wearing a ring, and when its number was checked against the ledger, it proved to have been ringed "
        "here as a nestling seven summers before. In all that time nobody had set eyes on it, although it had "
        "presumably never strayed far from the observatory. ‘Seven years,’ Darby said, writing it up. "
        "‘Not bad for a bird most people wouldn’t look at twice.’",
        43,
        "If that sounds dispiriting, it did not feel so as I walked back past the furled nets. I could "
        "no longer look at a bush full of small brown birds and see only that. Each of them, ringed or not, was a "
        "traveller with a history of its own, most of which nobody would ever know. That, I suspect, is what brings "
        "the ringers out before dawn: not the rare species or the far-flung recovery, but the chance of learning, "
        "now and then, where one of them has been.",
    ],
    "paragraphs": {
        "A": "I was to release it, she had told me, simply by opening my hand beside the door. For a second or two "
             "the bird sat there as if weighing up its options; then it was gone, a scrap of olive green heading for "
             "the pines. The rush lasted until almost eleven, when a freshening breeze set the mesh billowing and the "
             "nets were closed one by one.",
        "B": "In the third net hung a robin, hopelessly entangled, or so it seemed to me. Darby had it free in well "
             "under a minute, easing the mesh back over each wing in the reverse of the order in which the bird had "
             "flown into it and talking to it quietly throughout. Then it went, head first, into a small cotton "
             "bag, the first of a dozen we carried back.",
        "C": "Not every encounter, though, requires a second capture. Larger birds, gulls and waders in particular, "
             "are often fitted with coloured plastic rings as well as a metal one, and these can be read through a "
             "telescope from the far side of an estuary, so that a single individual may be reported dozens of "
             "times without ever being handled again.",
        "D": "Some of the most celebrated of those reports have answered questions centuries old. It was a single "
             "swallow, ringed in England and found in South Africa more than a hundred years ago, that settled where "
             "British swallows spend the winter, a puzzle for naturalists since the days when a few of them believed "
             "the birds slept through it at the bottom of ponds.",
        "E": "The reason, explained Helen Darby, who has run the ringing programme here for the best part of twenty "
             "years, is that a net is useless in a breeze. Moving mesh is visible mesh, and birds simply fly round "
             "it. On a still morning, by contrast, the fine black netting hangs slack and is almost impossible to see "
             "against the bushes.",
        "F": "That entry, pencilled into a ledger that already ran to several volumes, seemed to me to sum up the "
             "whole enterprise. I had arrived thinking of ringing as bird-watching with equipment. I left thinking of "
             "it as a kind of bookkeeping, slow, unglamorous and cumulative, in which the entries that matter may not "
             "be read for years, and then often by somebody else entirely.",
        "G": "None of these figures would mean much without the ring, fitted before anything else. It is a "
             "narrow band of soft metal, stamped with a unique number and an "
             "address to write to, and it is closed round the leg with special pliers, loose enough to turn "
             "freely but too small to slip over the foot. On a robin it looks rather like a wedding ring on a child’s "
             "finger.",
        "H": "Amazement, I soon discovered, is rationed. The second round produced nothing at all, the third a "
             "solitary wren, and by half past eight I had lost most of the feeling in my fingers. The ringers seemed "
             "not to notice. Every half hour, whatever the nets were likely to hold, somebody set off to walk the "
             "line again.",
    },
    "lex": ["furl / furled nets", "guy ropes", "a fiddly business", "piece sth together", "far-flung", "set eyes on", "take the trouble to", "the whole point of", "in single file", "with the unhurried air of", "brisk precision", "unglamorous", "cumulative", "dispiriting", "be rationed (fig.)", "a scrap of (colour)", "billow", "stray far from"],
    "items": [
        {"n": 37, "key": "E", "theory": ["4.1", "3.4"],
         "before": "El párrafo anterior deja algo sin explicar: el viento ha amainado, {{which, I was told, was "
                   "exactly what everyone had been hoping for}}. E empieza dando la explicación con un sustantivo "
                   "que la anuncia: {{The reason, explained Helen Darby}}, y la razón es justo esa calma: "
                   "{{a net is useless in a breeze}}.",
         "after": "E presenta a Darby con nombre completo y cargo ({{Helen Darby, who has run the ringing programme "
                  "here}}), y el párrafo siguiente ya la nombra solo por el apellido: {{Darby leading with a head "
                  "torch}} (§3.4). Además, E habla de las redes en general ({{the fine black netting}}) y el "
                  "párrafo siguiente pasa a las de esa mañana: {{The nets, ten in all}}."},
        {"n": 38, "key": "B", "theory": ["3.1", "4.1"],
         "before": "El párrafo anterior termina cuando empieza la primera revisión de las redes: {{the first round "
                   "of checks began}}. B cuenta lo que encontraron en ella: {{In the third net hung a robin}}.",
         "after": "B termina con el pájaro dentro de una bolsa ({{into a small cotton bag, the first of a dozen we "
                  "carried back}}), y el párrafo siguiente presupone esas bolsas y la vuelta a la caseta: "
                  "{{Back in the ringing room, the bags were hung in a row}}. Ningún otro párrafo menciona "
                  "las bolsas antes de ese punto.",
         "trap": {"letter": "H",
                  "why": "{{The second round produced nothing at all}} parece seguir a {{the first round of checks "
                         "began}}, pero se salta la primera ronda sin contarla, {{Amazement, I soon discovered, is "
                         "rationed}} no tiene ningún asombro anterior que recoger y el párrafo siguiente contradice a H: "
                         "tras {{nothing at all}} y {{a solitary wren}} no puede haber una fila de bolsas ({{the bags "
                         "were hung in a row}})."}},
        {"n": 39, "key": "G", "theory": ["4.1", "3.3"],
         "before": "El párrafo anterior enumera los datos que se toman de cada ave: la longitud del ala, el peso "
                   "y todo lo que se anota ({{A volunteer at the desk wrote everything down in a ledger}}). G "
                   "los recoge con un sustantivo resumen y un demostrativo: {{None of these figures}} (§4.4).",
         "after": "G describe la anilla y lo que lleva grabado: {{stamped with a unique number and an address to "
                  "write to}}. El párrafo siguiente retoma ese número con un demostrativo: {{That number is the "
                  "whole point of the exercise}}. G además pasa al presente ({{It is a narrow band of soft metal}}), "
                  "el plano de la explicación que sigue (§3.3).",
         "trap": {"letter": "F",
                  "why": "{{That entry, pencilled into a ledger}} parece recoger {{A volunteer at the desk wrote "
                         "everything down in a ledger}}, pero F cierra la visita ({{I left thinking of it as a kind of "
                         "bookkeeping}}) cuando la mañana acaba de empezar, y no menciona ningún número para "
                         "{{That number is the whole point of the exercise}}."}},
        {"n": 40, "key": "D", "theory": ["4.1", "3.2"],
         "before": "El párrafo anterior termina con los avisos que llegan al BTO y lo que revelan: {{each of those "
                   "encounters is reported}}, {{the reports show where birds go}}. D los retoma con un demostrativo: "
                   "{{Some of the most celebrated of those reports}}.",
         "after": "D cuenta un hallazgo célebre, la golondrina {{that settled where British swallows spend the "
                  "winter}}, y el párrafo siguiente se compara con él: {{Darby’s own favourite is altogether more modest}}. Sin un "
                  "caso famoso delante, [[favourite]] no tiene a qué referirse y [[more modest]] no tiene con qué "
                  "compararse (§4.1, comparativos).",
         "trap": {"letter": "C",
                  "why": "Encaja muy bien por detrás: {{Not every encounter, though, requires a second capture}} "
                         "recoge {{each of those encounters is reported}}. Pero falla por delante: C explica una "
                         "técnica, las anillas de colores, no un hallazgo célebre, así que {{altogether more modest}} "
                         "se queda sin término de comparación."}},
        {"n": 41, "key": "H", "theory": ["4.4", "3.3"],
         "before": "El párrafo anterior termina con la cita de Darby: {{Both of those things still amaze me}}. H "
                   "recoge el verbo con un sustantivo ({{Amazement, I soon discovered, is rationed}}) y vuelve del "
                   "comentario al relato de la mañana (§3.3, §4.4 nominalización).",
         "after": "H describe una mañana parada ({{The second round produced nothing at all, the third a solitary "
                  "wren}}), y el párrafo siguiente rompe esa espera: {{Then, a little after nine, everything "
                  "changed}}. La hora encaja: H llega a {{by half past eight}}.",
         "trap": {"letter": "F",
                  "why": "{{That entry}} podría parecer la carta del francés ({{sent in the number on its ring}}), "
                         "pero F cierra la visita ({{I left thinking of it as a kind of bookkeeping}}) y el párrafo "
                         "siguiente sigue la mañana ({{Then, a little after nine}}): cronología imposible."}},
        {"n": 42, "key": "A", "theory": ["4.1", "3.1"],
         "before": "El párrafo anterior deja al narrador con un reyezuelo en la mano: {{placed it in my palm and went "
                   "to fetch more bags}}. A empieza con ese pájaro ([[it]]) y con lo que Darby le había dicho que "
                   "hiciera: {{I was to release it, she had told me}}. El color confirma la especie: {{a scrap of "
                   "olive green}}.",
         "after": "A cierra la sesión ({{the nets were closed one by one}}), y el párrafo siguiente lo presupone: "
                  "{{The last bird of the morning}} solo tiene sentido si las redes ya se están recogiendo.",
         "trap": {"letter": "B",
                  "why": "Otro pájaro en una red ({{In the third net hung a robin}}) podría parecer parte de la "
                         "avalancha, pero deja sin soltar el reyezuelo que el narrador tiene en la mano y no cierra "
                         "la sesión, así que {{The last bird of the morning}} no tiene apoyo. Además, {{the first of a "
                         "dozen we carried back}} solo tiene sentido en la primera ronda."}},
        {"n": 43, "key": "F", "theory": ["4.1", "3.2"],
         "before": "El párrafo anterior termina con Darby anotando la recaptura del mirlo: {{writing it up}}. F "
                   "empieza con esa anotación: {{That entry, pencilled into a ledger}}.",
         "after": "F define el anillamiento como contabilidad lenta y poco lucida ({{slow, unglamorous and "
                  "cumulative}}, {{may not be read for years}}), y el párrafo siguiente responde a esa idea: {{If "
                  "that sounds dispiriting, it did not feel so}}. Además, F se despide ({{I left thinking}}) y el "
                  "párrafo siguiente es el camino de vuelta: {{as I walked back past the furled nets}}.",
         "trap": {"letter": "D",
                  "why": "Una anilla célebre después de una recaptura parece un buen enlace, pero {{those reports}} "
                         "no tiene antecedente: el mirlo lo han recapturado los propios anilladores, nadie lo ha "
                         "notificado. Y D es un éxito, nada que pueda resultar [[dispiriting]]: {{If that sounds "
                         "dispiriting}} se queda sin referente."}},
    ],
    "extra": {
        "letter": "C", "theory": ["5.1", "5.2"],
        "rules_out": [
            {"gaps": [37, 38, 39],
             "why": "{{Not every encounter, though}} presupone que el texto ya ha hablado de reencuentros con aves "
                    "anilladas, y hasta el párrafo de {{each of those encounters is reported}} no lo hace. Además, "
                    "C no presenta a Darby ({{Darby leading with a head torch}}), no habla de bolsas ({{the bags "
                    "were hung in a row}}) ni de ningún número ({{That number is the whole point}})."},
            {"gaps": [40],
             "why": "Encaje por un solo lado (§5.1): recoge bien {{each of those encounters is reported}}, pero "
                    "{{Darby’s own favourite is altogether more modest}} necesita delante un hallazgo célebre con el "
                    "que compararse, y C solo describe las anillas de colores."},
            {"gaps": [41, 42],
             "why": "C es una explicación en presente sin ningún suceso de la mañana: no prepara la espera que rompe "
                    "{{Then, a little after nine, everything changed}}, ni suelta el reyezuelo que el narrador tiene "
                    "en la mano ni cierra la sesión que presupone {{The last bird of the morning}}."},
            {"gaps": [43],
             "why": "Por detrás podría seguir a la recaptura del mirlo, pero no recoge {{writing it up}} y no hay "
                    "nada desalentador en un método que multiplica los avisos: {{If that sounds dispiriting}} se "
                    "queda sin referente."},
        ],
    },
}

# ---------- Part 7 · Multiple matching ----------
P7 = {
    "intro": "an article in which four people describe spending a winter at a research station in Antarctica",
    "units": "people",
    "lead": "Which person",
    "title": "The longest night",
    "standfirst": "Four people who stayed on through the Antarctic winter look back on the experience.",
    "compound": 3,
    "sections": [
        {"label": "A", "name": "Ruth Calder, glaciologist",
         "text": "I went south to measure how quickly the ice shelf beneath the station was moving, and I assumed "
                 "that the winter, with no fieldwork possible, would be the most productive period of my career. "
                 "I had a list of papers I meant to finish and a stack of books I had been saving for years. In "
                 "the event, I barely opened them. Something about the endless dark made sustained thought almost "
                 "impossible: I would sit down after breakfast with every intention of writing and find, at "
                 "lunchtime, that I had managed a paragraph. Before we left, a psychologist had spent an afternoon "
                 "warning us that winterers often lose the capacity to concentrate, and urging us to set ourselves "
                 "modest daily goals. I remember thinking it faintly patronising – we were, after all, a group of "
                 "reasonably accomplished adults. By June I had pinned her list of suggestions above my desk. It "
                 "was a humbling admission, but the small goals worked, and by the time the sun came back I had, "
                 "somewhat to my own surprise, finished the one paper that really mattered."},
        {"label": "B", "name": "Owen Prys, chef",
         "text": "I saw the advertisement on a Sunday evening, filled in the form before I could talk myself out "
                 "of it and had forgotten all about it by the time they called me for an interview. Morale, I was "
                 "told there, would be as much my responsibility as the menu, and I soon understood why. Once the "
                 "last aircraft had gone, there was nothing fresh to be had until the spring, so I spent the winter "
                 "coaxing variety out of tins, flour and a freezer the size of a garage. Food became our calendar: "
                 "Friday was curry, Sunday was a roast, and Midwinter’s Day was a feast we planned for weeks. I "
                 "learnt to read the base from the serving hatch, too. When someone started skipping breakfast or "
                 "pushing food round the plate, it was usually the first sign that they were struggling, often "
                 "long before they admitted it to themselves. Not that we were saints. The worst row of the winter "
                 "began over who had finished the last jar of peanut butter, and for a fortnight two grown men "
                 "refused to sit at the same table."},
        {"label": "C", "name": "Leila Haddad, doctor",
         "text": "As the only doctor on the station, I spent the months before departure acquiring skills I had "
                 "never expected to need, from filling teeth to running an operating theatre with a mechanic as my "
                 "assistant. What kept me awake in those months was the thought of a burst appendix or a serious "
                 "fall in the depths of winter, when no aircraft could reach us. In the end, the gravest thing I "
                 "treated was a broken wrist. What took up most of my time turned out to be something nobody had mentioned on any "
                 "training course. People came to the surgery with a stiff back or a sleepless night and stayed an "
                 "hour to talk about a marriage under strain or a parent who was ill at home. I became, without "
                 "ever quite deciding to, the person everyone confided in, and I took that more seriously than any "
                 "of the medicine. It was lonely in its own way, since there was nobody I could unburden myself to "
                 "in turn. I came home with an enormous respect for counsellors and for anyone else who listens to "
                 "other people’s troubles for a living."},
        {"label": "D", "name": "Callum Reid, generator mechanic",
         "text": "I had wanted to go south since I was a boy, and I applied three times before they finally took "
                 "me. My job was to keep the generators running, because if they failed, so did everything else: "
                 "heat, water, light, the lot. A man who had done three winters told me that the cold would be the "
                 "least of my worries, and he was right; at minus forty you simply dress for it. What nobody could "
                 "prepare me for was coming back. The first time I walked into a supermarket I had to leave after "
                 "five minutes – the noise, the smells, thirty kinds of bread. I had spent eight months in a place "
                 "where every job had an obvious purpose, and now I sit in meetings about meetings and find myself "
                 "far less patient with them than I used to be. If I have one regret, it is that I spent so many "
                 "winter evenings tinkering in the workshop. The aurora was out on many clear nights, and I "
                 "watched it far less often than I should have."},
    ],
    "lex": ["talk oneself out of sth", "coax sth out of sth", "serving hatch", "push food round the plate",
            "the lot", "tinker (in the workshop)", "in the depths of winter"],
    "items": [
        {"n": 44, "prompt": "had worries before leaving that proved to be groundless?", "key": "C",
         "theory": ["4.1", "3.3"],
         "elements": ["Preocupación previa: {{What kept me awake in those months was the thought of a burst "
                      "appendix or a serious fall in the depths of winter}} ([[in those months]] remite a "
                      "{{the months before departure}}).",
                      "Infundada: {{In the end, the gravest thing I treated was a broken wrist}}."],
         "trap": {"letter": "D", "kinds": ["7.7"],
                  "why": "Habla del frío antes de ir y de que no fue para tanto ({{at minus forty you simply "
                         "dress for it}}), pero nunca dice que le preocupara: lo que se cumple es un consejo "
                         "ajeno ({{A man who had done three winters told me that the cold would be the least of "
                         "my worries}}). El temor previo hay que suponerlo."}},
        {"n": 45, "prompt": "applied for the job on the spur of the moment?", "key": "B",
         "theory": ["3.3"],
         "elements": ["{{filled in the form before I could talk myself out of it}}; lo poco que lo pensó se "
                      "confirma con {{had forgotten all about it by the time they called me for an interview}}."],
         "trap": {"letter": "D", "kinds": ["7.5"],
                  "why": "También cuenta cómo llegó al puesto, pero es lo contrario de un impulso: un deseo de "
                         "toda la vida y varios intentos ({{I applied three times before they finally took "
                         "me}})."}},
        {"n": 46, "prompt": "found it unexpectedly difficult to focus on intellectual tasks?", "key": "A",
         "theory": ["4.1", "3.3"],
         "elements": ["Lo que esperaba: {{I assumed that the winter, with no fieldwork possible, would be the most "
                      "productive period of my career}}. Lo que pasó: {{Something about the endless dark "
                      "made sustained thought almost impossible}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "Lo que la ocupó tampoco fue lo que esperaba ({{What took up most of my time turned out to be something "
                         "nobody had mentioned on any training course}}), pero lo sorprendente es su contenido, "
                         "no que le costara concentrarse."}},
        {"n": 47, "prompt": "regrets how they spent some of their leisure time?", "key": "D",
         "theory": ["3.3", "3.4"],
         "elements": ["{{If I have one regret, it is that I spent so many winter evenings tinkering in the "
                      "workshop}}; lo que se perdió: {{I watched it far less often than I should have}}."],
         "trap": {"letter": "A", "kinds": ["7.7"],
                  "why": "Tampoco aprovechó el tiempo como pensaba ({{In the event, I barely opened them}}), "
                         "pero no expresa ningún pesar: lo explica por la oscuridad y lo que cuenta después "
                         "es cómo lo resolvió."}},
        {"n": 48, "prompt": "initially dismissed guidance that turned out to be sound?", "key": "A",
         "theory": ["4.1", "3.4"],
         "elements": ["Consejo recibido y desdeñado: {{I remember thinking it faintly patronising}}.",
                      "Acertado al final: {{By June I had pinned her list of suggestions above my desk}}, "
                      "y {{the small goals worked}}."],
         "trap": {"letter": "D", "kinds": ["7.6"],
                  "why": "Recibió un consejo que resultó cierto ({{and he was right}}), pero en ningún momento "
                         "lo despreció: falta el primer elemento."}},
        {"n": 49, "prompt": "took on a supportive role that was not part of their job?", "key": "C",
         "theory": ["3.3", "4.3"],
         "elements": ["{{I became, without ever quite deciding to, the person everyone confided in}}; que no "
                      "era parte del puesto lo dice antes: {{something nobody had mentioned on any training "
                      "course}}."],
         "trap": {"letter": "B", "kinds": ["7.6"],
                  "why": "También cuida del ánimo del grupo, pero como parte explícita de su trabajo: "
                         "{{Morale, I was told there, would be as much my responsibility as the menu}}."}},
        {"n": 50, "prompt": "learnt to detect signs of distress in others’ behaviour at mealtimes?",
         "key": "B", "theory": ["3.3"],
         "elements": ["{{When someone started skipping breakfast or pushing food round the plate, it was "
                      "usually the first sign that they were struggling}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "También descubre los problemas de los demás, pero en la consulta y porque se los "
                         "cuentan ({{stayed an hour to talk about a marriage under strain}}), no observando "
                         "cómo comen."}},
        {"n": 51, "prompt": "felt overwhelmed by ordinary surroundings on returning home?", "key": "D",
         "theory": ["3.3"],
         "elements": ["{{The first time I walked into a supermarket I had to leave after five minutes}}: "
                      "{{the noise, the smells, thirty kinds of bread}}."],
         "trap": {"letter": "C", "kinds": ["7.2"],
                  "why": "También habla de la vuelta ({{I came home with an enormous respect for counsellors}}), pero de lo que aprendió, no de un choque con el entorno."}},
        {"n": 52, "prompt": "recalls a petty disagreement that got out of hand?", "key": "B",
         "theory": ["3.3", "4.1"],
         "elements": ["{{The worst row of the winter began over who had finished the last jar of peanut "
                      "butter}}, y fue a más: {{for a fortnight two grown men refused to sit at the same "
                      "table}}."],
         "trap": {"letter": "C", "kinds": ["7.1"],
                  "why": "Aparecen conflictos ({{a marriage under strain}}), pero son problemas personales que "
                         "los demás le cuentan, ni triviales ni entre miembros de la base."}},
        {"n": 53, "prompt": "has less patience with routine aspects of work since coming back?", "key": "D",
         "theory": ["4.1", "3.4"],
         "elements": ["El contraste que lo explica: {{every job had an obvious purpose}}.",
                      "Menos paciencia ahora: {{now I sit in meetings about meetings and find myself far less "
                      "patient with them than I used to be}}."],
         "trap": {"letter": "C", "kinds": ["7.6"],
                  "why": "La experiencia también cambió su mirada sobre el trabajo, pero en sentido contrario "
                         "y sobre el de otros: {{I came home with an enormous respect for counsellors and for anyone else who listens "
                         "to other people’s troubles for a living}}."}},
    ],
}
