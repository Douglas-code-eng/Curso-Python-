somaidade=0

n=int(input("Informe a quantidade de pessoas: "))
velho=0
mulheresnovas=[]
for i in range(n):
    print("="*10 + " "+ str(i+1)+ "º pessoa ","="*10 )
    nome=input("\nNome:")
    idade= int(input("Idade: "))
    sexo= input("Sexo [F/M]: ")

    if (velho<idade and sexo=="M"):
        velho=idade
        nomemaisvelho=nome
    if (idade<20 and sexo=="F"):
        mulheresnovas.append(nome)

    somaidade+=idade
    
mediaidade=somaidade/n

print("-=-"*5, "\n RESULTADOS: \n","-=-"*5,
f"""\n1) A media de idade do grupo de {n} pessoas foi {round(mediaidade,2)} anos.
2) O homem mais velho é {nomemaisvelho} e tem {velho} anos.
3) Existe {len(mulheresnovas)} mulheres com menos de 20 anos.
""")
