# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"
# Aqui declaro todas las escenas
image bg fondo1 = "fondo1.jpg"
image bg fondo2 = "fondo2.jpg"
image bg fondo3 = "fondo3.jpg"
image bg fondo3_0 = "fondo3_0.jpg"
image bg fondo4 = "fondo4.jpg"
image bg fondo5 = "fondo5.jpg"
image bg ahorcado = "ahorcado.jpg"
image bg puerta = "puerta.jpg"
image bg sangre1 = "sangre1.jpg"
image bg sangre2 = "sangre2.jpg"
image bg sangre3 = "sangre3.jpg"
image bg sangre4 = "sangre4.jpg"
image bg blur = "blur.jpg"

# Aqui declaro todos los personajes
image muto normal = "muto_normal.png"
image muto irritated = "muto_irritated.png"
image shopkeep happy = "shopkeep_happy.png"
image shopkeep thinking = "shopkeep_thinking.png"
image shopkeep surprised = "shopkeep_surprised.png"
image shopkeep neutral = "shopkeep_neutral.png"
image nomiya dreamy = "nomiya_dreamy.png"
image nomiya frown = "nomiya_frown.png"
image nomiya talk = "nomiya_talk.png"
image nomiya talktongue = "nomiya_talktongue.png"
image nomiya veryhappy = "nomiya_veryhappy.png"
image kenji neutral = "kenji_neutral.png"
image yuuko cry = "yuuko_cry.png"
image yuuko smile = "yuuko_smile.png"

# Aqui uso una playlist para tener canciones durante el juego
play music [ Breathlessly.mp3, Cold_Iron.mp3,  Friendship.mp3, Innocence.mp3, Painful_History.mp3, Shadow_of_the_Truth.mp3, Wiosna.mp3 ] fadeout 1.0 fadein 1.0

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
# Aqui estan los personajes
define h = Character('Hombre', color="#0000ff")
define m = Character('Mujer', color="#ff69b4")
define j = Character('Jefe', color="#00ff00")
define d = Character('Desconocido', color="#ff0000")


# The game starts here.
# - El juego comienza aquí.
# Esta es la primera escena en donde sale en la casa
label start:
    
    scene bg fondo1

    "Una pareja de recién casados, era muy pobre y vivía de los favores de un pueblito del interior."

    show muto normal at right

    h "Querida yo voy a salir de la casa. Voy a viajar bien lejos, buscar un empleo y trabajar hasta tener condiciones para regresar y darte una vida más cómoda y digna."

    hide muto
    show muto irritated at right

    h "No sé cuanto tiempo voy a estar lejos; sólo te pido que me esperes y mientras yo este lejos, seas fiel a mí, pues yo te seré fiel a ti."

    scene bg fondo2

    "Así, caminó muchos días a pie, hasta encontrar un hacendado que estaba necesitando de alguien para ayudarlo en su hacienda."
    "El hombre llegó y se ofreció para trabajar y fue aceptado y pidió hacer un trato con su jefe."
    
    show muto normal at right

    h "Déjeme trabajar por el tiempo que yo quiera y cuando yo encuentre que debo irme, usted me libera de mis obligaciones."
    h "Yo no quiero recibir mi salario. Le pido señor que lo coloque en una cuenta de ahorros hasta el día en que me vaya."
    h "El día que yo salga usted me dará el dinero que yo haya ganado."
    
    hide muto

    "Estando ambos de acuerdo, aquel joven trabajó durante 20 años, sin vacaciones y sin descanso."
    "20 años despues..."
    
    scene bg fondo2 with Fade(1.5, 0.5, 2.0)
    show shopkeep happy at right

    h "Patrón, yo quiero mi dinero, pues quiero regresar a mi casa."

    hide shopkeep
    show nomiya dreamy

    j "Muy bien, hicimos un pacto y voy a cumplirlo. Sólo que antes quiero hacerte una propuesta."
    
    show nomiya frown
    
    j "Yo te doy tu dinero y tú te vas, o te doy tres consejos y no te doy el dinero y te vas."
    j "Vete a tu cuarto, piénsalo y después me das la respuesta."
    
    hide nomiya
    scene bg fondo2 with Fade(1.5, 0.5, 2.0)

    "Dos dias despues..."

    show shopkeep thinking at right

# Esta es la primera opcion o eleccion que el usuario hace
    menu:
        
        "Quiero los tres consejos.":
            jump tres_consejos

        "Quiero el dinero.":
            jump dinero
            

label tres_consejos:

    hide shopkeep
    show nomiya talk

    j "El primer consejo: NUNCA TOMES ATAJOS EN TU VIDA. Caminos más cortos y desconocidos te pueden costar la vida."
    
    show nomiya talktongue

    j "El segundo consejo: NUNCA SEAS CURIOSO DE AQUELLO QUE REPRESENTE EL MAL, pues la curiosidad por el mal puede ser fatal."
    
    show nomiya veryhappy

    j "El tercer consejo: NUNCA TOMES DECISIONES EN MOMENTOS DE ODIO Y DOLOR, pues puedes arrepentirte demasiado tarde."
    
    show nomiya dreamy

    j "AQUÍ TIENES TRES PANES: dos para comer durante el viaje y el tercero es para comer con tu esposa, cuando llegues a tu casa."
    
    hide nomiya
    scene bg fondo3_0
    
    "El hombre, entonces, siguió su camino de vuelta."
    
    "Después del primer día de viaje, encontró una persona que lo saludó."
    
    show kenji neutral at left

    d "Hacia donde vas?"

    hide kenji
    show shopkeep surprised at right

    h "Voy hacia un camino muy distante que queda a más de veinte  días de caminata por esta carretera."

    hide shopkeep
    show kenji neutral at left

    d "Hombre, este camino es muy largo."
    d "Yo conozco un atajo con el cual llegarás en pocos días."
    
    hide kenji
    scene bg fondo3

    "El joven, contento, comenzó a caminar por el atajo, cuando se acordó del primer consejo."

    scene bg blur with dissolve
    show nomiya talk
    j "El primer consejo: NUNCA TOMES ATAJOS EN TU VIDA. Caminos más cortos y desconocidos te pueden costar la vida."
    hide nomiya
    scene bg fondo3 with dissolve
    show shopkeep thinking at right
    
    "Y luego decidio..."
# Segunda eleccion
    menu:
        "...volver al camino normal":
            jump camino_normal
            
        "...seguir por ese camino":
            jump seguir_camino

label camino_normal:

    scene bg fondo3_0

    "El hombre regresa al camino original y continua..."
    
    scene bg fondo4
    "Después de algunos días de viaje, y cansado al extremo, encontró una pensión a la vera de la carretera, donde poder hospedarse."
    "Pagó la tarifa por día y, después de tomar un baño, se acostó a dormir."
    "De madrugada se levantó asustado con un grito aterrador. Se levantó de un salto y se dirigió hasta la puerta para ir a donde escuchó el grito."
    "Cuando estaba abriendo la puerta, se acordó del segundo consejo."

    scene bg blur with dissolve
    show nomiya talktongue
    j "El segundo consejo: NUNCA SEAS CURIOSO DE AQUELLO QUE REPRESENTE EL MAL, pues la curiosidad por el mal puede ser fatal."
    hide nomiya
    scene bg fondo4 with dissolve
    show shopkeep thinking at right

    "Entonces decidio..."
# Tercera eleccion
    menu:
        "...salir y ver el chambre del grito":
            jump chambre_grito
            
        "...regresar a dormir":
            jump ignorar_grito
            

label ignorar_grito:
    "El hombre regresa a dormir."
    "Cuando amanece el hombre regresa a su larga jornada, ansioso por llegar a su casa."
    
    scene bg fondo5
    
    "Después de muchos días y noches de caminata, ya al atardecer, vio entre los árboles humo saliendo de la chimenea de su pequeña casa."
    "Caminó y vio entre arbustos la silueta de su esposa. Estaba anocheciendo, pero alcanzó a ver que ella no estaba sola."
    "Anduvo un poco más y vio que ella tenía sobre su regazo, un hombre al que estaba acariciando los cabellos."
    "Cuando vio aquella escena, su corazón se llenó de odio y amargura y decidió correr al encuentro de los dos y matarlos sin piedad."
    "Luego recordo el tercer consejo..."

    scene bg blur with dissolve
    show nomiya veryhappy
    j "El tercer consejo: NUNCA TOMES DECISIONES EN MOMENTOS DE ODIO Y DOLOR, pues puedes arrepentirte demasiado tarde."
    hide nomiya
    scene bg fondo5 with dissolve
    show shopkeep thinking at right

    "Y decidio..."
# Ultima eleccion
    menu:
        "...calmarse y confrontarla en la mañana cuando este tranquilo":
            jump tranquilo
            
        "...seguir con el plan, pero antes bofetearla":
            jump no_tranquilo
        

label tranquilo:

    hide shopkeep

    "El hombre decidió dormir ahí mismo aquella noche y al día siguiente tomar una decisión."
    "Al amanecer, ya con la cabeza fría"

    show shopkeep surprised at right
    h "NO VOY A MATAR A MI ESPOSA. Voy a volver con mi patrón y a pedirle que me acepte de vuelta, sólo que antes, quiero decirle a mi esposa que siempre le fui fiel."  
    hide shopkeep

    scene bg puerta
    
    "Se dirigió a la puerta de la casa y tocó. Cuando la esposa le abrió la puerta y lo reconoció, se colgó de su cuello y lo abrazó afectuosamente."
    "Él trató de quitársela de encima, pero no lo consiguió. Entonces, con lágrimas en los ojos..."

    show shopkeep neutral at right
    h "Yo te fui fiel y tu me traicionaste"
    hide shopkeep

    show yuuko cry at left
    m "¿Cómo? Yo nunca te traicioné. Te esperé durante veinte años"
    hide yuuko

    show shopkeep surprised at right
    h "¿Y quién era ese hombre que acariciabas ayer por la tarde?"
    hide shopkeep

    show yuuko smile at left
    m "AQUEL HOMBRE ES NUESTRO HIJO. Cuando te fuiste, descubrí que estaba embarazada. Hoy él tiene veinte años de edad."
    hide yuuko

    "Entonces, el marido entró y abrazó a su hijo y les contó toda su historia, mientras su esposa preparaba la cena. Se sentaron a comer el último pan juntos. DESPUÉS DE LA ORACIÓN DE AGRADECIMIENTO, CON LÁGRIMAS DE EMOCIÓN, él partió el pan y al abrirlo, se encontró todo su dinero: el pago de sus veinte años  de dedicación."
    
    return
    
#consecuencia de ultima eleccion
label no_tranquilo:

    scene bg sangre4
    play sound "slap.mp3"

    "El hombre entra bofetea a su mujer y mata a todos, luego mira la billetera de el hombre y se da cuenta de que tiene sus apellidos en su cedula(es su hijo!)"
    
    scene bg ahorcado
    
    "El hombre se ahorca sin pensarlo dos veces."
    

    return
    
 #consecuencia de tercera eleccion   
label chambre_grito:
    
    scene bg sangre3
    play sound "grito.mp3"
    "El hombre sale de curioso y un loco lo mata y se lo come."

    return
    
#consecuencia de segunda eleccion
label seguir_camino:
    
    scene bg sangre2
    play sound "seguir.mp3"
    "El camino llevo al hombre a una emboscada en la cual lo secuestraron y mataron."

    return
    
# consecuencia de primera eleccion
label dinero:

    scene bg sangre1
    play sound "dinero.mp3"
    "El hombre recibe el dinero y luego abarca en su camino de regreso en el cual lo asaltan, lo violan y lo matan."

    return
