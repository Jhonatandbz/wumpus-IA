from ambiente import *
from random import randint
from posicao import *
import numpy as np

listaVizinho = []

class Agente:

    def vizinho(self, x, y, matriz):
        global listaVizinho
        listaVizinho.clear()
        for a in [(-1,0), (1,0), (0,-1), (0,1)]:
            if ((0 <= x+a[0] < len(matriz)) and (0 <= y+a[1] < len(matriz))):
                listaVizinho.append((x+a[0], y+a[1]))


    def printListaLinha(self, matriz, matrizSensacao):
        
        listaLinha = []

        for i in range(len(matriz)):
            listaLinha.clear()
            for j in range(len(matriz)):
                if(matrizSensacao[i,j] == 0):    listaLinha.append(" -- ")    #Sente nada
                elif(matriz[i,j] == 69):          listaLinha.append(" AG ")    #Agente 
                elif(matrizSensacao[i,j] == 6):  listaLinha.append(" BA ")    #Sente brisa
                elif(matrizSensacao[i,j] == 7):  listaLinha.append(" FR ")    #Sente Fedor
                elif(matrizSensacao[i,j] == 8):  listaLinha.append(" BO ")    #Sente Brilho
                elif(matrizSensacao[i,j] == 13): listaLinha.append("FRBA")    #Sente Fedor e Brisa    
                elif(matrizSensacao[i,j] == 14): listaLinha.append("BOBA")    #Sente Brilho e brisa
                elif(matrizSensacao[i,j] == 15): listaLinha.append("FRBO")    #Sente Fedor e Brilho
                elif(matrizSensacao[i,j] == 21): listaLinha.append("TUDO")    #Sente tudo
            print(listaLinha)


    def cria_matrizSensacao(self, matriz):   
        global listaVizinho
        matrizSensacao = np.zeros((len(matriz), len(matriz)))

        #########Brisa#########        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 1):
                    print(matriz[i, j])
                    self.vizinho(i,j,matriz)
                    for w in range(len(listaVizinho)):
                        matrizSensacao[listaVizinho[w]] = 6

        #########Fedor#########
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 2):
                    self.vizinho(i,j,matriz)
                    for w in range(len(listaVizinho)):
                        matrizSensacao[listaVizinho[w]] = matrizSensacao[listaVizinho[w]] + 7

        #########Brilho#########
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 3):
                    matrizSensacao[i, j] = matrizSensacao[i, j] + 8
        
        print(matrizSensacao)
        print("\n\n")      

        self.printListaLinha(matriz, matrizSensacao)

        return matrizSensacao

    
    def movimento(self, matriz, matrizSensacao):
        global listaVizinho
        mov = Posicao()
        listaSegura = [(0,0)]
        quantflecha = 1

        while True:
            print("\n")
            print(matriz)

            x, y = mov.buscarAgente(matriz)
            print(matrizSensacao[x, y])
            self.vizinho(x,y, matriz)
            direcao = randint(0, len(listaVizinho)-1)

            if(quantflecha == 1 and matrizSensacao[x, y] in [7, 13, 15]):
                direcaoFlecha = mov.atirarFlecha(matriz, listaSegura, listaVizinho)
                quantflecha = 0
                print(direcaoFlecha)
                if(matriz[listaVizinho[direcaoFlecha]]==2): 
                    matriz[listaVizinho[direcaoFlecha]] = 0
                    matrizSensacao = self.cria_matrizSensacao(matriz)
                
            else: 
                situacao = mov.movimentar(listaVizinho[direcao], matriz)

                if(situacao == 0 ): break

                elif(situacao == 2):
                    matriz[x, y] = 0
                    matriz[listaVizinho[direcao]] = 70
                    print("!!!Tu só não é mais incrivel que eu!!!")
                    print('/'*60)
                    matriz = mov.voltar(listaSegura,matriz)
                    print(matriz)
                    break

                elif(situacao == 1): 
                    matriz[x, y] = 0
                    matriz[listaVizinho[direcao]] = 69
            
            listaSegura.append(listaVizinho[direcao])

        self.vizinho(2,2 , matriz)

        print('\n\n\n\n\\n\n')
        print(listaVizinho)
        print('\n\n\n\n\\n\n')
        return matriz


 

    
    
        