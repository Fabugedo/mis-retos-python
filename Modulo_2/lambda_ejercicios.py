
def inventario_por_Stock(lista_invent: list) -> list:
    inventario_stock = sorted( lista_invent, key=lambda  p: p["stock"], reverse=True)
    return inventario_stock




inventario = [ {"nombre": "Silla Gamer", "stock": 3}, 
              {"nombre": "Audífonos", "stock": 15}, 
              {"nombre": "Webcam", "stock": 0}, 
              {"nombre": "Micrófono", "stock": 8}, ]    

print(inventario_por_Stock(inventario))








def ordenar_por_stock_y_precio(lista: list) -> list:
    inventario_precio = sorted(lista, key=lambda p: (-p["stock"], p["precio"]))
    return inventario_precio


print("***************************************************************")                               
inventario_teck = [ {"nombre": "Teclado", "stock": 5, "precio": 50}, 
              {"nombre": "Mouse", "stock": 5, "precio": 20}, 
              {"nombre": "Monitor", "stock": 10, "precio": 200}, ]

print(ordenar_por_stock_y_precio(inventario_teck))