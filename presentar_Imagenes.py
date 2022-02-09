from distutils import command
import os
from tkinter import *
from tkinter import messagebox
from pygame import mixer

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

#GLOBALES
contador=0

def cargarPresentacion(ventanaTutorial,tipoLista):

    global contador
    contador=0

    ventanaTutorial.withdraw()

    #VARIABLES

    listaL:list=[]
    listaM:list=[]
    listaC:list=[]

    if tipoLista == "L":
        slc=listaL

    if tipoLista == "M":
        slc=listaM

    if tipoLista == "C":
        slc=listaC

    #ROOT
    ventanaPresentacion= Toplevel(ventanaTutorial)
    ventanaPresentacion.resizable(0,0)
    ventanaPresentacion.title("Olympus on fire")

    #POSICIONANDO ROOT

    anchoVentana:int=700
    altoVentana:int=520

    xPos=ventanaPresentacion.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanaPresentacion.winfo_screenheight()//2-altoVentana//2-50

    ventanaPresentacion.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanaPresentacion.iconbitmap("imagenes\\logo.ico")

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaPresentacion)
    ventanaPresentacion.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #FRAME

    anchoVentana = 700
    altoVentana = 500

    #FUNCIONES

    def modificarContador(n,lista):
        
        global contador
        maximo = len(lista)

        if n == 1 and contador == maximo-1:
            ventanaPresentacion.destroy()
            ventanaTutorial.deiconify()

        try:
            lista[contador+n] = lista[contador+n]
            assert contador+n>=0
            contador+=n
            imagenPrincipal.config(image=lista[contador])
        except:
            pass

    #FRAME

    framePresentacion=Frame(ventanaPresentacion,width=anchoVentana,height=altoVentana)
    framePresentacion.pack()
    framePresentacion.config(bg="green")

    #CONFIGURAR IMAGENES

    L1 = PhotoImage(file="imagenes\\tutorial\\LogrosTutorial.png")
    M1 = PhotoImage(file="imagenes\\tutorial\\MapaTutorial.png")
    C1 = PhotoImage(file="imagenes\\tutorial\\CombateTutorial.png")

    listaL.append(L1)
    listaM.append(M1)
    listaC.append(C1)

    imagenPrincipal=Label(framePresentacion,image=slc[ contador ])
    imagenPrincipal.place(x=0,y=0)

    #BOTONES

    bReturn= Button(framePresentacion,text="Anterior",command= lambda:modificarContador(-1,slc))
    bReturn.config(font="Consolas 18",cursor="hand2",relief="groove")
    bReturn.place(x=210,y=437)

    bNext = Button(framePresentacion,text="Siguiente",command= lambda:modificarContador(1,slc))
    bNext.config(font="Consolas 18",cursor="hand2",relief="groove")
    bNext.place(x=370,y=437)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaPresentacion.destroy()

    ventanaPresentacion.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaPresentacion.mainloop()

tipoLista:str="M"

#cargarPresentacion(1,tipoLista)