import random
import time

todosjogos=[]
unico=[]
print("-"*40)
print(f'{"JOGOS DA MEGASENA":>30}')
print("-"*40)

njogos=int(input("Quantos jogos você que que eu sorteie? "))

for i in range(njogos):
    cont=0
    while True:
        num=random.randint(1,60)
        if num not in unico:
            unico.append(num)
            cont+=1
        if cont>=6:
            break    
    unico.sort()
    todosjogos.append(unico[:])
    unico.clear()

print("=="*4, f"SORTEANDO {njogos} JOGOS", "=="*4)
for k,j in enumerate(todosjogos):
    time.sleep(1)
    print(f"Jogo {k+1}: {j}")
print("=="*4, "<  BOA SORTE  >", "=="*4)