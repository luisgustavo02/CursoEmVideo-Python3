# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO, COSSENO E TANGENTE DESSE ÂNGULO.

from math import *

ang = float(input("DIGITE UM ANGULO: "))

print(f"O SENO DE {ang}° É: {sin(radians(ang))}")
print(f"O COSSENO DE {ang}° É: {cos(radians(ang))}")
print(f"A TANGENTE DE {ang}° É: {tan(radians(ang))}")
