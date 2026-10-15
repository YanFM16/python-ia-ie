# Criando dicionáario composto de cadastro de funcionário
funcionarios = {
    "44356":{
        "nome":"Vitor Davi",
        "telefone":"11912121315",
        "data_nascimento":"26/03/2010",
        "cargo":"Jovem Aprendiz",
        "habilidades":["front-end","java","python"]
     },
    "42568":{
        "nome":"Adriano",
        "telefone":"11940404040",
        "data_nascimento":"24/03/2010",
        "cargo":"Jovem Aprendiz",
        "habilidades":["front-end","java","python"]
    },
    "41703":{
        "nome":"Mimi Cristine",
        "telefone":"11970707070",
        "data_nascimento":"15/09/2010",
        "cargo":"Jovem Aprendiz",
        "habilidades":["front-end","java","python"]
    }
}

print(funcionarios["42568"]["telefone"])