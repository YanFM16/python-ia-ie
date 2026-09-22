# Solcitando o peso e altura ao usuário
peso = float(input("Dgite seu peso KG: "))
altura = float(input("Digite sua altura (m): "))

# Realizando o cálculo do IMC
imc = peso / altura**2

# Apresentando o resultado do IMC ao usuário
print("O seu IMC é ", imc)