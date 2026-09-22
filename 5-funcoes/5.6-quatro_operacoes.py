# Criando as funções das quatro operções
def somar(a,b):
    return numero_1 + numero_2

def subtrair(a,b):
    return  numero_1 - numero_2

def multiplicar(a,b):
    return numero_1 * numero_2 

def dividir(a,b):
    return numero_1 / numero_2

# Solicitando os dois números ao usuário
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))

# Chamando e apresentando as funções
print(f"Soma: {somar(numero_1,numero_2)}")
print(f"Subtração: {subtrair(numero_1,numero_2)}")
print(f"Multiplicação: {multiplicar(numero_1,numero_2)}")
print(f"Divisão: {dividir(numero_1,numero_2)}")