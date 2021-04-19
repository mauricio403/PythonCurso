#metodo lower

s = "ME ENCANRAN EL CHOCOLATE Y EL SHITPOST"

print(s.lower()) # a minusculas

s1 = "vamonos a la vrga"

print(s.upper()) # a mayusculas


#metodo count, indica cuantas veces esta escrito un caracter

print(s.count("E"))

#metodo capitalize , convierte la primera letra a mayuscula

s3 = "amor mio...xd"

print(s3.capitalize())


#metodo tittle, convierte cada primera letra de cada palabra a mayuscula

s4 = "que ella escuche por la radio mis besos al aire"
print(s4.title())

#metodo swapcase, convierte a minuscula las mayusculas y al revez

s5 = "hoy me pregunto QUE SERA DE TI"

print(s5.swapcase())

#metodo replace, reemplaza una palbra por otra que le indiquemos

s6 = "Labios compartidos"

print(s6.replace("compartidos","divididos"))


s = "El elefante tiene las orejas muy grandes"
print(s.split("e")) # Rompemos por la letra e minúscula

print(s.split(" "))# Rompemos por los espacios

print(s.split("tiene")) # Rompemos por la palabra tiene

#metodo strip, elimina espacios sobrantes

s = "     xd     "
print(s.strip())

#metodo rstrip() elimina espacios al final y el lstrip() elmina espacios al inicio


#El metodo find usca el caracter que le indiquemos y devuelve la primera posicion que aparece

s9 = "Este es un curso de Python para hacer en casa o en cualquier lado"
print(s9.find("e"))

print(s9.find("casa"))

print(s9.find("e", 10)) # Solamente indicamos start

print(s9.find("e", 30, 40)) # Indicamos start y end

#metodo index()
s = "Este es un curso de Python para hacer en casa o en cualquier lado"
print(s.index("e"))

