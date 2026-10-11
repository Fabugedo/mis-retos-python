import time

lista_ids = [101, 202, 303, 404, 505, 606, 707]
lista_desordenada = [505, 101, 707, 202, 404, 303, 606]


def buscar_id_usuario(ids: list, id_buscado: int) ->int:
    inicio = 0
    final =  len(ids) -1
    while inicio <= final:
        medio = (inicio + final)//2
        if ids[medio] == id_buscado:
            return medio
        elif id_buscado >= ids[medio]:
            inicio = medio + 1
        else:
            final = medio - 1
    return -1

print(buscar_id_usuario(lista_ids, 505)) # Debe retornar: True 
print(buscar_id_usuario(lista_ids, 999)) # Debe retornar: False

"""
#### 1. Regla Fundamental

* **La lista debe estar ordenada.** Sin orden, la Búsqueda Binaria no funciona porque no se puede saber qué mitad descartar.

#### 2 Las 3 Variables de Posición (Índices / Casillas)

* **inicio = 0**: El índice de la primera casilla.
* **final = len(lista) - 1**: El índice de la última casilla.
* **medio = (inicio + final) // 2**: El índice de la casilla del centro en cada iteración.

#### 3 Las 3 Decisiones dentro del `while inicio <= final:`

* **¿Es igual?** (`lista[medio] == objetivo`): ¡Encontrado! Retornamos **medio** (el índice de la casilla).
* **¿El objetivo es MAYOR?** (`objetivo > lista[medio]`): Descartamos la mitad izquierda moviendo la pared inicial hacia adelante: **inicio = medio + 1**.
* **¿El objetivo es MENOR?** (`objetivo < lista[medio]`): Descartamos la mitad derecha moviendo la pared final hacia atrás: **final = medio - 1**.
* **Si el bucle termina sin coincidencias**: Significa que el rango se cerró (`inicio > final`) y el elemento no existe, por lo que retornamos -1**.
"""

lista_gigante = list(range(1, 1000001))
numero_buscado = 999999 # Esta casi al final de la lista

##----------Prueba 1 
tiempo_inicio = time.perf_counter()
posicion_lineal = lista_gigante.index(numero_buscado) #recorrre 1 por 1 
tiempo_fin = time.perf_counter()
print(f"Busqueda lineal: Posición {posicion_lineal} | Tiempo: {tiempo_fin - tiempo_inicio:.6f}: segundos")

#--------------Prueba 2

tiempo_inicio = time.perf_counter()
posicion_binaria = buscar_id_usuario(lista_gigante, numero_buscado)
tiempo_fin = time.perf_counter()
print(f"Busqueda binaria: Posición {posicion_binaria} | Tiempo: {tiempo_fin - tiempo_inicio:.6f}: segundos")

print(buscar_id_usuario(lista_desordenada, 202))
print(buscar_id_usuario(lista_desordenada, 505))

#ticket 15.4 Busqueda binaria en el mundo real (lista de diccionarios)

def buscar_usuario_por_id(usuarios: list, id_buscado: int) ->dict | None:
    inicio = 0
    final =  len(usuarios) -1
    while inicio <= final:
        medio = (inicio + final)//2
        if usuarios[medio]["id"] == id_buscado:
            return usuarios[medio]
        elif id_buscado >= usuarios[medio]["id"] :
            inicio = medio + 1
        else:
            final = medio - 1
    return None

usuarios_db = [ {"id": 101, "nombre": "Ana", "rol": "Admin"}, 
               {"id": 202, "nombre": "Carlos", "rol": "Dev"}, 
               {"id": 303, "nombre": "Elena", "rol": "Design"}, 
               {"id": 404, "nombre": "Fernando", "rol": "DevOps"}, 
               {"id": 505, "nombre": "Gabriela", "rol": "QA"}, ] 
print(buscar_usuario_por_id(usuarios_db, 404)) # Debe retornar el dict de Fernando 
print(buscar_usuario_por_id(usuarios_db, 999)) # Debe retornar None

#ticket 15.5 
inventario_db = [ {"sku": 1001, "nombre": "Teclado Mecánico", "stock": 15}, 
                 {"sku": 1005, "nombre": "Mouse Inalámbrico", "stock": 0}, # Existe, pero agotado 
                 {"sku": 1010, "nombre": "Monitor 4K", "stock": 8}, 
                 {"sku": 1020, "nombre": "Audífonos Bluetooth", "stock": 0}, # Existe, pero agotado 
                 {"sku": 1050, "nombre": "Silla Gamer", "stock": 3}, ] 
# --- Casos de Prueba --- 


def verificar_stock_producto(inventario: list, sku_buscado: int) -> bool:
    inicio = 0
    final =  len(inventario) -1
    while inicio <= final:
        medio = (inicio + final)//2
        if inventario[medio]["sku"] == sku_buscado:
            if inventario[medio]["stock"] > 0:
                return True
            return False 
        elif sku_buscado >= inventario[medio]["sku"] :
            inicio = medio + 1
        else:
            final = medio - 1
    return False

print(verificar_stock_producto(inventario_db, 1001)) # Debe retornar: True (Existe y hay stock) 
print(verificar_stock_producto(inventario_db, 1005)) # Debe retornar: False (Existe pero stock es 0) 
print(verificar_stock_producto(inventario_db, 9999)) # Debe retornar: False (No existe en el sistema)

