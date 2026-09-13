from collections import deque

cola_trabajos = deque(["Reporte.pdf", "Foto.png", "Contrato.docx"])

print("Imprimiendo primer trabajo en cola..")
primero_Cola = cola_trabajos.popleft()
print(f"Este es el primer trabajo en cola: {primero_Cola}")
cola_trabajos.append("Plano.dwg")
ultimo_cola = cola_trabajos.pop()
print(f"Este fue el ultimo trabajo en cola: {ultimo_cola}")

##################################################
lapices_color = deque(["amarillo", "rojo", "azul", "verde", "celeste", "rosado"])


while lapices_color:
    sacando_lapices = lapices_color.popleft()
    print(f"Estos son los lapices que se van sacando en orden: {sacando_lapices}")
print("Todos los lapices fueron sacados del estuche")
