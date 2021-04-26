print("Introduce una palabra y yo te la devuelvo en mayúsculas")
word = input()
print(word.upper())

print("Introduce una frase y yo te devuelvo todas las palabras empezando en mayúscula")
s = input()
print(s.title())


print("Introduce una palabra con 3 letras o más y yo te devuelvo todas sus letras en minúscula salvo la tercera")
word = input()
word = word[:2].lower() + word[2].upper() + word[3:].lower()
print(word)


print("Introduce una palabra y yo te devuelvo todas sus letras en mayúscula salvo la primera y la última")
word = input()
word = word[0].lower() + word[1:(len(word) - 1)].upper() + word[-1].lower()
print(word)


subs = "su"
print("Introduce una frase y yo te la devuelvo sustituyendo las dos primeras letras de la primera palabra por las letras {}".format(subs))
s = input()
print(s.replace(s[:2], subs))




#deber en casa

title = "se busca tripulante"

message = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero. comida y bebida garantizada a lo largo de toda la aventura."

contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."

message1="se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero."

message2="comida y bebida garantizada a lo largo de toda la aventura."

contact.replace("pyratilla","PYRATILLA")

print(title.upper()+"\n"+message1.replace("pyratilla","PYRATILLA").capitalize()+message2.capitalize()+"\n"+contact.replace("pyratilla","PYRATILLA").capitalize())

