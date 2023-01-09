print("=="*10, "BANCO DOUGLAS", "=="*10)
teste=1
valor_sacado=int(input("Informe o valor a ser sacado: "))
cedulas_50=cedulas_1=cedulas_10=0
while (valor_sacado!=0):
    if (valor_sacado>=50):
        cedulas_50+=1
        valor_sacado-=50
    elif (valor_sacado<50 and valor_sacado>=10):
        cedulas_10+=1
        valor_sacado-=10
    elif(valor_sacado<10):
        cedulas_1+=1
        valor_sacado-=1
    
print(f"{cedulas_50} cedulas de 50 reais, {cedulas_10} de 10 reais, {cedulas_1} de 1 real")