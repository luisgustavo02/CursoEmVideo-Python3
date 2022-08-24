# O MESMO PROFESSOR DO DESAFIO 019 QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS.
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.

from random import shuffle

num = int(input("DIGITE A QUANTIDADE DE ALUNOS: "))

nomes = []
for i in range(0, num):
  name = str(input(f"DIGITE O NOME DO {i+1}º ALUNO: "))
  nomes.append(name)

shuffle(nomes)
print(f"A ORDEM SORTEADA FOI: {nomes}")
