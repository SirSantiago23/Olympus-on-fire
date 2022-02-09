from tkinter import *
import os

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

damagePoderes:dict={\
"NULO":0,\
"Lluvia acida":13000,"Tornado":13000,"Temblor":13000,"Eclipse(Oscuridad)":13000,\
"Ataque Feroz":25,"Miedo de batalla":50,"Fobia":58,"Desgracia":120,\
"Destello magico":25,"Rayos":50,"Energia flameante":58,"Luz Penetrante":120,\

"Golpe divino":20, "Persuación":45, "La esperanza como daño": 53,"Caja de pandora":135,\
"Tiro certero":27,"Agitación de los vientos":55, "Ataque canino":63,"Metamorfosis temporal":150,\
"Golpe rapido":33, "Engaño doloroso": 61, "Herida de lanza": 67, "Encanto Mortal": 160,\
"Fuego infernal":40, "Cegar y atacar": 65, "Embestida con carruaje": 73, "Destellos Finales": 180,\
"Puños divinos": 45, "Jabalina penetrante": 68, "Colmillos de Erimanto": 80, "Estrangulación": 189,\
"Lanza y escudo": 50, "Brutalidad": 75, "Transformación": 84, "Dios de la guerra": 200,\
"Ataque fugaz": 55, "Inteligencia superior": 80, "Jabalina al estomago": 89, "Desvanecimiento": 210,\
"Tridente de los mares": 60, "Epilepsia momentanea": 84, "Terremoto divino": 92, "El dios de los mares": 220,\
"Ataque con su casco": 70, "Reanimacion": 97, "Cerbero": 100, "Ira del inframundo": 240,\
"Rayo tenue": 110, "Golpe gigante": 135, "Rayos sin control": 155, "El poder del olimpo": 310
}

class Personajes():
    def __init__(self, _nombre, _id, _descripcion, _nivel, _mochila, _poderes, _desPoderes, _ruta):
        
        self.lista=[]
        self.lista.append(_nombre)
        self.lista.append(_id)
        self.lista.append(_descripcion)
        self.lista.append(_nivel)
        self.lista.append(_mochila)
        self.lista.append(_poderes)
        self.lista.append(_desPoderes)
        self.lista.append(_ruta)

    def getDatos(self, n):
        try:
            return self.lista[n-1]
        except:
            return
        
    def setDatos(self, n, var):
        try:
            self.lista[n-1]=var
        except:
            pass

#-----------------------------ZEUS--------------------------------------------

var1= "Zeus - Dios del trueno"
var2= "Zeus"
var3= """ Tambien llamado el padre 
 de los dioses y los
 hombres, es aquel que
 gobierna a los dioses del
 Olimpo como un padre.
"""
var4= 10
var5= ""
var6= {"PODER 1":"Rayo tenue",
        "PODER 2":"Golpe gigante",
        "PODER 3":"Rayos sin control",
        "PODER 4":"El poder del olimpo",
        "NULO":"NULO"
}

var7= {"PODER 1":"Usa su arma para inflingir una porcion de daño leve comparado al poder total de su arma",
        "PODER 2":"Zeus incrementa su tamaño hasta un aproximado de 23 metros para aplastar a su oponente con el pie",
        "PODER 3":"Zeus invoca una tormenta electrica que hace que caigan inumerables rayos del cielo haciendo demasiado daño a su oponente.",
        "PODER 4":"Desata todo el poder de su arma el rayo, con el cual ha matado Titanes y ha partido montañas a la mitad, para lanzarlo contra el rival haciendo muchisimo daño.",
}

var8="imagenes\\avatares\\zeus.png"

diosZeus=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------HADES--------------------------------------------

var1= "Hades - El invisible"
var2= "Hades"
var3= """ Hades es el dios del
 antiguo inframundo, es el
 hijo mayor de Cronos y
 Rea.
"""

var4= 9
var5= ""
var6= {"PODER 1":"Ataque con su casco",
        "PODER 2":"Reanimacion",
        "PODER 3":"Cerbero",
        "PODER 4":"Ira del inframundo",
        "NULO":"NULO"
}

var7= {"PODER 1":"Mediante su casco, Hades se hace invisible para apuñalar por la espalda al rival",
        "PODER 2":"Hades reanima a 5 cadaveres que atacan al rival con espadas",
        "PODER 3":"Hades invoca a su perro Cerbero para que ataque ferozmente al rival",
        "PODER 4":"Hace que su enemigo sienta la ira, miedo, frustracion, odio y todas los males del inframundo en su cabeza, por lo que es capaz de volver loco a su enemigo si no es lo suficientemente fuerte.",
}

var8="imagenes\\avatares\\hades.png"

diosHades=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------POSEIDON--------------------------------------------

var1= "Poseidon - Dios de mar"
var2= "Poseidon"
var3= """ Es el dios de los mares, 
 y de los terremotos. 
 Hermano de Zeus y Ares,
 es uno de los tres
 grandes."""

var4= 8
var5= ""
var6= {"PODER 1":"Tridente de los mares",
        "PODER 2":"Epilepsia momentanea",
        "PODER 3":"Terremoto divino",
        "PODER 4":"El dios de los mares",
        "NULO":"NULO"
}

var7= {"PODER 1":"Ataca a su enemigo sin piedad con el tridente forjado por los ciclopes.",
        "PODER 2":"Poseidon es capaz de crear en su enemigo ciertos tipos de perturbaciones mentales, haciendo que tenga un episodio de epilepsia dañandolo mentalmente",
        "PODER 3":"Genera un terremoto que abre el terreno donde esta parado su enemigo hiriendolo.",
        "PODER 4":"Poseidon hiende el suelo con su tridente, generando una montaña gigante de agua que rapidamente se convierte en una ola de gran velocidad que abalanza sobre su enemigo.",
}


var8="imagenes\\avatares\\poseidon.png"

diosPoseidon=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------ATENEA--------------------------------------------

var1= "Diosa Palas Atenea"
var2= "Atenea"
var3=""" Es la diosa de la
 Sabiduria. Fue una de las
 principales divinidades 
 del panteón griego y una 
 de los doce olímpicos.
""" 

var4= 7
var5= ""
var6= {"PODER 1":"Ataque fugaz",
        "PODER 2":"Inteligencia superior",
        "PODER 3":"Jabalina al estomago",
        "PODER 4":"Desvanecimiento",
        "NULO":"NULO"
}

var7= {"PODER 1":"Con la rapidez de una ninfa africana, ataca a su enemigo con una serie de golpes",
        "PODER 2":"Con uso de sus dotes ataca al enemigo prediciendo cada uno de sus siguientes movimientos",
        "PODER 3":"Justo como hizo con palas, clava en su enemigo la jabalina con un daño increible en el oponente",
        "PODER 4":"Con la habilidad que heredo de su madre, Atenea se desvanece en pensamientos para causar un enorme daño craneal al rival",
}

var8="imagenes\\avatares\\atenea.png"

diosAtenea=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------ARES--------------------------------------------

var1= "Ares - Dios guerrero"
var2= "Ares"
var3= """ En la guerra Ares
 representa la brutalidad,
 la violencia y los
 horrores de las batallas.
"""

var4= 6
var5= ""
var6= {"PODER 1":"Lanza y escudo",
        "PODER 2":"Brutalidad",
        "PODER 3":"Transformación",
        "PODER 4":"Dios de la guerra",
        "NULO":"NULO"
}

var7= {"PODER 1":"Ares logra encadenar una serie de golpes con la lanza y el escudo que logran que el enemigo no logre adoptar alguna defensa.",
        "PODER 2":" Con la brutalidad que lo representa, Ares ataca a su enemigo sin parar, esta brutalidad ha dejado aturdidos hasta a dioses, por lo que no es algo para tomar a la ligera",
        "PODER 3":"Ares lleno de ira se convierte en un jabali para desgarrar personalmente a su rival",
        "PODER 4":"Como dios de la guerra convoca a un ejercito montado en caballos de 20 soldados para que ataquen sin piedad a su enemigo",
}

var8="imagenes\\avatares\\ares.png"

diosAres=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------HERCULES--------------------------------------------

var1= "Hercules - El semidios"
var2= "Hercules"
var3= """ Hijo de Zeus y de la
 mortal Alcmena, llevó a
 cabo doce grandes
 trabajos y fue
 divinizado.
""" 

var4= 5
var5= ""
var6= {"PODER 1":"Puños divinos",
        "PODER 2":"Jabalina penetrante",
        "PODER 3":"Colmillos de Erimanto",
        "PODER 4":"Estrangulación",
        "NULO":"NULO"
}

var7= {"PODER 1":"Con su gran fuerza decide golpear a su enemigo",
        "PODER 2":"Tira desde su posicion hasta donde esta el rival una lanza que lo atraviesa",
        "PODER 3":"Suelta al jabali de Erimanto para que muerda con sus colmillos a su rival, los cuales tenian la fuerza de arrancar arboles de raiz.",
        "PODER 4":"Hercules estrangula a su enemigo causandole gran daño hasta que este pueda liberarse, ya que su fuerza es tanta, el oponente queda moribundo",
}

var8="imagenes\\avatares\\hercules.png"

diosHercules=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------HELIOS--------------------------------------------

var1= "Helios - Dios del sol"
var2= "Helios"
var3= """ Es un Titán hijo de los
 titanes Hiperión y Tea,
 lo veian como un dios 
 hermoso coronado con la
 brillante aureola solar. 
""" 
var4= 4
var5= ""
var6= {"PODER 1":"Fuego infernal",
        "PODER 2":"Cegar y atacar",
        "PODER 3":"Embestida con carruaje",
        "PODER 4":"Destellos Finales",
        "NULO":"NULO"
}

var7= {"PODER 1":"Helios quema a su enemigo",
        "PODER 2":"Despues de encandecer los ojos de su enemigo, helios lo ataca con sus propios puños ",
        "PODER 3":"Helios montado de en su carruaje tirado por sus caballos en llamas, embiste al enemigo proporcionandole un buen golpe",
        "PODER 4":"Helios compacta energia pura en una especie de 20 rayos muy finos, los cuales tira contra el cuerpo de sus enemigos atravesandolos por completo.",
}

var8="imagenes\\avatares\\helios.png"

diosHelios=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------AFRODITA--------------------------------------------

var1= "Afrodita - Belleza"
var2= "Afrodita"
var3= """ La diosa del amor, aunque
 antiguamente mas que al
 amor se referia al amor
 en el sentido erótico y
 no en el romántico.
"""

var4= 3
var5= ""
var6= {"PODER 1":"Golpe rapido",
        "PODER 2":"Engaño doloroso",
        "PODER 3":"Herida de lanza",
        "PODER 4":"Encanto Mortal",
        "NULO":"NULO"
}

var7= {"PODER 1":"Afrodita se teletransporta atras de su enemigo y le acierta dos golpes",
        "PODER 2":"Logra engañar a su rival haciendole pensar que el cuerpo que ataca es el de ella, cuando realmente se autolesiona el enemigo",
        "PODER 3":"Aprendio ciertas habilidades con la lanza de su amante Ares, asi que usa estas habilidades para herir con su lanza personal, ataca los ligamentos",
        "PODER 4":"Afrodita hace que despertar en su rival un amor sentimental y un deseo carnal insoportable, haciendo de este un blanco facil, clava una daga en el vientre",
}

var8="imagenes\\avatares\\afrodita.png"

diosAfrodita=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------ARTEMISA--------------------------------------------

var1= "Artemisa - Cazadora"
var2= "Artemisa"
var3= """ Fue una de las deidades
 mas veneradas y de las
 mas antiguas.
"""

var4= 2
var5= ""
var6= {"PODER 1":"Tiro certero",
        "PODER 2":"Agitación de los vientos",
        "PODER 3":"Ataque canino",
        "PODER 4":"Metamorfosis temporal",
        "NULO":"NULO"
}

var7= {"PODER 1":"Como la cazadora que es, le tira una flecha certera a su enemigo ",
        "PODER 2":"Con cierto control del viento, artemisa logra agitar los vientos lo suficiente como para dañar a su enemigo.",
        "PODER 3":"Artemisa hace que cuatro de sus canes ataquen al enemigo desgarrando parte de su piel y carne, logrando un gran daño.",
        "PODER 4":"Convierte a su rival en un oso/a, para clavarle flechas y lanzas y hacerle mucho mas daño al tener a su rival dominado.",
}

var8="imagenes\\avatares\\artemisa.png"

diosArtemisa=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------PANDORA--------------------------------------------

var1= "Pandora - Primera mujer"
var2= "Pandora"
var3= """ Fue la primera mujer,
 hecha por Hefesto por
 orden del dios Zeus.
"""

var4= 1
var5= ""
var6= {"PODER 1":"Golpe divino",
        "PODER 2":"Persuación",
        "PODER 3":"La esperanza como daño",
        "PODER 4":"Caja de pandora",
        "NULO":"NULO"
}

var7= {"PODER 1":"Da un fuerte golpe a su rival con sus manos",
        "PODER 2":"Gracias a su elocuencia y encanto, logra engañar al enemigo para acertarle un golpe ",
        "PODER 3":"Al poseer la esperanza por tanto tiempo, aprendio a arebatarsela a sus rivales",
        "PODER 4":"Abre la caja de pandora liberando todos los males del mundo dañando gravemente al enemigo",
}

var8="imagenes\\avatares\\pandora.png"

diosPandora=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)

#-----------------------------JUGADOR--------------------------------------------

var1= "Lumna - Diosa de la Luz"
var2= "Lumna"
var3= """ Diosa de la luz,
 poderosa hechicera,
 hija de los dioses
 nórdicos Odín y 
 Freyja. 

"""
var4= 1
var5= {"pocionHP100":1,"pocionHP250":2,"pocionHP500":0}
var6= {"PODER 1":"Destello magico","PODER 2":"Rayos","PODER 3":"Energia flameante","PODER 4":"Luz Penetrante"}
var7= var7= {"PODER 1":"Genera un destello de luz que hiere a su enemigo ","PODER 2":"Canaliza su energia en disparos a una velocidad impresionante","PODER 3":"Genera una bola de energia pura en la que encierra a su enemigo y lo quema en gran medida.","PODER 4":"Canaliza todo su gran poder un solo ataque de energia para hacerle todo el daño posible a su rival."}
var8="imagenes\\avatares\\lumna_inicial.png"

jugadorP=Personajes(var1, var2, var3, var4, var5, var6, var7, var8)
