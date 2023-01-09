def linha(tam=42):
    return '-'*tam


def titulo(msg):
    print(linha())
    print(f"\033[36m{(msg.upper()).center(42)}\033[m")
    print (linha())

def menu(lst):
    from time import sleep
    titulo('menu principal')
    k=0
    for i in lst:
        sleep(0.7)
        print(f'\033[33m{k+1}\033[m - \033[34m{i}\033[m', flush=True)
        k+=1
        
    print(linha())
    try:
        opc= int(input("\033[32mQual sua opção? \033[m"))
    except (ValueError, TypeError):
        print("\033[31mHouve um erro no tipo de dado casdastrado. Favor digite novamente\033[m")
    else:
        return opc

def leinaint(num):
    while True:
        try:
            num=int(input('Idade: '))
        except (TypeError, ValueError):
            print('\033[31mErro! Por favor digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print("\033[31mErro! usuário preferiu não digitar o valor\033[m")
            return 0
        else: 
            return num
