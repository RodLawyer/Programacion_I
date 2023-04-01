'''
scribir un programa que le pida al usuario que ingrese dos números enteros,
 y luego imprima "Los dos números son iguales" si los dos números son iguales,
   "El primer número es mayor" si el primer número es mayor que el segundo,
     o "El segundo número es mayor" si el segundo número es mayor que el primero.
'''

primer_numero_txt = input("Ingrese primer número: ")

primer_numero_int = int(primer_numero_txt)

segundo_numero_txt = input("Ingrese segundo número: ")

segundo_numero_int = int(segundo_numero_txt)

if primer_numero_int > segundo_numero_int:
    print("El primer número es el mayor")
elif segundo_numero_int > primer_numero_int:
    print("El segundo número es el mayor")
else:
    print("Los dos números son iguales")