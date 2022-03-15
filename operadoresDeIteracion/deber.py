num1 = int(input("Ingresa un numero:  "))
num2 = int(input("Ingresa otro  numero:  "))

i = num1
while i <=num2:

    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
        print(i)
        break

    i +=1

if i == num2 + 1:
    print("Dentro del intervalo no hay numeros que cumplan la condicion dada")