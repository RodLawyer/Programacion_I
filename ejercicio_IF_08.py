'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo,
 y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto,
   o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.
'''

import math

numero_txt = input("Ingrese número entero positivo: ")

numero_float = float(numero_txt)

if numero_float < 0 or numero_float % 1 != 0: # Si el resto de la div por 1 no es cero el numero no es entero
    print("El número ingresado no es entero o positivo")
else:
    if math.sqrt(numero_float).is_integer(): # TRUE si la raíz de la variable es un entero
        print("El número es un cuadrado perfecto")
    else:
        print("El número NO es un cuadrado perfecto")
            