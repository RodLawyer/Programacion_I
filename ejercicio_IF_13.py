'''
Escribir un programa que le pida al usuario que ingrese un número entero,
 y luego imprima "El número es divisible por 3 y por 5" si el número
   es divisible por 3 y por 5, o "El número no es divisible por 3 y por 5"
     si el número no es divisible por 3 y por 5.
'''

numero_txt = input("Ingrese número entero: ")

numero_int = int(numero_txt)

if numero_int % 3 == 0 and numero_int % 5 == 0:
    print("El número es divisible por 3 y por 5 simultáneamente")
else:
    print("El número NO es divisible por 3 y por 5 simultáneamente")