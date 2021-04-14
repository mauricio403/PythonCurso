#en python se usa la letra j para la unidad imaginaria



z = 2 +5j
print(type(z)) #nos da resultado de tipo complejo

#la funcion complex

z = complex(1, -7)

print(z)

z.real #obtiene la parte real

z.imag #obtiene la  parte imaginaria

#para sumar 2 numeros complejos

z1 = 2-6j
z2 = 5+4j

z1 + z2

#para restar 2 complejos
z1 - z2


#multiplicacion de numeros complejos

z1 * z2

#dividir 2 numeros complejos

z1 /z2


#condjugado de un numero complejo

x = -2 + 1j

x.conjugate() #nos devujelve el conjugado


#El modulo de un numero complejo

y = -2j

abs(y) #obtiene su modulo


#argumento de un numero complejo

#usamos la libreiria cmath

#import cmath

#cmath.phase(z)


#forma polar de un complejo

#import cmath

#cmath.polar(y)