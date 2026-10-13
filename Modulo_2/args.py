def calcular_presupuesto(descuento_pct: float, *precios) -> float:
    sub_totalsum = sum(precios)
    descuento = sub_totalsum * descuento_pct
    total = sub_totalsum - descuento
    return total

# Prueba 1: 3 productos con 10% de descuento (subtotal $100  -con 10% desc = $90.0) 
print(calcular_presupuesto(0.10, 50.0, 30.0, 20.0)) 
# Prueba 2: Sin productos (debe retornar 0.0) 
print(calcular_presupuesto(0.15))


def crear_configuracion_servidor(entorno: str, **opciones) -> dict:
        return f" Se ha creado en el entorno: {entorno}, Para las siguientes opciones: {opciones['entorno']} - {opciones['valor']} :  "



# Prueba 1: Con puerto y base de datos config_prod = crear_configuracion_servidor( "produccion", puerto=8080, db="postgresql", debug=False ) 
#print(config_prod) # Debe retornar: {'entorno': 'produccion', 'puerto': 8080, 'db': 'postgresql', 'debug': False} 
# Prueba 2: Solo con el entorno obligatorio config\_dev = crear\_configuracion\_servidor("desarrollo") 
#print(config_dev) # Debe retornar: {'entorno': 'desarrollo'}

def mostrar_datos(**kwargs): # Dentro de la función, 'kwargs' es un diccionario: {'nombre': 'Ana', 'edad': 25}
    for clave, valor in kwargs.items(): 
         print(f"{clave}: {valor}") 

# Llamada a la función pasándole clave=valor: 
mostrar_datos(nombre="Ana", edad=25)