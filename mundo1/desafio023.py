# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS

number = int(input("DIGITE UM NÚMERO ENTRE 0 E 9999: "))

if number > 9999 or number < 0:
  print("NÚMERO INVÁLIDO!")
  
elif number > 999:
  text = str(number)
  print(f"ANALISANDO O NÚMERO {number}...")
  print(f"UNIDADE: {text[3]}")
  print(f"DEZENA: {text[2]}")
  print(f"CENTENA: {text[1]}")
  print(f"UNIDADE DE MILHAR: {text[0]}")
  
elif number > 99:
  text = str(number)
  print(f"ANALISANDO O NÚMERO {number}...")
  print(f"UNIDADE: {text[2]}")
  print(f"DEZENA: {text[1]}")
  print(f"CENTENA: {text[0]}")
  
elif number > 9:
  text = str(number)
  print(f"ANALISANDO O NÚMERO {number}...")
  print(f"UNIDADE: {text[1]}")
  print(f"DEZENA: {text[0]}")
  
else:
  text = str(number)
  print(f"ANALISANDO O NÚMERO {number}...")
  print(f"UNIDADE: {text[0]}")
  
