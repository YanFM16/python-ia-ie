# Solicitando os dados do usuário
nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))

# Classificando a idade do paciente
if idade == 0:
    situacao = "Recém nascido"
elif idade <= 3:
    situacao = "Bebê"
elif idade <= 10:
    situacao = "Criança"
elif idade <=15:
    situacao = "Adolescente"
elif idade <= 30:
    situacao = "Jovem"
elif idade <= 60:
    situacao = "Adulto"
else:
    situacao = "Idoso"

print(f"A classificação do paciente {nome} é {situacao}")