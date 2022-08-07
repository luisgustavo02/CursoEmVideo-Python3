# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELA

thing = input("Digite algo: ")

print(f"O tipo primitivo da variável é {type(thing)}")
print(f"A variável possui tamanho: {len(thing)}")
print(f"A variável é alfabética: {thing.isalpha()}")
print(f"A variável é numérica: {thing.isnumeric()}")
print(f"A variável é alfanumérica: {thing.isalnum()}")
print(f"A variável possui somente espaços: {thing.isspace()}")
print(f"A variável possui somente letras maiúsculas: {thing.isupper()}")
print(f"A variável possui somente letras minúsculas: {thing.islower()}")
print(f"A variável possui é capitalizada: {thing.istitle()}")
