# Solicitando os dados do paciente
nome = input("Digite o nome do paciente: ")
peso = float(input("Digite o peso do paciente kg: "))
altura = float(input("Digite a altura do paciente m: "))

# Calculando o IMC do paciente
imc = peso / altura ** 2

# Definindo o quadro do paciente segundo o IMC
if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc <= 24.9:
    situacao = "Peso normal"
elif imc <= 29.9:
    situacao = "Sobrepeso"
elif imc <= 34.9:
    situacao = "Obesidade grau 1"
elif imc <= 39.9:
    situacao = "Obesidade grau 2"
else:
    situacao = "Obesidade grau 3"

print(f"O IMC do paciente {nome} é {imc:.1f}, e ele está em {situacao}")