'''
Escribir un programa que le pida al usuario que ingrese dos números enteros,
 y luego imprima "El primer número es positivo" si el primer número es mayor que cero,
   "El segundo número es positivo" si el segundo número es mayor que cero,
     o "Ambos números son negativos" si los dos números son negativos.
'''

primer_numero_txt = input("Ingrese primer número: ")

primer_numero_int = int(primer_numero_txt)

segundo_numero_txt = input("Ingrese segundo número")

segundo_numero_int = int(segundo_numero_txt)

if primer_numero_int > 0:
    print("El primer número es positivo")
if segundo_numero_int > 0:
    print("El segundo número es positivo")
if primer_numero_int < 0 and segundo_numero_int < 0:
    print("Ambos números son negativos")