
#Librerías
from tkinter import *
from tkinter import messagebox
import os
import modulo_historia3
from pygame import mixer


#Cargar contenido multimedia y códigos
#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

#La función para llamar la historia introductoria
def cargarhistoria2(ventanaInicio, id_P, ventanahistoria):
    #PANTALLA INICIAL: los tres personajes tienen diferente historia
    #Creación ventana
    ventanaInicio.withdraw()
    ventanahistoria.withdraw()
    ventanahistoria2=Toplevel(ventanaInicio)
    ventanahistoria2.title("Olympus on fire")
    ventanahistoria2.resizable(0,0)

    #Tamaño de la historia
    anchoVentana:int=700
    altoVentana:int=520
    #tamaño x y tamaño y de la ventana
    #winfo: Devuelve el número de píxeles del ancho/alto de la pantalla de este widget en píxeles.
    xPos=ventanahistoria2.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanahistoria2.winfo_screenheight()//2-altoVentana//2-50
    #geometry: Método para establecer las dimensiones de la ventana tk y establecer posición en escritorio
    ventanahistoria2.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanahistoria2.iconbitmap("imagenes\\logo.ico")

    #FRAME 1
    framehistoria2=Frame(ventanahistoria2, width=anchoVentana,height=altoVentana)
    framehistoria2.pack()

    
    #Info-Menú
    #Información de creadores
    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanahistoria2)
    ventanahistoria2.config(menu=menuInicio)
    #Label: etiqueta de texto
    #add_cascade: para desplegar el menú
    #command: comando del menú de la función /lo que va a ir escrito)
    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #FONDO
    #Imagen fondo
    fondo_historia= PhotoImage(file="imagenes\\historia\\fondoHistoria.png")
    #Fondo
    etiquetafondo=Label(framehistoria2,image=fondo_historia)
    etiquetafondo.config(width=700,height=500)
    etiquetafondo.place(x=0,y=0)

    #BOTON
    #Boton siguiente
    def verHistoria_next():
        modulo_historia3.cargarhistoria3(ventanaInicio,id_P,ventanahistoria2)

    botonnext=Button(framehistoria2,text="Siguiente", command=verHistoria_next)
    botonnext.config(font="Consolas 14 bold",cursor="hand2",relief="groove", fg="green")
    botonnext.config(width=10,height=1)
    botonnext.place(x=560, y=415)

    #Boton atrás
    def retornar():
        ventanahistoria2.destroy()
        ventanahistoria.deiconify()

    botonvolver=Button(framehistoria2,text="Volver", command=retornar)
    botonvolver.config(font="Consolas 14 bold",cursor="hand2",relief="groove")
    botonvolver.config(width=10,height=1)
    botonvolver.place(x=17, y=415)


    #VARIABLES

    variable_parraf1=Text(framehistoria2)
    variable_parraf1.config(font="Consolas 15")
    variable_parraf1.config(width=35,height=7)
    variable_parraf1.place(x=288,y=25)

    variable_parraf2=Text(framehistoria2)
    variable_parraf2.config(font="Consolas 15")
    variable_parraf2.config(width=35, height=7)
    variable_parraf2.place(x=25, y=215)    
    
    #Condicional para agregar la historia especifica del personaje escogido por el usuario

    if id_P=="Lumna":
        parraf1:str="""
 Lumna desde su infancia fue 
 sometida a un arduo entrenamiento,
 la exigencia de su padre, Odín, 
 fue orientada a ser la mejor diosa
 y hechicera en todos los aspectos.
     """
        variable_parraf1.insert(INSERT, parraf1)
        variable_parraf1.config(state=DISABLED)

        parraf2:str="""
 Es por ello que llegó a Grecia, 
 con el objetivo de cumplir los 
 caprichos de su padre y conocer 
 nuevas maneras técnicas para 
 manejar sus poderes
     """
        variable_parraf2.insert(INSERT, parraf2)
        variable_parraf2.config(state=DISABLED)

        #IMAGENES
        lumna1=PhotoImage(file="imagenes\\historia\\Lumna\\Lumna1.png")
        lumna1=lumna1.subsample(3)
        imagen_lumna1=Label(framehistoria2, image=lumna1)
        imagen_lumna1.place(x=25, y=25)

        lumna2=PhotoImage(file="imagenes\\historia\\Lumna\\Lumna2.png")
        lumna2=lumna2.subsample(3)
        imagen_lumna2=Label(framehistoria2, image=lumna2)
        imagen_lumna2.place(x=430, y=215)

    elif id_P=="Fobos":
        parraf1:str="""
 Fobos siempre fue el niño más 
 preciado del que era su padre,
 Hefesto, vivió toda su vida junto
 a él, a la sombra de una madre
 descuidada.
     """
        variable_parraf1.insert(INSERT, parraf1)
        variable_parraf1.config(state=DISABLED)

        parraf2:str="""
 Todo antes de que se enterara de
 que él en realidad no era su
 padre, siendo humillados por
 el Olimpo entero, su orgullo
 y dignidad destruidos...
     """
        variable_parraf2.insert(INSERT, parraf2)
        variable_parraf2.config(state=DISABLED)

        #Imagenes
        fobos1=PhotoImage(file="imagenes\\historia\\Fobos\\Fobos1.png")
        fobos1=fobos1.subsample(3)
        imagen_fobos1=Label(framehistoria2, image=fobos1)
        imagen_fobos1.place(x=25, y=25)
        
        fobos2=PhotoImage(file="imagenes\\historia\\Fobos\\Fobos2.png")
        fobos2=fobos2.subsample(3)
        imagen_fobos2=Label(framehistoria2, image=fobos2)
        imagen_fobos2.place(x=430, y=215)

    elif id_P=="Amalene":
        parraf1:str="""
 Amalene siempre había pertenecido
 a Japón, tierra natal de su madre,
 donde estuvo su infancia y
 adolescencia sin conocer a su
 otra progenitora.
     """
        variable_parraf1.insert(INSERT, parraf1)
        variable_parraf1.config(state=DISABLED)

        parraf2:str="""
 Poco antes de obtener finalmente
 sus poderes de diosa en un ritual
 después de un entrenamiento arduo,
 fue interrumpida por la confesión
 de su madre Amaterasu...
     """
        variable_parraf2.insert(INSERT, parraf2)
        variable_parraf2.config(state=DISABLED)

        #Imagenes
        amalene1=PhotoImage(file="imagenes\\historia\\Amalene\\Amalene1.png")
        amalene1=amalene1.subsample(3)
        imagen_amalene1=Label(framehistoria2, image=amalene1)
        imagen_amalene1.place(x=25, y=25)
        
        amalene2=PhotoImage(file="imagenes\\historia\\Amalene\\Amalene2.png")
        amalene2=amalene2.subsample(3)
        imagen_amalene2=Label(framehistoria2, image=amalene2)
        imagen_amalene2.place(x=430, y=215)
    
    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanahistoria2.destroy()

    ventanahistoria2.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanahistoria2.mainloop()

