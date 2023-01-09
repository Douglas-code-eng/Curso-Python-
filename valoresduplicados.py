valores=[]

while True:
    valor=int(input("Digite um valor: "))
    if valor in valores:
        print("Valor já existente, não vou adicionar. ")
    else:
        valores.append(valor)
        print("Valor adicionado com sucesso.")
    resposta= input("Deseja Continuar? [S/N]")
    if resposta=="N" or resposta=="n":
        break
valores.sort()
print(f"Os valores digitados foram: {valores}")

