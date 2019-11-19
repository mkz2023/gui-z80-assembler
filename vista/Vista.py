#! /usr/bin/python3/

# Vista genera le vantana y contiene los metodos asociado
# a la funcoinalidad de esta

from tkinter import *
from tkinter import filedialog
from io import open

class Vista:
    def __init__(self):
        self.raiz= Tk()
        self.raiz.title("Ensamblador para z-80 en python")
        self.raiz.iconbitmap('./imgs/logo-ingenieria.ico')
        self.framePrincipal=Frame(self.raiz)
        self.framePrincipal.config(background="#A79A97")
        #framePrincipal.config(width="600", height="600")

        self.labelCodigoEnsamblador = Label(self.framePrincipal, text="A continuación escriba o cargue su codigo ensamblador")
        self.labelCodigoEnsamblador.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        self.textoCodigoEnsamblador=Text( self.framePrincipal )
        self.textoCodigoEnsamblador.config(height=10)
        self.textoCodigoEnsamblador.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        self.scrollEnsamblador=Scrollbar(self.framePrincipal, command=self.textoCodigoEnsamblador.yview)
        self.scrollEnsamblador.grid(row=1, column=5, sticky="nsew")
        self.textoCodigoEnsamblador.config(yscrollcommand=self.scrollEnsamblador.set)

        self.botonCargar = Button(self.framePrincipal, text="Cargar", command=lambda : self.botonCargarPulsado())
        self.botonCargar.grid(row=2, column=0, padx=5, pady=5)
        self.botonLimpiar = Button(self.framePrincipal, text="Limpiar", command=lambda : self.botonLimpiarPulsado())
        self.botonLimpiar.grid(row=2, column=1, padx=5, pady=5)
        self.botonGuardar=Button(self.framePrincipal, text="Guardar", command=lambda : self.botonGuardarpulsado())
        self.botonGuardar.grid(row=2, column=2, padx=5, pady=5)
        self.botodEnsamblar=Button(self.framePrincipal, text="Ensamblar", command=lambda : self.botonEnsamblarPulsado())
        self.botodEnsamblar.grid(row=2, column=3, padx=5, pady=5)

        self.labelCodigoEX = Label(self.framePrincipal, text="Codigo EX o herrores despues de ensamblar")
        self.labelCodigoEX.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
        self.textoCodigoEX = Text(self.framePrincipal)
        self.textoCodigoEX.config(height=10)
        self.textoCodigoEX.grid(row=4, column=0, columnspan=5, padx=5, pady=5)
        self.scrollEX=Scrollbar(self.framePrincipal, command=self.textoCodigoEX.yview)
        self.scrollEX.grid(row=4, column=5, sticky="nsew")
        self.textoCodigoEX.config(yscrollcommand=self.scrollEX.set)
        self.botonGuardarEX = Button(self.framePrincipal, text="Guardar codigo EX", command=lambda : self.botonGuardarEXpulsado())
        self.botonGuardarEX.grid(row=5, column=4, padx=5, pady=5)

        self.labelCodigoLST= Label(self.framePrincipal, text="Codigo LST o herrores despues de ensamblar")
        self.labelCodigoLST.grid(row=6, column=0, columnspan=5, padx=5, pady=5)
        self.textoCodigoLST = Text(self.framePrincipal)
        self.textoCodigoLST.config(height=10)
        self.textoCodigoLST.grid(row=7, column=0, columnspan=5, padx=5, pady=5)
        self.scrollLST=Scrollbar(self.framePrincipal, command=self.textoCodigoLST.yview)
        self.scrollLST.grid(row=7, column=5, sticky="nsew")
        self.textoCodigoLST.config(yscrollcommand=self.scrollLST.set)
        self.botonGuardarLST = Button(self.framePrincipal, text="Guardar codigo LST ", command=lambda : self.botonGuardarLSTpulsado())
        self.botonGuardarLST.grid(row=8, column=4, padx=5, pady=5)
        

    
    def crearVentana(self):
        self.framePrincipal.pack()
        self.raiz.mainloop()

   
    # esta funcion lee el archivo .asm y regresa una lista con el contenido del archivo linea a linea
    def leerArchivoEnsamblador(self):
        print("ahora vamnos a leer el archivo ensamblador")

        rutaArchivo = filedialog.askopenfilename(title="Selecciona el archivo ASM para abrir", filetypes=(("asm","*.txt"),("Todos", "*.*")))
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
    
    # esta funcion lee el codigo ensamblador dede el Text ensamblador y se lo pasa a la funcion que lo requiera en una lista
    def leerCodigoEnsamblador(self):
        contenido=self.textoCodigoEnsamblador.get("1.0",'end-1c')
        return contenido
        # falta pasar el contenido de este string a una lista




    # a continuacion se crean las funciones que responden a la pulsacion de los botones
    def botonCargarPulsado(self):
        print("se ha pulsado el boton cargar")
        lista = self.leerArchivoEnsamblador()
        # a continuacion se agrega el contenido del archivo leido en el Text del codigo ensamblador
        #self.textoCodigoEnsamblador.insert(0.0,lista)
        contenido = ""
        for var in lista:
            contenido = str(contenido) + str(var)
        self.textoCodigoEnsamblador.insert("0.0", contenido)        

    def botonLimpiarPulsado(self):
        # se limpiara el contenido del Text donde esta el codigo ensamblador
        self.textoCodigoEnsamblador.delete("1.0", END)
        # tambien limpia el TEXT del codigo EX y el codigo LST
        self.textoCodigoEX.delete('1.0',END)
        self.textoCodigoLST.delete('1.0',END)

    def botonGuardarpulsado(self):
        print("se ha pulsado el boton guardar ensamblador")
    
    def botonEnsamblarPulsado(self):
        contenido = self.leerCodigoEnsamblador()
        # funcionalidad provicional
        self.textoCodigoEX.insert('0.0', contenido)
        self.textoCodigoLST.insert('0.0',contenido)
    
    def botonGuardarEXpulsado(self):
        print("Boton guardar EX pulsado")

    def botonGuardarLSTpulsado(self):
        print("se ha pulsado el boton guardar LST")
         
