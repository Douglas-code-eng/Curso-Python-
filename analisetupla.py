numbers=(int(input("Digite um número: ")), 
int(input("Digite um número: ")),
int(input("Digite um número: ")),
int(input("Digite um número: ")))
count=0
print(f"Vc digitou [number]")
for i in numbers:
    if (i%2==0):
        count+=1

print("O valor  9 apareceu", numbers.count(9), "vezes")
print("O primeiro 3 foi digitado na posição", numbers.index(3))
print("Existem ", count, " números pares nos digitados")
