from distutils import command
import os
from tkinter import *
import presentar_Imagenes
import modulo_mapa
import clase_personajes
from tkinter import messagebox
from pygame import mixer

from pygame import image

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

def cargarTutorial(ventanaInicio,ventanahistoria3):

    ventanahistoria3.withdraw()

    ventanaTutorial = Toplevel(ventanaInicio)
    ventanaTutorial.resizable(0,0)
    ventanaTutorial.title("Olympus on fire")

    #POSICIONANDO ROOT

    anchoVentana:int=700
    altoVentana:int=520

    xPos=ventanaTutorial.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanaTutorial.winfo_screenheight()//2-altoVentana//2-50

    ventanaTutorial.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))
    ventanaTutorial.iconbitmap("imagenes\\logo.ico")

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaTutorial)
    ventanaTutorial.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #FRAME

    anchoVentana = 700
    altoVentana = 500

    frameTutorial=Frame(ventanaTutorial,width=anchoVentana,height=altoVentana)
    frameTutorial.pack()


    #IMAGENES

    fondoTuto = PhotoImage(file="imagenes\\fondoTutorial.png")

    estatuaZeus = PhotoImage(file="imagenes\\estatuas\\estatuaZeus.png")
    estatuaArtemisa = PhotoImage(file="imagenes\\estatuas\\estatuaArtemisa.png")
    estatuaAres = PhotoImage(file="imagenes\\estatuas\\estatuaAres.png")    #216x270

    #FUNCIONES

    def cargarImagenes(n):
        presentar_Imagenes.cargarPresentacion(ventanaTutorial,n)

    def cargarModuloMapa():

        nombre=clase_personajes.jugadorP.getDatos(2)

        if nombre=="Amalene":
            nombre="Amalene\nDiosa de la luna"

        if nombre=="Fobos":
            nombre="Fobos\nDios del terror"

        if nombre=="Lumna":
            nombre="Lumna\nDiosa de la luz"

        nivel=clase_personajes.jugadorP.getDatos(4)
        ruta=clase_personajes.jugadorP.getDatos(8)

        modulo_mapa.cargarMapa(ventanaInicio,nombre,nivel,ruta,ventanaTutorial)


    #LABEL

    fondoPrincipal=Label(frameTutorial)
    fondoPrincipal.config(image=fondoTuto)
    fondoPrincipal.pack()

    titulo = Label(frameTutorial,text="  TUTORIAL  ")
    titulo.config(font="Consolas 35 bold",bg="#7ba22d")
    titulo.place(x=200,y=30)

    imagenZeus = Label(frameTutorial,image=estatuaZeus)
    imagenZeus.place(x=45,y=130)

    imagenArtemisa = Label(frameTutorial,image=estatuaArtemisa)
    imagenArtemisa.place(x=245,y=130)

    imagenAres = Label(frameTutorial,image=estatuaAres)
    imagenAres.place(x=445,y=130)

    #BOTONES

    skip = Button(frameTutorial,text="Saltar",command=cargarModuloMapa)
    skip.config(font= "Arial 17", cursor="hand2") 
    skip.place(x=590,y=30)

    seccion1 = Button(frameTutorial,text=" Logros ",command=lambda:cargarImagenes("L"))
    seccion1.config(font= "Arial 20", cursor="hand2")
    seccion1.place(x=85,y=390)

    seccion2 = Button(frameTutorial,text=" Mapa ",command=lambda:cargarImagenes("M"))
    seccion2.config(font= "Arial 20", cursor="hand2")
    seccion2.place(x=295,y=390)

    seccion3 = Button(frameTutorial,text="Combate",command=lambda:cargarImagenes("C"))
    seccion3.config(font= "Arial 20", cursor="hand2")
    seccion3.place(x=495,y=390)

    def colorearS1(event):
        seccion1.config(bg="#ffcb22")
    def descolorearS1(event):
        seccion1.config(bg="#f0f0f0")

    seccion1.bind("<Enter>",colorearS1)
    seccion1.bind("<Leave>",descolorearS1)

    #evento S2

    def colorearS2(event):
        seccion2.config(bg="#2b85dd")
    def descolorearS2(event):
        seccion2.config(bg="#f0f0f0")

    seccion2.bind("<Enter>",colorearS2)
    seccion2.bind("<Leave>",descolorearS2)

    #evento S3

    def colorearS3(event):
        seccion3.config(bg="#ff4148")
    def descolorearS3(event):
        seccion3.config(bg="#f0f0f0")

    seccion3.bind("<Enter>",colorearS3)
    seccion3.bind("<Leave>",descolorearS3)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaTutorial.destroy()

    ventanaTutorial.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaTutorial.mainloop()