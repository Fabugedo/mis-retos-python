import operaciones




cliente_1 = operaciones.generar_ticket(cliente="Fabrizio", monto_base=19500)
cliente_2 = operaciones.generar_ticket(cliente="Carola", monto_base=32450)
print(cliente_1)
print(cliente_2)


transferencia_1 = operaciones.realizar_transferencia(70000, destinatario="Nicolas")
transferencia_2 = operaciones.realizar_transferencia(100000,destinatario="Angela")
print(transferencia_1)
print(transferencia_2)

nave_alpha = operaciones.registrar_evento(evento="Despegue de la nave")
nave_beta  = operaciones.registrar_evento(evento="Aterrizaje en Marte")
print(nave_alpha)
print(nave_beta)

carrito_juan = operaciones.agregar_producto(producto="Polera", precio=15000.0)
carrito_maria= operaciones.agregar_producto(producto="Pantalón", precio=35000.0)
carrito_juan = operaciones.agregar_producto(producto="Zapatillas", precio=50000.0, carrito= carrito_juan )

print(carrito_juan)
print(carrito_maria)
print(carrito_juan)

logs_servidor = operaciones.registrar_log(ip="192.168.1.10", tipo_evento="Conexión exitosa")
logs_db       = operaciones.registrar_log(ip="10.0.0.5", tipo_evento="Acceso denegado")
logs_servidor = operaciones.registrar_log(ip="192.168.1.10", tipo_evento="Intento de Intrusión", historial=logs_servidor)

print(logs_servidor)
print(logs_db)

menor, mayor = operaciones.calcular_estadisticas_basicas([10, 50, 2, 99, 23])

print(menor, mayor)

informe_1, informe_2, informe_3 = operaciones.analizar_rendimiento(85.0,60.0)
print(informe_1)
print(informe_2)
print(informe_3)
