print("Estos son los números del 1 al 100")
for numeros_rang in range(1, 101):  ##aca bbuscamog rango de 1 a 101 
    if numeros_rang % 3 == 0 and numeros_rang % 5 == 0:  ## ojito al operador %3 == 0 , es para multiplos , condicion mas dura primero
        print("fizzbuzz")
    elif numeros_rang % 5 == 0:
        print("buzz")
    elif numeros_rang % 3 == 0:
        print("fizz")
    else:
        print(numeros_rang)  ##recien aca el print de todo, para q no aparezcan los numeros

