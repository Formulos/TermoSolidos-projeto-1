from math import *

class ArquivoTXT():

    def __init__(self):
        self.COORDINATES           = []
        self.ELEMENT_GROUPS        = []
        self.INCIDENCES            = []
        self.MATERIALS             = []
        self.GEOMETRIC_PROPERTIES  = []
        self.BCNODES               = []
        self.LOADS                 = []
        self.load("TermoSol.txt")

    def load(self, file):

        file = open(file, 'r')

        COORDINATES = [] # case 1
        ELEMENT_GROUPS = [] # case 2
        INCIDENCES = [] # case 3
        MATERIALS = [] # case 4
        GEOMETRIC_PROPERTIES = [] # case 5
        BCNODES = [] # case 6
        LOADS = [] # case 7

        case = 0
        temp = []
        palavra = ""



        for line in file:
            temp = []
            line = line.rstrip() # remove o /n escondido da linha
            line += " "
            #print(line)

            if line == "*COORDINATES ":
                case = 1
            elif line == "*ELEMENT_GROUPS ":
                case = 2
            elif line == "*INCIDENCES ":
                case = 3
            elif line == "*MATERIALS ":
                case = 4
            elif line == "*GEOMETRIC_PROPERTIES ":
                case = 5
            elif line == "*BCNODES ":
                case = 6
            elif line == "*LOADS ":
                case = 7

            else:
                for number in line:
                    print(number)
                    if number != " " : #start of something
                        palavra += number
                    else:
                        try:
                            temp.append(float(palavra)) # try to convert line to float
                            palavra = ""

                        except ValueError:  # if conversion to integer fails display a warning
                            print ("Warning: cannot convert to number string '%s'" % palavra)
                            temp.append((palavra))
                            palavra = ""
                            continue # skip to next line on error

            if case == 1 and len(temp) != 0:
                COORDINATES.append(temp)  # case 1
            if case == 2 and len(temp) != 0:
                ELEMENT_GROUPS.append(temp) # case 2
            if case == 3 and len(temp) != 0:
                INCIDENCES.append(temp) # case 3
            if case == 4 and len(temp) != 0:
                MATERIALS.append(temp) # case 4
            if case == 5 and len(temp) != 0:
                GEOMETRIC_PROPERTIES.append(temp) # case 5
            if case == 6 and len(temp) != 0:
                BCNODES.append(temp) # case 6
            if case == 7 and len(temp) != 0:
                LOADS.append(temp) # case 7


        file.close()

    #    print(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)
    #    return(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)

class Elemento():
    def __init__(self, numeroElemento):
        self.numeroE = numeroElemento - 1
        self.data = ArquivoTXT()

        self.incidencias   = self.data.matrizIndices[self.numeroE]
        self.material      = self.data.matrizMateriais[self.numeroE]
        self.propriedade   = self.data.matrizPropriedades[self.numeroE]
        print(self.propriedade)
        self.main()

    def main(self):
        self.getCordenadas()
        self.comprimento()
        self.cos()
        self.sin()
        self.area()
        self.getMatrixRigidez()

    def getCordenadas(self):
        self.coordenadas = [[0,0],[0,0]]

        self.coordenadas[0][0] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][1]
        self.coordenadas[0][1] = self.data.matrizCordenadas[int(self.incidencias[1] - 1)][2]

        self.coordenadas[1][0] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][1]
        self.coordenadas[1][1] = self.data.matrizCordenadas[int(self.incidencias[2] - 1)][2]

    def comprimento(self):
        self.comprimento = sqrt(pow(self.coordenadas[0][0] - self.coordenadas[1][0], 2) + pow(self.coordenadas[0][1] - self.coordenadas[1][1], 2))
        print(self.comprimento)

    def cos(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.c =  1
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.c =  0
        else:
            self.c = abs(self.coordenadas[0][1] - self.coordenadas[1][1])/(self.comprimento)
        print("cos :",self.c)

    def sin(self):
        if(self.coordenadas[0][1] == self.coordenadas[1][1]):
            self.s =  0
        elif(self.coordenadas[0][0] == self.coordenadas[1][0]):
            self.s =  1
        else:
            self.s = abs(self.coordenadas[0][0] - self.coordenadas[1][0])/(self.comprimento)
        print("sen :",self.s)

    def area(self):
        self.area = self.propriedade[self.numeroE + 1]
        print("Area:", self.area)

    def getMatrixRigidez(self):
        print(self.material[0])
        k = int((self.material[0] * self.area) / self.comprimento)
        print(k)
        matriz =    [[self.c**2 , self.c* self.s , -self.c**2, -self.c* self.s ],
                                 [self.c* self.s  , self.s**2 , -self.c* self.s , -self.s**2 ],
                                 [-self.c**2, -self.c* self.s , self.c**2 , self.c* self.s   ],
                                 [-self.c* self.s , -self.s**2, self.c* self.s  , self.s**2 ]]
        self.matrixRigidez = k * matriz
        print(self.matrixRigidez)


Elemento(1)
