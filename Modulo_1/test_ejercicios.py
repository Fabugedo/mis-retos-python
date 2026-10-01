import mod1_fun

##1
compras_mes = [
    {"monto": 25.0, "cuotas": 2},
    {"monto": 100.0, "cuotas": 1}
]
#test
print("************************************")
print(mod1_fun.procesar_facturacion_cuotas(compras_mes, "TRANSFERENCIA"))
print(mod1_fun.procesar_facturacion_cuotas(compras_mes, "CREDITO"))
print(mod1_fun.procesar_facturacion_cuotas(compras_mes, "CRYPTO"))
print(mod1_fun.procesar_facturacion_cuotas(compras_mes, "TARJETA"))