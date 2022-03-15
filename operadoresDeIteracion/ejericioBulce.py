texto = "Cuatro años sin mirarte 3 postales y un bolero"

letra= input('Introduce una letra:  ')

texto = texto.lower()

letra = letra.lower()

n = int(input("Introduce el maximo numero de vecs que aparezca la letra anterior:  "))

count = 0

for c in texto:
    if count >=n:
        print("Se supero el numero de pariciones")
        
        break
    if c == letra:
        count += 1
    elif c == "a" or c=="e" or c=="i" or c=="o" or c=="u":
        continue
    print(c, end="")
        