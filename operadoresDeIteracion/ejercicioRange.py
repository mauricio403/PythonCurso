a0 = int(input("Ingrese el termino inicial: "))
diferencia = int(input("Ingrese la diferencia: "))
fin = int(input("Ingrese el numero a finalizar: "))

sum = 0

for i in range(a0, fin + 1, diferencia):
    sum += i
    print(i)
print("La suma es {}".format(sum))



num = int(input("Ingrese la tabla que quiere ver:  "))

for i in range(1, 10+1):
    multi = num * i
    
    print("{} x {} = {}".format(num, i, multi))