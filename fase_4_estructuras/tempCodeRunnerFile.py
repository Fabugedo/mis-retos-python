##################################################
lapices_color = deque(["amarillo", "rojo", "azul", "verde", "celeste", "rosado"])


while lapices_color:
    sacando_lapices = lapices_color.popleft()
    print(f"Estos son los lapices que se van sacando en orden: {sacando_lapices}")
print("Todos los lapices fueron sacados del estuche")
