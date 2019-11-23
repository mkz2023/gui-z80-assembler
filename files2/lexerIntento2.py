import sys,string
from pprint import pprint
#DIGITOS = '0123456789'
SIMBOLOS= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SIMBOLOSNUM="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
SIMBOLOS_ESP = '():;+'
REGISTROS_BAND = ['A', 'B', 'C', 'D', 'E', 'H', 'L', 'AF', 'BC', 'DE', 'HL', 'IX', 'IY','SP', 'NZ', 'Z', 'NC', 'C', 'PO', 'PE', 'P', 'M']
LIS_ETIQUETAS = []
T_SIMB = {}


def parcero(lista):
    simTable={}
    instrucciones = []
    for linea in lista:
        cadena = linea.upper()
        if ";" in cadena:
            indice = cadena.index(";")
            cadena = cadena[:indice]
        if cadena.count(",") > 1:
            print("Error, del archivo., mas de una coma")
            print(cadena)
            sys.exit()
        elif cadena.count(":") > 1:
            print("Exeso de ':' en la linea:")
            print(cadena)
            sys.exit()
        cadena = cadena.replace(","," , ")
        cadena = cadena.replace(":", " : ")
        cadena = cadena.split(" ")
        cadena = [x for x in cadena if x != ""]
        if ":" in cadena and cadena.index(":") != 1:
            print("Error en el archivo, : no esta después de la primera instruccion")
            sys.exit()
        if ":" in cadena:
            del(cadena[1])
            instrucciones.append(["#"+cadena[0]])
            simTable["#"+cadena[0]] = [True,None]
            if len(cadena[1:])>0:
                cadena = cadena[1:]
        
        if "," in cadena and cadena.index(",") != 2:
            print("Error del archivo, coma en lugar inapropiado")
            print(cadena)
            sys.exit()
        elif "," in cadena:
            del(cadena[2])
            instrucciones.append(cadena)
        else:
            instrucciones.append(cadena)
    return instrucciones,simTable

def abstractor(tokenList,simTable):
    abstractTokenList = []
    for tokenLine in tokenList: ###Buscando LD, ADD
        if all(c in SIMBOLOS for c in tokenLine[0]):
            abstractTokenList.append([tokenLine[0]])
        elif tokenLine[0] in simTable:
            abstractTokenList.append(["NN"])
        else:
            print("Error, instruccion no valida")
            print(tokenLine)
            sys.exit()
        for token in tokenLine[1:]:
            if "#"+token in simTable:###Buscando etiquetas
                abstractTokenList[-1].append("NN")
            elif token.count("(")>=1 or token.count(")") >=1:##Buscando (NN),(N),(IY+d)
                if token.count("(")>1 or token.count(")")>1:
                    print("Error, instrucción no valida")
                    print(tokenLine)
                    sys.exit()
                elif token[0] != "(" or token[-1] != ")":
                    print("Error, instrucción no valida")
                    print(tokenLine)
                    sys.exit()
                else:
                    inter = token[1:len(token)-1]
                    if all(c in SIMBOLOSNUM for c in inter)or (all(c in SIMBOLOSNUM for c in inter[:2])) and all(c in SIMBOLOSNUM for c in inter[3:] and inter[2]=="+") :
                        if inter in REGISTROS_BAND:
                            abstractTokenList[-1].append(token)
                        elif len(inter)<3:
                            print("Error, En la linea")
                            print(token)
                            sys.exit()
                        elif len(inter) == 3:
                            if inter[2] != "H":
                                print("Error, instrucción no valida")
                                print(tokenLine)
                                sys.exit()
                            elif (all(c in string.hexdigits for c in inter[:-1])):
                                abstractTokenList[-1].append("(N)")
                            else:
                                print("Error, instrucción no valida")
                                print(tokenLine)
                                sys.exit()
                        elif len(inter) == 5:
                            if inter[4] != "H":
                                print("Error, instrucción no valida")
                                print(tokenLine)
                                sys.exit()
                            elif (all(c in string.hexdigits for c in inter[:-1])):
                                abstractTokenList[-1].append("(NN)")
                            else:
                                print("Error, instrucción no valida")
                                print(tokenLine)
                                sys.exit()
                        elif inter[:3] in ("IX+","IY+"):##Tal vez, esto haga no acepte menos
                            if len(inter[3:])==3 and inter[-1] == "H":
                                if (all(c in string.hexdigits for c in inter[3:-1])):
                                    if (127>=int(inter[3:-1],16)):
                                        abstractTokenList[-1].append(inter[:3]+"d")
                                    else:
                                        print("Error, instrucción no valida")
                                        print(tokenLine)
                                        sys.exit()
                                else:
                                    print("Error, instrucción no valida")
                                    print(tokenLine)
                                    sys.exit()
                            else:
                                    print("Error, instrucción no valida")
                                    print(tokenLine)
                                    sys.exit()
                        else:
                                    print("Error, instrucción no valida")
                                    print(tokenLine)
                                    sys.exit()
                    else:
                        print("Error, instruccion no valida")
                        print(tokenLine)
                        sys.exit()
            elif (all(c in SIMBOLOSNUM for c in token)):###Buscando N y NN
                if token in REGISTROS_BAND:
                        abstractTokenList[-1].append(token)
                elif len(token) < 3:
                    print("Error, posiblemente sea debido a una falta de H")
                    print(tokenLine)
                    sys.exit()
                elif len(token) == 3:
                    if token[2] != "H":
                        print("Error, instrucción no valida")
                        print(tokenLine)
                        sys.exit()
                    elif (all(c in string.hexdigits for c in token[:-1])):
                        abstractTokenList[-1].append("N")
                    else:
                        print("Error, instrucción no valida")
                        print(tokenLine)
                        sys.exit()
                elif len(token) == 5:
                    if token[4] != "H":
                        print("Error, instrucción no valida")
                        print(tokenLine)
                        sys.exit()
                    elif (all(c in string.hexdigits for c in token[:-1])):
                        abstractTokenList[-1].append("NN")
                    else:
                        print("Error, instrucción no valida")
                        print(tokenLine)
                        sys.exit()
            else:
                print("Error, instrucción no valida")
                print(tokenLine)
                sys.exit()
    return abstractTokenList
        
def run(ListaInstrucciones):
    tokenList,simTable = parcero(ListaInstrucciones)
    abstractTokenList = abstractor(tokenList,simTable)
    return tokenList,abstractTokenList,simTable
            


if __name__ == "__main__":
    lista = ["LD A,(1000H)","JP (10H), eti1","eti1: INC IY,IX","eti2:","LD A,10H;Esto,;Sirve para comprobar:::"] 
    run(lista)