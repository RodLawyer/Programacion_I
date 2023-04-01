
variable = input("Ingrese txt en variable")

variable_int = int(variable)

variable_float = float(variable)

#####

print("Hola Mundo")

print("Hola {0}, {1} y {2}".format("Juan", "Carlos", "Ana"))

#####

if variable_int < 0:
    print("Es negativo")
elif variable_int > 5 and variable_int < 10:
    print("Es mayor a 5 y menor a 10")
elif variable_int == 15 or variable_int == 20:
    print("Es igual a 15 o 20")
else:
    print("Otro")



lista = [1,2,3,4,5]

for i in lista: # Muestra el contenido de 'lista' uno por uno del 1 al 5
    print(i)

# break -> Detiene completamente la iteración del for

# continue -> Salta a la siguiente iteración del for

# range(start, stop, step)

for i in range(1, 10, 1): # Muestra lista de numeros del 1 al 9
    print(i)

#####

flag = True

if flag:
    print("Flag es True")
else:
    print("Flag es False")

######

import math # Permite usar comandos como math.sqrt()

math.sqrt(variable_int) # Da la raíz cuadrada de un número

variable_int.is_integer() # Da TRUE si es entero