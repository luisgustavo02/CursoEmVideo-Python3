# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# - O NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS
# - QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS)
# - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = str(input("DIGITE O SEU NOME: "))

print(f"NOME EM MAIÚSCULAS: {nome.upper()}")
print(f"NOME EM MINÚSCULAS: {nome.lower()}")

print(f"A QUANTIDADE TOTAL DE LETRAS É: {len(nome) - nome.count(" ")}")

nomeSeparado = nome.split(" ")

print(f"O NOME {nomeSeparado[0]} POSSUI {len(nomeSeparado[0])} LETRAS")
