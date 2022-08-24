# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA
# QUE AJUDE ELE, LENDO O NOME DOS ALUNOS E ESCREVENDO NA TELA O NOME DO ESCOLHIDO.

from random import randint

num = int(input("DIGITE A QUANTIDADE DE ALUNOS: "))

nomes = []
for i in range(0, num):
  name = str(input(f"DIGITE O NOME DO {i+1}° ALUNO: "))
  nomes.append(name)

print(f"O ALUNO SORTEADO FOI: {nomes[randint(0, num)]}")
