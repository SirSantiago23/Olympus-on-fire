from tkinter import messagebox
from tkinter import *
import clase_personajes
import os
from pygame import mixer

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

def cargarLogros(ventanaMapa,numeroLogros):
    
    ventanaMapa.withdraw()

    ventanaLogros=Toplevel(ventanaMapa)
    ventanaLogros.title("Olympus on fire")
    ventanaLogros.resizable(0,0)

    anchoVentana = 700
    altoVentana = 500

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaLogros)
    ventanaLogros.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #CENTRAR VENTANA

    xPos = ventanaLogros.winfo_screenwidth()//2 - anchoVentana//2
    yPos = ventanaLogros.winfo_screenheight()//2 - altoVentana//2 - 50

    ventanaLogros.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanaLogros.iconbitmap("imagenes\\logo.ico")

    #IMAGENES 

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

    personajeSecreto = PhotoImage(file= "imagenes\\avatares\\personajeSecreto.png")
    fondoLogros = PhotoImage(file= "imagenes\\fondoLogros.png")

    imgZeus = imgZeus.subsample(5)
    imgHades = imgHades.subsample(5)
    imgPoseidon = imgPoseidon.subsample(5)
    imgAtenea = imgAtenea.subsample(5)
    imgAres = imgAres.subsample(5)
    imgHercules = imgHercules.subsample(5)
    imgHelios = imgHelios.subsample(5)
    imgAfrodita = imgAfrodita.subsample(5)
    imgArtemisa = imgArtemisa.subsample(5)
    imgPandora = imgPandora.subsample(5)
    personajeSecreto = personajeSecreto.subsample(5)

    #FUNCIONES

    def ubicarLogros(numeroLogros,listaImagenes,listaTextos):

        for i in range(numeroLogros,10):
            listaImagenes[i].config(image= personajeSecreto)
            listaTextos[i].place_forget()

    def funcionRetornar():
        ventanaLogros.destroy()
        ventanaMapa.deiconify()

    #LABEL

    fondo_ventana=Label(ventanaLogros,image=fondoLogros)
    fondo_ventana.config(width=700,height=500)
    fondo_ventana.place(x=0,y=0)

    #------- bloque superior

    dios1=Label(ventanaLogros,image=imgPandora)
    dios1.place(x=30,y=20)
    texto1 = Label(ventanaLogros,text="Derrotaste a Pandora")
    texto1.place(x=33,y=145)

    dios2=Label(ventanaLogros,image=imgArtemisa)
    dios2.place(x=200,y=20)
    texto2 = Label(ventanaLogros,text="Derrotaste a Artemisa")
    texto2.place(x=203,y=145)

    dios3=Label(ventanaLogros,image=imgAfrodita)
    dios3.place(x=370,y=20)
    texto3 = Label(ventanaLogros,text="Derrotaste a Afrodita")
    texto3.place(x=373,y=145)

    dios4=Label(ventanaLogros,image=imgHelios)
    dios4.place(x=540,y=20)
    texto4 = Label(ventanaLogros,text="Derrotaste a Helios")
    texto4.place(x=550,y=145)

    #-------bloque central

    dios5=Label(ventanaLogros,image=imgHercules)
    dios5.place(x=30,y=180)
    texto5 = Label(ventanaLogros,text="Derrotaste a Hercules")
    texto5.place(x=33,y=305)

    dios6=Label(ventanaLogros,image=imgAres)
    dios6.place(x=200,y=180)
    texto6 = Label(ventanaLogros,text="Derrotaste a Ares")
    texto6.place(x=215,y=305)

    dios7=Label(ventanaLogros,image=imgAtenea)
    dios7.place(x=370,y=180)
    texto7 = Label(ventanaLogros,text="Derrotaste a Atenea")
    texto7.place(x=378,y=305)

    dios8=Label(ventanaLogros,image=imgPoseidon)
    dios8.place(x=540,y=180)
    texto8 = Label(ventanaLogros,text="Derrotaste a Poseidon")
    texto8.place(x=542,y=305)

    #------bloque inferior

    dios9=Label(ventanaLogros,image=imgHades)
    dios9.place(x=200,y=340)
    texto9 = Label(ventanaLogros,text="Derrotaste a Hades")
    texto9.place(x=210,y=465)

    dios10=Label(ventanaLogros,image=imgZeus)
    dios10.place(x=370,y=340)
    texto10 = Label(ventanaLogros,text="Derrotaste a Zeus")
    texto10.place(x=385,y=465)

    #BOTONES

    botonRetornar=Button(ventanaLogros,text="Volver",command=funcionRetornar)
    botonRetornar.config(cursor="hand2",font="Consolas 15",bg="#7d807e")
    botonRetornar.config(width=10,height=3)
    botonRetornar.place(x=540,y=360)

    botonRetornar2=Button(ventanaLogros,text="Volver",command=funcionRetornar)
    botonRetornar2.config(cursor="hand2",font="Consolas 15",bg="#7d807e")
    botonRetornar2.config(width=10,height=3)
    botonRetornar2.place(x=31,y=360)

    #CARGAR LOGROS

    listaImagenes:list=[]
    listaTextos:list=[]

    listaImagenes.append(dios1)
    listaImagenes.append(dios2)
    listaImagenes.append(dios3)
    listaImagenes.append(dios4)
    listaImagenes.append(dios5)
    listaImagenes.append(dios6)
    listaImagenes.append(dios7)
    listaImagenes.append(dios8)
    listaImagenes.append(dios9)
    listaImagenes.append(dios10)

    listaTextos.append(texto1)
    listaTextos.append(texto2)
    listaTextos.append(texto3)
    listaTextos.append(texto4)
    listaTextos.append(texto5)
    listaTextos.append(texto6)
    listaTextos.append(texto7)
    listaTextos.append(texto8)
    listaTextos.append(texto9)
    listaTextos.append(texto10)

    ubicarLogros(numeroLogros,listaImagenes,listaTextos)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaLogros.destroy()

    ventanaLogros.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanaLogros.mainloop()


