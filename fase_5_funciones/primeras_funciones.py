import operaciones






mensaje = operaciones.saludar()

print(mensaje)

#####################################################################

suma = operaciones.sumar(5,10)

print(suma)

#######################################################################

cliente_A = operaciones.calcular_precio_total(10000)
cliente_B = operaciones.calcular_precio_total(5000, 3)
cliente_c = operaciones.calcular_precio_total(20000, 2, 0.1)
cliente_c_desc = operaciones.aplicar_descuento(cliente_c, 10)

print(f"Total con cliente A : {cliente_A}")
print(f"Total con cliente B: {cliente_B}")
print(f"Total con cliente C: {cliente_c} pero aplicamos un descuento: {cliente_c_desc}")

#########################################################################

print(operaciones.sumar_todos(10,20)) #pasamos 2
print(operaciones.sumar_todos(5, 5, 5, 5, 5)) #pasamos 5
print(operaciones.sumar_todos(100))   #pasamos 1

##################################################################################

total = operaciones.procesar_compra(5000, 12000, 3000, cliente="Fabrizio", pago="tarjeta")
print(f"Total: {total}")

##############################################################################################

venta_1 = operaciones.generar_reporte_venta(12000, 4500, 8900, cliente="Fabrizio", metodo_pago="Efectivo")
venta_2 = operaciones.generar_reporte_venta(vendedor="Camila", sucursal="central", descuento_aplicado="True")

print(venta_1)
print(venta_2)

##################################################################################################
venta_total_1 = operaciones.calcular_total_comisiones(1500.0, 300.0, 500.0)
venta_total_2 = operaciones.calcular_total_comisiones(16000.0, 215.5, 25521.0, 512039.1, 22569.0)
print(venta_total_1)
print(venta_total_2)

############################################################################
