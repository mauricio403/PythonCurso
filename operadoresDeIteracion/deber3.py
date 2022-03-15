num = int(input("Introduce una rotacion :  "))

i = 65

while i <=90:
    if i + num <=90:
       print(chr(i) + ": " +chr(i + num))
    else:
        print(chr(i) + ": " + chr((i - 26) + num))

    i +=1