palabra = 'Quien lo diria que se podria hacer el amor por telepatia'

letra = input("Introduce la letra que deseas eliminar:  ")

letra = letra.lower()

palabra = palabra.lower()

for c in palabra:
    if c == letra:
        continue
    else:
        print(c,end = "")