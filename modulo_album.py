from distutils import command
from tkinter import *
from tkinter import messagebox
from pygame import mixer
import os
import clase_personajes

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

__contador:int=0

def retornarMapa(ventanaMapa, ventanaAlbum):
    ventanaMapa.deiconify()
    ventanaAlbum.destroy()

def cargarAlbum(ventanaMapa):

    ventanaMapa.withdraw()

    #ROOT

    ventanaAlbum=Toplevel(ventanaMapa)
    ventanaAlbum.title("Olympus on fire")
    ventanaAlbum.resizable(0,0)

    #POSICIONANDO VENTANA

    anchoVentana = 700
    altoVentana = 500

    anchoVentana:int=700
    altoVentana:int=520

    xPos=ventanaAlbum.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanaAlbum.winfo_screenheight()//2-altoVentana//2-50

    ventanaAlbum.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanaAlbum.iconbitmap("imagenes\\logo.ico")

    #FRAME

    frameAlbum=Frame(ventanaAlbum,width=anchoVentana,height=altoVentana)
    frameAlbum.pack()

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

        - Zharick Pinzon Salamanca                     
        - Andrés Santiago Cañón
        - Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaAlbum)
    ventanaAlbum.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #IMAGENES

    fondo = PhotoImage(file="imagenes\\fondoAlbum.png")
    imgPersonaje = PhotoImage(file=clase_personajes.jugadorP.getDatos(8))
    imgZeus = PhotoImage(file=clase_personajes.diosZeus.getDatos(8))
    imgHades = PhotoImage(file=clase_personajes.diosHades.getDatos(8))
    imgPoseidon = PhotoImage(file=clase_personajes.diosPoseidon.getDatos(8))
    imgAtenea = PhotoImage(file=clase_personajes.diosAtenea.getDatos(8))
    imgAres = PhotoImage(file=clase_personajes.diosAres.getDatos(8))
    imgHercules = PhotoImage(file=clase_personajes.diosHercules.getDatos(8))
    imgHelios = PhotoImage(file=clase_personajes.diosHelios.getDatos(8))
    imgAfrodita = PhotoImage(file=clase_personajes.diosAfrodita.getDatos(8))
    imgArtemisa = PhotoImage(file=clase_personajes.diosArtemisa.getDatos(8))
    imgPandora = PhotoImage(file=clase_personajes.diosPandora.getDatos(8))

    imgPersonajeG = imgPersonaje.subsample(2)
    imgZeusG = imgZeus.subsample(2)
    imgHadesG = imgHades.subsample(2)
    imgPoseidonG = imgPoseidon.subsample(2)
    imgAteneaG = imgAtenea.subsample(2)
    imgAresG = imgAres.subsample(2)
    imgHerculesG = imgHercules.subsample(2)
    imgHeliosG = imgHelios.subsample(2)
    imgAfroditaG = imgAfrodita.subsample(2)
    imgArtemisaG = imgArtemisa.subsample(2)
    imgPandoraG = imgPandora.subsample(2)

    imgPersonaje = imgPersonaje.subsample(8)
    imgZeus = imgZeus.subsample(8)
    imgHades = imgHades.subsample(8)
    imgPoseidon = imgPoseidon.subsample(8)
    imgAtenea = imgAtenea.subsample(8)
    imgAres = imgAres.subsample(8)
    imgHercules = imgHercules.subsample(8)
    imgHelios = imgHelios.subsample(8)
    imgAfrodita = imgAfrodita.subsample(8)
    imgArtemisa = imgArtemisa.subsample(8)
    imgPandora = imgPandora.subsample(8)

    #VARIABLES

    
    nombrePersonaje = StringVar()
    nombrePersonaje.set(clase_personajes.jugadorP.getDatos(1))

    nombrePoder1 = StringVar()
    nombrePoder1.set("1. "+clase_personajes.jugadorP.getDatos(6)["PODER 1"])

    nombrePoder2 = StringVar()
    nombrePoder2.set("2. "+clase_personajes.jugadorP.getDatos(6)["PODER 2"])

    nombrePoder3 = StringVar()
    nombrePoder3.set("3. "+clase_personajes.jugadorP.getDatos(6)["PODER 3"])

    nombrePoder4 = StringVar()
    nombrePoder4.set("4. "+clase_personajes.jugadorP.getDatos(6)["PODER 4"])

    #----------------------------

    descripcionPoder1 = StringVar()
    descripcionPoder1.set(clase_personajes.jugadorP.getDatos(7)["PODER 1"])

    descripcionPoder2 = StringVar()
    descripcionPoder2.set(clase_personajes.jugadorP.getDatos(7)["PODER 2"])

    descripcionPoder3 = StringVar()
    descripcionPoder3.set(clase_personajes.jugadorP.getDatos(7)["PODER 3"])

    descripcionPoder4 = StringVar()
    descripcionPoder4.set(clase_personajes.jugadorP.getDatos(7)["PODER 4"])

    #LABEL

    fondoPrincipal = Label(frameAlbum,image=fondo)
    fondoPrincipal.pack()

    cuadroPersonaje = Label(frameAlbum, image=imgPersonajeG)
    cuadroPersonaje.place(x=50,y=140)

    textoNombre=Label(frameAlbum,textvariable=nombrePersonaje)
    textoNombre.config(font="Consolas 18 bold")
    textoNombre.place(x=383,y=125)

    textoPoderes=Label(frameAlbum,text="Habilidades")
    textoPoderes.config(font="Consolas 16 bold")
    textoPoderes.place(x=460,y=295)

    textoPoder1=Label(frameAlbum,textvariable= nombrePoder1)
    textoPoder1.config(font="Consolas 15 bold",cursor= "hand2")
    textoPoder1.place(x=392,y=330)

    textoPoder2=Label(frameAlbum,textvariable= nombrePoder2)
    textoPoder2.config(font="Consolas 15 bold",cursor= "hand2")
    textoPoder2.place(x=392,y=360)

    textoPoder3=Label(frameAlbum,textvariable= nombrePoder3)
    textoPoder3.config(font="Consolas 15 bold",cursor= "hand2")
    textoPoder3.place(x=392,y=390)

    textoPoder4=Label(frameAlbum,textvariable= nombrePoder4)
    textoPoder4.config(font="Consolas 15 bold",cursor= "hand2")
    textoPoder4.place(x=392,y=420)

    #CUADROS PERSONAJES

    cuadroRojo=Label(frameAlbum)
    cuadroRojo.config(bg="red",width=12,height=6)
    cuadroRojo.place(x=145,y=12)

    cuadro1=Label(frameAlbum,image=imgPersonaje)
    cuadro1.place(x=150,y=20)

    cuadro2=Label(frameAlbum,image=imgZeus)
    cuadro2.place(x=260,y=20)

    cuadro3=Label(frameAlbum,image=imgHades)
    cuadro3.place(x=370,y=20)

    cuadro4=Label(frameAlbum,image=imgPoseidon)
    cuadro4.place(x=480,y=20)

    #FUNCIONES

    def clasificadorImagenes(n):
        lista=[]
        listaFinal=[]
        for i in range(4):
            if n<=10:
                lista.append(n)
            else:
                n-=11
                lista.append(n)
            n+=1

        print(lista)

        for i in lista:
            if i ==0:
                listaFinal.append(imgPersonaje)
            if i ==1:
                listaFinal.append(imgZeus)
            if i ==2:
                listaFinal.append(imgHades)
            if i ==3:
                listaFinal.append(imgPoseidon)
            if i ==4:
                listaFinal.append(imgAtenea)
            if i ==5:
                listaFinal.append(imgAres)
            if i ==6:
                listaFinal.append(imgHercules)
            if i ==7:
                listaFinal.append(imgHelios)
            if i ==8:
                listaFinal.append(imgAfrodita)
            if i ==9:
                listaFinal.append(imgArtemisa)
            if i ==10:
                listaFinal.append(imgPandora)

        return listaFinal

    def cambiarImagen(n):

        descripcionPersonaje.config(state=NORMAL)

        global __contador
        __contador+=n

        if __contador>10:
            __contador=0
        elif __contador <0:
            __contador=10

        if __contador==0:
            cuadroPersonaje.config(image=imgPersonajeG)
            nombrePersonaje.set(clase_personajes.jugadorP.getDatos(1))

            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.jugadorP.getDatos(3))
            
            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.jugadorP.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.jugadorP.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.jugadorP.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.jugadorP.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.jugadorP.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.jugadorP.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.jugadorP.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.jugadorP.getDatos(7)["PODER 4"])

        if __contador==1:
            cuadroPersonaje.config(image=imgZeusG)
            nombrePersonaje.set(clase_personajes.diosZeus.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosZeus.getDatos(3))

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosZeus.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosZeus.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosZeus.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosZeus.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosZeus.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosZeus.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosZeus.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosZeus.getDatos(7)["PODER 4"])

        if __contador==2:
            cuadroPersonaje.config(image=imgHadesG)
            nombrePersonaje.set(clase_personajes.diosHades.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosHades.getDatos(3))
            cuadro1.config(image=imgHades)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosHades.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosHades.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosHades.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosHades.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosHades.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosHades.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosHades.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosHades.getDatos(7)["PODER 4"])

        if __contador==3:
            cuadroPersonaje.config(image=imgPoseidonG)
            nombrePersonaje.set(clase_personajes.diosPoseidon.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosPoseidon.getDatos(3))
            cuadro1.config(image=imgPoseidon)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosPoseidon.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosPoseidon.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosPoseidon.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosPoseidon.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosPoseidon.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosPoseidon.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosPoseidon.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosPoseidon.getDatos(7)["PODER 4"])

        if __contador==4:
            cuadroPersonaje.config(image=imgAteneaG)
            nombrePersonaje.set(clase_personajes.diosAtenea.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosAtenea.getDatos(3))
            cuadro1.config(image=imgAtenea)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosAtenea.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosAtenea.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosAtenea.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosAtenea.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosAtenea.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosAtenea.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosAtenea.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosAtenea.getDatos(7)["PODER 4"])

        if __contador==5:
            cuadroPersonaje.config(image=imgAresG)
            nombrePersonaje.set(clase_personajes.diosAres.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosAres.getDatos(3))
            cuadro1.config(image=imgAres)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosAres.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosAres.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosAres.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosAres.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosAres.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosAres.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosAres.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosAres.getDatos(7)["PODER 4"])

        if __contador==6:
            cuadroPersonaje.config(image=imgHerculesG)
            nombrePersonaje.set(clase_personajes.diosHercules.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosHercules.getDatos(3))
            cuadro1.config(image=imgHercules)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosHercules.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosHercules.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosHercules.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosHercules.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosHercules.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosHercules.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosHercules.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosHercules.getDatos(7)["PODER 4"])

        if __contador==7:
            cuadroPersonaje.config(image=imgHeliosG)
            nombrePersonaje.set(clase_personajes.diosHelios.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosHelios.getDatos(3))
            cuadro1.config(image=imgHelios)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosHelios.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosHelios.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosHelios.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosHelios.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosHelios.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosHelios.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosHelios.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosHelios.getDatos(7)["PODER 4"])

        if __contador==8:
            cuadroPersonaje.config(image=imgAfroditaG)
            nombrePersonaje.set(clase_personajes.diosAfrodita.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosAfrodita.getDatos(3))
            cuadro1.config(image=imgAfrodita)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosAfrodita.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosAfrodita.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosAfrodita.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosAfrodita.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosAfrodita.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosAfrodita.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosAfrodita.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosAfrodita.getDatos(7)["PODER 4"])

        if __contador==9:
            cuadroPersonaje.config(image=imgArtemisaG)
            nombrePersonaje.set(clase_personajes.diosArtemisa.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosArtemisa.getDatos(3))
            cuadro1.config(image=imgArtemisa)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosArtemisa.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosArtemisa.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosArtemisa.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosArtemisa.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosArtemisa.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosArtemisa.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosArtemisa.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosArtemisa.getDatos(7)["PODER 4"])

        if __contador==10:
            cuadroPersonaje.config(image=imgPandoraG)
            nombrePersonaje.set(clase_personajes.diosPandora.getDatos(1))
            descripcionPersonaje.delete("1.0",END)
            descripcionPersonaje.insert(INSERT,clase_personajes.diosPandora.getDatos(3))
            cuadro1.config(image=imgPandora)

            lista=clasificadorImagenes(__contador)

            cuadro1.config(image=lista[0])
            cuadro2.config(image=lista[1])
            cuadro3.config(image=lista[2])
            cuadro4.config(image=lista[3])

            nombrePoder1.set("1. "+clase_personajes.diosPandora.getDatos(6)["PODER 1"])
            nombrePoder2.set("2. "+clase_personajes.diosPandora.getDatos(6)["PODER 2"])
            nombrePoder3.set("3. "+clase_personajes.diosPandora.getDatos(6)["PODER 3"])
            nombrePoder4.set("4. "+clase_personajes.diosPandora.getDatos(6)["PODER 4"])

            descripcionPoder1.set(clase_personajes.diosPandora.getDatos(7)["PODER 1"])
            descripcionPoder2.set(clase_personajes.diosPandora.getDatos(7)["PODER 2"])
            descripcionPoder3.set(clase_personajes.diosPandora.getDatos(7)["PODER 3"])
            descripcionPoder4.set(clase_personajes.diosPandora.getDatos(7)["PODER 4"])

        descripcionPersonaje.config(state=DISABLED)
            
    #BOTONES

    botonAnterior=Button(frameAlbum,text="\u25C0",command=lambda:cambiarImagen(-1))
    botonAnterior.config(width=4,cursor="hand2")
    botonAnterior.config(font="Consolas 25")
    botonAnterior.place(x=50,y=26)

    botonSiguiente=Button(frameAlbum,text="\u25B6",command=lambda:cambiarImagen(1))
    botonSiguiente.config(width=4,cursor="hand2")
    botonSiguiente.config(font="Consolas 25")
    botonSiguiente.place(x=580,y=26)

    botonRetornar2=Button(ventanaAlbum,text="Volver",command=lambda:retornarMapa(ventanaMapa,ventanaAlbum))
    botonRetornar2.config(cursor="hand2",font="Consolas 15",bg="#dd3536")
    botonRetornar2.config(width=8,height=1)
    botonRetornar2.place(x=150,y=450)

    #TEXT

    descripcionPersonaje=Text(frameAlbum)
    descripcionPersonaje.config(font="Consolas 15")
    descripcionPersonaje.config(width=26,height=5)
    descripcionPersonaje.place(x=384,y=168)

    descripcion1:str=clase_personajes.jugadorP.getDatos(3)

    descripcionPersonaje.insert(INSERT,descripcion1)
    descripcionPersonaje.config(state=DISABLED)

    #EVENTO MENSAJE

    def mensajePoder1(event):
        titulo= nombrePoder1.get()
        titulo=titulo.replace("1. ","")
        messagebox.showinfo(titulo,descripcionPoder1.get())

    def mensajePoder2(event):
        titulo= nombrePoder2.get()
        titulo=titulo.replace("2. ","")
        messagebox.showinfo(titulo,descripcionPoder2.get())

    def mensajePoder3(event):
        titulo= nombrePoder3.get()
        titulo=titulo.replace("3. ","")
        messagebox.showinfo(titulo,descripcionPoder3.get())

    def mensajePoder4(event):
        titulo= nombrePoder4.get()
        titulo=titulo.replace("4. ","")
        messagebox.showinfo(titulo,descripcionPoder4.get())

    #EVENTO COLOR

    def colorPoder1(event):
        textoPoder1.config(bg="red")
    def uncolorPoder1(event):
        textoPoder1.config(bg="#f0f0f0")

    def colorPoder2(event):
        textoPoder2.config(bg="red")
    def uncolorPoder2(event):
        textoPoder2.config(bg="#f0f0f0")

    def colorPoder3(event):
        textoPoder3.config(bg="red")
    def uncolorPoder3(event):
        textoPoder3.config(bg="#f0f0f0")

    def colorPoder4(event):
        textoPoder4.config(bg="red")
    def uncolorPoder4(event):
        textoPoder4.config(bg="#f0f0f0")

    textoPoder1.bind("<Button-1>",mensajePoder1)
    textoPoder1.bind("<Enter>",colorPoder1)
    textoPoder1.bind("<Leave>",uncolorPoder1)

    textoPoder2.bind("<Button-1>",mensajePoder2)
    textoPoder2.bind("<Enter>",colorPoder2)
    textoPoder2.bind("<Leave>",uncolorPoder2)

    textoPoder3.bind("<Button-1>",mensajePoder3)
    textoPoder3.bind("<Enter>",colorPoder3)
    textoPoder3.bind("<Leave>",uncolorPoder3)

    textoPoder4.bind("<Button-1>",mensajePoder4)
    textoPoder4.bind("<Enter>",colorPoder4)
    textoPoder4.bind("<Leave>",uncolorPoder4)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaAlbum.destroy()

    ventanaAlbum.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaAlbum.mainloop()