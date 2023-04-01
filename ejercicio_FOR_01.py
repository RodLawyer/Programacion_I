'''
Dada una lista de números, imprimir el número más grande de la lista.
'''

import random

for _ in range(10):
    lista_numeros = random.randint(1, 100) # Genera lista de 10 numeros aleatorios
    print(lista_numeros)

#lista_numeros_int = int(lista_numeros)

flag_primero = True

for i in lista_numeros:
    if flag_primero == True or i > mayor:
        mayor = i
        flag_primero = False

print("El mayor es {0}".format(mayor))
