import random
import time
import operator
jogo={}

jogo['Jogador1']=random.randint(1,6)
jogo['Jogador2']=random.randint(1,6)
jogo['Jogador3']=random.randint(1,6)
jogo['Jogador4']=random.randint(1,6)
print(f'{"VALORES SORTEADOS":>22}')
for k, v in jogo.items():
    time.sleep(0.5)
    print(f"O {k} tirou {v} no dado")

print(f'{"RANKING DE JOGADORES":>25}')

ranking={}
ranking=sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    time.sleep(0.5)
    print(f"{k+1}º lugar: {v[0]} com {v[1]}")


