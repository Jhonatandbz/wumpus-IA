from random import randint

class Posicao():

    def movimentar(self, direcao, matriz):
        if(matriz[direcao] == 1):
            print("Caiu no poço")
            return 0

        if(matriz[direcao] == 2):
            print("Wumpus te matou")
            return 0
            
        if(matriz[direcao] == 3):
            print("Pegou o ouro")
            return 2

        return 1

    def atirarFlecha(self, matriz, listaSegura, listaVizinho):

        while True:

            direcao = randint(0, len(listaVizinho)-1)

            if(listaVizinho[direcao] not in listaSegura and matriz[listaVizinho[direcao]] == 2):
                print("="*60)
                print("Grito!!!")
                print("Matou o wumpus")
                break
            elif(listaVizinho[direcao] not in listaSegura and matriz[listaVizinho[direcao]] == 0):
                print("="*60)
                print("Errou o Wumpus")
                break

        return direcao


    def buscarAgente(self, matriz):

        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if(matriz[i, j]==69 or matriz[i, j]==70):
                    return i, j

    def voltar(self, listaSegura, matriz):

        print("bugou na hr de voltar")
        i = len(listaSegura)-1

        while i >= 0:
            print(matriz)
            x, y = self.buscarAgente(matriz)
            matriz[x, y] = 0
            matriz[listaSegura[i]] = 70
            i -= 1

        return matriz

