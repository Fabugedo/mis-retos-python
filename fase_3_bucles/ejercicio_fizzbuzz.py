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

############################################################ 
################### EJERCICIO 2##########################


gestion_cliente = []


while True:
print("Bienvenido a Indisa")
print("Por favor ingrese una opción operativa: ")
print("1) Registrar usuario nuevo. ")
print("2) Revisar el orden de atención.")
print("3) Remover paciente atendido exitosamente ya.")
print("4) Buscar paciente por su nombre")
opcion_sv = int(input("Ingrese la opción al sistema: "))
if opcion_sv == 1:
nombre_cli = input("Ingrese el nombre de pila a registrar: ").lower()
apellido_cli = input("Ingrese el primer apellido a registrar: ").lower()
gestion_cliente.append((nombre_cli, apellido_cli))
print("Nombre registrado con exito")
elif opcion_sv == 2:
print(f"Esta es la lista de clientes: {gestion_cliente}" )
elif opcion_sv == 3:
if len(gestion_cliente) > 0 :
paciente_atentido = gestion_cliente.pop(0)
print(f"el siguiente paciente fue atendido con exito: {paciente_atentido}")
else:
print("No tenemos ningún paciente en lista de espera.")

elif opcion_sv == 4:
if len(gestion_cliente) == 0:
print("No hay pacientes en sistema")
else:
nombre_busca = input("Ingrese el nombre de pila: ").lower()
apellido_busca = input("Ingrese el apellido: ").lower()
for mirar in gestion_cliente:
if (nombre_busca, apellido_busca) == mirar:
posicion = gestion_cliente.index(mirar) + 1
print(f"Paciente encontrado en el turno {posicion}.")
else:
print("Seleccione una opción valida")


termine el primero, creo q me falto el sort si . Me demore como 4-5 horas y tuve uqe pedir ayuda en google, aun me cuesta, mañana sigo con los otros