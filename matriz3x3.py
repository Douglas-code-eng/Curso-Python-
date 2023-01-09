matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma1=soma2=maior=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f"Digite um valor para posição [{l+1}, {c+1}]: "))
print("-="*30)
for l  in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]:^5}" , end="")
    print()
print("-="*30)

for l in range(3):
    for c in range(3):
        if matriz[l][c]%2==0:
            soma1+=matriz[l][c]
        if matriz[l][c]==matriz[l][2]:
            soma2+=matriz[l][c]
        if matriz[l][c]==matriz[1][c]:
            if matriz[l][c]>maior:
                maior=matriz[l][c]

print(f"A soma dos números pares é {soma1}")
print(f"A soma dos números da terceira coluna é {soma2}")
print(f"O maior valor da segunda linha é {maior}")

