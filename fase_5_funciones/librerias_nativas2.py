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