'''
Escribir un programa que le pida al usuario que ingrese su edad,
 y luego imprima "Eres un niño" si la edad es menor a 12,
   "Eres un adolescente" si la edad está entre 12 y 17 inclusive,
     "Eres un adulto" si la edad está entre 18 y 64
'''

edad_txt = input("Ingrese edad: ")

edad_int = int(edad_txt)

if edad_int > 0 and edad_int < 12:
    print("Eres un niño")
elif edad_int >= 12 and edad_int <= 17:
    print("Eres un adolescente")
else:
    print("Eres un adulto")