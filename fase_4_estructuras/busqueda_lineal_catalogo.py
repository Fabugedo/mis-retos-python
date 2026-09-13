
catalogo = list(range(1,1001))
pasos = 0
elemento_buscado = 888
for i in catalogo:
    pasos += 1
    if i == elemento_buscado:
        print(f"variable encontrada! hubo un total de: {pasos} pasos, antes de encontrarla")
        break

#############################

# 1. Definir los límites del rango en la lista
inicio = 0
fin = len(catalogo) - 1
pasos_binaria = 0

# 2. Bucle que se ejecuta mientras el rango sea válido
while inicio <= fin:
    pasos_binaria += 1
    
    # Calcular el índice del punto medio (división entera con //)
    medio = (inicio + fin) // 2
    
    # Evaluar el elemento del centro
    if catalogo[medio] == elemento_buscado:
        print(f"¡Encontrado con Búsqueda Binaria en solo {pasos_binaria} pasos!")
        break
    elif catalogo[medio] < elemento_buscado:
        # El objetivo está en la mitad derecha: descartamos la mitad izquierda
        inicio = medio + 1
    else:
        # El objetivo está en la mitad izquierda: descartamos la mitad derecha
        fin = medio - 1
