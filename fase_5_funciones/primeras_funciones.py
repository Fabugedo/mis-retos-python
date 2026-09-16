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
