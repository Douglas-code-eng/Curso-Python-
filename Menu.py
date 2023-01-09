import time

n1=int(input("Primeiro numero: "))
n2=int(input("Segundo numero: "))

while (True):
   
    print("=-="*11)
    print("""
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Digitar novos números
    [5] Sair """)
    resp=int(input(">>>>> O que deseja fazer? "))

    print("=-="*11)

    if (resp==1):
        time.sleep(1)
        print(f"Soma: {n1} + {n2} = {n1+n2}")
    if (resp==2):
        time.sleep(1)
        print(f"Multiplicação: {n1} x {n2} = {n1*n2}")
    if (resp==3):
        time.sleep(1)
        if (n1==n2):
            print(f"Ambos os números são iguais")
        elif(n1>n2):
            print(f"{n1} é o maior")
        else:
            print(f"{n2} é o maior")
    if (resp==4):
        print("Informe os números novamente ")
        n1=int(input("Primeiro numero: "))
        n2=int(input("Segundo numero: "))
    if (resp==5):
        print("Finalizando...")
        time.sleep(3)
        break

print("Programa finalizado com sucesso! Até a próxima")
