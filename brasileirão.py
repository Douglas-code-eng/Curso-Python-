tabela=("Palmeiras", "Internacional","FLuminense","Corintinhas", "Flamengo", "Átletico-PR", "Átletico-MG", "Fortaleza","São Paulo", "América-MG","Botafogo", "Santos", "Goiás", "Bragantino", "Curitiba", "Cuiabá", "Ceará", "Atletico-GO","Avai", "Juventude")

print("Cinco primeiros colocados: ",tabela[:5])
print("Quatro últimos colocados: ", tabela[16:])
print("Ordem alfabética: ", sorted(tabela))
print("O flamengo está na ",tabela.index("Flamengo") + 1," posição")
