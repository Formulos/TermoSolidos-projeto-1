file = open('tostador.txt', 'w')

choice = input('\nBem vindo(a) ao ponte Simulator 2k18! O que deseja fazer?\n1- Criar dados \n2- Alterar dados \n3- Realizar contas \n4- Limpar dados \n')
if(choice == '1'):
    listaCoord = []
    listaEl = []
    listaIn = []
    listaMa = []
    listaGe = []
    listaNo = []
    listaLo = []


    ponty = input('Insira o numero de pontos de sua ponte/slaoq: ')
    ponty = int(ponty)
    print("Insira as coordenadas no padrão x y (em metros)")
    file.write("*COORDINATES"+" \n")
    file.write(str(ponty)+" \n")
    print("Modelo de input: (ponto X) (ponto Y)")
    for i in range(1, ponty + 1):
        print("Coordenada do ponto ")
        coord = input(str(i)+" ")
        file.write(str(i)+" "+str(coord)+" \n")
        listaCoord.append(coord)
        i += 1
    print("\n")

    elementy = input('Insira o número de grupos de elementos: ')
    elementy = int(elementy)
    file.write("*ELEMENT_GROUPS"+" \n")
    file.write(str(elementy)+" \n")
    print("Modelo de input: (elementos no grupo) (tipo)")
    for i in range(1, elementy + 1):
        print("Numero do grupo ")
        elementG = input(str(i)+" ")
        file.write(str(i)+" "+str(elementG)+" \n")
        listaEl.append(elementG)
        i += 1
    print("\n")

    incidency = input('Insira o número de Incidências: ')
    incidency = int(incidency)
    file.write("*INCIDENCES"+" \n")
    file.write(str(incidency)+" \n")
    print("Modelo de input: (inicio) (fim)")
    for i in range(1, incidency + 1):
        print("Número da incidência ")
        incidenceG = input(str(i)+" ")
        file.write(str(i)+" "+str(incidenceG)+" \n")
        listaIn.append(incidenceG)
        i += 1
    print("\n")

    materialy = input('Insira o número de materiais utilizados: ')
    materialy = int(materialy)
    file.write("*MATERIALS"+" \n")
    file.write(str(materialy)+" \n")
    print("Modelo de input: (modulo de elasticidade)")
    for i in range(1, materialy + 1):
        print("Valor do modulo de elasticidade ")
        materialG = input()
        file.write(str(i)+" "+str(materialG)+" \n")
        listaMa.append(materialG)
        i += 1
    print("\n")

    geometry = input('Insira o número de partes com secções diferentes: ')
    geometry = int(geometry)
    file.write("*GEOMETRIC_PROPERTIES"+" \n")
    file.write(str(geometry)+" \n")
    print("Modelo de input: (Área de secção)")
    for i in range(1, geometry + 1):
        print("Valor da área de secção ")
        geometryG = input()
        file.write(str(i)+" "+str(geometryG)+" \n")
        listaGe.append(geometryG)
        i += 1
    print("\n")

    nody = input('Insira o número de nodes fixos: ')
    nody = int(nody)
    file.write("*BCNODES"+" \n")
    file.write(str(nody)+" \n")
    print("Modelo de input: (x = 1 e y = 2)")
    for i in range(1, nody + 1):
        print("Grau de liberdade no node ")
        nodesG = input()
        file.write(str(i)+" "+str(nodesG)+" \n")
        listaNo.append(nodesG)
        i += 1
    print("\n")

    loady = input('Insira o número de forças aplicadas: ')
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
    print("\n")


file.close()