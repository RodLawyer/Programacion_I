'''
Escribir un programa que le pida al usuario que ingrese su edad, 
y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18,
o "Eres menor de edad" si la edad es menor a 18.
'''

edad_txt = input("Por favor ingrese su edad: ")

edad_int = int(edad_txt)

if(edad_int < 18):
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
