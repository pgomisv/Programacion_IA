# abs() : Devuelve el valor absoluto de un número. 
print(abs(34))
print(abs(-100))


# all(): Comprueba si todos los items de uan lista son verdaderos, si alguno es falso, devuelve falso
print(all([True, True, True]))  # devuelve TRUE
print(all([False, True, True]))  # devuelve FALSE


''' 
dir(): Esta función devolverá la lista de funciones de una biblioteca importada, o dicho de otro modo, 
es la forma de leer qué métodos contienen un proyecto importado, por ejemplo.

Viene bien para consultar la lista de métodos/funciones de forma rápida 
por si no te acuerdas del nombre en concreto de una y no quieres acudir a la web para consultarla.
'''
 # print(dir())


'''
help():Invoca la ayuda de la biblioteca estándar. 
Este función se puede usar con o sin argumentos, es decir, 
si incluyes una función en concreta como argumento, de devolverá la ayuda de ésta.
''' 
 # help()


# hex(): Convierte un número entero a su valor exadecimal (y en minúsculas).
 # print(hex(255))


# len(): Devuelve la longitud del número de items de un objeto. 
# El argumento debe ser una secuencia, tales como una cadena de texto, bytes, tupla, etc.
print(len('Aprendiendo Phyton'))


#print(): Imprime por salida estándar (consola Python, intérprete Python, etc.) información del programa.
print('Hola Mundo')


# range(): Devuelve una secuencia de números indicando el inicio o final.
for n in range(1, 10): print(n)





