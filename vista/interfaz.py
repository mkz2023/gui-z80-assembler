# !/usr/bin/python3.7

from tkinter import *

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

botonCargar = Button(framePrincipal, text="Cargar")
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