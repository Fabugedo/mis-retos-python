def procesar_facturacion_cuotas(ordenes: list, metodo_pago: str) -> float | str:
        subtotal = 0
       
        try:
            for i in ordenes:
             subtotal += i['monto'] * i['cuotas']
             
            if metodo_pago == "TRANSFERENCIA":
                 total = subtotal * 0.95
                 return total
            elif metodo_pago == "TARJETA":
                 total = subtotal
                 return total
            elif metodo_pago == "CREDITO":
                 total = subtotal * 1.10
                 return total
            else:
                 return "Error: Método de pago no soportado."
        
        except (ValueError, TypeError):
             return "Error, Datos de monto o cuotas inválidos."
        except KeyError:
             return "Error, Estructura de orden inválida"