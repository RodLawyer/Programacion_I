'''
Escribir un programa que le pida al usuario que ingrese su nombre,
y luego imprima "Hola [nombre]" si el nombre ingresado es "Juan",
"María" o "Pedro", o "Hola desconocido" si el nombre ingresado no es uno de esos tres.
'''

nombre_ingresado_txt = input("Ingrese su nombre: ")

if(nombre_ingresado_txt == "Juan" or nombre_ingresado_txt == "María" or nombre_ingresado_txt == "Pedro"):
    print("Hola {0}".format(nombre_ingresado_txt))
else:
    print("Hola desconocido")