nombre= "Carlos"
print(nombre)

nombre_completo= "Carlos García"
print(nombre_completo)

numero_1= 7
print(numero_1)

print(nombre_completo, numero_1)

nombre2, apellido, edad= "Pilar", "Gomis", 44
print(nombre2, apellido, edad)

# tipos de variable: string, int, float, boolean
# para saber el tipo de variable que son: 
print(type(nombre))
print(type(edad))

#concatenar:
print(nombre2 + " " + apellido)

# LISTAS:
[0, 1, 2, 3, 4, 5] # Lista que contiene elementos del mismo tipo (integers)
['Sun', 'Venus', 'Mars', 'Jupiter'] # Lista que contiene elementos del mismo tipo (strings)
['Football', 'Rugby', 'Squash', 1, 3, False] # Lista que contiene elementos de diferentes tipos


# COMPROBAR EL TIPO DE DATO
type(3) # Tipo Integer
type(3.222) # Tipo Float
type(True) # Tipo Boolean
type("Good morning, Mr. Marshall") # Tipo String
type(2 + 3j) # Tipo Complex
type([1, 3, 4]) # Tipo List
type({'name' : 'Ironman'}) # Tipo Dict
type((2, 3, 4)) # Tipo Tuple
type({93.3, 33.23, 36.3}) # Tipo Set

texto = 'Hola Python'
print(len(texto))

#TABULACIONES
print('Table of Results\n')
print('Id\tType\tPoints')
print('1\tA\t10')
print('2\tB\t15')
print('3\tC\t7')

# f-String
name = 'Cristóbal Colón'
discover = 'The New World: The Americas'
print(f'{name} discovered {discover}, long time ago')