import random 

def sortear(lista):
    return random.choice(lista)

nomes = ["Dominique", "Matheus", "João", "Giovana", "Pamela", "Alana", "Lorena", "Vitor", "Adriano", "Luis"]

print(sortear(nomes))