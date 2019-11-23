import treeGen
import string
import sys
from pprint import pprint
DEBUG = False
class FirstPassParser():
    def __init__(self,archivoOpCode,tokenList,abstractTokenL
    ,symbolTable):
        self.file = archivoOpCode
        self.tList = tokenList
        self.abstactTList = abstractTokenL
        self.symbolTable = symbolTable#Its incomplete until first pass
        self.arbol = treeGen.run(archivoOpCode)###Gets the hash tree for search
        self.sizeList = []
        self.opCodeList = []
    
    def _firstPassPart1(self):
        cL = 0
        for instruccion,instructReal in zip(self.abstactTList,self.tList):
            if len(instruccion)==1 and instruccion[0]== "NN":
                if instructReal[0] in self.symbolTable:
                    self.symbolTable[instructReal[0]][1] = hex(cL)
                    self.sizeList.append(hex(cL))
                else:
                    if DEBUG:
                        print("Error, no se encuentra definido en la tabla")
                        print("Error mortal")
                        sys.exit()
            else:
                size,opCode = self.arbol.search(instruccion)
                if size == False:
                    print("Error en la instrucción:")
                    print(instruccion)
                    sys.exit()
                try:
                    size = int(size,16)
                    self.sizeList.append(hex(cL))
                    cL+=size

                except Exception as e:
                    if not (all(c in string.hexdigits for c in size) and 
                    all(c in string.hexdigits for c in size) ) and DEBUG:
                            print("This means the developers made a mistake, it should had been\
                                evaluated before")
                            print("valor actual",size)
                            print("valor dado",cL)
                            print(self.sizeList)
                            print(e)
                            sys.exit()
                    print("Error")
        if DEBUG:
            for i in self.symbolTable():
                if i[2] ==None:
                    print("Error, algunas etiquetas no tienen dirección")
                    print(self.symbolTable)
    
    def _secondPass(self):###TAbla opcode no necesariamente tendrá el tamaño de las anteriores
        #por las directivas.
        def normalize(absOp,realOp):
            if absOp == "NN" and ("#"+realOp in self.symbolTable):
                dir = self.symbolTable["#"+realOp][1]
                dir = str(dir[2:])
                if 4 - len(dir) > 0:
                 #(('0x0', ['ORG', '05H'], ' '),
                    dir = "0"*(4-len(dir))+dir

                
                return dir[2:]+dir[:2] 
            elif absOp == "NN" or absOp == "(NN)":
                c = realOp.replace("h","").replace("H","").replace("(","").replace(")","")
                if len(c)<4:
                    c = "0"*(4-len(c))+c
                return c[2:]+c[:2]
            elif absOp == "N":
                return realOp.replace("h","").replace("H","")    
            else: return "" ##Se asume es un registro o una bandera.           
        for realInst,absInst in zip(self.tList,self.abstactTList):
            opCode=""
            op1 = ""
            op2 = ""
            if len(absInst)==1 and realInst[0][0]== "#":
                pass
            else:
                size,opCode = self.arbol.search(absInst)
                if opCode == -1 and DEBUG:
                    print("Error en la instrucción:")
                    print(realInst)
                    print(absInst)
                    sys.exit()
                else:
                    if opCode == "-":
                        if absInst[0] == "DB":
                            opCode = normalize(absInst[1],realInst[1])
                        else:
                            opCode = " "
                    else:
                        ##operand1
                        if len(absInst) == 1:
                            pass
                        else:
                            if absInst[1] == "-":
                                pass
                            else:
                                if absInst[1]=="NN":#solo las etiquetas usan NN
                                    if realInst[1] in self.symbolTable:
                                        op1 = normalize("NN",self.symbolTable[realInst[1]])
                                    else:
                                        op1 = normalize("NN",realInst[1])
                                else:
                                    op1 = normalize(absInst[1],realInst[1])
                                if len(absInst) == 2:
                                    pass
                                else:
                                    if absInst[2] == "-":
                                        pass
                                    elif absInst[2]=="NN":
                                        if realInst[2] in self.symbolTable:
                                            op1 = normalize("NN",self.symbolTable[realInst[2]])
                                        else:
                                            op1 = normalize("NN",realInst[2])
                                    else:op2 = normalize(absInst[2],realInst[2])
            opCode+=op1 
            opCode+=op2
            self.opCodeList.append(opCode)
            
def run(archivo,TL,ATL,ST):
    fparser = FirstPassParser(archivo,TL,ATL,ST)
    fparser._firstPassPart1()
    fparser._secondPass()
    pprint(tuple(zip(fparser.sizeList,fparser.tList,fparser.opCodeList)))
    print("#####################Tabla de simbolos")
    
    def dirST(realOp):
        dir = realOp[1]
        dir = str(dir[2:])
        if 4 - len(dir) > 0:
            dir = "0"*(4-len(dir))+dir
        return dir[2:]+dir[:2] 
    for i in ST.keys():
        print(i,ST[i][0],dirST(ST[i]))


if __name__ == "__main__":
    archivo = "z80_table.txt"
    TL = [
            ["LD","A","0200H"],["LD","D","A"],["LD","C","08"],
            ["#eti1"],["DEC","C"],["RLCA"],["JP","NC","eti1"]
            ,["HALT"]                
        ]
    ATL = [
        ["LD","A","(NN)"],["LD","D","A"],["LD","C","N"],
            ["#eti1"],["DEC","C"],["RLCA"],["JP","NC","NN"]
            ,["HALT"]
        ]
    ST = {"eti1":[True,None]}
    fparser = FirstPassParser(archivo,TL,ATL,ST)
    fparser._firstPassPart1()
    fparser._secondPass()
    pprint(tuple(zip(fparser.sizeList,fparser.tList,fparser.opCodeList)))
    print("#####################Tabla de simbolos")
    pprint(ST)

