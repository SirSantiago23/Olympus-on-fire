from ast import Num
from tkinter import messagebox
from tkinter import *
import os
from turtle import left
import modulo_logros
import modulo_album
import clase_personajes
import modulo_combate
from pygame import mixer

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

levelP1:int=0

def cargarMapa(ventanaInicio,namePersonaje, nivelPersonaje, rutaImagen, ventanahistoria3):

    #MUSICA

    mixer.init()
    mixer.music.load("musica\\cancion1.mp3")
    mixer.music.set_volume(0.30)

    mixer.music.stop()
    mixer.music.play(loops=-1,start=520)

    global levelP1

    levelP1 = nivelPersonaje

    ventanahistoria3.destroy()

    ventanaMapa=Toplevel(ventanaInicio)
    ventanaMapa.title("Olympus on fire")
    ventanaMapa.resizable(0,0)

    #DEFINIENDO VENTANA PRINCIPAL

    anchoVentana:int=700
    altoVentana:int=520

    xPos = ventanaMapa.winfo_screenwidth()//2-anchoVentana//2
    yPos = ventanaMapa.winfo_screenheight()//2-altoVentana//2-50

    ventanaMapa.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanaMapa.iconbitmap("imagenes\\logo.ico")

    #FRAME

    frameMapa=Frame(ventanaMapa,width=anchoVentana,height=altoVentana)
    frameMapa.pack()

    #VARIABLES

    variableNombre:str=StringVar()
    variableNombre.set("")
    variableNombre.set( namePersonaje + "\nNivel {}".format(nivelPersonaje) )

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaMapa)
    ventanaMapa.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #IMAGENES

    fondoMapa = PhotoImage(file="imagenes\\mapa2.png")
    imagenP1 = PhotoImage(file=rutaImagen)
    imagenLogros = PhotoImage(file="imagenes\\logros.png")
    imagenAlbum = PhotoImage(file="imagenes\\album.png")

    imagenP1= imagenP1.subsample(7)
    imagenLogros = imagenLogros.subsample(8)
    imagenAlbum = imagenAlbum.subsample(8)

    #FONDO

    labelFondo = Label(frameMapa,image=fondoMapa)
    labelFondo.config(width=700,height=500)
    labelFondo.place(x=0,y=0)

    #FUNCIONES

    def presionarBoton(listaUbicaciones,num):

        global levelP1

        val=clase_personajes.jugadorP.getDatos(4)

        if num==10:
            levelP1=10
            clase_personajes.jugadorP.setDatos(4,11)
        elif num == val:
            levelP1=num+1
            clase_personajes.jugadorP.setDatos(4,num+1)

        variableNombre.set( namePersonaje + "\nNivel {}".format(levelP1))
        
        cambiarBotones(listaUbicaciones)

        nameP1= clase_personajes.jugadorP.getDatos(1)
        id_P1= clase_personajes.jugadorP.getDatos(2)
        poderesP1:dict=clase_personajes.jugadorP.getDatos(6)
        mochila= clase_personajes.jugadorP.getDatos(5)
        foto1:str= clase_personajes.jugadorP.getDatos(8)
        fondo:str="imagenes\\bg_olimpo.png"

        if num==1:
            nameP2:str= clase_personajes.diosPandora.getDatos(1)
            id_P2:str= clase_personajes.diosPandora.getDatos(2)
            poderesP2:dict=clase_personajes.diosPandora.getDatos(6)
            foto2:str= clase_personajes.diosPandora.getDatos(8)

        if num==2:
            nameP2:str= clase_personajes.diosArtemisa.getDatos(1)
            id_P2:str= clase_personajes.diosArtemisa.getDatos(2)
            poderesP2:dict=clase_personajes.diosArtemisa.getDatos(6)
            foto2:str= clase_personajes.diosArtemisa.getDatos(8)

        if num==3:
            nameP2:str= clase_personajes.diosAfrodita.getDatos(1)
            id_P2:str= clase_personajes.diosAfrodita.getDatos(2)
            poderesP2:dict=clase_personajes.diosAfrodita.getDatos(6)
            foto2:str= clase_personajes.diosAfrodita.getDatos(8)

        if num==4:
            nameP2:str= clase_personajes.diosHelios.getDatos(1)
            id_P2:str= clase_personajes.diosHelios.getDatos(2)
            poderesP2:dict=clase_personajes.diosHelios.getDatos(6)
            foto2:str= clase_personajes.diosHelios.getDatos(8)

        if num==5:
            nameP2:str= clase_personajes.diosHercules.getDatos(1)
            id_P2:str= clase_personajes.diosHercules.getDatos(2)
            poderesP2:dict=clase_personajes.diosHercules.getDatos(6)
            foto2:str= clase_personajes.diosHercules.getDatos(8)

        if num==6:
            nameP2:str= clase_personajes.diosAres.getDatos(1)
            id_P2:str= clase_personajes.diosAres.getDatos(2)
            poderesP2:dict=clase_personajes.diosAres.getDatos(6)
            foto2:str= clase_personajes.diosAres.getDatos(8)

        if num==7:
            nameP2:str= clase_personajes.diosAtenea.getDatos(1)
            id_P2:str= clase_personajes.diosAtenea.getDatos(2)
            poderesP2:dict=clase_personajes.diosAtenea.getDatos(6)
            foto2:str= clase_personajes.diosAtenea.getDatos(8)

        if num==8:
            nameP2:str= clase_personajes.diosPoseidon.getDatos(1)
            id_P2:str= clase_personajes.diosPoseidon.getDatos(2)
            poderesP2:dict=clase_personajes.diosPoseidon.getDatos(6)
            foto2:str= clase_personajes.diosPoseidon.getDatos(8)

        if num==9:
            nameP2:str= clase_personajes.diosHades.getDatos(1)
            id_P2:str= clase_personajes.diosHades.getDatos(2)
            poderesP2:dict=clase_personajes.diosHades.getDatos(6)
            foto2:str= clase_personajes.diosHades.getDatos(8)

        if num==10:
            nameP2:str= clase_personajes.diosZeus.getDatos(1)
            id_P2:str= clase_personajes.diosZeus.getDatos(2)
            poderesP2:dict=clase_personajes.diosZeus.getDatos(6)
            foto2:str= clase_personajes.diosZeus.getDatos(8)
        
        modulo_combate.cargarCombate(ventanaInicio,ventanaMapa,nameP1,nameP2,id_P1,id_P2,poderesP1,poderesP2,mochila,foto1,foto2,fondo,num)

    #UBICACIONES MAPA

    nombrePersonaje=Label(frameMapa,textvariable=variableNombre)
    nombrePersonaje.config(font="Consolas 10 bold")
    nombrePersonaje.place(x=110,y=30)

    imagenPersonaje=Label(frameMapa,image=imagenP1)
    imagenPersonaje.config(font="Consolas 10")
    imagenPersonaje.place(x=15,y=10)

    Punto1=Button(frameMapa,text="1",command=lambda:presionarBoton(listaUbicaciones,1))
    Punto1.config(width=2,height=1,cursor="hand2")
    Punto1.config(state=NORMAL,bg="#efb810",font="bold")
    Punto1.place(x=628,y=310)

    Punto2=Button(frameMapa,text="2",command=lambda:presionarBoton(listaUbicaciones,2))
    Punto2.config(width=2,height=1,cursor="hand2")
    Punto2.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto2.place(x=610,y=456)

    Punto3=Button(frameMapa,text="3",command=lambda:presionarBoton(listaUbicaciones,3))
    Punto3.config(width=2,height=1,cursor="hand2")
    Punto3.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto3.place(x=325,y=135)

    Punto4=Button(frameMapa,text="4",command=lambda:presionarBoton(listaUbicaciones,4))
    Punto4.config(width=2,height=1,cursor="hand2")
    Punto4.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto4.place(x=380,y=235)

    Punto5=Button(frameMapa,text="5",command=lambda:presionarBoton(listaUbicaciones,5))
    Punto5.config(width=2,height=1,cursor="hand2")
    Punto5.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto5.place(x=95,y=135)

    Punto6=Button(frameMapa,text="6",command=lambda:presionarBoton(listaUbicaciones,6))
    Punto6.config(width=2,height=1,cursor="hand2")
    Punto6.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto6.place(x=240,y=300)

    Punto7=Button(frameMapa,text="7",command=lambda:presionarBoton(listaUbicaciones,7))
    Punto7.config(width=2,height=1,cursor="hand2")
    Punto7.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto7.place(x=30,y=210)

    Punto8=Button(frameMapa,text="8",command=lambda:presionarBoton(listaUbicaciones,8))
    Punto8.config(width=2,height=1,cursor="hand2")
    Punto8.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto8.place(x=15,y=430)

    Punto9=Button(frameMapa,text="9",command=lambda:presionarBoton(listaUbicaciones,9))
    Punto9.config(width=2,height=1,cursor="hand2")
    Punto9.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto9.place(x=275,y=430)

    Punto10=Button(frameMapa,text="10",command=lambda:presionarBoton(listaUbicaciones,10))
    Punto10.config(width=2,height=1,cursor="hand2")
    Punto10.config(state=DISABLED,bg="#e3e4e5",font="bold")
    Punto10.place(x=390,y=50)

    #BOTON LOGROS

    def verLogros():

        global levelP1
        if clase_personajes.jugadorP.getDatos(4)>10:
            modulo_logros.cargarLogros(ventanaMapa,levelP1)
        else:
            modulo_logros.cargarLogros(ventanaMapa,levelP1-1)

    def verAlbum():

        modulo_album.cargarAlbum(ventanaMapa)

    botonLogros=Button(frameMapa, image=imagenLogros, command=verLogros)
    botonLogros.config(cursor="hand2")
    botonLogros.place(x=620,y=20)

    botonAlbum=Button(frameMapa, image=imagenAlbum, command=verAlbum)
    botonAlbum.config(cursor="hand2")
    botonAlbum.place(x=540,y=20)

    #CONFIGURAR COLOR

    listaUbicaciones:list=[]

    listaUbicaciones.append(Punto1)
    listaUbicaciones.append(Punto2) 
    listaUbicaciones.append(Punto3)
    listaUbicaciones.append(Punto4)
    listaUbicaciones.append(Punto5)
    listaUbicaciones.append(Punto6)
    listaUbicaciones.append(Punto7)
    listaUbicaciones.append(Punto8)
    listaUbicaciones.append(Punto9)
    listaUbicaciones.append(Punto10)

    def cambiarBotones(listaUbicaciones):

        global levelP1

        for i in range(levelP1):
            listaUbicaciones[i].config(state=NORMAL,bg="#e3e4e5")

        listaUbicaciones[levelP1-1].config(bg="#efb810")

        for i in range(10):
            if i<levelP1:
                pass
            else:
                listaUbicaciones[i].config(state=DISABLED)

        #YA SE SUPERARON LOS 10 NIVELES

        if  clase_personajes.jugadorP.getDatos(4) > 10:
            for i in listaUbicaciones:
                i.config(state=NORMAL,bg="#efb810")
            variableNombre.set(namePersonaje + "\nJuego Completado")
    
    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaMapa.destroy()

    ventanaMapa.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaMapa.mainloop()


name1="Lumna\nDiosa de la luz"
nivel=1
rP1 = "imagenes\\avatares\\lumna_inicial.png"

#cargarMapa(0,name1,nivel,rP1,0)