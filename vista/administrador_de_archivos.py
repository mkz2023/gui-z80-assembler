#! /usr/bin/python3
# Esta clase contiene las funciones necesarias para abrir las ventanas del exlorador de archivos
#necesarias para
# 1-> Abrir un archivo entregandolo linea a linea en una lista
# 2-> Guardar un archivo leyendolo de una lista
# 

from tkinter import *
from tkinter import filedialog
from io import open

class AdministradorArchivos:
    def __init__(self):
        self.rutaArchivo = ""

    def leerArchivo ( self ):
        self.rutaArchivo = filedialog.askopenfilename(title="Selecciona archivo para Abrir")
        print("la ruta fue: ", self.rutaArchivo)
    def escribirArchivo(self):
        self.rutaArchivo = filedialog.asksaveasfile(title="Selecciona nombre para guardar")
        print("ruta a guardar fue", self.rutaArchivo)
    
    def leerArchivoASM(self):
        self.rutaArchivo = filedialog.askopenfilename(title="Selecciona el archivo ASM para abrir", filetypes=(("Archivos Ensamblador","*.ASM"),("Todos", "*.*")))
        print("ruta a abrir: ", self.rutaArchivo)
        #una ves tenemos la ruta procedemos a leer el archivo y regresar el contenido en una lista
        if self.rutaArchivo == None:
            print("No se obtuvo la ruta")
        else:
            archivo = open(self.rutaArchivo, "r")
            lineas=archivo.readlines()
            #print(lineas)
            # ahora regresamos la lista a la funcion que llamo a este metodo
            archivo.close()
            return lineas


#admin = AdministradorArchivos()
#admin.leerArchivo()
#admin.escribirArchivo()
#admin.leerArchivoASM()