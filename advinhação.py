import random
import time
computador=random.randint(0,5)
print("-"*10, "JOGO DA ADIVINHAÇÃO", "-"*10, "\n")

print("="*55)
print("Vou pensar em um número entre 0 e 5. Tente advinhar....")
print("="*55)

number=int(input("Em qual número pensei? "))
print("hmmmm.....")
time.sleep(2)

if (number==computador):
    print("\nVOCÊ ACERTOU!!!")
    print("Tu é um telepata? haha ")
else:
    print("\nVOCÊ ERROU!")
    print("Mais sorte da próxima vez...")
