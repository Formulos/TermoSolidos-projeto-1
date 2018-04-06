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
                del temp[-1]
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

    #    print(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)
    #    return(COORDINATES,ELEMENT_GROUPS,INCIDENCES,GEOMETRIC_PROPERTIES,BCNODES,LOADS)

class Element():
    def __init__(self, element):
        self.tmp = FILE()
        print(self.tmp.INCIDENCES)

        #In case of elements starting in 1, make element -1 (else, make element)
        self.INCIDENCES   = self.tmp.INCIDENCES[element]
        self.MATERIALS    = self.tmp.MATERIALS[element]
        self.GEOMETRIC_PROPERTIES   = self.tmp.GEOMETRIC_PROPERTIES[element]
        self.COORDINATES = self.tmp.COORDINATES[element]
#       print(self.INCIDENCES)


    def main(self):
        self.cos()
        self.sin()
        self.area()
        self.COORDINATES()
        self.lengh()
        self.thick()

    def COORDINATES(self):
        self.c = [[0,0],[0,0]]

        self.c[0][1] = self.COORDINATES[int(self.INCIDENCES [1] - 1)][2]
        self.c[1][0] = self.COORDINATES[int(self.INCIDENCES [2] - 1)][1]
        self.c[1][1] = self.COORDINATES[int(self.INCIDENCES [2] - 1)][2]
        self.c[0][0] = self.COORDINATES[int(self.INCIDENCES [1] - 1)][1]

    def E():
        self.E = self.MATERIALS[0]

    def A():
        self.A = self.PROPERTIES[self.element + 1]

    def lengh():
        self.lengh = sqrt(pow(self.lengh[0][0] - self.lengh[1][0], 2) + pow(self.lengh[0][1] - self.lengh[1][1], 2))

    def cos():
        self.cos = abs(self.c[0][1] - self.c[1][1])/(self.lengh)

    def sin():
        self.sin = abs(self.c[0][0] - self.c[1][0])/(self.lengh)

    def rigidez():
        c = self.cos
        s = self.sin
        mds = np.array([[c**2, c*s, -(c**2), -(c*s)],
                        [c*s, s**2, -(c*s), -(s**2)],
                        [-(c**2), -(c*s), c**2, c*s],
                        [-(c*s), -(s**2), c*s, s**2]])
        k = int((self.A * self.E) / self.lengh)
        self.rigidez = k * mds
        print(self.rigidez)

Element(2)