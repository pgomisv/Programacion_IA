# Ejercicio 2
maximo_permitido = 20
if maximo_permitido >= 20:
    print("El valor es igual o mayor a 20")
else: 
    print("El valor es menor a 20")


# Ejercicio 3
temperatura = 21
if temperatura >0 and temperatura <=10:
    print('Hace mucho frío')
elif temperatura > 11 and temperatura <= 20:
    print('Hace algo de frío')    
elif temperatura > 20 and temperatura <= 30:
    print('Hay temperatura cálida')
elif temperatura > 30 and temperatura <= 40:
    print('Hace calor')
else:
    print('Vamos a morir!!!')
            
# Ejercicio 4
edad = input("¿Cuántos años tienes?")
if edad.isdigit():
    if int (edad) >= 18:
        print("Puedes sacarte el carnet de conducir")
    else: 
        print(f'Aún te faltan{18-int(edad)}años.')
else: 'No has intriducido el número'


# Ejercicio 5
colores = ['blanco', 'rojo', 'azul']
if 'azul' not in colores:
    colores.append('azul')
    print('Color azul añadido')
else:
    print('El color azul ya está en la lista')
    
            
