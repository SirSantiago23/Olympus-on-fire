from tkinter import messagebox
from tkinter import *
import os
import clase_personajes
import modulo_tutorial
from pygame import mixer

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

def cargarhistoria3(ventanaInicio, id_P, ventanahistoria2):
    #última ventana de historia de esta sección (al finalizar el juego habrá otra ventana de historia)
    ventanahistoria2.withdraw()
    ventanahistoria3=Toplevel(ventanaInicio)
    ventanahistoria3.title("Olympus on fire")
    ventanahistoria3.resizable(0,0)

    #Tamaño de la historia
    anchoVentana:int=700
    altoVentana:int=520
    #tamaño x y tamaño y de la ventana
    #winfo: Devuelve el número de píxeles del ancho/alto de la pantalla de este widget en píxeles.
    xPos=ventanahistoria3.winfo_screenwidth()//2-anchoVentana//2
    yPos=ventanahistoria3.winfo_screenheight()//2-altoVentana//2-50
    #geometry: Método para establecer las dimensiones de la ventana tk y establecer posición en escritorio
    ventanahistoria3.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))

    ventanahistoria3.iconbitmap("imagenes\\logo.ico")

    #FRAME 
    framehistoria3=Frame(ventanahistoria3, width=anchoVentana,height=altoVentana)
    framehistoria3.pack()

    
    #Info-Menú
    #Información de creadores
    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanahistoria3)
    ventanahistoria3.config(menu=menuInicio)
    #Label: etiqueta de texto
    #add_cascade: para desplegar el menú
    #command: comando del menú de la función /lo que va a ir escrito)
    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #FONDO
    #Imagen fondo
    fondo_historia= PhotoImage(file="imagenes\\historia\\fondoHistoria.png")
    #Fondo
    etiquetafondo=Label(framehistoria3,image=fondo_historia)
    etiquetafondo.config(width=700,height=500)
    etiquetafondo.place(x=0,y=0)

    def cargarModuloTutorial(ventanaInicio):

        modulo_tutorial.cargarTutorial(ventanaInicio,ventanahistoria3)

    #BOTONES
    botonnext=Button(framehistoria3,text="Siguiente",command=lambda:cargarModuloTutorial(ventanaInicio))
    botonnext.config(font="Consolas 14 bold",cursor="hand2",relief="groove", fg="green")
    botonnext.config(width=10,height=1)
    botonnext.place(x=560, y=415)

    #Boton atrás
    def retornar():
        ventanahistoria3.destroy()
        ventanahistoria2.deiconify()

    botonvolver=Button(framehistoria3,text="Volver", command=retornar)
    botonvolver.config(font="Consolas 14 bold",cursor="hand2",relief="groove")
    botonvolver.config(width=10,height=1)
    botonvolver.place(x=17, y=415)

    #Texto #ESTANDAR
    frase3=Text(framehistoria3)
    frase3.config(font="Consolas 15")
    frase3.config(width=60,height=7)
    frase3.place(x=17,y=20)

    if id_P=="Lumna":
        frase_3:str="""
 Odín le había dado un poco de libertad con la condición
 de lograr acortar el Panteón, y así brindarles más poder 
 en el mismo. Su vida ya estaba planeada por su padre,
 cada paso que ella realizaba, cada pensamiento que tenía...
 ¿Seguirá teniendo su padre este control?
    """
        frase3.insert(INSERT, frase_3)
        frase3.config(state=DISABLED)

        #Imagenes
        lumna3=PhotoImage(file="imagenes\\historia\\Lumna\\Lumna3.png")
        lumna3=lumna3.subsample(3)
        imagen_lumna3=Label(framehistoria3, image=lumna3)
        imagen_lumna3.place(x=17, y=200)
        
        lumna4=PhotoImage(file="imagenes\\historia\\Lumna\\Lumna4.png")
        lumna4=lumna4.subsample(3)
        imagen_lumna4=Label(framehistoria3, image=lumna4)
        imagen_lumna4.place(x=341, y=200)

    elif id_P=="Fobos":
        frase_3:str="""
 Después de afrontar la dura traición de su madre, su plan 
 para vengarse empezó, un plan detallado batalla por 
 batalla que tendría que afrontar para destruir a las 
 deidades griegas, brindandole a su padre y a sí mismo el 
 poder que nunca tuvieron en Grecia y el Panteón.
    """
        frase3.insert(INSERT, frase_3)
        frase3.config(state=DISABLED)

        #Imagenes
        fobos3=PhotoImage(file="imagenes\\historia\\Fobos\\Fobos3.png")
        fobos3=fobos3.subsample(3)
        imagen_fobos3=Label(framehistoria3, image=fobos3)
        imagen_fobos3.place(x=17, y=200)
        
        fobos4=PhotoImage(file="imagenes\\historia\\Fobos\\Fobos4.png")
        fobos4=fobos4.subsample(3)
        imagen_fobos4=Label(framehistoria3, image=fobos4)
        imagen_fobos4.place(x=341, y=200)

    elif id_P=="Amalene":
        frase_3:str="""
 “Grecia te espera, debes arreglar el caos del Panteón para
 finalizar tu entrenamiento, solo así podrás obtener tus 
 poderes”. Fue así como Amalene llegó a Grecia, encontrando 
 una parte que su madre nunca le había contado, descubrió 
 su verdadero ser, uno totalemente desconocido…
    """
        frase3.insert(INSERT, frase_3)
        frase3.config(state=DISABLED)

        #Imagenes
        amalene3=PhotoImage(file="imagenes\\historia\\Amalene\\Amalene3.png")
        amalene3=amalene3.subsample(3)
        imagen_amalene3=Label(framehistoria3, image=amalene3)
        imagen_amalene3.place(x=17, y=200)
        
        amalene4=PhotoImage(file="imagenes\\historia\\Amalene\\Amalene4.png")
        amalene4=amalene4.subsample(3)
        imagen_amalene4=Label(framehistoria3, image=amalene4)
        imagen_amalene4.place(x=341, y=200)

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanahistoria3.destroy()

    ventanahistoria3.protocol("WM_DELETE_WINDOW", cerrarPrograma)

    ventanahistoria3.mainloop()
