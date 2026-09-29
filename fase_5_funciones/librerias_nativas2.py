import operaciones_2

print(operaciones_2.procesar_pago_cuotas("1200.0", "12"))
print(operaciones_2.procesar_pago_cuotas("500.0", "0"))
print(operaciones_2.procesar_pago_cuotas("mil", "6"))
##ejercicio 2 con diccionario
base_datos_usuarios = [
        {"id": 1, "nombre": "Ana", "email": "ana@empresa.com"},
        {"id": 2, "nombre": "Carlos", "email": "carlos@empresa.com"},
        {"id": 3, "nombre": "Beatriz", "email": "beatriz@empresa.com"}
    ]
print(operaciones_2.obtener_email_usuario(base_datos_usuarios, "2"))

##ejercicio reforzamiento diccionario

catalogo_productos = [
    {"nombre": "Teclado Mécanico", "precio": 120.0},
    {"nombre":"Mouse Gamer", "precio": 45.0},
    {"nombre":"Monitor 24 Pulgadas", "precio": 220.0},
    {"nombre":"Pad mouse", "precio": 15.0}
]
print(operaciones_2.filtrar_por_precio_maximo(catalogo_productos, "100.0"))
print(operaciones_2.filtrar_por_precio_maximo(catalogo_productos, "-50"))
print(operaciones_2.filtrar_por_precio_maximo(catalogo_productos, "gratis"))

##ejercicio reforzamiento 2 diccionario

inventario = [
      {"id": 101, "nombre": "Laptop Pro", "stock": 5},
      {"id": 102, "nombre": "Cargador usb-c", "stock": 12},
      {"id": 103, "nombre": "Audífonos bluetooth", "stock": 0}
]
print("***********************************************************")
print(operaciones_2.verificar_stock(inventario, "101", "3"))
print(operaciones_2.verificar_stock(inventario, "101", "10"))
print(operaciones_2.verificar_stock(inventario, "101", "-2"))
print(operaciones_2.verificar_stock(inventario, "999", "1"))
print(operaciones_2.verificar_stock(inventario, "101", "dos"))
print(operaciones_2.verificar_stock(inventario, "102", "1"))

print("***********************************************************")
carrito_compras = [
    {"nombre": "Polera", "precio": 15.0, "cantidad": 2},
    {"nombre": "Pantalón", "precio": 40.0, "cantidad": 1}
]
print(operaciones_2.calcular_total_con_descuento(carrito_compras, "DESCUENTO10")) # Debería dar 63.0
print(operaciones_2.calcular_total_con_descuento(carrito_compras, "")) # Debería dar 70.0
print(operaciones_2.calcular_total_con_descuento(carrito_compras, "OFERTA_FAK3")) # Error de código inválido

print("***********************************************************")
compra = [
    {"nombre": "Silla Gamer", "precio": 50.0, "cantidad":1},
    {"nombre": "Mousepad", "precio": 10.0, "cantidad":2},
]
print(operaciones_2.calcular_factura_final(compra, "CL")) # Subtotal 70 + IVA(13.3) + Envío(15) = 98.3
print(operaciones_2.calcular_factura_final(compra, "US")) # Subtotal 70 + Imp(5.6) + Envío(15) = 90.6
print(operaciones_2.calcular_factura_final(compra, "JP"))

print("********************************************")
historial = [{"monto": 100.0}, {"monto": 50.0}] # Total gastado = 150.0
print(operaciones_2.calcular_puntos_fidelidad(historial, "PLATA")) # 150 \* 2 = 300
print(operaciones_2.calcular_puntos_fidelidad(historial, "DIAMANTE"))  # Error