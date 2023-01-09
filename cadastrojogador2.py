
total=0
gols=[]
geral=[]
while True:
    jogadores={'Nome':input("Nome: ")}
    npartidas=int(input(f"Quantas partidas {jogadores['Nome']} jogou? "))
    for i in range(npartidas):
        gol=int(input(f"Quantos gols {jogadores['Nome']} fez na {i+1}º partida? "))
        total+=gol
        gols.append(gol)
    jogadores['Gols']=gols
    jogadores['Total']=total
    geral.append(jogadores.copy())
 
    while True:
        resp=input("Deseja continuar? [S/N]").upper()[0]
        if resp in "SN":
            break
        print("Erro! Digite apenas S ou N")
    if resp in "Nn":
        break
    print("-="*25)
    gols=[]
    jogadores.clear()
    total=gol=0

print("-="*30)
print(f"{'COD':<4}{'NOME':<15}{'GOLS':>9}{'TOTAL':>11}")
print("-"*40)

for j,i in enumerate(geral):
    print(f"{j:<4}", end="")
    for v in i.values():
         print(f'{str(v):<15}', end='')
    print()
print("-"*40)

while True:
    opc=int(input("Deseja consultar os gols de qual jogador? [999 interrompe] "))
    if opc==999:
        print("Finalizando programa... até breve!")
        break
    if opc>=len(geral):
        print("Erro! índice do jogador não está presente no escopo.")
        break
    else:
        print("--"*25)
        print(f"LEVANTAMENTO DO JOGADOR {str(geral[opc]['Nome']).upper()}")
        
        for i, j in enumerate(geral[opc]['Gols']):
            print(f"{'=>':>6} Na {i+1}º partida, fez {str(j)} gols")