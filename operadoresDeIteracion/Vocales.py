s = 'yo solo quiero ser tu amigo y me muero por salir contigo'
s = s.lower()

i = 0
count = 0
while i < len(s):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count += 1
    i +=1


print("En total hay ", count, "vocales")


#programa cuenta las volcaes que hay en un string