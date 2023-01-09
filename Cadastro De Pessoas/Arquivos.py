from bibliotecas import titulo

def arquivoexiste(nome):
    try: 
        a=open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True

def criararquivo(nome):
    try:
        a=open(nome, 'xt+')
        a.close()
    except:
        print("\033[31mHouve um erro na criação do arquivo\033[m")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def lerarquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print("\033[31mHouve um erro na leitura do arquivo\033[m")
    else:
        titulo('Pesssoas cadastradas')
        print(a.read())

    finally:
        a.close()    
def cadastro(arq,nome='<Desconhecido>', idade=0):
    try: 
        a= open(arq, 'at')
    except:
        print("\033[31mHouve um erro na abertura do arquivo.\033[m")
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos\n' )
        except:
            print("\033[31mHouve um erro na hora de cadastrar os dados.\033[m")
        else:
            print(f"{nome} cadastrado com sucesso.")
            a.close()

