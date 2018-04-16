while(True):

    choice = input('\nBem vindo(a) ao ponte Simulator 2k18! O que deseja fazer?\n1- Criar dados \n2- Alterar dados \n3- Realizar contas \n4- Limpar dados \n')
    if(choice == '1'):
        file = open('tostador.txt', 'w')
        listaCoord = []
        listaCoordCheck = []
        listaEl = []
        listaIn = []
        listaMa = []
        listaGe = []
        listaNo = []
        listaLo = []
        nodeList = []

        while(True):
            ponty = input('Insira o numero de pontos de sua ponte (mínimo 2) ')
            if ((ponty.isdigit()) and (int(ponty) > 1)):
                ponty = int(ponty)
                print("Insira as coordenadas no padrão x y (em metros)")
                file.write("*COORDINATES"+" \n")
                file.write(str(ponty)+" \n")
                print("Modelo de input: (ponto X) (ponto Y)")
                i = 1
                k = 0
                while(i < ponty + 1):
                    print("Coordenada do ponto ")
                    coordX = input(str(i)+" "+"X"+" ")
                    if (not coordX.isdigit()):
                        print("Seu input é inválido!")
                    if (coordX.isdigit()):
                        print("Coordenada do ponto ")
                        coordY = input(str(i)+" "+"Y"+" ")
                        if (not coordY.isdigit()):
                            print("Seu input é inválido! \n")
                        else:
                            #print("0000"+str(listaCoordCheck))
                            listaCoord.append(coordX)
                            #print("1111"+str(listaCoordCheck))
                            #print("A"+str(listaCoord))
                            listaCoord.append(coordY)
                            #print("B"+str(listaCoord))
                            #print("C"+str(listaCoordCheck))
                            listaCoordCheck.append(listaCoord)
                            #print("D"+str(listaCoordCheck))
                            j = 0
                            for j in range(1, len(listaCoordCheck)):
                                if listaCoord == listaCoordCheck[j]: 
                                    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
                                    if not listaCoord == listaCoordCheck[k]: #se ocorrer outra vez o valor da listaCoord em um indice diferente de listaCoordCheck(k) 
                                        print("Coordenada já existente!")
                                        j = len(listaCoordCheck)
                            else:
                                del listaCoord[:]
                                file.write(str(i)+" "+str(coordX)+" "+str(coordY)+"\n")
                                i += 1
                                k += 1

                file.write("\n")
                print("\n")
                break
            else: 
                print("Insira um numero de pontos válidos! \n")

        while(True):
            elementy = input('Insira o número de grupos de elementos: ')
            if ((not elementy.isdigit()) or (int(elementy) <= 0)):   
                print("Insira um numero válido de elementos!")
            else:
                elementy = int(elementy)
                file.write("*ELEMENT_GROUPS"+" \n")
                file.write(str(elementy)+" \n")
                listaEl.append(elementy)
                print("Modelo de input: (elementos no grupo) (tipo (BAR, etc))")
                i = 1
                while(i < elementy + 1):
                    print("Numero de elementos no grupo ")
                    elementGN = input(str(i)+" ")
                    if (not elementGN.isdigit()):  
                        print("Insira uma quantidade válida de elementos em um grupo!")
                    if (elementGN.isdigit()):
                        elementGT = int(input("Tipo de elemento do grupo "+str(i)+"\n1-BAR\n2-BEAM\n3-Outro\n"))
                        if (elementGT == 1):
                            file.write(str(i)+" "+str(elementGN)+" "+str("BAR")+"\n")
                            listaEl.append(elementGN)
                            listaEl.append("BAR")
                            listaEl.append("next")
                            i += 1
                        elif (elementGT == 2):
                            file.write(str(i)+" "+str(elementGN)+" "+str("BEAM")+"\n")
                            listaEl.append(elementGN)
                            listaEl.append("BEAM")
                            listaEl.append("next")
                            i += 1                       
                        elif (elementGT == 3):
                            elementGTO = input("Insira o tipo do elemento ")
                            if (elementGTO.isdigit()):
                                print("Insira um tipo válido de elemento!")
                            else:
                                file.write(str(i)+" "+str(elementGN)+" "+str(elementGTO)+"\n")
                                listaEl.append(elementGN)
                                listaEl.append(elementGTO)
                                listaEl.append("next")
                                i += 1
                        else:
                            print("Opção inválida!")

                file.write("\n")
                print("\n")
                break
                

        while(True):
            incidency = input('Insira o número de Incidências: ')
            if ((incidency.isdigit()) and (ponty == 2) and (int(incidency) == 1)):
                print("porra")
                incidency = int(incidency)
                file.write("*INCIDENCES"+" \n")
                file.write(str(incidency)+" \n")
                print("Modelo de input: (inicio) (fim)")
                i = 1
                while (i < incidency + 1):
                    print("Número do nó ")
                    incidenceF = input(str(i)+" "+"Início"+" ")
                    if (not incidenceF.isdigit()):
                        print("Nó inválido!")
                    if (incidenceF.isdigit()):
                        incidenceL = input(str(i)+" "+"Fim"+" ")
                        if (not incidenceL.isdigit()):  
                            print("Nó inválido!")
                        else:
                            file.write(str(i)+" "+str(incidenceF)+" "+str(incidenceL)+"\n")
                            listaIn.append("Incidencia " + str(i))
                            listaIn.append(incidenceF)
                            listaIn.append(incidenceL)
                            i += 1

                file.write("\n")
                print("\n")
                break

            elif ((not incidency.isdigit()) or (int(incidency) < ponty)):
                print("Insira um número válido de incidências! \n")
            else:
                incidency = int(incidency)
                file.write("*INCIDENCES"+" \n")     
                file.write(str(incidency)+" \n")
                print("Modelo de input: (inicio) (fim)")
                i = 1
                while (i < incidency + 1):
                    print("Número do nó ")
                    incidenceF = input(str(i)+" "+"Início"+" ")
                    if (not incidenceF.isdigit()):
                        print("Nó inválido!")
                    if (incidenceF.isdigit()):
                        incidenceL = input(str(i)+" "+"Fim"+" ")
                        if (not incidenceL.isdigit()):  
                            print("Nó inválido!")
                        else:
                            file.write(str(i)+" "+str(incidenceF)+" "+str(incidenceL)+"\n")
                            listaIn.append("Incidencia " + str(i))
                            listaIn.append(incidenceF)
                            listaIn.append(incidenceL)
                            i += 1
                file.write("\n")
                print("\n")
                break
                

        while(True):
            materialy = input('Insira o número de materiais utilizados: ')
            if ((not materialy.isdigit()) or (int(materialy) <= 0)):  
                print("Insira um número válido de materiais!")
            else:
                materialy = int(materialy)
                file.write("*MATERIALS"+" \n")
                file.write(str(materialy)+" \n")
                print("Modelo de input: (modulo de elasticidade)")
                i = 1
                for i in range(1, materialy + 1):
                    print("Valor do modulo de elasticidade ")
                    materialG = input()
                    file.write(str(i)+" "+str(materialG)+"\n")
                    listaMa.append(materialG)
                    i += 1

                print("\n")
                break

        while(True):
            geometry = input('Insira o número de partes com secções diferentes: ')
            if ((not geometry.isdigit()) or (int(geometry) > incidency)):  
                print("Insira um número válido de partes!")
            else:
                geometry = int(geometry)
                file.write("*GEOMETRIC_PROPERTIES"+" \n")
                file.write(str(geometry)+" \n")
                print("Modelo de input: (Área de secção)")
                i = 0
                for i in range(1, geometry + 1):
                    print("Valor da área de secção ")
                    geometryG = input()
                    file.write(str(i)+" "+str(geometryG)+" \n")
                    listaGe.append(geometryG)
                    i += 1

                file.write("\n")
                print("\n")
                break


        while(True):
            nody = input('Insira o número de nodes fixos: ')
            if ((not nody.isdigit()) or (int(nody) > ponty)):  
                print("Insira um número válido de nós!")
            else:
                nody = int(nody)
                file.write("*BCNODES"+"\n")
                file.write(str(nody)+"\n")
                i = 0
                while(i < nody):
                    nodyN = input("Insira o número do nó com grau de liberdade restrito ")
                    if nodeList == []:
                        nodeList.append(nodyN)
                        print(nodeList) 
                    else:
                        nodeList.append(nodyN)
                        j = 0
                        k = 0
                        for j in range(0, len(nodeList[j])):
                            if nodyN == nodeList[j]:
                                print("Nó já existente!")
                                del nodeList[j]
                                j = len(nodeList)
                                i -= 1
                            elif nodyN != nodeList[j]:
                                print("pq")
                                j += 1
                                k += 1
                    i += 1
                print(nodeList)
                nodeList.sort()
                print(nodeList)
                i = 0
                while(i < len(nodeList)):
                    print("Insira o número de eixos com grau de liberdade restrito para o nó: ")
                    nodeGLN = input(str(nodeList[i])+" ")
                    if(not nodeGLN.isdigit() or int(nodeGLN) > 3 or int(nodeGLN) <= 0):
                        print("Grau de liberdade impossível!")
                    else:
                        nodeGLN = int(nodeGLN)
                        if (nodeGLN == 1):
                            nodeGLF = input("Insira o número equivalente ao eixo restrito \n1-X\n2-Y\n3-Z\n")
                            if(not nodeGLF.isdigit() or int(nodeGLF) <=0 or int(nodeGLF) > 3 ):
                                print("Opção inválida!")
                            else:
                                nodeGLF = int(nodeGLF)
                                if (nodeGLF == 1):
                                    file.write(str(nodeList[i])+" "+"1"+"\n")
                                elif (nodeGLF == 2):
                                    file.write(str(nodeList[i])+" "+"2"+"\n")
                                elif (nodeGLF == 3):
                                    file.write(str(nodeList[i])+" "+"3"+"\n")

                        elif (nodeGLN == 2):
                            nodeGLF = input("Insira o número equivalente aos eixos restritos \n1-XY\n2-YZ\n3-XZ\n")
                            if(not nodeGLF.isdigit() or int(nodeGLF) <=0 or int(nodeGLF) > 3 ):
                                print("Opção inválida!")
                            else:
                                nodeGLF = int(nodeGLF)
                                if (nodeGLF == 1):
                                    file.write(str(nodeList[i])+" "+"1"+"\n")
                                    file.write(str(nodeList[i])+" "+"2"+"\n")
                                elif (nodeGLF == 2):
                                    file.write(str(nodeList[i])+" "+"2"+"\n")
                                    file.write(str(nodeList[i])+" "+"3"+"\n")
                                elif (nodeGLF == 3):
                                    file.write(str(nodeList[i])+" "+"1"+"\n")
                                    file.write(str(nodeList[i])+" "+"3"+"\n")
                        

                        elif (nodeGLN == 3):
                            file.write(str(nodeList[i])+" "+"1"+"\n")
                            file.write(str(nodeList[i])+" "+"2"+"\n")
                            file.write(str(nodeList[i])+" "+"3"+"\n")
                        
                    i +=1
                file.write("\n")
                print("\n")
                break
        
        while(True):
            loady = input('Insira o número de forças aplicadas: ')
            if ((not loady.isdigit()) or (int(loady) > ponty)):  
                print("Insira um número válido de forças aplicadas!")
            else:
                loady = int(loady)
                file.write("*LOADS"+" \n")
                file.write(str(loady)+" \n")
                print("Modelo de input: (reformular)")
                for i in range(1, loady + 1):
                    print("Força aplicada no node ")
                    loadG = input()
                    file.write(str(i)+" "+str(loadG)+" \n")
                    listaLo.append(loadG)
                    i += 1

                file.write("\n")
                print("\n")
                break


        file.close()
        print("Arquivo salvo com sucesso!")