import numpy as np
from random import randint

class Ambiente:

    def vizinho(self, x, y, matriz):
        listaVizinho =[]
        for a in [(-1,0), (1,0), (0,-1), (0,1)]:
            if ((0 <= x+a[0] < len(matriz)) and (0 <= y+a[1] < len(matriz))):
                listaVizinho.append((x+a[0], y+a[1]))
        
        
        return listaVizinho

    def cria_matrizAmbiente(self, num_linhas, num_colunas):
        um_linhas = num_linhas
        num_colunas = num_colunas
        matriz = np.zeros((num_linhas, num_colunas))
        i=0
        media = int((num_linhas+num_colunas)/2) 
        while (i < media-1):                        #poço
            x = randint(0, num_linhas-1)
            y = randint(0, num_colunas-1)
            if(x+y !=0 and matriz[x, y]== 0):
                matriz[x, y] = 1
                i += 1
        while True:                                 #wumpus                                             
            x = randint(0, num_linhas-1)
            y = randint(0, num_colunas-1)
            if(x+y !=0 and matriz[x, y]==0):
                matriz[x, y] = 2
                break
        while True:                                 #ouro
            x = randint(0, num_linhas-1)
            y = randint(0, num_colunas-1)
            if(x+y !=0 and matriz[x, y]==0):
                matriz[x, y] = 3
                break

        print(matriz)
        print("\n")

        matrizSensacao = self.cria_matrizSensacao(matriz)

        return matriz, matrizSensacao

    
    def cria_matrizSensacao(self, matriz):
        matrizSensacao = np.zeros((len(matriz), len(matriz)))

        #########Brisa#########        
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 1):
                    listaVizinho = self.vizinho(i,j,matriz)
                    for w in range(len(listaVizinho)):
                        matrizSensacao[listaVizinho[w]] = 6

        #########Fedor#########
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 2):
                    listaVizinho = self.vizinho(i,j,matriz)
                    for w in range(len(listaVizinho)):
                        matrizSensacao[listaVizinho[w]] = matrizSensacao[listaVizinho[w]] + 7

        #########Brilho#########
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j] == 3):
                    matrizSensacao[i, j] = matrizSensacao[i, j] + 8
        
        print(matrizSensacao)
        print("\n\n")      

        return matrizSensacao