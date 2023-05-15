import numpy as np
from random import randint

class Ambiente:
    def cria_matrizAmbiente(self, num_linhas, num_colunas):
        self.num_linhas = num_linhas
        self.num_colunas = num_colunas
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

        matriz[0, 0] = 69
        print(matriz)
        print("\n")
        return matriz 
        