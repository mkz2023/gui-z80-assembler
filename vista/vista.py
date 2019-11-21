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
        #self.raiz.iconbitmap('./imgs/logo-ingenieria.ico') # esta solo funciona en widows
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
        self.botonEnsamblar=Button(self.framePrincipal, text="Ensamblar", command=lambda : self.botonEnsamblarPulsado())
        self.botonEnsamblar.grid(row=2, column=3, padx=5, pady=5)
        self.botonSimular=Button(self.framePrincipal, text="simular", command=lambda: self.botonSimularPuldado())
        self.botonSimular.grid(row=2, column=4, padx=5, pady=5)

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
        self.framePrincipal.grid()
        # debe inicia con las 3 secciones ocultas
        self.ocultarPrimeraSeccion()
        self.ocultarSegundaSeccion()
        self.ocultarTerceraSeccion()
        self.raiz.mainloop()
        # while True:
        #     self.raiz.update_idletasks()
        #     self.raiz.update()
    
    def actualizarVentana( self ):
        self.raiz.update_idletasks()
        self.raiz.update()
    
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
        # mostrar la primera seccion
        self.mostrarPrimeraSeccion()
        #ocultar las demas
        self.ocultarSegundaSeccion()
        self.ocultarTerceraSeccion()        

    def botonLimpiarPulsado(self):
        # se limpiara el contenido del Text donde esta el codigo ensamblador
        self.textoCodigoEnsamblador.delete("1.0", END)
        # tambien limpia el TEXT del codigo EX y el codigo LST
        self.textoCodigoEX.delete('1.0',END)
        self.textoCodigoLST.delete('1.0',END)
        #ocultar las secciones
        self.ocultarPrimeraSeccion()
        self.ocultarSegundaSeccion()
        self.ocultarTerceraSeccion()

    def botonGuardarpulsado(self):
        #print("se ha pulsado el boton guardar ensamblador")
        #ruta = self.getRutaGuardarEnsamblador()
        self.guardarEnsamblador()
    
    def botonEnsamblarPulsado(self):
        contenido = self.leerCodigoEnsamblador()
        # funcionalidad provicional
        # ya no tiene caso mostrar el codigo fuente
        self.ocultarPrimeraSeccion()
        #self.botonEnsamblar.configure(state=NORMAL)
        self.botonLimpiar.configure(state=NORMAL)
        self.mostrarSegundaSeccion()
        self.mostrarTerceraSeccion()
        self.textoCodigoEX.insert('0.0', contenido)
        self.textoCodigoLST.insert('0.0',contenido)
    
    def botonSimularPuldado(self):
        # obtener el conteido de ...
        print("Se ha pulsado el boton simular")
    
    def botonGuardarEXpulsado(self):
        self.guardarEX()

    def botonGuardarLSTpulsado(self):
        self.guardarLST()
         
    # funciones para manejar el comportamiento de la interfas
    def ocultarPrimeraSeccion(self):
        self.labelCodigoEnsamblador.grid_remove()
        self.textoCodigoEnsamblador.grid_remove()
        self.scrollEnsamblador.grid_remove()
        self.botonGuardar.configure(state=DISABLED)
        self.botonEnsamblar.configure(state=DISABLED)
        self.botonLimpiar.configure(state=DISABLED)
        self.botonSimular.configure(state=DISABLED)


    def mostrarPrimeraSeccion(self):
        self.labelCodigoEnsamblador.grid()
        self.textoCodigoEnsamblador.grid()
        self.scrollEnsamblador.grid()
        self.botonGuardar.configure(state=NORMAL)
        self.botonEnsamblar.configure(state=NORMAL)
        self.botonLimpiar.configure(state=NORMAL)
        self.botonSimular.configure(state=DISABLED)

    
    def ocultarSegundaSeccion(self):
        self.labelCodigoEX.grid_remove()
        self.textoCodigoEX.grid_remove()
        self.botonGuardarEX.grid_remove()
        self.scrollEX.grid_remove()
    
    def mostrarSegundaSeccion(self):
        self.labelCodigoEX.grid()
        self.textoCodigoEX.grid()
        self.botonGuardarEX.grid()
        self.scrollEX.grid()
        self.botonSimular.configure(state=NORMAL)
    
    def ocultarTerceraSeccion(self):
        self.labelCodigoLST.grid_remove()
        self.textoCodigoLST.grid_remove()
        self.botonGuardarLST.grid_remove()
        self.scrollLST.grid_remove()
    
    def mostrarTerceraSeccion(self):
        self.labelCodigoLST.grid()
        self.textoCodigoLST.grid()
        self.botonGuardarLST.grid()
        self.scrollLST.grid()

    # funciones para guardar archivos
    def getRutaGuardarEnsamblador(self):
        #print("pregunta donde guardar el ensambldor")
        ruta = filedialog.asksaveasfile()
        if ruta is not None:
            #print(ruta)
            #direccion =str(ruta.get(1.0, END))
            #print(direccion)
            #return direccion
            return ruta
    
    def getRutaGuardarEX(self):
        ruta=filedialog.asksaveasfile()
        if ruta is not None:
            return ruta

    
    def getRutaGuardarLST(self):
        ruta=filedialog.asksaveasfile()
        if ruta is not None:
            return ruta

    def guardarEnsamblador(self):
        ruta=self.getRutaGuardarEnsamblador()
        path=ruta.name
        #print("path: ", path)
        archivo = open(path,'w')
        contenido=self.textoCodigoEnsamblador.get('0.0','end-1c')
        #print(contenido)
        archivo.write(contenido)
        archivo.close()
    
    def guardarEX(self):
        ruta=self.getRutaGuardarEX()
        path=ruta.name
        archivo=open(path,'w')
        contenido=self.textoCodigoEX.get('0.0','end-1c')
        archivo.write(contenido)
        archivo.close()
  
    def guardarLST(self):
        ruta=self.getRutaGuardarLST()
        path=ruta.name
        archivo = open(path,'w')
        contenido=self.textoCodigoLST.get('0.0','end-1c')
        archivo.write(contenido)
        archivo.close()
    