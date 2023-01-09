
def voto(a=0):
    from datetime import datetime
    
    idade=datetime.now().year-a
    if idade<16:
        return print(f"Com {idade} anos, o voto é NEGADO")
    elif (idade>=16 and idade<18) or idade>=70:
        return print(f"Com {idade} anos, o voto é OPCIONAL")
    else:
        return print(f"Com {idade} anos, o voto é OBRIGÁTORIO")

ano=int(input("Em que ano vc nasceu? "))
voto(ano)



