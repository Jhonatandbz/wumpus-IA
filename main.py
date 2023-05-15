from ambiente import *
from agente import *


class main:
    gen = Agente()
    amb = Ambiente()
    matriz = amb.cria_matrizAmbiente(4, 4)
    matrizSensacao = gen.cria_matrizSensacao(matriz)
    matriz = gen.movimento(matriz, matrizSensacao)