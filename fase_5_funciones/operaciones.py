def sumar(a, b):
    return a + b

def saludar(nombre="invitado"):
    return f"Hola {nombre}, Bienvenido a la fase 5!"

def calcular_precio_total(precio_bbase, cantidad=1, impuesto=0.19):
                    precio_total = precio_bbase * cantidad
                    impuesto_altotal = precio_total * (1 + impuesto )
                    return impuesto_altotal
def aplicar_descuento(monto_total, porcentaje_descuento=0):
        monto_final = monto_total * (1 - (porcentaje_descuento / 100))
        return monto_final

