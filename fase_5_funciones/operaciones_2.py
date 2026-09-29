import re
import math
import random

###### fase 5, manejo de excepciones // try / except / else / finally

#try:
#    numero = int(input("ingresa tu edad: "))
#    resultado = 100 / numero

#except ValueError:
#    print("Debes ingresar un número entero válido")
#except ZeroDivisionError:
#    print("La edad no puede ser cero")
#except Exception as e:
    # Captura de respaldo para errores que no son previstos
#    print(f"Ocurrio un error inesperado: {type (e).__name__} - {e}")
#
##Excepciones manuales (raise), a veces por codigo no falla pero si por reglas de negocio. Para estos casos usamos "raise", la cual fuerza
##la excepcion

def registrar_usuario(edad: int):
    if edad < 0:
        #forzamos un ValueError xq edad negativa no hace sentido
        raise ValueError("La edad no puede ser un número negativo")
    print(f"Usuario registrado con {edad} años.")

##ejemplo integrador (caso de estudio) ##
def cargar_configuracion(ruta_archivo: str) -> dict:
    archivo = None
    try:
        print("1. Intentando abrir el archivo de configuracion...")
        archivo = open(ruta_archivo, "r")
        contenido = archivo.read()
        ### simulamos converción a diccionario o procesamiento
        return {"status": "ok", "data": contenido}
    except FileNotFoundError:
        print("2. El archivo no existe en el disco")
        return {}
    except Exception as e:
        print(f"2. Error no previsto al leer el archivo : {e}")
        return {}
    else:
        ##se ejecuta si el archivo pasa
        print("3. Lectura completada sin ningun inconveniente.")
    finally:
        #se ejecuta SIEMPRE para asegurar que el archivo se cierre si se abrió
        if archivo:
            archivo.close()
            print("4. Limpieza: Archivo cerrado correctamente.")

##ejercicio pasarela de pago , el usuario ingresa el monto y la cantidad de cuotas como texto. Si ingresa letras o elige 0 cueotas
## el  sistema no puede caese , debe capturar el error y responder con un mensaje claro.
# crear funcion procesar _ pago _ cuotas (monto_str , cuotas_str ), bloqeu try tiene que tener monto _str a float, cuotas_str a int
# calcula el valor de la cuota monto / cuotas 
# retorna el valor de cada cuota es $x , puede usarse f string
# 2. manejo de errorr con except:
#
def procesar_pago_cuotas(monto_str: str, cuotas_str: str) ->str :
    try:
        monto_float = float(monto_str)
        cuotas_int = int(cuotas_str)
        valor_cuota = monto_float / cuotas_int
        return f"El valor de cada cuota es ${valor_cuota}."
    except ValueError:
        return "Error: Los valores ingresados deben ser numéricos."
    except ZeroDivisionError:
        return "Error: La cantidad de cuotas debe ser mayor a cero."
    
def obtener_email_usuario(usuarios: list, usuario_id_str: str) ->str:

    try:
        traer_id = int(usuario_id_str)
        for x in usuarios:
            if x["id"] == traer_id:
                return f"Email encontrado: Usuario: {x['nombre']} y Correo: {x['email']}"
        else:
            return "No hay usuarios con ese nombre"
    except ValueError:
        return "Error: El ID de usuario debe ser un número entero."
    except KeyError:
        return "Estructura de datos de usuario invalida."

def filtrar_por_precio_maximo(productos: list, precio_max_str) ->list | str:
        try:
            precio_max_float = float(precio_max_str)
            if precio_max_float <= 0:
                    return "Error: EL precio debe ser mayor a 0"
            productos_filtrados = []

            for i in productos:
                if i["precio"] <= precio_max_float:
                    productos_filtrados.append(i)
            return productos_filtrados
        except ValueError:
            return "el precio debe tener un valor numerico"
        except KeyError:
            return "Error: estructura de caracteres invalida"
        


def verificar_stock(productos: list, producto_id_str: str, cantidad_str: str) ->str:
    try:
        producto_id_int = int(producto_id_str)
        cantidad_int = int(cantidad_str)
        if cantidad_int <= 0:
                     return "La cantidad solicitada debe ser mayor a 0"

        for i in productos:
            if i["id"] == producto_id_int:
                  if i["stock"] >= cantidad_int:
                        return f"Stock disponible de {i['nombre']}. Disponible: {i['stock']}. "
                  else:
                        return f"Stock insuficiente para {i['nombre']}. Disponible: {i['stock']}."
        else:
                return "Producto no encontrado."
    except ValueError:
          return "Error: El ID y la cantidad deben ser enteros validos."
    except KeyError:
          return "Error: Estructura de inventario inválida."

def calcular_total_con_descuento(carrito: list, codigo_promo: str) -> float | str:
            subtotal = 0.0
            try:  
                for i in carrito:
                        subtotal += i["precio"] * i["cantidad"]
                if codigo_promo == "DESCUENTO10":
                        total = subtotal - (subtotal * 0.10)
                        
                elif codigo_promo == "DESCUENTO20":
                        total = subtotal - (subtotal * 0.20)
                       
                elif codigo_promo == "":
                        total = subtotal
                        
                else:
                        return "Ingrese el codigo correcto de la promoción "
                return total
            except ValueError:
                 return "Valor de precio o cantidad no son numericos "
            except KeyError:
                 return "Llaves incorrectas"
            except TypeError:
                 return "valor de precio o cantidad no son numericos "

def calcular_factura_final(items: list, region: str) -> float | str:
            subtotal = 0.0
            try:
                for i in items:
                    subtotal += i["precio"] * i["cantidad"]
                    
                         
                if subtotal >= 100:
                     costo_envio = 0.0
                else:
                     costo_envio = 15.0  





                if region == "CL":
                    impuesto = 0.19
                    
                elif region == "MX":
                     impuesto = 0.16

                elif region == "US":
                     impuesto = 0.08
                   
                else:
                     return "Ingrese codigo pais correcto"
                monto_impuesto = subtotal * impuesto
                total_final = subtotal + monto_impuesto + costo_envio
                return total_final
                
            except ValueError:
                 return "Valores incorrectos"
            except TypeError:
                 return "Valores incorrectos"
            except KeyError:
                 return "falta clave diccionario o clave incorrecta"

            ### nota, siempre descomponen en 2 fases , fase 1 acumular con for , fase 2 hacer las reglas de negocio

def calcular_puntos_fidelidad(compras: list, nivel_cliente: str)-> int | str:
     try:
        total_gastado = 0
        puntos = 0
        for i in compras:
              total_gastado += i["monto"]

        if nivel_cliente == "BRONCE":
             puntos +=  1
        elif nivel_cliente == "PLATA":
             puntos +=  2
        elif nivel_cliente == "ORO":
             puntos +=  3
        else:
            return "nivel de cliente inválido."
        total_comprado = total_gastado * puntos
        return total_comprado
     
     except ValueError:
          return "Error: monto numérico invalido"
     except KeyError:
          return "Error: Estructura de compra inválida"