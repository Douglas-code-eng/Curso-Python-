dados={'Nome':input("Nome: ")}
total=0
gols=[]
npartidas=int(input(f"Quantas partidas {dados['Nome']} jogou? "))

for i in range(npartidas):
    gol=int(input(f"Quantos gols {dados['Nome']} fez na {i+1}º partida? "))
    total+=gol
    gols.append(gol)
dados['Gols']=gols
dados['Total']=total

print("-="*30)
print(dados)
print("-="*30)

for k,v in dados.items():
    print(f"O campo {k} tem o valor {v}")

print("-="*30)
print(f"O jogador {dados['Nome']} jogou {npartidas} partidas.")

for i, j in enumerate(gols):
    print(f"{'=>':>6} Na {i+1}º partida, fez {j} gols")
    
print(f"For um total de {total} gols")