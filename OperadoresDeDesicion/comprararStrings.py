print('Quito' > 'Zuleta') #nos devuelve false en funcion de la primera letra de la palbara


#metodos con strings

s = "la  loma grande y la guaragua"

print(s.startswith('m')) #le pregunto si la cadena empiza con el string indicado como parametro

print(s.endswith('a'))  #le pregunto si termina con el string indicado como parametro


d = "Python365"

print(d.isalnum()) #devuelve true si todos son alfanumericos

#no se consideran alfanumericos strings con espacios y cualquiera que no este en a-z , 0-9


e = "Abremelapuertaverbenita"
print(e.isalpha()) #devuelve si todos pertenecen al alfabeto


f = '13484'

print(f.isdigit()) #verifica si es un numero
