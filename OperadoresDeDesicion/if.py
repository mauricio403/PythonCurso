#resolviendo ecuaciones de primer grado

A = float(input("Coeficiente A = "))
B = float(input("Coeficiente B = "))

if A != 0:
  sol = -B / A
  print("La solución es x =", sol)
else:
  print("No hay ecuación que resolver, porque A = 0")