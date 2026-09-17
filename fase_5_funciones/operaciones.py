from datetime import datetime
import random
import math

def sumar(a, b):
    return a + b

def saludar(nombre="invitado"):
    return f"Hola {nombre}, Bienvenido a la fase 5!"

def calcular_precio_total(precio_bbase, cantidad=1, impuesto=0.19):
                    """ acá estamos calculando el total y calculandole el impuesto
                    le pasamos precio_bbase por la cantidad y a eso con una operacion matematica le calculmaos el
                    porcentaje de impuesto (que ya viene con 0.19 por defecto)
                    y eso nos devuelve el impuesto al total
                    """
                    precio_total = precio_bbase * cantidad
                    impuesto_altotal = precio_total * (1 + impuesto )
                    return impuesto_altotal
def aplicar_descuento(monto_total, porcentaje_descuento=0):
                    """
                    acá simplemente vemos si le aplicamos descuento al monto total que traemos desde la funcion de arriba
                    la operacion matematica nos permite aplicar la funcion incluso si nos equivamos y la llamamos si no hay descuento
                    no cambiará el total

                    """
                    monto_final = monto_total * (1 - (porcentaje_descuento / 100))
                    return monto_final


def sumar_todos(*numeros: float) -> float:
        """
        Suma cualquier cantidad de números que reciba 
        """
        return sum(numeros) #sum es nativa de python y suma elementos de una tupla o lista

def procesar_compra(*precios: float, **opciones) -> float:
        """ Suma todos los precios y muestra las opciones adicionales recibidas."""
        total = sum(precios)
        print(f"Opciones de la compra: {opciones}")
        return total

def generar_reporte_venta(*precios: float, **meta_datos) -> str:
        """
        Genera reportes con total de articulos, total de ventas y los metadatos  
        """
        cantidad_productos = len(precios) 
        ventatotal = sum(precios) if precios else 0.0
        
        return f"Se vendio un total de {cantidad_productos} productos, por una suma de {ventatotal}. estos fueron los datos de venta: {meta_datos}"

def generar_ticket(cliente: str, monto_base: float) -> str:
        fecha = datetime.now()
        fecha_formato = fecha.strftime("%d/%m/%Y, %H:%M")

        promo_regalo = random.randint(5, 20)
        descuento_monto = monto_base * (1 - (promo_regalo / 100))

        total_final = math.ceil(descuento_monto)
        return f"{cliente} | fecha: {fecha_formato} | Descuento: {promo_regalo}% | Total a pagar: {total_final}"

SALDO_CUENTA = 100000.0

def realizar_transferencia(monto: float, destinatario: str) -> str:
        """
        Funcion que ocupa un scope con una variable global (saldo_cuenta) y una local. Restamos a global y condicionamos para el funcionamiento
        """
        global SALDO_CUENTA
        costo_fijo = 300
        saldo_final = monto + costo_fijo
        if saldo_final > SALDO_CUENTA:
                return f"No puede realizarce la acción por saldo insuficiente"
        else:
                SALDO_CUENTA -= saldo_final
                return  f"Operacion realizada con exito, se transfirio ${saldo_final} a {destinatario}. Su nuevo saldo es {SALDO_CUENTA}"
      