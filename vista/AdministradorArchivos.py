#! /usr/bin/python3
# Esta clase contiene las funciones necesarias para abrir las ventanas del exlorador de archivos
#necesarias para
# 1-> Abrir un archivo entregandolo linea a linea en una lista
# 2-> Guardar un archivo leyendolo de una lista
# 

from tkinter import *
from tkinter import filedialog
class AdministradorArchivos:
    def __init__(self):
        self.rutaArchivo = ""

    def leerArchivo ( self ):
        self.rutaArchivo = filedialog.askopenfilename(title="Selecciona archivo para Abrir")
        print("la ruta fue: ", self.rutaArchivo)
    def escribirArchivo(self):
        self.rutaArchivo = filedialog.asksaveasfile(title="Selecciona nombre para guardar")
        print("ruta a guardar fue", self.rutaArchivo)


admin = AdministradorArchivos()
#admin.leerArchivo()
admin.escribirArchivo()