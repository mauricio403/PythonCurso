#use break

anterior = 1
actual = 1
indice = 3

print("El termino {} ocupa la pisicion {}".format(actual, anterior))
print("El termino {} ocupa la pisicion {}".format(actual, 2))

while actual <= 5000000 :
    temp = actual
    actual = actual + anterior
    anterior = temp

    print("El termino {} ocuapa la posicion {}".format(actual, indice))

    if indice == 20 :
        break

    indice += 1