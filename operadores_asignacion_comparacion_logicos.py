"""
= asignación
+= sumar y asignar
-= restar y asignar
/= dividir y asignar
**= elevar y asignar
"""
numero_1 = 10
numero_1 += 5
print(numero_1)

numero_1 -= 5
print(numero_1)


"""
Operadores de Comparación
== igualdad  (devuelve True o False)
> mayor
>= mayor o igual
< menor
<= menor o igual
!= distinto
"""
expresion = 3==3
print(expresion)

expresion_1 = 7==2
print(expresion_1)

expresion_2 = "Carlos" == "Carlos"
print(expresion_2)

expresion_3 = 7>=5
print(expresion_3)

expresion_4 = 5 != 7
print(expresion_4)


"""
Operadores Lógicos:
and
or
not
(Devuelven True o False)
"""
resultado = 3==3 and 5==5
print(resultado)

resultado_2 = 3==0 and 5==5
print(resultado_2)

resultado_3 = 1>3 or 2>5
print(resultado_3)
