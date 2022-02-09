
# Librerías
from tkinter import *
from tkinter import messagebox
import os
import modulo_mapa
import clase_personajes
from pygame import mixer

os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

def cargarRetorno(ventanaInicio,ventanaMapa,nivelGlobal):

    if nivelGlobal ==10:

        ventanaretorno=Toplevel(ventanaMapa)
        ventanaretorno.title("Olympus on fire")
        ventanaretorno.resizable(0,0)
        
        #Tamaño de la historia
        anchoVentana:int=700
        altoVentana:int=500

        xPos=ventanaretorno.winfo_screenwidth()//2-anchoVentana//2
        yPos=ventanaretorno.winfo_screenheight()//2-altoVentana//2-50

        ventanaretorno.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))
        
        #FRAME 
    
        frameretorno=Frame(ventanaretorno, width=anchoVentana,height=altoVentana)
        frameretorno.pack()

        def popInfo():
            mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

            messagebox.showinfo("Creadores",mensaje)

        menuInicio= Menu(ventanaretorno)
        ventanaretorno.config(menu=menuInicio)

        menuInicio.add_cascade(label="Info",command=lambda:popInfo())

        #IMAGENES
        fondo_historia= PhotoImage(file="imagenes\\bg_inicial.png")
        lumna=PhotoImage(file="imagenes\\retorno\\Lumna1.png")
        amalene=PhotoImage(file="imagenes\\retorno\\Amalene1.png")
        fobos=PhotoImage(file="imagenes\\retorno\\Fobos1.png")

        #LABEL

        etiquetafondo=Label(frameretorno,image=fondo_historia)
        etiquetafondo.config(width=700,height=500)
        etiquetafondo.place(x=0,y=0)

        titulofeliz=Label(frameretorno,text="¡FELICITACIONES!")
        titulofeliz.config(bg="White", font="Consolas 35 bold")
        titulofeliz.place(x=140, y=20)

        avisofeliz=Label(frameretorno,text="¡Derrotaste a todo el Olímpo, eres un gran guerrero!")
        avisofeliz.config(bg="White", font="Consolas 15")
        avisofeliz.place(x=60, y=90)

        culminacionhistoria=Label(frameretorno, text="Terminemos la historia de este gran guerrero...")
        culminacionhistoria.config(bg="White", font="Consolas 15")
        culminacionhistoria.place(x=77, y=130)

        pregunta=Label(frameretorno, text="¿Quieres volver a jugar desde cero?")
        pregunta.config(bg="White", fg="Purple", font="Consolas 15")
        pregunta.place(x=150, y=380)

        #TEXTO

        final=Text(frameretorno)
        final.config(font="Consolas 15")
        final.config(width=38,height=8)
        final.place(x=17,y=170)

        id_P=clase_personajes.jugadorP.getDatos(2)

        if id_P=="Lumna":
            frase:str="""
 Batalla por batalla, ella se dió 
 cuenta de la manipulación a la que
 estaba sometida por su propio padre,
 decidió entonces terminar su trabajo
 como diosa pero no lo haría por 
 su familia, sino por ella misma.  
    """
            final.insert(INSERT, frase)
            final.config(state=DISABLED)

            lumna=lumna.subsample(3)
            imagen_lumna=Label(frameretorno, image=lumna)
            imagen_lumna.place(x=455, y=170)

        elif id_P=="Fobos":
            frase:str="""
 Durante su recorrido, el rencor por 
 el Olimpo se fue apagando, ya no lo
 satisfacía. Ahí se cuando se dió 
 cuenta que algo tan grande no debía
 ser por algo pequeño. Su ambición de
 poder determinó su triunfo.
    """
            final.insert(INSERT, frase)
            final.config(state=DISABLED)
            #Imagenes
            
            fobos=fobos.subsample(3)
            imagen_fobos=Label(frameretorno, image=fobos)
            imagen_fobos.place(x=455, y=170)

        elif id_P=="Amalene":
            frase:str="""
 En un papiro estaba escrito, su
 segunda madre era Selene, titán
 griega. Ella pertenecía al Olímpo
 que iba a destruir, los dioses no 
 eran como sus progenitoras, era su
 deber cambiar ello, y lo logró.
    """
            final.insert(INSERT, frase)
            final.config(state=DISABLED)
            #Imagenes
            amalene=amalene.subsample(3)
            imagen_amalene=Label(frameretorno, image=amalene)
            imagen_amalene.place(x=455, y=170)
    
    #BOTONES
    #botón donde vuelve a jugar desde 0
        
        def reiniciarJuego():

            mixer.init()
            mixer.stop()
            mixer.music.load("musica\\musica_epica.mp3")
            mixer.music.set_volume(0.2)

            mixer.music.play(loops=-1)

            ventanaretorno.destroy()
            ventanaInicio.deiconify()
            

        botonsi=Button(frameretorno,text="Sí", command=reiniciarJuego)
        botonsi.config(font="Consolas 14 bold",cursor="hand2",relief="groove", fg="green")
        botonsi.config(width=5,height=1)
        botonsi.place(x=280, y=415)

        def continuarJuego():
            ventanaMapa.deiconify()
            ventanaretorno.destroy()

        botonno=Button(frameretorno,text="No", command=continuarJuego)
        botonno.config(font="Consolas 14 bold",cursor="hand2",relief="groove")
        botonno.config(width=5,height=1)
        botonno.place(x=380, y=415)
        
        ventanaretorno.mainloop()

        def cerrarPrograma():
            print("PROGRAMA FINALIZADO")
            mixer.music.stop()
            mixer.quit()
            ventanaretorno.destroy()

        ventanaretorno.protocol("WM_DELETE_WINDOW", cerrarPrograma)
    
    else:
        ventanaMapa.deiconify()

#cargarRetorno()