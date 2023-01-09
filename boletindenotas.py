boletim=[]

while True:
    nome=input("Nome: ")
    nota1=float(input("Nota 1: "))
    nota2=float(input("Nota 2: "))
    media=(nota1+nota2)/2
    boletim.append([nome, [nota1, nota2], media])

    resp=input("Deseja continuar? [S/N] ")
    if resp in "Nn":
        break

print("-="*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-"*30)

for j,k in enumerate(boletim):
    print(f'{j:<4}{k[0]:<10}{k[2]:>8.1f}')
print("-"*30)
while True:
    opc=int(input("Deseja ver as notas de qual aluno? (999 para parar) "))
    if opc==999:
        print("Finalizando programa...")
        break
    print(f"As notas de {boletim[opc][0]} são: {boletim[opc][1]}")
    