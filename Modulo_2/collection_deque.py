from collections import deque
#1 PRIMERO DE LA FILA
fila_banco = deque(["Carlos","Ana","Diego"])
cliente_atendido = fila_banco.popleft()
fila_banco.append("Alberto")
print(cliente_atendido)
print(fila_banco)
#2 funcion
def procesar_siguiente_cliente(cola_espera: deque) -> str:
    try:
        #1. Si no hay clientes en la cola ( está vacia)
        if not cola_espera:
            return "No hay clientes en cola"
        cliente = cola_espera.popleft()
        return f"atendiendo a {cliente}"
    except (AttributeError, TypeError):
        return "Error: La estructura recibida no es una cola valida"
#Prueba
# Creamos la cola 
fila_banco = deque(["Carlos", "Ana", "Diego"]) 
# Primera llamada: Debe atender a  Carlos 
print(procesar_siguiente_cliente(fila_banco)) 
# Salida esperada: "Atendiendo a: CARLOS" 
# # Segunda llamada: Debe atender a Ana 
print(procesar_siguiente_cliente(fila_banco)) # Salida esperada: "Atendiendo a: ANA"

#3 funcion stack lifo

def deshacer_ultima_accion(historial: deque)-> str:
    try:
        if not historial:
            return "No hay acciones para deshacer"
        deshacer = historial.pop()
        return f"Acción: '{deshacer}' realizada con exito."
    except (AttributeError, TypeError):
        return "Error: La estructura recibida no es valida."

# 1\. Creamos la pila con el historial de acciones (en orden cronológico) 
acciones = deque(["Escribir titulo", "Insertar imagen", "Borrar texto"]) 
# 2\. Deshacemos la última acción (debe sacar 'Borrar texto') 
print(deshacer_ultima_accion(acciones)) 
# Resultado esperado: "Acción deshecha: BORRAR TEXTO" 
# 3\. Deshacemos la siguiente (debe sacar 'Insertar imagen') 
print(deshacer_ultima_accion(acciones)) 
# Resultado esperado: "Acción deshecha: INSERTAR IMAGEN"

#### CONJUNTOS SET Y BUSQUEDAS ULTRARAPIDDAS

def filtrar_ips_unicas(registro_ips: list, ip_sospechosa: str) ->dict | str:
    
    try:
        ips_unicas = set(registro_ips)
        
        ips_revisadas = {
            "total_unicas": len(ips_unicas),
            "detectada": ip_sospechosa in ips_unicas}
        
        return ips_revisadas
    except (AttributeError, TypeError):
        return "Error: Parámetro de entrada inválidos."

# Lista de accesos al servidor con muchas IPs repetidas: 
accesos = [ "192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.1", "10.0.0.5", "192.168.1.1" ] 
# Prueba 1: Buscar una IP que SÍ existe 
print(filtrar_ips_unicas(accesos, "10.0.0.5")) 
# Resultado esperado: {'total_unicas': 3, 'detectada': True} 
# Prueba 2: Buscar una IP que NO existe 
print(filtrar_ips_unicas(accesos, "185.220.101.5")) 
#  Resultado esperado: {'total_unicas': 3, 'detectada': False}

#Practica producto en común entre sucursales (E-commerce)
def encontrar_productos_comunes(sucurla_a: list, sucursal_b: list) -> dict | str :
    try:
        sucursal_a_limpia = set(sucurla_a)
        sucursal_b_limpia = set(sucursal_b)
        comunes = sucursal_a_limpia & sucursal_b_limpia
        productos_encontrados = {
            "productos_comunes": list(comunes),
            "total": len(comunes)
        }
        return productos_encontrados
    except (AttributeError, TypeError):
        return "Error: listas de sucursales inválidas"

tienda_centro = ["Teclado", "Mouse", "Monitor", "Audífonos"] 
tienda_norte = ["Silla Gaming", "Mouse", "Audífonos", "Webcam"] 
# Prueba a ejecutar: 
print(encontrar_productos_comunes(tienda_centro, tienda_norte)) 
# Resultado esperado: {'productos_comunes': ['Mouse', 'Audífonos'], 'total': 2} 
# (El orden interno de la lista puede variar porque los sets no tienen orden)

def validar_configuracion_servidor(config: tuple) -> dict | str:
    try:
        host, puerto, ssl_activo = config
        validado = {
                "servidor": host.lower(),
                "puerto_seguro": puerto == 443 and ssl_activo
            }
        return validado
    except (AttributeError, TypeError):
        return "Claves o tipos errados"
# Tupla inmutable de configuración: 
config_prod = ("SERVER-DB-01", 443, True) 
# Prueba 1: 
print(validar_configuracion_servidor(config_prod)) 
# Resultado esperado: {'servidor': 'server-db-01', 'puerto\_seguro': True} 
# # Prueba 2 (Con puerto no estándar): 
config_dev = ("SERVER-DEV", 8080, False) 
print(validar_configuracion_servidor(config_dev)) # Resultado esperado: {'servidor': 'server-dev', 'puerto\_seguro': False}

def procesar_coordenadas_entrega(punto_gps: tuple, distancia_km: float) ->dict | str:
    latitud, longitud, ciudad = punto_gps
    
    logistica = {
        "ubicación": f"Se encuentra en la ciudad de:{ciudad}, latitud: {latitud}, longitud: {longitud}",
        "costo_envio": 5000 if distancia_km > 15.0 else 2500,
    }
    return logistica

def procesar_transaccion_bancaria(transcaccion: tuple) ->dict | str:
    try:
        id_tx, monto, tipo = transcaccion
        
        if tipo.upper() == "RETIRO":
             comision = monto * 0.02
             
        elif tipo.upper() == "DEPOSITO":
            comision = 0.0
            

        transa_procesa = {
            "id": id_tx,
            "monto_neto": round(monto - comision, 2),
            "comision_aplicada": comision
        }
        return transa_procesa
    except (AttributeError, TypeError):
        return "Error de atributo o tipo"

def procesar_producto_inventario(producto: tuple) -> dict | str:
    try:
        sku, precio_base, categoria, en_oferta = producto
        if en_oferta == True:
            descuento = precio_base * 0.15
        else:
            descuento = 0.0
        proc_invn = {
            "sku": sku.upper(),
            "categoría": categoria.lower(),
            "precio_final": round(precio_base - descuento, 2)
        }
        return proc_invn
    except (ArithmeticError, TypeError):
        return "Error de atributo o tipo"

