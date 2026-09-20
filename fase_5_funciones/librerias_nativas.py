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

venta_total_1 = operaciones.calcular_total_comisiones(1500.0, 300.0, 500.0)
venta_total_2 = operaciones.calcular_total_comisiones(16000.0, 215.5, 25521.0, 512039.1, 22569.0)
print(venta_total_1)
print(venta_total_2)

qwa_dict1 = operaciones.guardar_configuraciones(Modo_oscuro=True, volumen=80, idioma="es")
qwa_dict2 = operaciones.guardar_configuraciones(Modo_claro= False, volumen=30, idioma="eng")
print(qwa_dict1)
print(qwa_dict2)


######### ejercicio ##############
##1
logs_usuario1 = operaciones.historial_servidor(ip_cliente="192.168.1.10", mensaje_evento="validando la funcion")
logs_usuario2 = operaciones.historial_servidor(ip_cliente="192.168.1.12", mensaje_evento="validando la funcion en otra ip")
print(logs_usuario1)
print(logs_usuario2)
print("-----------------")

##2
mediciones_dia1 = operaciones.mediciones_servidor(24.0,150.2,10.0,15.1,20,1)
mediciones_dia2 = operaciones.mediciones_servidor(10.2,24.5,30.0)
mediciones_dia3 = operaciones.mediciones_servidor(0)
print(mediciones_dia1)
print(mediciones_dia2)
print(mediciones_dia3)
print("------------------")
##3
fichero_tecnico1 = operaciones.registro_datos_servidor(Ram="1028", Región="V region", proveedor="VTR")
fichero_tecnico2 = operaciones.registro_datos_servidor(SO="Windows", Región="Metropolitana")
print(fichero_tecnico1)
print(fichero_tecnico2)
print("--------------------")