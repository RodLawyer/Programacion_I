'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
 y luego imprima "El número es primo" si el número es primo,
 o "El número no es primo" si el número no es primo.
'''

import math

numero_txt = input("Ingrese número entero positivo: ")

numero_int = int(numero_txt)

if(numero_int < 2):
    print("El número NO es primo")
else:
    flag_primo = True
    for i in range(2, numero_int):
        if (numero_int % i == 0):
            flag_primo = False
            break

    if flag_primo:
        print("El número es primo")
    else:
        print("El número NO es primo")

