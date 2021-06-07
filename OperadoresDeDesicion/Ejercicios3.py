#Comprobar si una año es bisiesto

#Un año es bisiesto si es divisible entre 4 pero no es multiplo de 100 a no ser que sea 400

# año = int(input("Ingresa el año: "))

# if año % 4 == 0:
    
#     if año % 100:
        
#         if año % 400:
            
#             print("El año es bisiesto")
            
#         else: print("El año no es bisiesto")
          
#     else: print("El año es bisiesto")
        
# else:
#     print("El año no es bisisesto xd")




#ejericio 1

# num = int(input("Ingresa cualquier numero: "))

# if num > 0:
#     print("El numero {} es un numero positivo".format(num))
# elif num <0:
#     print("El numero {}  es un numero negativo".format(num))
# elif num == 0:
#     print("El numero {} es 0".format(num))
# else:
#     print("Ingresa un numero pues mmvrg")



#ejercicio 2


# nombre = input("Ingresa tu nombre pelotudo: ")
# cantidad = int(len(nombre))
# if cantidad >= 10:
#     print("{} tiene {} de caracteres".format(nombre, cantidad))
# else:
#     print("{} tiene {} de caracteres".format(nombre, cantidad))


#Ejrcicio 3
 
# nombre = input("Ingresa tu nombre pelotudo: ")
# cantidad = int(len(nombre))

# print("{} tiene {} de caracteres".format(nombre, cantidad)) if cantidad >= 10 else  print("{} tiene {} de caracteres".format(nombre, cantidad))



#Ejericio 4 


# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))

# if num1 > num2:
#     print("El primer numero es mayor que el segundo numero")
# else:
#     print("El primer numero es menor")


#Ejercicio 5

# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))
# residuo = num1 % num2
# cociente = num1 // num2

# if num1 > num2:
#     if residuo == 0:
#         print("El Residuo es {} la division es entera".format(residuo))
#     else:
#         print("El cociente es {} y el residuo es {} no es divison entera".format(cociente, residuo)) 
# else:
#     print("El numero 1 no es mayor que el numero 2")        

#El ejercicio 6 ya esta hecho xdd


#Ejercicio 7


# num1 = int(input("Ingresa un numero: "))
# num2 = int(input("Ingresa otro numero: "))


# if num1 % num2:
#     print("El numero es numltiplo del otro")
    
# else: 
#     print("Los numeros no son multiplos")


#Ejericio 8

word = input()
if word.find(" ") == -1:
    if word[0].isupper():
        print("La palabra introducida empieza por mayúscula")
    else:
        print("La palabra introducida empieza por minúscula")
else:
    print("El string que has introducido tiene más de una palabra.")