numbers= ("zero", "um", "dois", "três", "quatro", "cinco", "seis","sete","oito", "nove", "dez")

num=int(input("Digite um número entre 0 e 10: "))

while (num>10 or num<0):
    num=int(input("Digite novamente: "))

print(numbers[num])