#! /usr/bin/python3
# from paquete.archivo import Clase
from vista.vista import Vista
import threading
from multiprocessing import Process

class ControladorVista():
    
    def __init__(self):
        self.vista=Vista()
        self.raiz=self.vista.getRaiz()
        self.comand = 0 # 0 -> dibuja pantalla y vuelve a consultar
    
    
    def ocultarPrimeraSeccion(self):
        self.raiz.ocultarPrimeraSeccion()
    
    def mostrarPrimeraSeccion(self):
        self.raiz.mostrarPrimeraSeccion()
        self.raiz.actualizarVentana()

    def ejecutarVentana(self):
        self.raiz.crearVentana()
    
    # creacion del hilo
    def mostrarVentana(self):
        hilo = threading.Thread( target=self.ejecutarVentana )
        #threads.append(hilo)
        hilo.start()

    # def mostrarVentana(self):
    #     self.raiz.crearVentana()

    # intentando mediante multiprocessing
    
    def mostrarVentana1(self):
        proceso = Process(target=self.ejecutarVentana)
        proceso.start()
    

