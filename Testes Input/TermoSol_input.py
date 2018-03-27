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


    #REVER LOGICA DE INPUT DO BCNODES E LOADS

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

"""

elif(choice == '2'):
    print('Os seguintes arquivos foram encontrados:')
    fileList = []
    count = 0

    fileList2 = []
    count2 = 0

    for i in sorted(os.listdir('Saves')):

        print(str(count) + ' - ' + i)
        fileList.append(i)
        count+= 1

    while(True):
        print('Escolha o arquivo: (Sem o .wav)')
        choice = input()
        try:
            if(choice.isdigit()):
                print("\nLOADING BY INDEX")
                self.wav, self.fs= sf.read("Saves/" + fileList[int(choice)]);
                audio = self.wav
                if(not isinstance(self.wav[0], float)):
                    audio = self.wav[:,0]
            else:
                print('\nLOADING BY NAME')
                self.wav, self.fs = sf.read("Saves/" + choice + ".wav");
                audio = self.wav
                if(not isinstance(self.wav[0], float)):
                    audio = self.wav[:,0]

            break
        except:
            print('arquivo requisitado nao existe!!!\n')

while(True):
    print('1- Salvar\n2- Reproduzir \n3- plotar grafico \n4- Aplicar passa baixa\n5- Tentar novamente\n6- Desmodularizar\n7- Adicionar na stack\n8- Reproduzir stack')
    choice = input()
    if(choice == '1'):
        print("Com qual nome devemos gravar")
        name = input()
        self.escrever(name, audio)
        print("Salvo como: " + name )
    elif(choice == '2'):
        print("Reproduzindo")
        self.playSound(audio, wait = False)
        print("Para parar aperte ENTER" )
        input()
        sd.stop()
    elif(choice == '3'):
        print('\nAplicar transformada de fourier ? (Y ou N)')
        ft = input()
        if(ft == 'y'):
            fftAudio = self.FFT(audio)
            print(fftAudio)
            print(len(fftAudio[0]))
            plt.plot(fftAudio[0],fftAudio[1]) 
            plt.title('Recebido', fontsize=18)
            plt.xlabel('Frequencia (Hz)', fontsize=16)
            plt.ylabel('Energia', fontsize=16)
            plt.show()
        elif(ft == 'n'):
            print('mostrar um zoom do grafico ? (Y ou N)')
            zoom = input()
            plt.plot(np.arange(len(audio) if zoom == 'n' else 1000),audio if zoom == 'n' else audio[40000:41000])
            plt.show()
        else:
            print('opcaoo invalida')
    elif(choice == '4'):
        print("\nDesmodularizar com passa baixa")
        print("\nFrequência de corte (deve ser igual à frequencia de corte na modularização)")
        while True:
            try:
                choice = int(input())
                break
            except:
                print('Coloque uma frequencia valida')
        audio = self.LPF(audio,2000,self.fs)
        maxAudio = max(audio)
        print(maxAudio)
        audio /= maxAudio
        #self.stack.append([audio,choice]) #formato wavFreq
        
        print('Filtrado!\nQuer reprouzir? (Y ou N)')
        choice = input()
        if(choice == 'y' or choice == 'Y'):
            self.playSound(audio, wait = False)
            print("Para parar aperte ENTER" )
            input()
            sd.stop()
    elif(choice == '5'):
        return
    elif(choice == '6'):
        print('Frequência da desmodularização (deve ser igual à modularização):')
        while True:
            try:
                choice = int(input())
                break
            except:
                print('Coloque uma frequencia valida')
        audio = self.desmodularizar(audio,choice)
        print("Desmodularizado")
    elif(choice == '7'):
        print('colocando na stack')
        self.stack.append(audio) #formato wavFreq
        print("salvo na stack na posição ", len(self.stack) - 1)
    elif(choice == '8'):
        print("Juntando canais...")
        stream = self.stack[0]
        
        for i in range(1,len(self.stack)):
            stream = self.Somar(stream, self.stack[i]);
            
            fftAudio = self.FFT(stream)
            plt.plot(fftAudio[0],fftAudio[1]) 
            plt.title('Recebido', fontsize=18)
            plt.xlabel('Frequencia (Hz)', fontsize=16)
            plt.ylabel('Energia', fontsize=16)
            plt.show()
            
        print("Reproduzindo")
        self.playSound(audio, wait = False, looping = True)
        print("Para parar aperte ENTER" )
        input()
        sd.stop()
        
    else:
        print("\nalgo errado com a sua escolha\n")"""