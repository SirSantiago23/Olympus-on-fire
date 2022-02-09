from email.mime import image
from tkinter import *
from tkinter import messagebox
import os
import clase_personajes
import modulo_mapa
import random
from pygame import mixer
import modulo_retorno

#os.chdir("C:\\Users\\santi\\Documents\\1-Personal\\Cursos\\Programacion en Python\\Proyecto_Programacion")

nivelGlobal=0

def darPociones(ventanaInicio,ventanaMapa,levelP1:int): 

    global nivelGlobal
    nivelGlobal=levelP1
   
    ventanaPociones=Toplevel(ventanaMapa)
    ventanaPociones.title("Olympus on fire")
    ventanaPociones.resizable(0,0)
    anchoVentana:int= 700
    altoVentana:int= 500

    #IMAGENES

    pandora_muertef=PhotoImage(file= "imagenes\\derrotados\\pandora_muerte.png")
    artemisa_muertef= PhotoImage(file= "imagenes\\derrotados\\artemisa_muerte.png")
    afrodita_muertef= PhotoImage(file= "imagenes\\derrotados\\afrodita_muerte.png")
    helios_muertef= PhotoImage(file= "imagenes\\derrotados\\helios_muerte.png")
    hercules_muertef= PhotoImage(file= "imagenes\\derrotados\\hercules_muerte.png")
    ares_muertef= PhotoImage(file= "imagenes\\derrotados\\ares_muerte.png")
    atenea_muertef= PhotoImage(file = "imagenes\\derrotados\\atenea_muerte.png")
    poseidon_muertef= PhotoImage(file = "imagenes\\derrotados\\poseidon_muerte.png")
    hades_muertef= PhotoImage(file = "imagenes\\derrotados\\hades_muerte.png")
    zeus_muertef= PhotoImage(file= "imagenes\\derrotados\\zeus_muerte.png")

    pandora_muertef= pandora_muertef.subsample(1)
    artemisa_muertef= artemisa_muertef.subsample(1)
    zeus_muertef= zeus_muertef.subsample(1)
    afrodita_muertef= afrodita_muertef.subsample(1)
    helios_muertef= helios_muertef.subsample(1)
    hercules_muertef= hercules_muertef.subsample(1)
    ares_muertef= ares_muertef.subsample(1)
    atenea_muertef= atenea_muertef.subsample(1)
    poseidon_muertef= poseidon_muertef.subsample(1)
    hades_muertef= hades_muertef.subsample(1)

    #MENU

    def popInfo():

        mensaje:str="""Juego creado por:

- Zharick Pinzon Salamanca                     
- Andrés Santiago Cañón
- Mateo Bustos Aguilar
    """

        messagebox.showinfo("Creadores",mensaje)

    menuInicio= Menu(ventanaPociones)
    ventanaPociones.config(menu=menuInicio)

    menuInicio.add_cascade(label="Info",command=lambda:popInfo())

    #VARIABLES

    dios_actual=pandora_muertef
    dios= "Pandora"
    num_pociones = 0
    num_pociones2 = 0
    tipo_pocion= ""
    tipo_pocion2= ""
    nombrePocion=[]
    incremento1=0
    incremento2=0
    incremento3=0
    incremento4=0

    if levelP1 == 1:
        dios_actual= pandora_muertef
        dios= "Pandora"
        num_pociones= 1
        tipo_pocion= "pocionHP100"
        nombrePocion.append('HP100')

        incremento1=random.randint(5,7)
        incremento2=random.randint(5,7)
        incremento3=random.randint(5,7)
        incremento4=random.randint(10,15)
    
    if levelP1 == 2:
        dios_actual = artemisa_muertef
        dios = "Artemisa"
        num_pociones=2
        tipo_pocion= "pocionHP100"
        nombrePocion.append('HP100')

        incremento1=random.randint(5,7)
        incremento2=random.randint(5,7)
        incremento3=random.randint(5,7)
        incremento4=random.randint(10,15)
    
    if levelP1 == 3:
        dios_actual = afrodita_muertef
        dios= "Afrodita"
        num_pociones= 3 
        tipo_pocion= "pocionHP100"
        nombrePocion.append('HP100')

        incremento1=random.randint(5,7)
        incremento2=random.randint(5,7)
        incremento3=random.randint(5,7)
        incremento4=random.randint(10,15)

    if levelP1 == 4:
        dios_actual = helios_muertef
        dios = "Helios" 
        num_pociones= 2
        num_pociones2= 1
        tipo_pocion= "pocionHP100"  
        tipo_pocion2 ="pocionHP250"
        nombrePocion.append('HP100')
        nombrePocion.append('HP250')

        incremento1=random.randint(5,7)
        incremento2=random.randint(5,7)
        incremento3=random.randint(5,7)
        incremento4=random.randint(10,15)

    if levelP1 == 5:
        dios_actual = hercules_muertef
        dios= "Hercules"
        num_pociones= 3
        num_pociones2= 1
        tipo_pocion= "pocionHP100"
        tipo_pocion2= "pocionHP250"
        nombrePocion.append('HP100')
        nombrePocion.append('HP250')

        incremento1=random.randint(5,7)
        incremento2=random.randint(5,7)
        incremento3=random.randint(5,7)
        incremento4=random.randint(10,15)

    if levelP1 ==6:
        dios_actual= ares_muertef
        dios= "Ares"
        num_pociones= 4
        num_pociones2= 5
        tipo_pocion= "pocionHP100"
        tipo_pocion2= "pocionHP250"
        nombrePocion.append('HP100')
        nombrePocion.append('HP250')

        incremento1=random.randint(7,10)
        incremento2=random.randint(7,10)
        incremento3=random.randint(7,10)
        incremento4=random.randint(12,16)

    if levelP1 == 7:
        dios_actual= atenea_muertef
        dios= "Atenea"
        num_pociones= 5
        num_pociones2= 4
        tipo_pocion= "pocionHP100"
        tipo_pocion2= "pocionHP250"
        nombrePocion.append('HP100')
        nombrePocion.append('HP250')

        incremento1=random.randint(7,10)
        incremento2=random.randint(7,10)
        incremento3=random.randint(7,10)
        incremento4=random.randint(12,16)

    if levelP1 == 8:
        dios_actual= poseidon_muertef
        dios= "Poseidón"
        num_pociones= 5
        num_pociones2= 5
        tipo_pocion= "pocionHP250"
        tipo_pocion2= "pocionHP500"
        nombrePocion.append('HP250')
        nombrePocion.append('HP500')

        incremento1=random.randint(7,10)
        incremento2=random.randint(7,10)
        incremento3=random.randint(7,10)
        incremento4=random.randint(15,20)

    if levelP1 == 9:
        dios_actual= hades_muertef
        dios = "Hades"
        num_pociones= 3
        num_pociones2= 2
        tipo_pocion = "pocionHP250"
        tipo_pocion2= "pocionHP500"
        nombrePocion.append('HP250')
        nombrePocion.append('HP500')

        incremento1=random.randint(7,10)
        incremento2=random.randint(7,10)
        incremento3=random.randint(7,10)
        incremento4=random.randint(15,20)

    if levelP1 == 10:
        dios_actual= zeus_muertef
        dios= "Zeús"
        num_pociones= 6
        num_pociones2= 6
        tipo_pocion= "pocionHP250"
        tipo_pocion2= "pocionHP500"
        nombrePocion.append('HP250')
        nombrePocion.append('HP500')

        incremento1=random.randint(10,15)
        incremento2=random.randint(10,15)
        incremento3=random.randint(10,15)
        incremento4=random.randint(10,15)
    
    #CENTRAR VENTANA

    xPos = ventanaPociones.winfo_screenwidth()//2 - anchoVentana//2
    yPos = ventanaPociones.winfo_screenheight()//2 - altoVentana//2 - 50

    ventanaPociones.geometry("{}x{}+{}+{}".format(anchoVentana,altoVentana,xPos,yPos))
    ventanaPociones.iconbitmap("imagenes\\logo.ico")

    #FRAME
    
    framePrueba= Frame(ventanaPociones, width= anchoVentana, height= altoVentana)
    framePrueba.pack()
    #framePrueba.config(bg= "#3f403f")
    #framePociones.pack_propagate(False)
    #framePociones.grid_propagate(False)

    #LABEL
    
    labelFondo= Label(framePrueba, image= dios_actual)
    labelFondo.config(width=anchoVentana, height= altoVentana)
    labelFondo.pack_propagate(False)
    labelFondo.pack()
    
    labelVictoria= Label(framePrueba, text=f"Felicidades, has vencido a {dios} satisfactoriamente")
    labelVictoria.config(font="Consolas 14 bold", bg="#7d807e", fg="white",relief= "groove")
    labelVictoria.place(x=80, y=40)

    labelPocion= Label(framePrueba)
    labelPocion.config(font="Consolas 14 bold", bg="#7d807e", fg="white")

    poder1=" - "+clase_personajes.jugadorP.getDatos(6)["PODER 1"] + " \u2794" + f" +{incremento1} daño"
    poder2=" - "+clase_personajes.jugadorP.getDatos(6)["PODER 2"] + " \u2794" + f" +{incremento2} daño"
    poder3=" - "+clase_personajes.jugadorP.getDatos(6)["PODER 3"] + " \u2794" + f" +{incremento3} daño"
    poder4=" - "+clase_personajes.jugadorP.getDatos(6)["PODER 4"] + " \u2794" + f" +{incremento4} daño"

    descripcion= " Daño de habilidades incrementado \n\n{}\n\n{}\n\n{}\n\n{}".format(poder1,poder2,poder3,poder4)

    labelPoderes= Label(framePrueba,text=descripcion, justify="left")
    labelPoderes.config(font="Consolas 14 bold", bg="#7d807e", fg="white",relief= "groove")
    labelPoderes.place(x=65, y= 230)

    clase_personajes.damagePoderes[ clase_personajes.jugadorP.getDatos(6)["PODER 1"] ] += incremento1
    clase_personajes.damagePoderes[ clase_personajes.jugadorP.getDatos(6)["PODER 2"] ] += incremento2
    clase_personajes.damagePoderes[ clase_personajes.jugadorP.getDatos(6)["PODER 3"] ] += incremento3
    clase_personajes.damagePoderes[ clase_personajes.jugadorP.getDatos(6)["PODER 4"] ] += incremento4

    #MODIFICACIONES DINAMICAS

    if levelP1 == 1 or levelP1 == 2 or levelP1 == 3:
        textoPocion=f"Por tu enorme valentia recibiras {num_pociones} pociones de {nombrePocion[0]}"
        
        labelPocion.config(text= textoPocion, relief= "groove")
        labelPocion.place(x=92, y= 80)

    if levelP1 == 4 or levelP1 == 5 or levelP1 == 6 or levelP1 == 7 or levelP1 == 8 or levelP1 == 9:
        textoPocion= f"Por tu enorme valentia recibiras {num_pociones} pociones de {nombrePocion[0]}\n y {num_pociones2} pociones de {nombrePocion[1]} "
        
        labelPocion.config(text= textoPocion, relief= "groove")
        labelPocion.place(x=89, y= 80)

    if levelP1 == 10:
        textoVictoria= "¡Felicidades! \n Al derrotar finalmente a Zeus, lograste acabar con los \n dioses mas poderosos del olimpo"
        textoPocion= f"Por tu enorme valentia recibiras {num_pociones} pociones de {nombrePocion[0]}\n y {num_pociones2} de {nombrePocion[1]}"

        labelVictoria.config(text=textoVictoria, relief= "groove")
        labelVictoria.place(x=75, y=40)

        labelPocion.config(text= textoPocion, relief= "groove")
        labelPocion.place(x=95, y= 130)
        
    def anadirPocion():

        global nivelGlobal

        #pocion HP100 - HP250 - HP500

        if nivelGlobal <=3:
            var1= clase_personajes.jugadorP.getDatos(5)
            var1[tipo_pocion]+= num_pociones
            clase_personajes.jugadorP.setDatos(5,var1)

        if nivelGlobal >= 4:
            var1= clase_personajes.jugadorP.getDatos(5)
            var1[tipo_pocion]+= num_pociones
            var1[tipo_pocion2]+= num_pociones2
            clase_personajes.jugadorP.setDatos(5,var1)

        #MUSICA

        mixer.init()
        mixer.music.stop()
        mixer.music.load("musica\\cancion1.mp3")
        mixer.music.set_volume(0.30)
        mixer.music.play(loops=-1,start=550)

        ventanaPociones.destroy()
        modulo_retorno.cargarRetorno(ventanaInicio,ventanaMapa,nivelGlobal)
        
    botonAceptar= Button(framePrueba, text="Aceptar", command= lambda:anadirPocion())
    botonAceptar.config(width=10, height=2, cursor="hand2")
    botonAceptar.place(x=460, y=295)
    botonAceptar.config(font="Consolas 20 bold", bg="#cd8e2b",fg="White")
    botonAceptar.config(highlightcolor="Black",highlightbackground="Black")

    def cerrarPrograma():
        print("PROGRAMA FINALIZADO")
        mixer.music.stop()
        mixer.quit()
        ventanaPociones.destroy()

    ventanaPociones.protocol("WM_DELETE_WINDOW", cerrarPrograma)
    
    ventanaPociones.mainloop()    

nivel= 4
varMochila= clase_personajes.jugadorP.getDatos(5)

#darPociones(nivel,varMochila)


