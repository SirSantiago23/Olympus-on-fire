#Librerías
from tkinter import *
from tkinter import messagebox
import os
import modulo_historia2
import clase_personajes
import modulo_mapa
import modulo_tutorial
from pygame import mixer

#Cargar contenido multimedia y códigos
#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

#La función para llamar la historia introductoria
def cargarhistoria(id_P, ventanaInicio):

    ventanaInicio.withdraw()

    #PANTALLA INICIAL: los tres personajes tienen la misma

    #Creación ventana
    ventanahistoria=Toplevel(ventanaInicio)
    ventanahistoria.title("Olympus on fire")
    ventanahistoria.resizable(0,0)
    

    #Tamaño de la historia
    anchoVentana:int=700
    altoVentana:int=520
    #tamaño x y tamaño y de la ventana
    #winfo: Devuelve el número de píxeles del ancho/alto de la pantalla de este widget en píxeles.
    xPos=ventanahistoria.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanahistoria.winfo_screenheight()//2-altoVentana//2-50
    #geometry: Método para establecer las dimensiones de la ventana tk y establecer posición en escritorio
    ventanahistoria.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanahistoria.iconbitmap("imagenes\\logo.ico")

    #FRAME 1
    framehistoria=Frame(ventanahistoria,width=anchoVentana,height=altoVentana)
    framehistoria.pack()

    #MUSICA

    mixer.init()
    mixer.music.load("musica\\cancion1.mp3")
    mixer.music.set_volume(0.4)

    mixer.music.stop()
    mixer.music.play(loops=-1,start=30)
    
    #Info-Menú
    #Información de creadores
    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanahistoria)
    ventanahistoria.config(menu=menuInicio)
    #Label: etiqueta de texto
    #add_cascade: para desplegar el menú
    #command: comando del menú de la función /lo que va a ir escrito)
    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #FONDO
    #Imagen fondo
    fondo_historia= PhotoImage(file="imagenes\\historia\\fondoHistoria.png")
    #Fondo
    etiquetafondo=Label(framehistoria,image=fondo_historia)
    etiquetafondo.config(width=700,height=500)
    etiquetafondo.place(x=0,y=0)

    #LABEL
    titulohistoria=Label(framehistoria,text="EL HILO DEL DESTINO")
    titulohistoria.config(bg="#F9E79F", font="Consolas 35 bold")
    titulohistoria.place(x=95, y=20)

    frase1_intro=Text(framehistoria)
    frase1_intro.config(font="Consolas 15")
    frase1_intro.config(width=60,height=5)
    frase1_intro.place(x=17,y=100)
    frase1:str="""
  Los dioses griegos siempre se han caracterizado por ser
  una versión sumamente desvergonzada y déspota de los
  humanos, una deshonra para el Panteón universal.
    """
    frase1_intro.insert(INSERT, frase1)
    frase1_intro.config(state=DISABLED)

    frase2_intro=Text(framehistoria)
    frase2_intro.config(font="Consolas 15")
    frase2_intro.config(width=33, height=7)
    frase2_intro.place(x=310,y=235)
    frase2:str="""
 El destino requiere un guerrero
 capaz de arruinar el presente 
 lleno de excesos, errores 
 e injusticias de estos seres, 
 mal llamados dioses.
    """
    frase2_intro.insert(INSERT, frase2)
    frase2_intro.config(state=DISABLED)

    #IMAGENES
    imagen_1=PhotoImage(file="imagenes\\historia\\imagen1.png")
    imagen_1= imagen_1.subsample(3)
    imagenPersonaje=Label(framehistoria,image=imagen_1)
    imagenPersonaje.place(x=17,y=235)

    #BOTONES
    #Boton siguiente
    def verHistoria_next():
        modulo_historia2.cargarhistoria2(ventanaInicio,id_P,ventanahistoria)

    def saltarHistoria():
        modulo_tutorial.cargarTutorial(ventanaInicio,ventanahistoria)

    botonnext=Button(framehistoria,text="Siguiente", command=verHistoria_next)
    botonnext.config(font="Consolas 14 bold",cursor="hand2",relief="groove", fg="green")
    botonnext.config(width=10,height=1)
    botonnext.place(x=560, y=415)

    botonsaltar=Button(framehistoria,text="Saltar",command=saltarHistoria)
    botonsaltar.config(font="Consolas 14 bold",cursor="hand2",relief="groove")
    botonsaltar.config(width=8,height=1)
    botonsaltar.place(x=17, y=415)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanahistoria.destroy()

    ventanahistoria.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanahistoria.mainloop()

#varID = clase_personajes.jugadorP.getDatos(2)
#cargarhistoria(varID)