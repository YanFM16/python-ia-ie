# Solicitando o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))

# Criamdo  condição caso for >= a 18anos
if idade >= 18:
    print("Maior de idade")

else:
    print("Menor de idade")