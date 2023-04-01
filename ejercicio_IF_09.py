'''
Escribir un programa que le pida al usuario que ingrese una letra,
 y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u),
   o "Es una consonante" si la letra es una consonante.
'''

letra_txt = input("Ingrese una letra: ")

if(letra_txt == "a" or letra_txt == "e" or letra_txt == "i" or letra_txt == "o" or letra_txt == "u"):
    print("Es una vocal")
else:
    print("Es una consonante")
