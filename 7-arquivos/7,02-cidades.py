import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["Jardim Belval","Barueri","SP","06420916"],
    ["Parque Santana I","Santana de Parnaíba","SP","06845120"],
    ["Suburbano","Itapevi","SP","04388567"],
    ["Centro","Jandira","SP","01244836"]
]

with open("7.02-cidades.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerow(dados_tabela)