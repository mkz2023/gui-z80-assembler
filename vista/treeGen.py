from pprint import pprint
from functools import reduce
from copy import copy
import sys
import os

DEBUG = False #If modified as true, it will print more
MAXSIZE  = 6


class ParserOpTable():
    def __init__(self,dirArch):
        self.dirArchivo=dirArch
        self.opTable = None
        self.dicTree={}
        
        self._leerTablaOp()
        for subItemList in self.opTable:##plain creation of dictionary.
            self.addToDict(subItemList)
        

    def _leerTablaOp(self):
        with open(self.dirArchivo) as f:##Leemos el archivo 
            self.opTable = []
            lineas = f.readlines()
            for linea in lineas:#Parceamos el archivo
                subItemList = linea.split("\t")
                subItemList[-1]=subItemList[-1].strip("\n")
                self.opTable.append(subItemList)
        del(lineas)#liberar memoria
        
        size=(4,5,6)
        correct = {"tam: "+str(i):0 for i in size}##instrucciones correctas por tamaño
        incorrect = 0
        mistake = []
        for i in self.opTable:##Analizamos que las instrucciones sean correctas
            if len(i) not in  size:#vemos que tenga 4,5 o 6 operandos
                print("Format error:")
                print("La siguientes instrucciones no cumplen con el formato")
                print("Si es porque no cuenta con dichos parametros, llenar con -")
                print("Separar con tabulaciones")
                mistake.append(i)
                incorrect+=1
            else:
                correct["tam: "+str(len(i))]+=1
        if incorrect != 0:##Si hubo algun error, morira
            if DEBUG:
                print(mistake)
            print("End of error")
            print("correcto",correct)
            print("incorrecto",incorrect)
            sys.exit()
        else:
            if DEBUG:
                print("correcto",correct)
                print("incorrecto",incorrect)
            print("La tabla de opcode parece ser correcta")

    def _sortOpTable(self):#ordenar tabla, not really implemented
        lamb = lambda x:x[0]
        self.opTable =  sorted(self.opTable,key=lamb)

    def addToDict(self,listaElem):##herramienta linea por linea
        #añade al arbol de diccionarios
        unwanted = ("")

        for i in range(len(listaElem)):#Llenamos elementos vacios con -
            if listaElem[i].strip(" ") in unwanted:
                listaElem[i] = "-"

        for i in range(MAXSIZE-len(listaElem)):##Llenamos elementos faltantes con ---
            listaElem.append("-")

        ##Ya que normalizamos los datos, vamos a crear el diccionario-añadir valores
        instruct = listaElem[0]
        numOp = listaElem[3]
        op1 = listaElem[4]
        op2 = listaElem[5]
        data = listaElem[1:3]#Elementos 1 y 2, tamaño inst y opcode
        parseElements = [instruct,numOp,op1,op2]
       
        actualDic = self.dicTree

        ##Crea un arbol de diccionarios, llamado dicTree
        ##Se encarga de crear nuevas ramas de forma iterativa
        #creando las ramas faltantes y añadir los elementos.
        for i in range(len(parseElements)):
            elemento = parseElements[i]
            if  elemento in actualDic:
                if i == len(parseElements)-1:
                    if DEBUG:
                        print("Debe haber una instruccion repetida")
                        print("Datos originales",parseElements)
                        print("Ultimo elemento",elemento)
                elif not isinstance(actualDic[elemento],dict):#Si no almacena un diccionario, algo esta mal
                    if DEBUG:
                        print("Debe haber una instruccion repetida")
                        print("Datos originales",parseElements)
                        print("diccionario",actualDic)
                        sys.exit()
                    break
                else:
                    actualDic = actualDic[elemento]
            else:
                if i == len(parseElements)-1:
                    actualDic[elemento]=data
                else:
                    actualDic[elemento]={}
                    actualDic = actualDic[elemento]

    def printdicTree(self,file=None):
        if file ==None:
            pprint(self.dicTree)
        else:
            with open(file,"w") as arch:
                pprint(self.dicTree,arch)

    def printOpTable(self,file=None):
        if file ==None:
            pprint(self.opTable)
        else:
            with open(file,"w") as arch:
                pprint(self.opTable,arch)


class Tree():
    def __init__(self,dicTree):
        self.tree = dicTree
            
    def search(self,raw):#format of instruccion [instruction,operand1,operand2]
        #it can be missing from right to left, except for the instruction
        ##returns [size,objectCode]
        instruction = copy(raw)
        if len(instruction) == 0:
            if DEBUG:
                print("Llego una instrucción vacía")
                sys.exit()
            else:
                return None,None
        else:
            numOp = len(instruction)-1
            instruction.insert(1,str(numOp)) #Añadimos numero de operandos
            for i in range(4-len(instruction)):##Llenamos elementos faltantes con ---
                instruction.append("-")
            instruction = list(map(str,instruction)) ##Aseguramos que todo sea un string
            try:
                salida =  reduce(dict.get,instruction, self.tree)
                if salida == None:
                    return False,-1
                return salida
            except TypeError as T:
                if DEBUG:
                    print(T)
                    print(type(self.tree))
                return False,-1  #no existe el valor


    def print(self,archivo=None):
        if archivo != None:
            with open(archivo,"w") as arch:
                pprint(self.tree,arch)
        else:
            pprint(self.tree)
def run(archivo):
    pars1 = ParserOpTable(archivo)
    arbol = Tree(pars1.dicTree)
    return arbol

if __name__ == "__main__":
    DEBUG = True
    imprimir = False

    arbol = run("z80_table.txt")
    instruction = ["LD","A","NN"]
    print(instruction)
    a,b = arbol.search(instruction)
    print(a,"\n",b)
    if imprimir:
        arbol.print("arbolito.sh")