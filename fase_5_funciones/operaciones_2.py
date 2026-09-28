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
