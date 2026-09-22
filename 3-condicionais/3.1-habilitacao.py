# Solicitando o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))

# Criamdo  condição caso for >= a 18anos
if idade >= 18:
    possui_carteira = input("Possui carteira de motorista s/n: ")
    if possui_carteira == "s":
        print("Pode dirigir")
    else:
        print("Não pode dirigir")

else:
    print("Menor de idade")