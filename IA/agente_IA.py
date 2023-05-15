from functools import cached_property
from random import random, randrange, randint, choice
from typing import Sized
import numpy as np


class Agente():
    def __init__(self, nome, geracao=0):
        self.nome = nome
        self.geracao = geracao
        self.flecha = True
        self.vivo = True
        self.matou = False
        self.ouro = False
        self.ganhou = False
        self.posicao = (0, 0)
        self.andou_fora = 0
        self.andou_dentro = 0
        self.fitness = 0
        self.cromossomo = []

    def crossover(self, pai2):

        tam1 = len(self.cromossomo)
        tam2 = len(pai2.cromossomo)

        corte1 = randrange(tam1)
        corte2 = randrange(tam2)

        filho1 = self.cromossomo[:corte1] + pai2.cromossomo[corte2:]

        filho2 = pai2.cromossomo[:corte2] + self.cromossomo[corte1:]

        filhos = [Agente(f'{self.geracao+1}-{0}', self.geracao+1),
                  Agente(f'{self.geracao+1}-{0}', self.geracao+1)]

        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2

        return filhos

    def mutacao(self, taxa_mutacao):

        if random() < taxa_mutacao:

            tamanhoCromossomo = len(self.cromossomo)

            if tamanhoCromossomo > 1:
                x, y = randrange(tamanhoCromossomo), randrange(
                    tamanhoCromossomo)

                ', '.join(self.cromossomo[:x])

                self.cromossomo = self.cromossomo[:x] + [self.cromossomo[y]] + \
                    self.cromossomo[x+1:y] + \
                    [self.cromossomo[x]] + self.cromossomo[y+1:]

        return self


class Gerador():
    def __init__(self, tamanho_populacao, matrizAmb, matrizSen, max_Cromossomo, taxa_mutacao, quant_geracoes):
        self.tamanho_populacao = tamanho_populacao
        self.max_cromossomo = max_Cromossomo
        self.populacao: Agente = []
        self.geracao = 0
        self.melhor_solucao: Agente = Agente('teste')
        self.matrizAmb = matrizAmb
        self.matrizSen = matrizSen
        self.taxa_mutacao = taxa_mutacao
        self.quant_geracoes = quant_geracoes

    def movimento(self, cromossomo: list, flecha: bool):

        wumpus = False
        gold = False
        percorreu = 0

        x, y = 0, 0

        if len(cromossomo) > self.max_cromossomo:
            del(cromossomo[self.max_cromossomo:])

        for i in range(len(cromossomo)):

            if self.matrizAmb[x, y] == 2:
                del(cromossomo[i+1:])
                return cromossomo, flecha, wumpus, gold, percorreu, False, False
            if self.matrizAmb[x, y] == 1:
                del(cromossomo[i+1:])
                return cromossomo, flecha, wumpus, gold, percorreu, False, False
            if x+y == 0 and gold:
                del(cromossomo[i+1:])
                return cromossomo, flecha, wumpus, gold, percorreu, True, True

            direcao = self.vizinho(x, y, self.matrizAmb)
            caminho = cromossomo[i]

            if caminho not in direcao:
                caminho = choice(direcao)

            # Verifica se tem ouro
            if self.matrizSen[x, y] in [8, 15, 21]:
                cromossomo[i] = 'P'
                self.matrizAmb[x, y] = 0
                self.matrizSen[x, y] -= 8
                gold = True

            # verifica se esta sentindo fedor e tem flecha pra atirar
            elif self.matrizSen[x, y] in [7, 13] and flecha:
                if caminho == 'N' or caminho == 'AN':
                    cromossomo[i] = 'AN'
                    if self.matrizAmb[x+1, y] == 2:
                        self.matrizAmb[x+1, y] = 0
                        wumpus = True

                if caminho == 'S' or caminho == 'AS':
                    cromossomo[i] = 'AS'
                    if self.matrizAmb[x-1, y] == 2:
                        self.matrizAmb[x-1, y] = 0
                        wumpus = True

                if caminho == 'L' or caminho == 'AL':
                    cromossomo[i] = 'AL'
                    if self.matrizAmb[x, y+1] == 2:
                        self.matrizAmb[x, y+1] = 0
                        wumpus = True

                if caminho == 'O' or caminho == 'AO':
                    cromossomo[i] = 'AO'
                    if self.matrizAmb[x, y-1] == 2:
                        self.matrizAmb[x, y-1] = 0
                        wumpus = True

                flecha = False

            else:
                if caminho == 'N':
                    cromossomo[i] = 'N'
                    x += 1

                if caminho == 'S':
                    cromossomo[i] = 'S'
                    x -= 1

                if caminho == 'L':
                    cromossomo[i] = 'L'
                    y += 1

                if caminho == 'O':
                    cromossomo[i] = 'O'
                    y -= 1

                percorreu += 1

        tamanho = len(cromossomo)
        while tamanho < self.max_cromossomo:

            if self.matrizAmb[x, y] == 2:
                return cromossomo, flecha, wumpus, gold, percorreu, False, False
            if self.matrizAmb[x, y] == 1:
                return cromossomo, flecha, wumpus, gold, percorreu, False, False
            if x+y == 0 and gold:
                return cromossomo, flecha, wumpus, gold, percorreu, True, True

            direcao = self.vizinho(x, y, self.matrizAmb)
            caminho = choice(direcao)

            # Verifica se tem ouro
            if self.matrizSen[x, y] in [8, 15, 21]:
                cromossomo.append('P')
                self.matrizAmb[x, y] = 0
                self.matrizSen[x, y] -= 8
                gold = True

            # verifica se esta sentindo fedor e tem flecha pra atirar
            elif self.matrizSen[x, y] in [7, 13] and flecha:
                if caminho == 'N':
                    cromossomo.append('AN')
                    if self.matrizAmb[x+1, y] == 2:
                        self.matrizAmb[x+1, y] = 0
                        wumpus = True
                if caminho == 'S':
                    cromossomo.append('AS')
                    if self.matrizAmb[x-1, y] == 2:
                        self.matrizAmb[x-1, y] = 0
                        wumpus = True
                if caminho == 'L':
                    cromossomo.append('AL')
                    if self.matrizAmb[x, y+1] == 2:
                        self.matrizAmb[x, y+1] = 0
                        wumpus = True
                if caminho == 'O':
                    cromossomo.append('AO')
                    if self.matrizAmb[x, y-1] == 2:
                        self.matrizAmb[x, y-1] = 0
                        wumpus = True

                flecha = False

            else:
                if caminho == 'N':
                    cromossomo.append(caminho)
                    x += 1
                if caminho == 'S':
                    cromossomo.append(caminho)
                    x -= 1
                if caminho == 'L':
                    cromossomo.append(caminho)
                    y += 1
                if caminho == 'O':
                    cromossomo.append(caminho)
                    y -= 1
                percorreu += 1

            tamanho += 1

        return cromossomo, flecha, wumpus, gold, percorreu, True, False

    def melhoSer(self, ser: Agente):

        if self.melhor_solucao.fitness < ser.fitness:
            self.melhor_solucao = ser

    def selecionaPai(self):
        soma = 0

        pai = 0

        for i in range(self.tamanho_populacao):
            soma += self.populacao[i].fitness

        sorteio = randrange(soma)
        pai = -1

        while soma > sorteio:
            pai += 1
            soma -= self.populacao[pai].fitness

        return pai

    def gerarGeracao(self):

        nova_populacao = []

        aux = 0

        self.geracao += 1

        for novos_individuos in range(0, self.tamanho_populacao, 2):

            pai1 = 0
            pai2 = self.selecionaPai()
            while pai1 == pai2:
                pai2 = self.selecionaPai()

            filhos = self.populacao[pai1].crossover(self.populacao[pai2])

            filhos[0].nome = f'{self.geracao}-{aux}'
            filhos[1].nome = f'{self.geracao}-{aux+1}'

            aux += 2

            nova_populacao.append(filhos[0].mutacao(self.taxa_mutacao))
            nova_populacao.append(filhos[1].mutacao(self.taxa_mutacao))

        return nova_populacao

    def calcularFitness(self):

        for individuo in self.populacao:

            soma = 0

            if individuo.vivo:
                soma += 100
            else:
                soma -= 100
            if individuo.matou:
                soma += 350
            if individuo.ouro:
                soma += 550
            if individuo.ganhou:
                soma += 1234

            #soma -= (individuo.andou_fora*2)

            soma += (individuo.andou_dentro * 2)
            #soma += (individuo.andou_dentro*2)

            if soma <= 0:
                soma = 1

            individuo.fitness = soma

    def vizinho(self, x, y, matriz):
        contador = 0
        direcao = []
        for a in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if ((0 <= x+a[0] < len(matriz)) and (0 <= y+a[1] < len(matriz))):
                if contador == 0:
                    direcao.append('S')
                if contador == 1:
                    direcao.append('N')
                if contador == 2:
                    direcao.append('O')
                if contador == 3:
                    direcao.append('L')
            contador += 1

        return direcao

    def inicio(self):

        for individuo in range(self.tamanho_populacao):
            ag = Agente(f'{self.geracao}-{individuo}')
            ag.cromossomo, ag.flecha, ag.matou, ag.ouro, ag.andou_dentro, ag.vivo, ag.ganhou = self.movimento(
                ag.cromossomo, ag.flecha)

            self.populacao.append(ag)

        self.calcularFitness()

        self.populacao = sorted(
            self.populacao, key=lambda populacao: populacao.fitness, reverse=True)


        self.melhor_solucao = self.populacao[0]

        for ger in range(self.quant_geracoes):

            nova_populacao: list = self.gerarGeracao()
            self.populacao = []

            for individuo in range(self.tamanho_populacao):
                ag: Agente = nova_populacao[individuo]

                ag.cromossomo, ag.flecha, ag.matou, ag.ouro, ag.andou_dentro, ag.vivo, ag.ganhou = self.movimento(
                    ag.cromossomo, ag.flecha)

                self.populacao.append(ag)

            self.calcularFitness()

            self.populacao = sorted(
                self.populacao, key=lambda populacao: populacao.fitness, reverse=True)

            self.melhoSer(self.populacao[0])

            print(f'Nome -> {self.populacao[0].nome}\
                \nTamanho Cromossomo -> {len(self.populacao[0].cromossomo)}\
                \nFitness - > {self.populacao[0].fitness}\n\n')

            # \n{self.populacao[0].cromossomo}\

        return self.melhor_solucao
