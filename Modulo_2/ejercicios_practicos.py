numero = [1,2,3,4,5,6,7,8,9,10]
pares = [p * 2 for p in numero if p % 2 == 0 ]
print(pares)

nombres = ["ana", "carlos", "pedro", "maria"]
mayusculas = [n.upper() for n in nombres]
print(mayusculas)

precios = [15.0, 60.0, 100.0, 30.0]
descuentos = [ p * 0.90 for p in precios if p > 50.0]
print(descuentos)

print("***************************************************************************")

def obtener_productos_disponibles(inventario: list, precio_maximo: float) -> list | str:
        try:
                #en una sola linea asignamos el list comprhension:
                disponible = [
                        p["nombre"]
                        for p in inventario
                        if p["stock"] > 0 and p["precio"] <= precio_maximo
                ]
                return disponible

        except (ValueError, TypeError):
                return "Error: Parámetro de precio inválido"

catalogo = [ {"nombre": "Teclado", "precio": 30.0, "stock": 5}, 
            {"nombre": "Mouse", "precio": 15.0, "stock": 0}, 
            {"nombre": "Monitor", "precio": 150.0, "stock": 2}, 
            {"nombre": "Audífonos", "precio": 25.0, "stock": 3}, ]



print(obtener_productos_disponibles(catalogo, 50.0))
print(obtener_productos_disponibles(catalogo, 20.0))
print("***************************************************************************")

def obtener_empleados_bono(empleados: list, bono_minimo: float) -> list | str:
        try:
                bono_venta = [
                        e["nombre"]
                        for e in empleados
                        if e["departamento"] == "VENTAS" and e["bono"] >= bono_minimo
                ]
                return bono_venta
        except (ValueError, TypeError):
                return "Error: Parámetro de bono inválido"
        except (KeyError):
                return "Error: Estructura de empleado inválida."

plantilla = [ {"nombre": "Carlos", "departamento": "VENTAS", "bono": 500.0}, {"nombre": "Ana", "departamento": "IT", "bono": 800.0}, 
             {"nombre": "Sofia", "departamento": "VENTAS", "bono": 300.0}, {"nombre": "Diego", "departamento": "VENTAS", "bono": 600.0} ]

# Prueba 1: 
print(obtener_empleados_bono(plantilla, 500.0)) # Resultado esperado: ['Carlos', 'Diego'] 
# Prueba 2: 
print(obtener_empleados_bono(plantilla, 1000.0)) # Resultado esperado: []

print("*******************************************************************************")
def sanear_correos_activos(usuarios: list) -> list | str:
        try:
                ext_correo = [
                        u["email"].lower()
                        for u in usuarios
                        if u["activo"] == True
                ]
                return ext_correo
        except (ValueError, TypeError):
                return "Error: Parámetro de datos inválido"
        except (KeyError):
                return "Error: Estructura de datos inválido"

usuarios_registrados = [
        {"email": "JUAN@GMAIL.COM", "activo": True},
        {"email": "PEDRO@HOTMAIL.COM", "activo": False},
        {"email": "MARIA@YAHOO.COM", "activo": True}
]
print(sanear_correos_activos(usuarios_registrados))

print("*******************************************************************************")
def aplicar_aumento_categoria(producto: list, categoria: str, porcentaje: float) -> list | str:
        try:
                aumento = [
                         round(p["precio"] * (1 + porcentaje / 100), 2)
                        for p in producto
                        if p["categoria"] == categoria
                        ]
                return aumento
        except (ValueError, TypeError):
                        return "Error: Parámetro de datos inválido"
        except (KeyError):
                        return "Error: Estructura de datos inválido"

catalogo_tienda = [
        {"nombre": "Laptor", "precio": 1000.0, "categoria": "TECNOLOGIA"},
        {"nombre": "Silla", "precio": 100.0, "categoria": "HOGAR"},
        {"nombre": "Mouse", "precio": 50.0, "categoria": "TECNOLOGIA"}
]
print(aplicar_aumento_categoria(catalogo_tienda, "TECNOLOGIA", 10.0))

############################################################################ -------------------- ######################################
def crear_indice_productos(productos: list) -> dict | str:
        try:
                precios = {
                        p["id"]: p["nombre"].upper() for p in productos if p["activo"]
                }
                return precios
        except (ValueError, TypeError):
                                return "Error: Parámetro de datos inválido"
        except (KeyError):
                                return "Error: Estructura de datos inválido"
inventario_raw = [ {"id": 101, "nombre": "teclado", "activo": True}, 
                   {"id": 102, "nombre": "mouse", "activo": False}, {"id": 103, "nombre": "monitor", "activo": True}, ]
print(crear_indice_productos(inventario_raw)) # Resultado esperado: {101: 'TECLADO', 103: 'MONITOR'}

###################################
def mapear_precios_descuento(productos: list, porcentaje_descuento: float) -> dict | str:
        try:
                disponibles = {
                        p["id"]: round(p["precio"] * (1 - porcentaje_descuento / 100), 2) for p in productos if p["disponible"]
                }
                return disponibles
        except (ValueError, TypeError):
                                        return "Error: Parámetro de datos inválido"
        except (KeyError):
                                        return "Error: Estructura de datos inválido"
inventario_tienda = [ {"id": "PROD-01", "precio": 100.0, "disponible": True}, 
                      {"id": "PROD-02", "precio": 200.0, "disponible": False}, # Agotado
                       {"id": "PROD-03", "precio": 50.0, "disponible": True} ]
# Prueba: 
print(mapear_precios_descuento(inventario_tienda, 20.0)) 
# Resultado esperado: {'PROD-01': 80.0, 'PROD-03': 40.0}

########################
print("----------------------------------------------")
def obtener_jugadores_destacados(jugadores: list, puntaje_minimo: int) -> dict | str:
        try:
                jugador = {
                        j["usuario"].upper(): j["puntaje"] for j in jugadores if j["baneado"] == False and j["puntaje"] >= puntaje_minimo
                }
                return jugador
        except (ValueError, TypeError):
                                                return "Error: Parámetro de datos inválido"
        except (KeyError):
                                                return "Error: Estructura de datos inválido"

lista_jugadores = [ {"usuario": "shadow", "puntaje": 1500, "baneado": False}, 
                   {"usuario": "vortex", "puntaje": 2000, "baneado": True}, # Baneado 
                   {"usuario": "alpha", "puntaje": 800, "baneado": False} # Puntaje bajo 
                   ] 
# Prueba: 
print(obtener_jugadores_destacados(lista_jugadores, 1000)) # Resultado esperado: {'SHADOW': 1500}