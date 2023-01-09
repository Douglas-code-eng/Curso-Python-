dados=[]
pessoas={}
mulheres=[]
soma=media=0
while True:
   
    pessoas['Nome']=input("Nome: ")
    
    while True:
        pessoas['Sexo']=input("Sexo [M/F]: ").upper()
        if pessoas["Sexo"] in "MF":
            break
        print("Erro. Por favor digite M ou F! ")
    if pessoas["Sexo"]=="F":
        mulheres.append(pessoas["Nome"])
    pessoas['Idade']=int(input("Idade: "))
    soma+=pessoas['Idade']
    dados.append(pessoas.copy())
    pessoas={}
    resp=input("Deseja continuar?[S/N]: ")
    if resp in "Nn":
        break
print("-="*40)
media=soma/len(dados)

print(f"- O grupo tem {len(dados)} pessoas;")
print(f"- A média das idades é {media:5.1f} anos;")
print(f"- A mulheres no grupo são {mulheres};")
print(f"- As pessoas ácima da média são: ")
for p in dados:
    if p['Idade']>=media:
        print(F"  -> {p}")