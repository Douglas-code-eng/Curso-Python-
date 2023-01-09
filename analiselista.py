valores=[]
n=0
while True:
    
    valores.append(int(input("Digite um valor:")))
    resposta=input("Deseja continuar?[S/N] ")
    if resposta=="N":
        break

print(f"Você digitou {len(valores)} elementos.")
valores.sort(reverse=True)
print(f"A ordem inversa descrecente deles é {valores}.")

if 5 in valores:
    print("O valor 5 está presente na lista.")
else:
    print("O valore 5 não está presente na lista.")