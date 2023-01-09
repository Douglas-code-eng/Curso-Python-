import random 
import time

itens= ("Pedra", "Papel", "Tesoura")

computador= random.randint(0, 2)
print("""Suas opções são:
[0] Pedra 
[1] Papel
[2] Tesoura""")
jogador= int(input("Qual sua jogada? "))

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO!!!")


print("-="*16)
print("\nJogador jogou {} ".format(itens[jogador]))
print("Computador jogou {} \n".format(itens[computador]))
print("-="*16)

if (computador==0):
    if (jogador==0):
        print("Empate! Tente novamente. " )
    elif (jogador==1):
        print("Jogador Ganhou! Parabéns!")
    elif (jogador==2):
        print("Computador Ganhou! Boa sorte na próxima")

elif (computador==1):
    if (jogador==0):
        print("Computador Ganhou! Boa sorte na próxima")
    elif (jogador==1):
        print("Empate! Tente novamente. " )
    elif (jogador==2):
        print("Jogador Ganhou! Parabéns!")

elif (computador==2):
    if (jogador==0):
        print("Jogador Ganhou! Parabéns!")
    elif (jogador==1):
        print("Computador Ganhou! Boa sorte na próxima")
    elif (jogador==2):
        print("Empate! Tente novamente. " )
    




