ponty = 4
loadList = []
loadList = []



file = open('tostador.txt', 'w')

while(True):
    loady = input('Insira o número de nós com forças aplicadas: ')
    if ((not loady.isdigit()) or (int(loady) > ponty)):  
        print("Insira um número válido de nós!")
    else:
        loady = int(loady)
        file.write("*LOADS"+"\n")
        file.write(str(loady)+"\n")
        i = 0
        while(i < loady):
            loadyN = input("Insira o número do nó com forças aplicadas ")
            if loadList == []:
                loadList.append(loadyN)
            else:
                loadList.append(loadyN)
                j = 0
                k = 0
                for j in range(0, len(loadList[j])):
                    if loadN == loadList[j]:
                        print("Nó já existente!")
                        del loadList[j]
                        j = len(loadList)
                        i -= 1
                    elif loadN != loadList[j]:
                        print("pq")
                        j += 1
                        k += 1
            i += 1
        print(loadList)
        loadList.sort()
        print(loadList)
        i = 0
        while(i < len(loadList)):
            print("Insira o número de eixos com forças aplicadas para o nó: ")
            loadGLN = input(str(loadList[i])+" ")
            if(not loadGLN.isdigit() or int(loadGLN) > 3 or int(loadGLN) <= 0):
                print("Grau de liberdade impossível!")
            else:
                loadGLN = int(loadGLN)
                if (loadGLN == 1):
                    loadGLF = input("Insira o número equivalente ao eixo com força aplicada \n1-X\n2-Y\n3-Z\n")
                    if(not loadGLF.isdigit() or int(loadGLF) <=0 or int(loadGLF) > 3 ):
                        print("Opção inválida!")
                    else:
                        loadGLF = int(loadGLF)
                        if (loadGLF == 1):
                            file.write(str(loadList[i])+" "+"1"+"\n")
                        elif (loadGLF == 2):
                            file.write(str(loadList[i])+" "+"2"+"\n")
                        elif (loadGLF == 3):
                            file.write(str(loadList[i])+" "+"3"+"\n")

                elif (loadGLN == 2):
                    loadGLF = input("Insira o número equivalente aos eixos com forças aplicadas \n1-XY\n2-YZ\n3-XZ\n")
                    if(not loadGLF.isdigit() or int(loadGLF) <=0 or int(loadGLF) > 3 ):
                        print("Opção inválida!")
                    else:
                        loadGLF = int(loadGLF)
                        if (loadGLF == 1):
                            #for k in range(0,2): TERMINAR!
                            file.write(str(loadList[i])+" "+"1"+"\n")
                            file.write(str(loadList[i])+" "+"2"+"\n")
                        elif (loadGLF == 2):
                            file.write(str(loadList[i])+" "+"2"+"\n")
                            file.write(str(loadList[i])+" "+"3"+"\n")
                        elif (loadGLF == 3):
                            file.write(str(loadList[i])+" "+"1"+"\n")
                            file.write(str(loadList[i])+" "+"3"+"\n")
                

                elif (loadGLN == 3):
                    file.write(str(loadList[i])+" "+"1"+"\n")
                    file.write(str(loadList[i])+" "+"2"+"\n")
                    file.write(str(loadList[i])+" "+"3"+"\n")
                
            i +=1
        break


print("ripperino")

file.close()
