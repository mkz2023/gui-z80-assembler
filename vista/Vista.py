#! /usr/bin/python3/

# Vista genera le vantana y contiene los metodos asociado
# a la funcoinalidad de esta

from tkinter import *

class Vista:
    def __init__(self):
        print("la clase esta funcionando")
    
    def crearVentana(self):
        raiz= Tk()
        raiz.title("Ensamblador para z-80 en python")
        framePrincipal=Frame(raiz)
        #framePrincipal.config(background="blue")
        #framePrincipal.config(width="600", height="600")
        framePrincipal.pack()

        labelCodigoEnsamblador = Label(framePrincipal, text="A continuación escriba o cargue su codigo ensamblador")
        labelCodigoEnsamblador.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        textoCodigoEnsamblador=Text( framePrincipal )
        textoCodigoEnsamblador.config(height=10)
        textoCodigoEnsamblador.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        scrollEnsamblador=Scrollbar(framePrincipal, command=textoCodigoEnsamblador.yview)
        scrollEnsamblador.grid(row=1, column=5, sticky="nsew")
        textoCodigoEnsamblador.config(yscrollcommand=scrollEnsamblador.set)

        botonCargar = Button(framePrincipal, text="Cargar", command=lambda : print("BotonCargar ha sido pulsado"))
        botonCargar.grid(row=2, column=0, padx=5, pady=5)
        botonLimpiar = Button(framePrincipal, text="Limpiar")
        botonLimpiar.grid(row=2, column=1, padx=5, pady=5)
        botonGuardar=Button(framePrincipal, text="Guardar")
        botonGuardar.grid(row=2, column=2, padx=5, pady=5)
        botodEnsamblar=Button(framePrincipal, text="Ensamblar")
        botodEnsamblar.grid(row=2, column=3, padx=5, pady=5)

        labelCodigoEX = Label(framePrincipal, text="Codigo EX o herrores despues de ensamblar")
        labelCodigoEX.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        textoCodigoEX = Text(framePrincipal)
        textoCodigoEX.config(height=10)
        textoCodigoEX.grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        scrollEX=Scrollbar(framePrincipal, command=textoCodigoEX.yview)
        scrollEX.grid(row=4, column=5, sticky="nsew")
        textoCodigoEX.config(yscrollcommand=scrollEX.set)
        botonGuardarEX = Button(framePrincipal, text="Guardar codigo EX")
        botonGuardarEX.grid(row=5, column=4, padx=5, pady=5)

        labelCodigoLST= Label(framePrincipal, text="Codigo LST o herrores despues de ensamblar")
        labelCodigoLST.grid(row=6, column=0, columnspan=5, padx=5, pady=5)
        textoCodigoLST = Text(framePrincipal)
        textoCodigoLST.config(height=10)
        textoCodigoLST.grid(row=7, column=0, columnspan=5, padx=5, pady=5)
        scrollLST=Scrollbar(framePrincipal, command=textoCodigoLST.yview)
        scrollLST.grid(row=7, column=5, sticky="nsew")
        textoCodigoLST.config(yscrollcommand=scrollLST.set)
        botonGuardarLST = Button(framePrincipal, text="Guardar codigo LST ")
        botonGuardarLST.grid(row=8, column=4, padx=5, pady=5)
        raiz.mainloop()

   
    # esta funcion lee el archivo .asm y regresa una lista con el contenido del archivo linea a linea
    def leerArchivoEnsamblador(self):
        print("ahora vamnos a leer el archivo ensamblador")

        rutaArchivo = filedialog.askopenfilename(title="Selecciona el archivo ASM para abrir", filetypes=(("Archivos Ensamblador","*.ASM"),("Todos", "*.*")))
        #una ves tenemos la ruta procedemos a leer el archivo y regresar el contenido en una lista
        if rutaArchivo == None:
            print("No se obtuvo la ruta")
        else:
            archivo = open(rutaArchivo, "r")
            lineas=archivo.readlines()
            #print(lineas)
            # ahora regresamos la lista a la funcion que llamo a este metodo
            archivo.close()
            return lineas

    # a continuacion se crean las funciones que responden a la pulsacion de los botones
    def botonCargarPulsado(self):
        print("se ha pulsado el boton cargar")
        contenido = self.leerArchivoEnsamblador()

    def botonLimpiarPulsado(self):
        print("se ha pulsado del boton limpiar")

    def botonGuardarpulsado(self):
        print("se ha pulsado el boton guardar ensamblador")
    
    def botonGuardarEXpulsado(self):
        print("se ha pulsado el boton guardar EX")

    def botonGuardarLSTpulsado(self):
        print("se ha pulsado el boton guardar LST")
         
