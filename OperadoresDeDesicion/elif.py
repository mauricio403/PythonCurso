# age = 20

# if age > 40:
#   print("No puedes pertenecer a la tripulación, te pasas de la edad límite que ha puesto el gran capitán Pyratilla.")
# elif age >= 16:
#   print("Podrás optar a pertenecer la tripulación. Aún te queda superar la entrevista con el capitán.")
# else:
#   print("Eres muy pequeño todavía para la vida pirata!")
  
  
#operador ternario

# edad = int(input("Ingresa tu edad: "))

# text1 = "Eres mayor de edad en Latam"

# text2 = "Eres menor de edad en latam"

# print(text1) if edad>=18 else print(text2)


#Comprobar si el numero es par o impar

# numero = int(input("Ingresa un numero: "))

# print("El numero: {} es un numero par".format(numero)) if numero % 2 ==0 else print("El numero es impar..xd")


age = 20
name = "Martin"

if age >= 18:
  if name.startswith("M") or name.startswith("m"):
    print("Eres mayor de edad pues tienes {} años y tu nombre, que es {}, empieza por M".format(age, name))
  else:
    print("Eres mayor de edad pues tienes {} años".format(age))
else:
  print("Eres muy joven")