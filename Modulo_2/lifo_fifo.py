from collections import deque

pila = [] 
# 1\ Agregar arriba (Push) 
pila.append("https://google.com") 
pila.append("https://github.com") 
# 2\. Consultar el elemento de arriba sin borrarlo (Peek) 
pagina_actual = pila[-1] # "https://github.com" 
# 3\. Quitar el de arriba (Pop) 
ultima_pagina = pila.pop() # Elimina y retorna "https://github.com"


historial_navegacion = [] 

def visitar_pagina(historial: list, url: str) -> None:
    historial.append(url)
    
def boton_atras(historial: list) -> str:
    if historial:
        return historial.pop()
    return "No hay páginas en el historial"


# Simulación de navegación: 
visitar_pagina(historial_navegacion, "google.com") 
visitar_pagina(historial_navegacion, "mouredev.com") 
visitar_pagina(historial_navegacion, "github.com") 
print("**1**")  
print(historial_navegacion) # Debería mostrar las 3 URLs
# Simulación de presionar "Atrás": 
print("**2**") 
print(boton_atras(historial_navegacion)) # Debe retornar: "github.com" 
print("**3**") 
print(boton_atras(historial_navegacion)) # Debe retornar: "mouredev.com" 
print("**4**") 
print(historial_navegacion) # Ahora solo debería quedar ['google.com']


cola_atencion = deque() 
# 1. Agregar al final de la cola 
cola_atencion.append("Cliente 1") 
cola_atencion.append("Cliente 2") 
# 2. Atender/sacar al PRIMERO de la fila (O(1)) 
siguiente = cola_atencion.popleft() # Retorna "Cliente 1"

def atender_siguiente_cliente(cola: deque) -> str:
    if cola:
        atencion = cola.popleft()
        return atencion
    return "No hay clientes en espera"

cola_banco = deque(["Ana (Ticket 101)", "Carlos (Ticket 102)", "Elena (Ticket 103)"]) 
print(atender_siguiente_cliente(cola_banco)) # Debe retornar: "Ana (Ticket 101)" 
print( atender_siguiente_cliente(cola_banco) ) # Debe retornar: "Carlos (Ticket 102)" 
print(cola_banco) # Debe quedar únicamente deque(['Elena (Ticket 103)'])