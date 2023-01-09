from datetime import datetime

dados={
    'Nome': input("Nome: "),
    'Idade': datetime.now().year -(int(input("Ano de Nascimento: "))),
    'CTPS': int(input("Carteira de trabalho (0 não tem): "))}

if dados['CTPS']==0:
    print("-="*20)
    for k, v in dados.items():
        print(f"O {k} tem valor {v}")
else:
    dados['Contrato']=int(input("Ano de Contratação: "))
    dados['Salario']=float(input("Salário: "))
    dados['Aposentadoria']= ((35-(2023-dados['Contrato']))+dados['Idade'])
    print("-="*20)
    for k,v in dados.items():
        print(f"O {k} tem valor {v}")


