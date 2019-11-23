import firstPassParser
import lexerIntento2

import sys


if __name__ == "__main__":
    archivo = "z80_table.txt"
    if len(sys.argv)==1:
        lol = "entrada.ASM"
    else:
        lol = sys.argv[1]
    with open(lol) as entrada:
        ListaInstrucciones = entrada.readlines()
    ListaInstrucciones = [x.strip("\n") for x in ListaInstrucciones]
    print(ListaInstrucciones)
    
    tokenList,abstractTokenList,simTable=lexerIntento2.run(ListaInstrucciones)
    firstPassParser.run(archivo,tokenList,abstractTokenList,simTable)