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

def registrar_evento(evento: str, bitacora: list= None) ->list:
        """ Ocupando list = None en bitacora, Nos permite crear una lista NUEVA e independiente en la RAM cada vez que alguien llama al a funcion
        sin pasarle una. Lo que prevee la contaminación de la misma lista en la PVM
        """
        if bitacora is None:
                bitacora =  []
        bitacora.append(evento)
        return bitacora

def agregar_producto(producto: str, precio: float, carrito: dict = None) ->dict:
        """
        Mismo que la funcion anterior ahora ocupando diccionarios , el detalle cambia por ejemplo en que le pasamos ahora al carrito un producto
        con un precio al final, a diferencia del append. Tambien añadir que debemos declarar solo con el nombre del diccionario el que queremos cambiar
        ejemplo: carrito= carrito_juan ), no es necesario corxetes ni tanta sintaxis
        """
        if carrito is None:
                carrito = {}
        carrito[producto] = precio
        return carrito

def registrar_log(ip: str, tipo_evento: str, historial: list = None) ->list:
        """
        El cambio que tenemos acá , es integrar f-strings , para crear log_texto y pasarselos a historial de forma comoda
        """
        if historial is None:
                historial = []
        log_texto = f"[{ip}] - {tipo_evento}"
        historial.append(log_texto)
        return historial

###Ejemplo micro-sintactico 
def calcular_estadisticas_basicas(numeros: list) ->tuple:
        """Calcula y retorna el valor mínimo y máximo de una lista. 
        """
        return min(numeros), max(numeros) #devuelve tupla implicita
##########################################################

def analizar_rendimiento(uso_cpu: float, uso_ram: float) -> tuple:

        """
        Prom entre usocpu y ram , detectaremos cualquier uso que supere el 0.8 
        """
        alerta = False
        prom_cpuram = (uso_cpu + uso_ram)/2
        if uso_cpu >= 80.0 or uso_ram >= 80.0:
                alerta = True
        mensaje = f"Este es el promedio entre el cpu y la ram {prom_cpuram}, actualmente este es el estado de alerta: {alerta}"
        return prom_cpuram, alerta, mensaje

############ ejemplos  *ARGS  ###################
##*ARGS es atrapar toodos los valores sueltos en una tupla 
##**kwargs atrapa todo con nombre y valor  y los empaqueta en diccionario

def sumar_todos(*numeros)-> float:
        """
        suma una cantidad indefinida de numeros pasados por parametros
        """
        #numeros se converte en una tupla con todo lo que le envies
        return sum(numeros)
#se puede llamar con la cantidad de numeros que queramos
total_1 = sumar_todos(10.0, 20.0) #devuelve 30
total_2 = sumar_todos(5.0, 15.0, 30.0, 50.0) #devuelve 100

############  **KAWRGS ###############
def crear_perfil_usuario(**datos)-> dict:
        """
        recibbe cualquier cantidad de datos en formato clave= valor.
        """
        # ' dato ' se convierte automaticamente en un diccionario 
        return datos

#la llamas asignando los nombres que quieras al vuelo:
usuario_1 = crear_perfil_usuario(nombre="Juan", rol="Junior", pais="Chile")
#devuelve: {'nombre': 'Juan', 'rol': 'Junior', 'pais': 'Chile}


####################################fin ejemplos#####################################


def calcular_total_comisiones(*comisiones) -> float:
        """
        agrupa y suma todas las comisiones en una tupla
        """
        return sum(comisiones)

def guardar_configuraciones(**opciones) ->dict:
        """
        **kwargs nos permite guardar todos los elementos ordenados en formato diccionario con clave y valor
        el formato de los datos puede ser int,float,str,booleano
        """
        return opciones

def historial_servidor(ip_cliente: str, mensaje_evento: str, historial_msg: list = None) -> list:
        """
        concateno las ip y los mensajes en una variable, para enlazar ip por mensaje
        me aseguro de dejar un condicional , de que si detecta que no viene nada por historial_msg
        cree la lista nueva
        De no ser así, continua concatenando con sus ip y mensaje
        """
        if historial_msg is None:
                historial_msg = []
        mensaje_log = f"{ip_cliente}: {mensaje_evento}"
        historial_msg.append(mensaje_log)
        return historial_msg

def mediciones_servidor(*mediciones: float) -> tuple:
        """
        recibo mediciones, calculo primero la cantidad de mediciones, para validar que existan, si no, devuelve mensaje 
        evitamos procesar o gastar recursos de manera temprana
        luego calculamos el total por la cantidad de mediciones para obtener el promedio
        ocupamos condicionales
        ocupamos la variable local estado_Critico en booleano como falso para marcar el estado por defecto
        ocupamos la condicion de 75% para cambiar el estado critico del boleano y preparar el mensaje
        finalmente devolvemos el promedio, el estado y un mensaje
        """
        estado_critico = False
        cantidad_mediciones = len(mediciones)
        if cantidad_mediciones == 0:
                return 0.0, False, f"no se recibieron mediciones"
        total_mediciones = sum(mediciones)
        promedio_mediciones = round(total_mediciones / cantidad_mediciones, 2)
        if promedio_mediciones >= 75.0:
                estado_critico = True
        mensaje = f"Este es el promedio entre las mediciones {promedio_mediciones:.2f}, actualmente este es el estado del servidor: {estado_critico}"
        return promedio_mediciones, estado_critico, mensaje

def registro_datos_servidor(ip: str,**metadatos) -> dict:
        """
        creamos el registro en modo Kwargs, de modo que recibamos claves y valores para crear el expediente del cliente
        """
        metadatos["ip_origen"] = ip
        return metadatos



