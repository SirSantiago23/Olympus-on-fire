 
from tkinter import *
from tkinter import messagebox
import os
import random
from typing import Dict
from pygame import mixer
import pygame
import clase_personajes
import modulo_recompensas

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

#VARIABLES GLOBALES - VIDA

SaludP1:int=29
SaludP2:int=29

SaludP1Falsa:int=1000
SaludP2Falsa:int=1000

#VARIABLES GLOBALES - NO VIDA

nombreP1:str=""
nombreP2:str=""

idP1:str=""
idP2:str=""

ListaPoderesP1:list={}
ListaPoderesP2:list={}

ListaInventario:dict={}
respaldoInventario:dict={}

foto1:str=""
foto2:str=""
fondo:str=""

nivelGlobal=0

#LISTA PODERES

"""  
1. PANDORA
2. ARTEMISA
3. AFRODITA
4. HELIOS
5. HERCULES
6. ARES
7. ATENEA
8. POSEIDON
9. HADES
10. ZEUS
"""

#LISTA REDUCTORES Y AMPLIFICADORES

lessDamage:dict={"Zeus":1.6 ,"Hades":1.54, "Poseidon":1.42, "Atenea": 1.35, "Ares": 1.21, "Hercules":1.12, "Helios":1.09, "Afrodita":1.05, "Artemisa":1.03, "Pandora":1}
moreDamage:dict={"Zeus":0.66 ,"Hades":0.69, "Poseidon":0.74, "Atenea": 0.83, "Ares": 0.87, "Hercules":0.9, "Helios":1.05, "Afrodita":1.1, "Artemisa":1.2, "Pandora":1.3}

probPociones:dict={"Zeus":[6,7], "Hades":[5,7], "Poseidon":[5,7], "Atenea":[4,7], "Ares":[4,6], "Hercules":[3,6], "Helios":[3,5], "Afrodita":[2,5], "Artemisa":[2,5], "Pandora":[1,5]}

#CONTROL TURNOS

turnosAtaques:list=[0,0,0,0] 

#MENSAJES EN PANTALLA

def popInfo():

    mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """
    messagebox.showinfo("Creadores",mensaje)

def popPerdiste(ventanaInicio,ventanaMapa,ventanaCombate):

    global SaludP1,SaludP2,SaludP1Falsa,SaludP2Falsa
    global nombreP1,nombreP2,idP1,idP2,ListaPoderesP1,ListaPoderesP2,ListaInventario,foto1,foto2,fondo
    global respaldoInventario
    global turnosAtaques
    global nivelGlobal

    opcion=messagebox.showwarning("Perdiste","¿Volver a intentar?")

    if opcion=="ok":

        SaludP1,SaludP2 = 29, 29
        SaludP1Falsa,SaludP2Falsa = 1000,1000
        turnosAtaques=[0,0,0,0]

        ventanaCombate.destroy()
        cargarCombate(ventanaInicio,ventanaMapa,nombreP1,nombreP2,idP1,idP2,ListaPoderesP1,ListaPoderesP2,respaldoInventario,foto1,foto2,fondo,nivelGlobal)

def retornarMapa(ventanaInicio,ventanaMapa,ventanaCombate):

    global nivelGlobal
    ventanaCombate.destroy()
    modulo_recompensas.darPociones(ventanaInicio,ventanaMapa,nivelGlobal)

def cargarCombate(ventanaInicio,ventanaMapa,nameP1,nameP2,id_P1,id_P2,poderesP1,poderesP2,mochila,_foto1,_foto2,_fondo,nivelActual):

    ventanaMapa.withdraw()

    mixer.init()
    mixer.music.load("musica\\musica_batalla.mp3")
    mixer.music.set_volume(0.3)

    mixer.music.play(loops=-1)

    global SaludP1,SaludP2,SaludP1Falsa,SaludP2Falsa
    global nombreP1,nombreP2,idP1,idP2,ListaPoderesP1,ListaPoderesP2,ListaInventario,foto1,foto2,fondo
    global SaludP1,SaludP2,SaludP1Falsa,SaludP2Falsa
    global respaldoInventario
    global turnosAtaques
    global nivelGlobal

    nombreP1=nameP1
    nombreP2=nameP2
    idP1=id_P1
    idP2=id_P2
    ListaPoderesP1=poderesP1.copy()
    ListaPoderesP2=poderesP2.copy()
    ListaInventario=mochila.copy()
    respaldoInventario=mochila.copy()

    foto1=_foto1
    foto2=_foto2
    fondo=_fondo
    nivelGlobal = nivelActual

    SaludP1=29
    SaludP2=29
    SaludP1Falsa=1000
    SaludP2Falsa=1000
    turnosAtaques=[0,0,0,0]

    ventanaCombate=Toplevel(ventanaMapa)
    ventanaCombate.title("Olympus on fire")
    ventanaCombate.resizable(0,0)

    #VARIABLES

    nombre1=StringVar()
    nombre1.set(nombreP1)

    nombre2=StringVar()
    nombre2.set(nombreP2)

    vidaP1=StringVar()
    vidaP1.set("HP "+str(SaludP1Falsa))

    vidaP2=StringVar()
    vidaP2.set("HP "+str(SaludP2Falsa))

    #DEFINIENDO VENTANA PRINCIPAL

    anchoVentana:int=700
    altoVentana:int=520

    xPos = ventanaCombate.winfo_screenwidth()//2-anchoVentana//2
    yPos = ventanaCombate.winfo_screenheight()//2-altoVentana//2-50

    ventanaCombate.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanaCombate.iconbitmap("imagenes\\logo.ico")

    #FRAME

    frameCombate=Frame(ventanaCombate,width=700,height=500)
    frameCombate.pack()

    #IMAGENES

    bg_olimpo=PhotoImage(file=fondo)
    #710-507

    personaje1=PhotoImage(file=foto1)
    personaje1= personaje1.subsample(4)

    personaje2=PhotoImage(file=foto2)
    personaje2= personaje2.subsample(4)

    #FONDO

    fondo_ventana=Label(frameCombate,image=bg_olimpo)
    fondo_ventana.config(width=700,height=500)
    fondo_ventana.place(x=0,y=0)

    #MENU

    menuInicio= Menu(ventanaCombate)
    ventanaCombate.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #CUADRO PERSONAJE 1

    imagenPersonaje1=Label(frameCombate,image=personaje1)
    imagenPersonaje1.place(x=110,y=160)

    fondoDescripcion1=Label(frameCombate)
    fondoDescripcion1.config(bg="#3f403f",width=56,height=4)
    fondoDescripcion1.place(x=277,y=236)

    descripcion1=Label(frameCombate,textvariable=nombre1)
    descripcion1.config(width=35,height=1)
    descripcion1.config(font="Consolas 15 bold",bg="#7d807e",fg="White")
    descripcion1.place(x=280,y=240)

    vida1=Label(frameCombate,textvariable=vidaP1)
    vida1.config(width=10,height=1)
    vida1.config(font="Consolas 15 bold",bg="#7d807e",fg="White")
    vida1.place(x=320,y=270)

    barraVida1Total=Label(frameCombate)
    barraVida1Total.config(width=29,height=1)
    barraVida1Total.config(bg="Red")
    barraVida1Total.place(x=440,y=274)

    barraVida1=Label(frameCombate)
    barraVida1.config(width= SaludP1,height=1)
    barraVida1.config(bg="#18c020")
    barraVida1.place(x=440,y=274)

    #LABEL PERSONAJE 2

    imagenPersonaje2=Label(frameCombate,image=personaje2)
    imagenPersonaje2.place(x=450,y=30)

    fondoDescripcion2=Label(frameCombate)
    fondoDescripcion2.config(bg="#3f403f",width=56,height=4)
    fondoDescripcion2.place(x=40,y=45)

    descripcion2=Label(frameCombate,textvariable=nombre2)
    descripcion2.config(width=35,height=1)
    descripcion2.config(font="Consolas 15 bold",bg="#7d807e",fg="White")
    descripcion2.place(x=43,y=49)

    vida2=Label(frameCombate,textvariable=vidaP2)
    vida2.config(width=10,height=1)
    vida2.config(font="Consolas 15 bold",bg="#7d807e",fg="White")
    vida2.place(x=83,y=79)

    barraVida2Total=Label(frameCombate)
    barraVida2Total.config(width=29,height=1)
    barraVida2Total.config(bg="Red")
    barraVida2Total.place(x=203,y=83)

    barraVida2=Label(frameCombate)
    barraVida2.config(width= SaludP2 ,height=1)
    barraVida2.config(bg="#18c020")
    barraVida2.place(x=203,y=83)

    #LABELS ESTETICOS INFERIORES

    fondoCuadroLabel=Label(frameCombate)
    fondoCuadroLabel.config(width=96,height=10)
    fondoCuadroLabel.config(bg="#3f403f")
    fondoCuadroLabel.place(x=11,y=330)

    CuadroLabel1=Label(frameCombate)
    CuadroLabel1.config(width=42,height=8)
    CuadroLabel1.config(bg="#7d807e")
    CuadroLabel1.place(x=20,y=345)

    CuadroLabel2=Label(frameCombate)
    CuadroLabel2.config(width=49,height=8)
    CuadroLabel2.config(bg="#7d807e")
    CuadroLabel2.place(x=330,y=345)

    labelPregunta=Label(frameCombate)
    labelPregunta.config(text="¿Qué quiere \nhacer?")
    labelPregunta.config(font="Didot 30 bold",bg="#7d807e",fg="White")
    labelPregunta.place(x=50,y=357)

    #BOTONES INFERIORES

    fondoBotonBatalla=Label(frameCombate)
    fondoBotonBatalla.config(width=21,height=6,bg="Black")
    fondoBotonBatalla.place(x=345,y=360)
    
    fondoBotonMaleta=Label(frameCombate)
    fondoBotonMaleta.config(width=21,height=6,bg="Black")
    fondoBotonMaleta.place(x=505,y=360)

    botonBatalla=Button(frameCombate,text="LUCHAR",command=lambda:moduloLucha(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,vidaP1,vidaP2))
    botonBatalla.config(width=9,height=2,cursor="hand2")
    botonBatalla.config(font="Consolas 20 bold",bg="#dd3536",fg="White")
    botonBatalla.place(x=350,y=365)

    botonMaleta=Button(frameCombate,text="MALETA",command=lambda:moduloMaleta(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,botonBatalla,barraVida1,barraVida2,vidaP1,vidaP2))
    botonMaleta.config(width=9,height=2)
    botonMaleta.config(font="Consolas 20 bold",bg="#cd8e2b",fg="White",cursor="hand2")
    botonMaleta.config(highlightcolor="Black",highlightbackground="Black")
    botonMaleta.place(x=510,y=365)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaCombate.destroy()

    ventanaCombate.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaCombate.mainloop()

#ATAQUES PERSONALES

def ataqueP1(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,nombrePoder,barraVida1,barraVida2,vidaP1,vidaP2,RetornarLucha,turno):

        global idP1,idP2,ListaPoderesP1
        global SaludP1,SaludP2,SaludP1Falsa,SaludP2Falsa
        global lessDamage,moreDamage
        global turnosAtaques

        #AUMENTAR TURNOS

        if turno == 1:
            turnosAtaques[turno-1] = 1
        elif turno ==2:
            turnosAtaques[turno-1] = 1
        elif turno ==3: 
            turnosAtaques[turno-1] = 2
        elif turno ==4:
            turnosAtaques[turno-1] = 3

        #REDUCIR BLOQUEO DE ATAQUES

        for i in range(4):
            if turnosAtaques[i]>0 and i != turno-1:
                turnosAtaques[i]-=1

        nombrePoder=ListaPoderesP1[nombrePoder]

        #ARMADURA OPONENTE

        reductor:int=lessDamage[idP2]

        if SaludP1==0 or SaludP2==0:
            return
        
        #FUNCION

        def retornarAtaque():

            CuadroLucha1.place_forget()
            CuadroLucha2.place_forget()
            labelPregunta.place_forget()
            labelPregunta2.place_forget()
            botonRetorno.place_forget()

            ataqueP2(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,vidaP1,vidaP2)
            RetornarLucha()

        #LABELS ESTETICOS

        CuadroLucha1=Label(frameCombate)
        CuadroLucha1.config(width=45,height=8)
        CuadroLucha1.config(bg="#7d807e")
        CuadroLucha1.place(x=20,y=345)

        CuadroLucha2=Label(frameCombate)
        CuadroLucha2.config(width=49,height=8)
        CuadroLucha2.config(bg="#7d807e")
        CuadroLucha2.place(x=330,y=345)

        #AJUSTAR LA UBICACIÓN DEL NOMBRE

        PosicionX=35

        #TEXTO

        labelPregunta=Label(frameCombate)
        labelPregunta.config(text="{} uso {}".format(idP1,nombrePoder))
        labelPregunta.config(font="Didot 20 bold",bg="#7d807e",fg="White")
        labelPregunta.place(x= PosicionX ,y=370)

        labelPregunta2=Label(frameCombate)
        labelPregunta2.config(text="Su rival a sufrido {} de daño".format(int(clase_personajes.damagePoderes[nombrePoder]//reductor)))
        labelPregunta2.config(font="Didot 20 bold",bg="#7d807e",fg="White")
        labelPregunta2.place(x= PosicionX ,y=410)

        #CONFIGURAR VIDA OPONENTE

        SaludP2Falsa-= clase_personajes.damagePoderes[nombrePoder]//reductor
        SaludP2Falsa = int(SaludP2Falsa)

        if SaludP2Falsa<0:
            SaludP2Falsa=0

        SaludP2= int( (SaludP2Falsa*29)//1000 )
 
        if (SaludP2Falsa*29)/1000 >= 0.029 and SaludP2==0:
            SaludP2=1

        if SaludP2>0:
            barraVida2.config(width= SaludP2)

        vidaP2.set( "HP {}".format(SaludP2Falsa))

        #¿GANADOR?

        if SaludP2==0:
            retornarMapa(ventanaInicio,ventanaMapa,ventanaCombate)
            return

        #RETORNO

        botonRetorno=Button(frameCombate,text="\u00D7",command=lambda:retornarAtaque())
        botonRetorno.config(width=2,height=2,relief="groove",borderwidth=3)
        botonRetorno.config(font="Consolas 18 bold",bg="Red",fg="White",cursor="hand2")
        botonRetorno.place(x=630,y=345)

def ataqueP2(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,vidaP1,vidaP2):

    global SaludP1,SaludP1Falsa,SaludP2,SaludP2Falsa
    global ListaPoderesP2, idP2, damagePoderes
    global lessDamage,moreDamage,probPociones

    nombrePoder:str="NULO"
    pocion:int=0

    #DAÑO RIVAL
    amplificador:int=moreDamage[idP2]

    #SELECCION ATAQUE
    
    inicial:int=probPociones[idP2][0]
    final:int=probPociones[idP2][1]

    seleccion:int=random.randint(5,7)
    seleccionPociones:int=random.randint(inicial,final)

    if seleccion == seleccionPociones:
        print(seleccion,seleccionPociones)
    else:
        seleccion:int=random.randint(1,4)

    if seleccion==1:
        nombrePoder="PODER 1"

    if seleccion==2:
        nombrePoder="PODER 2"

    if seleccion==3:
        nombrePoder="PODER 3"

    if seleccion==4:
        nombrePoder="PODER 4"
    
    if seleccion==5:
        pocion=100

    if seleccion==6:
        pocion=250

    if seleccion==7:
        pocion=500

    #VIDA JUGADOR

    nombrePoder = ListaPoderesP2[nombrePoder]

    SaludP1Falsa -=  clase_personajes.damagePoderes[nombrePoder] //amplificador 
    SaludP1Falsa = int(SaludP1Falsa)

    if SaludP1Falsa<0:
        SaludP1Falsa=0

    SaludP1= int((SaludP1Falsa*29)//1000)

    if (SaludP1Falsa*29)/1000 >= 0.029 and SaludP1==0:
        SaludP1=1

    if SaludP1>0:
        barraVida1.config(width= SaludP1)

    if SaludP1<0:
        SaludP1=0
        barraVida1.place_forget()

    vidaP1.set( "HP {}".format(SaludP1Falsa))

    #------------------- MENSAJE ATAQUE OPONENTE ---------------

    def retornarAtaque():
            CuadroLucha1.place_forget()
            CuadroLucha2.place_forget()
            labelPregunta.place_forget()
            labelPregunta2.place_forget()
            botonRetorno.place_forget()

    #LABELS ESTETICOS

    CuadroLucha1=Label(frameCombate)
    CuadroLucha1.config(width=45,height=8)
    CuadroLucha1.config(bg="#7d807e")
    CuadroLucha1.place(x=20,y=345)

    CuadroLucha2=Label(frameCombate)
    CuadroLucha2.config(width=49,height=8)
    CuadroLucha2.config(bg="#7d807e")
    CuadroLucha2.place(x=330,y=345)

    #UBICACION TEXTO

    PosicionX=35
    PosicionY=370
    PosicionY2=410
        
    #TEXTO EN PANTALLA

    if pocion == 0:
        fraseTexto:str="{} uso {}".format(idP2, nombrePoder)
        fraseTexto2:str="Has sufrido {} de daño".format(int(clase_personajes.damagePoderes[nombrePoder] //amplificador))
    else:
        fraseTexto:str="{} ha usado una poción".format(idP2)
        fraseTexto2:str="Ha recuperado {} HP".format(pocion)
        PosicionX=35

        SaludP2Falsa =  SaludP2Falsa+pocion if (SaludP2Falsa>0 and SaludP2Falsa<=1000-pocion) else 1000

        if SaludP2Falsa<0:
            SaludP2Falsa=0

        SaludP2= (SaludP2Falsa*29)//1000

        if (SaludP2Falsa*29)/1000 >= 0.00029 and SaludP2==0:
            SaludP2=1

        barraVida2.config(width= SaludP2)

        vidaP2.set("HP {}".format(SaludP2Falsa))


    labelPregunta=Label(frameCombate)
    labelPregunta.config(text=fraseTexto)
    labelPregunta.config(font="Didot 20 bold",bg="#7d807e",fg="White")
    labelPregunta.place(x= PosicionX ,y=PosicionY)

    labelPregunta2=Label(frameCombate)
    labelPregunta2.config(text=fraseTexto2)
    labelPregunta2.config(font="Didot 20 bold",bg="#7d807e",fg="White")
    labelPregunta2.place(x= PosicionX ,y=PosicionY2)

    #¿GANADOR?

    if SaludP1==0:
        barraVida1.place_forget()
        popPerdiste(ventanaInicio,ventanaMapa,ventanaCombate)

    #RETORNO

    botonRetorno=Button(frameCombate,text="\u00D7",command=lambda:retornarAtaque())
    botonRetorno.config(width=2,height=2,relief="groove",borderwidth=3)
    botonRetorno.config(font="Consolas 18 bold",bg="Red",fg="White",cursor="hand2")
    botonRetorno.place(x=630,y=345)

#INVENTARIO

def mensajeInventario(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,cantidad,vidaP1,vidaP2):

        global SaludP1,SaludP2
        global turnosAtaques

        #REDUCIR BLOQUEO DE ATAQUES

        for i in range(4):
            if turnosAtaques[i]>0:
                turnosAtaques[i]-=1

        #MENSAJE EN PANTALLA

        if SaludP1==0 or SaludP2==0:
            return

        def retornarAtaque():
            CuadroLucha1.place_forget()
            CuadroLucha2.place_forget()
            labelPregunta.place_forget()
            botonRetorno.place_forget()
            ataqueP2(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,vidaP1,vidaP2)

        CuadroLucha1=Label(frameCombate)
        CuadroLucha1.config(width=45,height=8)
        CuadroLucha1.config(bg="#7d807e")
        CuadroLucha1.place(x=20,y=345)

        CuadroLucha2=Label(frameCombate)
        CuadroLucha2.config(width=49,height=8)
        CuadroLucha2.config(bg="#7d807e")
        CuadroLucha2.place(x=330,y=345)
        
        #TEXTO

        labelPregunta=Label(frameCombate)
        labelPregunta.config(text="Has usado una poción de {} HP".format(cantidad))
        labelPregunta.config(font="Didot 20 bold",bg="#7d807e",fg="White")
        labelPregunta.place(x=35,y=370)

        #RETORNO

        botonRetorno=Button(frameCombate,text="\u00D7",command=lambda:retornarAtaque())
        botonRetorno.config(width=2,height=2,relief="groove",borderwidth=3)
        botonRetorno.config(font="Consolas 18 bold",bg="Red",fg="White",cursor="hand2")
        botonRetorno.place(x=630,y=345)

#VENTANAS DESPLEGABLES

def moduloLucha(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,vidaP1,vidaP2):

        global ListaPoderesP1
        global turnosAtaques

        def RetornarLucha():
            CuadroLucha1.place_forget()
            CuadroLucha2.place_forget()
            botonRetorno.place_forget()
            botonPoder1.place_forget()
            botonPoder2.place_forget()
            botonPoder3.place_forget()
            botonPoder4.place_forget()

        #LABELS ESTETICOS

        CuadroLucha1=Label(frameCombate)
        CuadroLucha1.config(width=45,height=8)
        CuadroLucha1.config(bg="#7d807e")
        CuadroLucha1.place(x=20,y=345)

        CuadroLucha2=Label(frameCombate)
        CuadroLucha2.config(width=49,height=8)
        CuadroLucha2.config(bg="#7d807e")
        CuadroLucha2.place(x=330,y=345)

        #BOTONES

        botonRetorno=Button(frameCombate,text="\u25C0",command=lambda:RetornarLucha())
        botonRetorno.config(width=5,height=2,relief="groove",borderwidth=3)
        botonRetorno.config(font="Consolas 18 bold",bg="#3f403f",fg="White",cursor="hand2")
        botonRetorno.place(x=50,y=370)

        botonPoder1=Button(frameCombate,text=ListaPoderesP1["PODER 1"],command=lambda:ataqueP1(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,"PODER 1",barraVida1,barraVida2,vidaP1,vidaP2,RetornarLucha,1))
        botonPoder1.config(width=18,height=1,relief="groove",borderwidth=3)
        botonPoder1.config(font="Consolas 18 bold",bg="#dd3536",fg="White",cursor="hand2")
        botonPoder1.place(x=150,y=355)

        botonPoder2=Button(frameCombate,text=ListaPoderesP1["PODER 2"],command=lambda:ataqueP1(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,"PODER 2",barraVida1,barraVida2,vidaP1,vidaP2,RetornarLucha,2))
        botonPoder2.config(width=18,height=1,relief="groove",borderwidth=3)
        botonPoder2.config(font="Consolas 18 bold",bg="#cd8e2b",fg="White",cursor="hand2")
        botonPoder2.place(x=150,y=412)

        botonPoder3=Button(frameCombate,text=ListaPoderesP1["PODER 3"],command=lambda:ataqueP1(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,"PODER 3",barraVida1,barraVida2,vidaP1,vidaP2,RetornarLucha,3))
        botonPoder3.config(width=18,height=1,relief="groove",borderwidth=3)
        botonPoder3.config(font="Consolas 18 bold",bg="#29771c",fg="White",cursor="hand2")
        botonPoder3.place(x=410,y=355)

        botonPoder4=Button(frameCombate,text=ListaPoderesP1["PODER 4"],command=lambda:ataqueP1(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,"PODER 4",barraVida1,barraVida2,vidaP1,vidaP2,RetornarLucha,4))
        botonPoder4.config(width=18,height=1,relief="groove",borderwidth=3)
        botonPoder4.config(font="Consolas 18 bold",bg="#307daa",fg="White",cursor="hand2")
        botonPoder4.place(x=410,y=412)

        #DESACTIVAR BOTONES

        if turnosAtaques[0] > 0:
            botonPoder1.config(state=DISABLED)

        if turnosAtaques[1] > 0:
            botonPoder2.config(state=DISABLED)

        if turnosAtaques[2] > 0:
            botonPoder3.config(state=DISABLED)

        if turnosAtaques[3] > 0:
            botonPoder4.config(state=DISABLED)

        ventanaCombate.mainloop()

def moduloMaleta(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,botonBatalla,barraVida1,barraVida2,vidaP1,vidaP2):

    def RetornarMochila():
        labelFondo.place_forget()
        labelBlanco.place_forget()
        lineaInventario.place_forget()
        textoInventario.place_forget()
        botonRetorno.place_forget()
        botonBatalla.config(state=NORMAL)

        botonUsar.place_forget()
        pocionHP100.place_forget()
        pocionHP250.place_forget()
        pocionHP500.place_forget()     
    
    def usarObjeto():

        global SaludP1,SaludP1Falsa
        cantidad:int=0

        if varOpcion.get()==1 and ListaInventario["pocionHP100"]>0:

            SaludP1Falsa = SaludP1Falsa+100 if (SaludP1Falsa>0 and SaludP1Falsa<=900) else 1000
            SaludP1= (SaludP1Falsa*29)//1000
            barraVida1.config(width=SaludP1)
            cantidad=100

            ListaInventario["pocionHP100"]= ListaInventario["pocionHP100"]-1

        if varOpcion.get()==2 and ListaInventario["pocionHP250"]>0:
            
            SaludP1Falsa = SaludP1Falsa+250 if (SaludP1Falsa>0 and SaludP1Falsa<=750) else 1000
            SaludP1= (SaludP1Falsa*29)//1000
            barraVida1.config(width=SaludP1)
            cantidad=250

            ListaInventario["pocionHP250"]= ListaInventario["pocionHP250"]-1

        if varOpcion.get()==3 and ListaInventario["pocionHP500"]>0:
            
            SaludP1Falsa = SaludP1Falsa+500 if (SaludP1Falsa>0 and SaludP1Falsa<=500) else 1000
            SaludP1= (SaludP1Falsa*29)//1000
            barraVida1.config(width=SaludP1)
            cantidad=500

            ListaInventario["pocionHP500"]= ListaInventario["pocionHP500"]-1

        if cantidad!=0:
            mensajeInventario(ventanaInicio,ventanaMapa,ventanaCombate,frameCombate,barraVida1,barraVida2,cantidad,vidaP1,vidaP2)

        vidaP1.set( "HP "+str(SaludP1Falsa))

        RetornarMochila()

    botonBatalla.config(state=DISABLED)

    #LABELS ESTETICOS

    labelFondo=Label(frameCombate)
    labelFondo.config(bg="#3f403f",width=72,height=20)
    labelFondo.place(x=100,y=10)

    labelBlanco=Label(frameCombate)
    labelBlanco.config(bg="White",width=69,height=18)
    labelBlanco.place(x=110,y=25)

    lineaInventario=Label(frameCombate)
    lineaInventario.config(bg="#8fb8d2",width=69,height=4)
    lineaInventario.place(x=110,y=25)

    textoInventario=Label(frameCombate,text="INVENTARIO")
    textoInventario.config(bg="#8fb8d2",font="Consolas 25 bold",fg="Black")
    textoInventario.place(x=140,y=35)

    botonRetorno=Button(frameCombate,text="\u00D7",command=lambda:RetornarMochila())
    botonRetorno.config(width=2,height=1,relief="groove",borderwidth=3)
    botonRetorno.config(font="Consolas 18 bold",bg="Red",fg="White",cursor="hand2")
    botonRetorno.place(x=550,y=25)

    botonUsar=Button(frameCombate,text="Usar",command=lambda:usarObjeto())
    botonUsar.config(width=8,height=1,relief="groove",borderwidth=3)
    botonUsar.config(font="Consolas 18 bold",bg="Green",fg="White",cursor="hand2")
    botonUsar.place(x=300,y=240)

    #BUTTONS RADIO

    varOpcion=IntVar()
    varOpcion.set(0)

    pocionHP100 = Radiobutton(frameCombate,text="Poción 100HP - Disponible {}".format( ListaInventario["pocionHP100"] ) ,variable= varOpcion,value=1)
    pocionHP100.config(font="Consolas 20",bg="White")
    pocionHP100.place(x=120,y=100)

    pocionHP250 = Radiobutton(frameCombate,text="Poción 250HP - Disponible {}".format( ListaInventario["pocionHP250"] ) ,variable= varOpcion,value=2)
    pocionHP250.config(font="Consolas 20",bg="White")
    pocionHP250.place(x=120,y=140)

    pocionHP500 = Radiobutton(frameCombate,text="Poción 500HP - Disponible {}".format( ListaInventario["pocionHP500"] ) ,variable= varOpcion, value=3)
    pocionHP500.config(font="Consolas 20",bg="White")
    pocionHP500.place(x=120,y=180)

#---------------------------
#---------------------------
#---------------------------
#---------------------------
##PROBAR MODULO

"""
ventanaInicio=0
ventanaMapa=0
mochila= clase_personajes.jugadorP.getDatos(5)

nameP1:str= clase_personajes.jugadorP.getDatos(1)
nameP2:str= clase_personajes.diosPandora.getDatos(1)

id_P1:str= clase_personajes.jugadorP.getDatos(2)
id_P2:str= clase_personajes.diosPandora.getDatos(2)

poderesP1:dict=clase_personajes.jugadorP.getDatos(6)
poderesP2:dict=clase_personajes.diosPandora.getDatos(6)

foto1:str= clase_personajes.jugadorP.getDatos(8)
foto2:str= clase_personajes.diosPandora.getDatos(8)

fondo:str="imagenes\\bg_olimpo.png"

cargarCombate(ventanaInicio,ventanaMapa,nameP1,nameP2,id_P1,id_P2,poderesP1,poderesP2,mochila,foto1,foto2,fondo)
"""
