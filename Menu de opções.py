import time

n1=int(input("Primeiro numero: "))
n2=int(input("Segundo numero: "))

while (True):
   

    print("""O que deseja fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Digitar novos números
    [5] Sair
    """)
    resp=int(input())

    if (resp==1):
        print(f"{n1} + {n2} = {n1+n2}")
    if (resp==2):
        print(f"{n1} x {n2} = {n1*n2}")
    if (resp==3):
        if (n1==n2):
            print(f"Ambos os números são iguais")
        elif(n1>n2):
            print(f"{n1} é o maior")
        else:
            print(f"{n2} é o maior")
    if (resp==4):
        n1=int(input("Primeiro numero: "))
        n2=int(input("Segundo numero: "))
    if (resp==5):
        print("Finalizando...")
        time.sleep(3)
        break

print("Programa finalizado com sucesso! Até a próxima")
