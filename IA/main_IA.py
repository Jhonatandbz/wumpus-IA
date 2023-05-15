from agente_IA import Gerador
from agente_IA import Agente
from ambiente_IA import Ambiente

#def main()

tamanho_populacao = 100
max_cromossomo = 200
taxa_mutacao = 0.05
quant_geracoes = 100

amb = Ambiente()
ag = Agente('primeiro')
ambiente, sensacao = amb.cria_matrizAmbiente(5, 5)
inicio = Gerador(tamanho_populacao, ambiente, sensacao, max_cromossomo, taxa_mutacao, quant_geracoes)
ag = inicio.inicio()

print("="*20)
print(f'Nome -> {ag.nome}\
        \nTamanho Cromossomo -> {len(ag.cromossomo)}\
        \nFitness - > {ag.fitness}\n\n')
print("="*20)
#if __name__ == 'main':
    #main()