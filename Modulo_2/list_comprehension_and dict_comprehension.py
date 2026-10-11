numeros = [1, 2, 3, 4, 5, 6] 
resultado = [] 
for n in numeros: 
    if n % 2 == 0: 
     resultado.append(n * 2) # resultado: [4, 8, 12]
print(resultado)

resultado_2 = [n * 2 for n in numeros if n % 2 == 0]
print(resultado_2)
#Filtre únicamente los precios mayores o iguales a **20.0**. aplica 19%
precios_usd = [10.0, 25.0, 50.0, 100.0, 5.0]
precios_con_iva = [p * 1.19 for p in precios_usd if p >=  20 ]
print(precios_con_iva)

usuarios = [ 
            {"nombre": "Ana",  "activo": True, "rol": "Admin"}, 
            {"nombre": "Carlos", "activo": False, "rol": "Dev"}, 
            {"nombre": "Elena", "activo": True, "rol": "Dev"}, 
            {"nombre": "Fernando", "activo": True, "rol": "Admin"}, ]

admin_activos = [a["nombre"] for a in usuarios if a["rol"] == "Admin" and a["activo"] ]
print(admin_activos)

productos = [ {"id": 101, "nombre": "Teclado", "precio": 50}, 
             {"id": 202, "nombre": "Mouse", "precio": 25}, 
             {"id": 303, "nombre": "Monitor", "precio": 200}, ]

mapa_precios = {m["nombre"]: m["precio"] for m in productos}
print(mapa_precios) 
print("*********")
productos_caros = {p["nombre"]: p["precio"] for p in productos if p["precio"] > 30}
print(productos_caros)