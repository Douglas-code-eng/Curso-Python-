try:
    a=int(input("Numerador: "))
    b=int(input("Denominador: "))
    r=a/b
except (TypeError, ValueError):
    print("Tivemos um problema com os tipos de valores digitados")
except (ZeroDivisionError):
    print("Não é possível dividir por zero. ")
except (KeyboardInterrupt):
    print("Usuário preferiu não informar os valores")
else: 
    print(f"O resultado foi {r}")
