# The script of the game goes in this file.

image secretaria = "secretaria.png"
image contrato = "contrato.jpg"
image hiago_oculos = "hiago_oculos.png"
image hatsuneMiku = "hatsuneMiku.png"
image ciel = "ciel.png"
image deco_beto_first = "deco_beto_first.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]", color="#e84393")
define db_unknown = Character("??", color="#3a70f5")
define db = Character("Deco Beto", color="#3a70f5")
define hb = Character("Hiago Bahú", color="#d63031")
define mc = Character("Mateus Calza", color="#341f97")
define ht = Character("Hatsune Miku", color="#0EEADF")

$ romance_points = 0

# The game starts here.

label start:

    stop music fadeout 3.0
    scene bg unoesc
    with Dissolve(6.0)

    "Hoje é o seu primeiro dia de aula na sua nova faculdade."
    "O ambiente no câmpus é de grande euforia e movimento de pessoas novas se conhecendo."
    "No caminho várias pessoas te abordam e se apresentam a você em busca de fazer novas amizades."
    "Entretanto alguns documentos não estão certos, é necessário ir até a secretaria assinar alguns papeis."

    scene bg secretaria
    with fade

    "A sala te dá uma sensação de déjà vu. Seu design parece chique porém presente em outro jogo de mesma franquia."   

    show secretaria
    with fade
    
    "Moça da Secretaria" "Olá, você é a aluna nova certo?"

    menu: 

        "Oi, sim sou a aluna nova.":
            jump escolha_nome
    
    return

label escolha_nome:
        
    "Moça da Secretaria" "Seja muito bem vinda! Preciso que você assine esses papeis."
    show contrato

    python:

        povname = renpy.input("Assine os papeis com o seu nome:")
        povname = povname.strip()

    hide contrato

    "Moça da Secretaria" "Obrigada e BEM VINDA A MAIOR FACULDADE DO OESTE DE SANTA CATARINA CAMPUS VIDEIRA."

    hide secretaria

    jump primeira_aula

    return

label primeira_aula:

    show secretaria

    "Você escuta algo"
    play sound "audio/siren.mp3"
    "..."
    pov "Poxa já tá na hora de ir pra aula. Sabe me dizer onde é a sala hoje?"

    "Moça da Secretaria" "Claro, eu te acompanho até lá."

    scene bg corredor
    with fade

    "Moça da Secretaria" "É aqui, vai ter uma dinâmica entre os cursos, qualquer coisa que precisar é só aparecer na secretária."

    hide secretaria

    scene bg decogroup
    with fade

    "Você entra na sala e vê diversos grupos formados discutindo temas."
    "Um menino em especial lhe chama atenção em um dos grupos."
    "Ele parece com muito sono e entediado forçando prestar atenção no que o velho fala e você se identifica com ele."

    pov "E a voltinha no cabelo dele hein. Muito estilo."

    scene bg black
    with fade

    play sound "audio/siren.mp3"

    "Após a apresentação, aulas normais acontecem e em seguida você vai embora para casa."
    "Nova na cidade, você busca opções de bares para descontrair e conhecer pessoas."

    jump bola_intro

    return

label bola_intro:
    
    scene bg bola7_frente
    with fade

    play music "audio/theNightIsCalling.mp3" fadeout 1.0 fadein 1.0

    "Devido à grande falta de boas opções em uma cidade de fim de mundo como Joaçaba, onde está se hospedando, você acaba indo para um dos poucos locais de jovens da cidade: O bar Bola7."
    "Há uma grande quantidade de pessoas na rua. Você resolve entrar para pegar algumas bebidas e aproveitar o show."

    scene bg bola7_dentro
    with fade

    "Está acontecendo o show da Hatsune Miko, uma artista local da cidade."

    show hatsuneMiku

    "Você vê um garoto loiro esquisito empolgado com o show. Outras pessoas chegam pra lhe cumprimentar e conversar contigo."
    
    hide hatsuneMiku
    with fade

    show ciel
    with fade

    "??" "Ei você é nova aqui né?"
    "Ciel" "Eu me chamo Ciel oiiiiiiiiii!!! Como que é teu nome???"

    "Você ouve alguém gritar o nome de Ciel de fora bem alto."

    "Ciel" "Ai amiga alguém tá me chamando já volto aí mas aproveita a noite bastante beijo!!"

    hide ciel
    with fade

    "Você continua assistindo ao show e bebendo, curtindo bastante o show."
    "Você bebe a noite inteira."

    scene bg black

    stop music fadeout 1.0

    "Você não se lembra muito bem o que acontece depois disso."

    jump deco_beto_rescue

    return

label deco_beto_rescue:

    "Você se levanta rapidamente e assustada."

    scene bg deco_room
    with vpunch

    pov "Ouch..."
    pov "Onde eu estou???"

    show deco_beto_first

    db_unknown "Ouch... Precisava me bater com a cabeça assim?"

    menu:

        "MEU DEUS O QUE VOCÊ FEZ COMIGO SEU CANALHA?!?!?":
            $ romance_points =+ 1
            jump deco_beto_reasoning

        "Quem é você???":
            jump deco_beto_intro

        "Credo estou tonta... o que aconteceu?":
            $ romance_points =- 1
            jump deco_beto_intro

    return

label deco_beto_reasoning:

    db_unknown "NADA SUA PIRANHA POR QUE EU FARIA ALGO COM VOCÊ??"

    menu: 

        "Imagina você desmaiando por ter bebido demais e acordando no quarto de um cara seu idiota!!":
            db_unknown "Oh... faz sentido, olha aí o precedente criminal vindo, mas calma vou te explicar o que aconteceu."

        "VAI TOMAR NO SEU CÚ!!":
            $ romance_points =+ 1
            db_unknown "Quanta agressividade..."
        
        "Eu estava inconsciente e acordei no seu quarto?":
            $ romance_points =- 1
            db_unknown "Ah... certo, antes que haja mal entendidos preciso me apresentar."

    jump deco_beto_intro

    return

label deco_beto_intro:

    db "Eu me chamo André Roberto, mais conhecido como Deco Beto muito prazer! (@deco_beto no twitter mulheres)"
    db "Você tava largada bêbada no chão da rua desmaiada então eu achei que devia te trazer pra dentro de casa descansar."
    db "Aqui é literalmente na frente do bola como você pode ver."

    "Você acaba se lembrando dele... Ele é o menino com a voltinha no cabelo!!!"

    menu:

        "Muito prazer.. eu acho?":
            jump pegando_coquinha_geladinha

        "FODASE QUEM VOCÊ É EU ESTOU INDO EMBORA!!!":
            $ romance_points =+ 2
            jump frente_ap_deco
        
        "Oi... rs":
            $ romance_points =- 1
            jump pegando_coquinha_geladinha
        
