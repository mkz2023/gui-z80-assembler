import firstPassParser
import lexerIntento2
from pprint import pprint
import sys
def hextoInt(cadena):
    return int(cadena,16)
def intToHex(entero):
    salida = hex(entero)
    salida = salida[2:]
    return salida



def archivoHex(sizeList,opCodeList):
    tam = len("".join(opCodeList))
    if(tam %0) == 0:
        


if __name__ == "__main__":
    archivo = "z80_table.txt"
    if len(sys.argv)==1:
        lol = "entrada.ASAM"
    else:
        lol = sys.argv[1]
    ###Lo importante es la ruta


    with open(lol) as entrada:
        ListaInstrucciones = entrada.readlines()
    ListaInstrucciones = [x.strip("\n") for x in ListaInstrucciones]
    ###Leeer iun archivo, generar lista de instrucciones
    
    ####Codigos, metodo run.
    tokenList,abstractTokenList,simTable=lexerIntento2.run(ListaInstrucciones)
    sizeList,tList,opCodeList,Tabla=firstPassParser.run(archivo,tokenList,abstractTokenList,simTable)##Este hace los prints
    
    for x,y,z in zip(sizeList,opCodeList,tokenList):
        print(x,"\t"*2,y,"\t"*2,"".join(z))

    print(Tabla)




    #