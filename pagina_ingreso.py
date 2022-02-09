from cgitb import enable
from faulthandler import disable
from tkinter import *
from tkinter import messagebox
import os
import clase_personajes
from pygame import mixer
import modulo_historia
import sys

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

#MUSICA

mixer.init()
mixer.music.load("musica\\musica_epica.mp3")
mixer.music.set_volume(0.2)

mixer.music.play(loops=-1)

#ROOT

ventanaInicio=Tk()
ventanaInicio.title("Olympus on fire")
ventanaInicio.resizable(0,0)

#ventanaInicio.wm_attributes("-transparentcolor", "gray")
#ventanaInicio.attributes("-alpha",0.5)

#POSICIONANDO ROOT

anchoVentana:int=700
altoVentana:int=520

xPos=ventanaInicio.winfo_screenwidth()//2-anchoVentana//2
yPos=ventanaInicio.winfo_screenheight()//2-altoVentana//2-50

ventanaInicio.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

ventanaInicio.iconbitmap("imagenes\\logo.ico")

#FRAME

frameInicio=Frame(ventanaInicio,width=700,height=500)
frameInicio.pack()
frameInicio.pack_forget()

#FRAME PORTADA

framePortada=Frame(width=700,height=500)
framePortada.pack()

#IMAGENES

bg_inicial=PhotoImage(file="imagenes\\bg_inicial.png")
    #710-507

personaje_1=PhotoImage(file="imagenes\\avatares\\amalene_inicial.png")
personaje_1= personaje_1.subsample(3)

personaje_2=PhotoImage(file="imagenes\\avatares\\fobos_inicial.png")
personaje_2= personaje_2.subsample(3)

personaje_3=PhotoImage(file="imagenes\\avatares\\lumna_inicial.png")
personaje_3= personaje_3.subsample(3)

#FONDO

fondo_ventana=Label(frameInicio,image=bg_inicial)
fondo_ventana.config(width=700,height=500)
fondo_ventana.place(x=0,y=0)

fondo_ventana=Label(framePortada,image=bg_inicial)
fondo_ventana.config(width=700,height=500)
fondo_ventana.place(x=0,y=0)

#MENU

def popInfo():

    mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

    messagebox.showinfo("Creadores",mensaje)

menuInicio= Menu(ventanaInicio)
ventanaInicio.config(menu=menuInicio)

menuInicio.add_cascade(label="Info",command=lambda:popInfo())

#VARIABLES

opcion:int=0

#FUNCION

def cargarHistoria():
    global opcion

    if opcion == 0:

        var1= "Amalene - Diosa lunar"
        var2= "Amalene"
        var3= """ Diosa del tiempo y el 
 ciclo lunar, hija de
 la titán griega 
 Selene y de la diosa 
 japonesa Amaterasu.

"""
        var4= 1
        var5= {"pocionHP100":1,"pocionHP250":2,"pocionHP500":0}
        var6= {"PODER 1":"Lluvia acida","PODER 2":"Tornado","PODER 3":"Temblor","PODER 4":"Eclipse(Oscuridad)"}
        var7= {"PODER 1":"La diosa de la luna logra que de los cielos caiga lluvia acida quemando la piel de sus enemigos ","PODER 2":"En la palma de sus manos logra generar vientos lo suficientemente fuertes como para que al momento de soltarlo, genera un tornado descontrolable dejando aturdido a su rival ","PODER 3":"Amalene usa la gravedad de la luna para generar maremotos y temblores en la tierra" ,"PODER 4":"Amalene usa el eclipse para dejar ciego parcialmente al rival y atacarlo mientras se encuentra vulnerable generandole ciertos dolencias reumaticas inaguantables."}
        var8="imagenes\\avatares\\amalene_inicial.png"

        clase_personajes.jugadorP.setDatos(1,var1)
        clase_personajes.jugadorP.setDatos(2,var2)
        clase_personajes.jugadorP.setDatos(3,var3)
        clase_personajes.jugadorP.setDatos(4,var4)
        clase_personajes.jugadorP.setDatos(5,var5)
        clase_personajes.jugadorP.setDatos(6,var6)
        clase_personajes.jugadorP.setDatos(7,var7)
        clase_personajes.jugadorP.setDatos(8,var8)

        modulo_historia.cargarhistoria(var2,ventanaInicio)

    if opcion ==1:
        
        var1= "Fobos - Dios del terror"
        var2= "Fobos"
        var3= """ Dios griego del temor 
 y el horror, gran 
 guerrero, hijo de 
 Ares y Afrodita.

"""
        var4= 1
        var5= {"pocionHP100":1,"pocionHP250":2,"pocionHP500":0}
        var6= {"PODER 1":"Ataque Feroz","PODER 2":"Miedo de batalla","PODER 3":"Fobia","PODER 4":"Desgracia"}
        var7= var7= {"PODER 1":"Con su propia espada, fobos ataca al rival generando miedo el simple hecho de verse atacado por la personificacion del terror.","PODER 2":"Causa el miedo por el cual se le reconoce a fobos, genera en el rival un miedo increible a enfrentarlo, por lo le hara un daño mas grande","PODER 3":"Fobos logra generar una fobia en el rival hacial el, el rival empieza a correr desesperado y Fobos se divierte disparandole flechas ","PODER 4":"Fobos logra generar en su rival una pesadilla que se siente real, generando un ataque de nervios y un estado cercano al de la locura"} 
        var8="imagenes\\avatares\\fobos_inicial.png"

        clase_personajes.jugadorP.setDatos(1,var1)
        clase_personajes.jugadorP.setDatos(2,var2)
        clase_personajes.jugadorP.setDatos(3,var3)
        clase_personajes.jugadorP.setDatos(4,var4)
        clase_personajes.jugadorP.setDatos(5,var5)
        clase_personajes.jugadorP.setDatos(6,var6)
        clase_personajes.jugadorP.setDatos(7,var7)
        clase_personajes.jugadorP.setDatos(8,var8)

        modulo_historia.cargarhistoria(var2,ventanaInicio)

    if opcion ==2:
        
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

        clase_personajes.jugadorP.setDatos(1,var1)
        clase_personajes.jugadorP.setDatos(2,var2)
        clase_personajes.jugadorP.setDatos(3,var3)
        clase_personajes.jugadorP.setDatos(4,var4)
        clase_personajes.jugadorP.setDatos(5,var5)
        clase_personajes.jugadorP.setDatos(6,var6)
        clase_personajes.jugadorP.setDatos(7,var7)
        clase_personajes.jugadorP.setDatos(8,var8)

        modulo_historia.cargarhistoria(var2,ventanaInicio)

#LABEL

textoUniversidad=Label(frameInicio,text="\u00A9 Universidad Nacional de Colombia - Facultad de Ingeniería")
textoUniversidad.place(x=10,y=470)
textoUniversidad.config(font="Arial 10")

imagenPersonaje=Label(frameInicio,image=personaje_1)
imagenPersonaje.place(x=140,y=180)

tituloJuego=Label(frameInicio,text="OLYMPUS ON FIRE")
tituloJuego.config(font="Consolas 40")
tituloJuego.place(x=130,y=20)

escogerPersonaje=Label(frameInicio,text="Escoge tu personaje")
escogerPersonaje.config(fg="navy",font="Consolas 20")
escogerPersonaje.place(x=200,y=130)

#LABEL PORTADA

tituloP=Label(framePortada,text="OLYMPUS ON FIRE")
tituloP.config(font="Consolas 50")
tituloP.place(x=65,y=150)

dobleClick=Label(framePortada,text="PRESIONA UNA TECLA")
dobleClick.config(font="Italic 15 bold")
dobleClick.place(x=190,y=260)

textoP=Label(framePortada,text="\u00A9 Universidad Nacional de Colombia - Facultad de Ingeniería")
textoP.place(x=10,y=470)
textoP.config(font="Arial 10")

#TEXT

descripcionPersonaje=Text(frameInicio)
descripcionPersonaje.config(font="Consolas 15")
descripcionPersonaje.config(width=21,height=8)
descripcionPersonaje.place(x=350,y=188)

descripcion1:str="""     DESCRIPCION
 
 Diosa del tiempo 
 y el ciclo lunar, 
 hija de la titán 
 griega Selene y 
 de la diosa japonesa
 Amaterasu.

"""

descripcion2:str="""     DESCRIPCION

 Dios griego del 
 temor y el horror, 
 gran guerrero, 
 hijo de Ares y 
 Afrodita.

"""

descripcion3:str="""     DESCRIPCION

 Diosa de la luz,
 poderosa hechicera,
 hija de los dioses
 nórdicos Odín y 
 Freyja. 

"""

descripcionPersonaje.insert(INSERT,descripcion1)
descripcionPersonaje.config(state=DISABLED)

#BOTONES

botonJugar=Button(frameInicio,text="Jugar",command=cargarHistoria)
botonJugar.config(font="Consolas 14 bold",cursor="hand2",relief="groove")
botonJugar.config(width=10,height=1)
botonJugar.place(x=295,y=400)

botonDerecha=Button(frameInicio,text="\u25B6",command=lambda:cambiarPersonaje(1))
botonDerecha.config(font="Consolas 20",cursor="hand2",relief="groove")
botonDerecha.place(x=590,y=255)

botonIzquierda=Button(frameInicio,text="\u25C0",command=lambda:cambiarPersonaje(-1))
botonIzquierda.config(font="Consolas 20",cursor="hand2",relief="groove")
botonIzquierda.place(x=90,y=255)

#frameInicio.pack_forget()
#frameInicio.pack()

#EVENTOS

def cargarJuego(event):
    framePortada.pack_forget()
    frameInicio.pack()

ventanaInicio.bind("<Key>",cargarJuego)

def cambiarPersonaje(n):

    global opcion, descripcion1,descripcion2,descripcion3,descripcionPersonaje

    if opcion==2 and n==1:
        opcion=0
    elif opcion==0 and n==-1:
        opcion=2
    else:
        opcion=opcion+n

    #CONFIGURAR DESCRIPCION & IMAGEN

    descripcionPersonaje.config(state=NORMAL)
    descripcionPersonaje.delete("1.0",END)

    if opcion == 0:
        descripcionPersonaje.insert(INSERT,descripcion1)
        imagenPersonaje.config(image=personaje_1)
    elif opcion == 1:
        descripcionPersonaje.insert(INSERT,descripcion2)
        imagenPersonaje.config(image=personaje_2)
    else:
        descripcionPersonaje.insert(INSERT,descripcion3)
        imagenPersonaje.config(image=personaje_3)

    descripcionPersonaje.config(state=DISABLED)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaInicio.destroy()

    ventanaInicio.protocol("WM_DELETE_WINDOW", cerrarPrograma)

ventanaInicio.mainloop()

mixer.init()
mixer.music.stop()
sys.exit()

