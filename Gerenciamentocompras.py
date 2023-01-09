import time

print("="*5, "Lojas São Paulo", "="*5, "/n")

valor=float(input("Qual foi o valor da sua compra?  $"))

print("""\nOpções de pagamento: 
[0] À vista dinheiro/cheque;
[1] À vista no cartão;
[2] Até duas vezes no cartão;
[3] 3 ou mais vezes no cartão.
""")

opcao=int(input("Com qual opção irá pagar? "))
print("Processando valores....")
time.sleep()
print("-="*30)
if opcao==0:
    preco_final= valor*0.90
    print(f"\nSua compra foi ${valor} reais, mas com desconto de 10% por pagar à vista ficou por ${preco_final} reais. ")
elif opcao==1:
    preco_final=valor*0.95
    print(f"\nSua compra foi ${valor} reais, mas com desconto de 5% ficou por ${preco_final} reais. ")
elif opcao==2:
    parcelas=int(input("\nEm quantas vezes irá parcelar? "))
    preco_final= valor/parcelas
    print(f"\nSua compra será divida em {parcelas} parcelas sem juros de ${preco_final} reais cada.")
elif opcao==3: 
    parcelas=int(input("\nEm quantas vezes irá parcelar? "))
    preco_final= (valor*1.20)/parcelas
    print(f"\nSua será divida em {parcelas} parcelas com juros de 20% e ${preco_final} reais cada.")
    print(f"\nAssim, sua compra de ${valor} reais sariá por ${(valor*1.20)} reais")
else:
    print("Opção de pagamento inválida. ")