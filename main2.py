# -*- coding: utf-8 -*-

import math
import numpy as np
import metodos

class read_FILE():

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
        self.qtd_pontos = self.COORDINATES.pop(0)

        self.ELEMENT_GROUPS.pop(-1)
        self.ELEMENT_GROUPS.pop(0)

        self.INCIDENCES.pop(-1)
    #    self.INCIDENCES.pop(0)

        self.MATERIALS.pop(-1)
        self.MATERIALS.pop(0)

        self.GEOMETRIC_PROPERTIES.pop(-1)
        self.GEOMETRIC_PROPERTIES.pop(0)

        self.BCNODES.pop(-1)
        self.BCNODES.pop(0)

        self.qtd_forcas = self.LOADS.pop(0)

        self.c = []


        print(self.LOADS)

class Element():
    def __init__(self):
        self.file = read_FILE()

        #In case of elements starting in 1, make element -1 (else, make element)
        self.matrizes_regidez = [] #todas as matrizes de rigidez de cada elemto em uma [[[141000, 0, -141000, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 188000, 0, -188000]]] listas de listas de listas triple yammy
        self.complete_liberty = [] # todos os graues de liberdade em ordem cresente de elemento
        self.higest_liberty = 0 #fala quantas linhas e colunas a matriz combal vai ter, nota: haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa please kill me



        for i in range(len(self.file.INCIDENCES)):
            self.element = i
            self.INCIDENCES   = self.file.INCIDENCES[self.element]
            self.MATERIALS    = self.file.MATERIALS[self.element]
            self.PROPERTIES   = self.file.GEOMETRIC_PROPERTIES[self.element]
            self.liberty = []
            self.rigidez_individual()

        self.init_matrix_global()
        self.fill_matriz_global()
        self.loads()
        self.cdc()



    def rigidez_individual(self):


        self.COORDINATES()
        self.get_E()
        self.get_A()
        self.get_lengh()
        self.rigidez()
        self.matrixlib()
        self.results()


    def COORDINATES(self):
        self.c = [[0,0],[0,0]]

        #print(self.file.COORDINATES)

        self.c[0][1] = self.file.COORDINATES[int(self.INCIDENCES [1] - 1)][2]
        self.c[1][0] = self.file.COORDINATES[int(self.INCIDENCES [2] - 1)][1]
        self.c[1][1] = self.file.COORDINATES[int(self.INCIDENCES [2] - 1)][2]
        self.c[0][0] = self.file.COORDINATES[int(self.INCIDENCES [1] - 1)][1]

    def get_E(self):
        self.E = self.MATERIALS[0]

    def get_A(self):
        self.A = self.PROPERTIES[1]

    def get_lengh(self):
        self.lengh = math.sqrt(pow(self.c[0][0] - self.c[1][0], 2) + pow(self.c[0][1] - self.c[1][1], 2))

    def rigidez(self):
        #cosseno
        if(self.c[0][1] == self.c[1][1]):
            self.cos = 1
        elif(self.c[0][0] == self.c[1][0]):
            self.cos = 0
        else:
            self.cos = abs(self.c[0][1] - self.c[1][1])/(self.lengh)
        #seno
        if(self.c[0][1] == self.c[1][1]):
            self.sin = 0
        elif(self.c[0][0] == self.c[1][0]):
            self.sin = 1
        else:
            self.sin = abs(self.c[0][0] - self.c[1][0])/(self.lengh)
        #matriz de senos e cossenos
        mds =    [[self.cos**2 , self.cos*self.sin , -self.cos**2, -self.cos*self.sin ],
                    [self.cos* self.sin  , self.sin**2 , -self.cos* self.sin , -self.sin**2 ],
                    [-self.cos**2, -self.cos* self.sin , self.cos**2 , self.cos* self.sin   ],
                    [-self.cos* self.sin , -self.sin**2, self.cos* self.sin  , self.sin**2 ]]
        #matriz de rigidez
        self.final_rigidez = []
        for i in mds:
            matriz_intermediaria = []
            for j in i:
                matriz_intermediaria.append(int((self.E * self.A) / self.lengh)*j)
            self.final_rigidez.append(matriz_intermediaria)
        self.matrizes_regidez.append(self.final_rigidez)

    def matrixlib(self):
        for i in (self.INCIDENCES[1:]):
                self.liberty.append((i * 2) -1)
                self.liberty.append(i * 2)

        temp = max(self.liberty)
        if temp > self.higest_liberty: #acha a maior liberdade
            self.higest_liberty = temp

        self.complete_liberty.append(self.liberty)

    def results(self):
        print("Elemento: ", self.element + 1)
        print("Incidencias: ",self.INCIDENCES)
        print("Comprimebto: ",self.lengh)
        print("seno: ", self.sin)
        print("Cos: ", self.cos)
        print("Propriedade: ",self.PROPERTIES)
        print("Liberdade:", self.liberty)
        print("Liberdade Completa: ", self.complete_liberty)
        print("Rigidez: ",self.final_rigidez)
        print()

    def init_matrix_global(self):
        self.global_matrix = []
        int_high = int(self.higest_liberty)
        for i in range(int_high):
             self.global_matrix.append([0] * int_high)


    def fill_matriz_global(self): # isso so demorou minha sanidade para fazer mas vou tentar explicar
        #print(self.global_matrix)
        for i in range(len(self.complete_liberty)): #percorre todos os graus de liberdade (as listas dentro dos graus de liberdade)

            current_colun = 0
            self.current_line = 0

            for j in self.complete_liberty[i]: #percorre todos os elementos dentro de uma das listas dos graus de liberdade
                linha = int(j) -1 #a linha que em que o elemento da matrix de rigidez especifica vai ser esse

                for h in self.complete_liberty[i]: #percorre todos os elementos novamente agente vai estar fazendo basicamente a permutação de todos os elementos
                    coluna = int(h) -1 #a coluna do elemento da matriz de rigidez não global vai ser esse
                    self.global_matrix[linha][coluna] += self.matrizes_regidez[i][self.current_line][current_colun] #pega aonde o elemento deveria ir e soma oque ja esta la com o elemento da matrix de rigidez não global
                    current_colun += 1

                current_colun = 0
                self.current_line += 1


        """
        basicamente as current* percorrem a matrix especifica
        os linhas e colunas "calculam" onde aquele elemento da matriz especifica deve ser inserido na matrix global
        """

        print("Matriz global final:",self.global_matrix)

    def loads(self): #ler a explicacao pedro

        """aqui tem uma matriz de zeros com o tamanho definido por essa variavel que o Paulo cria na global.
            Ela tem que ser um vetor, e nao uma lista, entao o segundo argumento eh 1, para fazer uma listas
            de listas. """

        self.loads_matrix = np.zeros((int(self.higest_liberty), 1))

        """Aqui vamos iterar pela quantidade de forcas, essa variavel eh definida quando o Paulo
        da POP na hora de fazer a matriz quando ele ta lendo o TXT"""

        for i in range(int(self.file.qtd_forcas[0])):
            value = self.file.LOADS[i][2] #forca
            indice = int(self.file.LOADS[i][0]) #indice
            """Aqui vamos ver se a forca esta em x (1) ou y (2)"""
            if(self.file.LOADS[i][1] == 1.0):
                self.loads_matrix[(indice*2)-2][0] = value
            if(self.file.LOADS[i][1] == 2.0):
                self.loads_matrix[(indice*2)-1][0] = value

            """Por fim, para cada indice lido do txt na parte de LOADS,
            voce coloca o valor da forca na posicao certa do vetor"""

            '''np.delete 0 = linha 1 = coluna'''

    def cdc(self):
        #condicoes de contorno para matriz global
        self.global_cut = np.array(self.global_matrix)
        self.loads_cut = np.array(self.loads_matrix)

        for node in self.file.BCNODES:
            print(node)
            if(node[1] == 1):
                self.global_cut = np.delete(self.global_cut,(node[0]*2)-1 ,0)
                self.global_cut = np.delete(self.global_cut,(node[0]*2) -1 ,1)
                self.loads_cut = np.delete(self.loads_cut,(node[0]*2-1),0)



            elif(node[1] == 2):
                self.global_cut = np.delete(self.global_cut,(node[0]*2)-2 ,0)
                self.global_cut = np.delete(self.global_cut,(node[0]*2)-2 ,1)
                self.loads_cut = np.delete(self.loads_cut,(node[0]*2-2),0)



        print(self.loads_cut) #b
        print(self.global_cut) #A

        self.deslocamentos = metodos.jacobe(self.global_cut,self.loads_cut)
        self.deslocamentos = metodos.gauss(self.global_cut,self.loads_cut)



class write_FILE():


    def __init__(self):
        self.E = Element()
        self.file = read_FILE()
        self.saida = open("Saida.txt","w")
        self.write()
        self.saida.close()

    def write(self):
        self.saida.write("*DISPLACEMENTS\n")

        for i in range(len(self.file.INCIDENCES)-1):
            self.saida.write("{} {}\n".format(i+1, self.E.deslocamentos[i]))

        self.saida.write("*ELEMENT_STRAINS\n")

        self.saida.write("*ELEMENT_STRESSES\n")

        self.saida.write("*REACTION_FORCES\n")




write_FILE()
