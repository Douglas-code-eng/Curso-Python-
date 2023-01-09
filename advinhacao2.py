import random
import time
computador=random.randint(0,10)
contX=contY=0

print("-=-"*10)
print("     JOGO DA ADIVINHAÇÃO")
print("-=-"*10)

print("""\nOlá, sou seu computador. 
Acabei de pensar em um número entre 0 e 10.
Você consegue adivinha-lo sabixão?""")
number=int(input("\nEm qual número pensei? "))
print("hmmmm.....")
time.sleep(2)


while (computador!=number):
    if (computador>number):
        print("\nMais... tente mais uma vez.")
        number=int(input("Qual o seu palpite? "))
        contX+=1
    elif(computador<number):
        print("Menos... tente mais uma vez. ")
        number=int(input("Qual o seu palpite? "))
        contY+=1

if ((contX+contY)==0):
    print("VOCÊ ACERTOU DE PRIMEIRA!!! Tá usando hack? haha")
else:
    print(f"Parabéns! você acertou com {contY+contX+1} tentativas. Tente advinhar em menos vezes na próxima!. ")