# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E MOSTRE NA TELA A SUA TABUADA

num = int(input("DIGITE UM NÚMERO: "))

for i in range(1, 11):
  print(f"{num} x {i} = {num * i}")
