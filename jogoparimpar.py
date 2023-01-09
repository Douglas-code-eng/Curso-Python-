import random
contX=contY=0

print("-="*15)
print("JOGO DO PAR OU ÍMPAR")
print("-="*15)


while(True):
    jogador=int(input("Digite um valor: "))
    escolha= input("Par ou Ímpar [P/I]: ")

    computador=random.randint(0,10)
    soma=jogador+computador
    if soma % 2 == 0:
        print("--"*30)
        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma}  e PAR ")
        print("--"*30) 
        if (escolha=="P"):  
            print("""Você GANHOU!
            Vamos mais uma vez...""")
            contX+=1
        elif(escolha=="I"):
            print("Você PERDEU!")
            break
    else:
        print("--"*30)
        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma}  e ÍMPAR ")
        print("--"*30) 
        if (escolha=="P"):  
            print("Você PERDEU!")
            break
        elif(escolha=="I"):
            print("""Você GANHOU!
            Vamos mais uma vez...""")
            contY+=1

print(f"\nGAME OVER. Você venceu {contX+contY} vezes")
