import bibliotecas
import Arquivos
from time import sleep
arq="Cadastro.txt"

if not Arquivos.arquivoexiste(arq):
    Arquivos.criararquivo(arq)

while True:   
    resp= bibliotecas.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp==1:
        Arquivos.lerarquivo(arq)
    elif resp==2:
        bibliotecas.titulo('Novo Cadastro')
        n=str(input("Nome: "))
        i=bibliotecas.leinaint("Idade: ")
        Arquivos.cadastro(arq, n, i)
    elif resp==3:
        sleep(0.2)
        bibliotecas.titulo("O programa está sendo finalizado...")
        sleep(0.5)
        
        break
 
    sleep(2)