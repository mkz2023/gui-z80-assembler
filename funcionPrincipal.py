#! /usr/bin/python3
# from paquete.archivo import Clase
from vista.vista import Vista
import threading

from vista.administrador_de_archivos import AdministradorArchivos

print("funcion principal del ensablador de z-80 en python")

vista = Vista()
#tratando de recivir el objeto por referencia



#raiz = vista.getRaiz()
#raiz.ocultarPrimeraSeccion()
#raiz.ocultarSegundaSeccion()
#raiz.ocultarTerceraSeccion()

#hilo = threading.Thread()

vista.crearVentana()
#vista.actualizarVentana()

# for i in range (40000):
#     vista.actualizarVentana()

# print("salimos de la primer ejecucion")

#while True:
#    vista.actualizarVentana()

#print("el hilo1 esta iniciado")
