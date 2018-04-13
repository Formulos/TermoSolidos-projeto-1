import math
import numpy as np

class FILE():

    def __init__(self):
        self.load("TermoSol.txt")

    def load(self, file):

        file = open(file, 'r')

        self.COORDINATES = [] # case 1
        self.ELEMENT_GROUPS = [] # case 2
        self.INCIDENCES = [] # case 3
        self.MATERIALS = [] # case 4
        self.GEOMETRIC_PROPERTIES = [] # case 5
        self.BCNODES = [] # case 6
        self.LOADS = [] # case 7

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
                    #print(number)
                    if number != " " : #start of something
                        palavra += number
                    else:
                        try:
                            temp.append(float(palavra)) # try to convert line to float
                            palavra = ""

                        except ValueError:  # if conversion to integer fails display a warning
                            #print ("Warning: cannot convert to number string '%s'" % palavra)
                            temp.append((palavra))
                            palavra = ""
                            continue # skip to next line on error



            if case == 1 and len(temp) != 0:
                #del temp[-1]
                self.COORDINATES.append(temp)  # case 1
            if case == 2 and len(temp) != 0:
                self.ELEMENT_GROUPS.append(temp) # case 2
            if case == 3 and len(temp) != 0:
                self.INCIDENCES.append(temp) # case 3
            if case == 4 and len(temp) != 0:
                self.MATERIALS.append(temp) # case 4
            if case == 5 and len(temp) != 0:
                self.GEOMETRIC_PROPERTIES.append(temp) # case 5
            if case == 6 and len(temp) != 0:
                self.BCNODES.append(temp) # case 6
            if case == 7 and len(temp) != 0:
                self.LOADS.append(temp) # case 7

        file.close()


        self.COORDINATES.pop(-1)
        self.COORDINATES.pop(0)
        
        self.ELEMENT_GROUPS.pop(-1)
        self.ELEMENT_GROUPS.pop(0)
        
        self.INCIDENCES.pop(-1)
        self.INCIDENCES.pop(0)
        
        self.MATERIALS.pop(-1)
        self.MATERIALS.pop(0)
        
        self.GEOMETRIC_PROPERTIES.pop(-1)
        self.GEOMETRIC_PROPERTIES.pop(0)
        
        self.BCNODES.pop(-1)
        self.BCNODES.pop(0)
        #self.LOADS.pop(-1)




    #    return(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)

class Element():
    def __init__(self, element):
        self.tmp = FILE()

        #In case of elements starting in 1, make element -1 (else, make element)
        self.INCIDENCES   = self.tmp.INCIDENCES[element]
        self.MATERIALS    = self.tmp.MATERIALS[element]
        self.PROPERTIES   = self.tmp.GEOMETRIC_PROPERTIES[element]
        self.liberdade = []
        self.c = []
        self.main()


    def main(self):
        self.COORDINATES()
        self.cos()
        self.sin()
        self.A()
        self.E()
        self.lengh()
        self.thick()
        self.rigidez()
        self.liberty()
        self.status()

    def COORDINATES(self):
        self.c = [[0,0],[0,0]]

        #print(self.tmp.COORDINATES)
        print(self.tmp.INCIDENCES[1])
        print(self.tmp.COORDINATES[self.INCIDENCES [1] ] [2])
        self.c[0][1] = self.tmp.COORDINATES[int(self.INCIDENCES [1] - 1)][2]
        self.c[1][0] = self.tmp.COORDINATES[int(self.INCIDENCES [2] - 1)][1]
        self.c[1][1] = self.tmp.COORDINATES[int(self.INCIDENCES [2] - 1)][2]
        self.c[0][0] = self.tmp.COORDINATES[int(self.INCIDENCES [1] - 1)][1]

    def E(self):
        self.E = self.MATERIALS[0]

    def A(self):
        self.A = self.PROPERTIES[1]

    def lengh(self):
        self.lengh = math.sqrt(pow(self.lengh[0][0] - self.lengh[1][0], 2) + pow(self.lengh[0][1] - self.lengh[1][1], 2))

    def cos(self):
        if(self.c[0][1] == self.c[1][1]):
            self.cos = 1
        elif(self.c[0][0] == self.c[1][0]):
            self.cos = 0
        else:
            self.cos = abs(self.c[0][1] - self.c[1][1])/(self.lengh)
        print(self.tmp.COORDINATES)

    def sin(self):
        if(self.c[0][1] == self.c[1][1]):
            self.cos = 0
        elif(self.c[0][0] == self.c[1][0]):
            self.cos = 1
        else:
            self.sin = abs(self.c[0][0] - self.c[1][0])/(self.lengh)
        print(self.tmp.INCIDENCES)

    def rigidez(self):
        mds =    [[self.cos**2 , self.cos* self.sin , -self.cos**2, -self.cos* self.sin ],
                    [self.cos* self.sin  , self.sin**2 , -self.cos* self.sin , -self.sin**2 ],
                    [-self.cos**2, -self.cos* self.sin , self.cos**2 , self.cos* self.sin   ],
                    [-self.cos* self.sin , -self.sin**2, self.cos* self.sin  , self.sin**2 ]]

        self.final_rigidez = []
        for e in mds:
            self.matriz_intermediaria = []
            for i in e:
                self.matriz_intermediaria.append(int((E * A) / self.lengh)*i)
            self.final_rigidez.append(self.matriz_intermediaria)

    def liberty(self):
        for i in (self.INCIDENCES[1:]):
                self.liberty.append((i * 2) -1)
                self.liberty.append(i * 2)

    def results(self):
        print("Elemento: ",self.element -1)
        print("Incidencias: ",self.INCIDENCES)
        print("Comprimebto: ",self.lengh)
        print("Propriedade: ",self.propriedade)
        print("Liberdade:", self.liberdade )
        print("Rigidez: ",self.final_rigidez)
        print()


Element(1)
