empleados = [ {"nombre": "Laura", "departamento": "Ventas", "salario": 2400.0}, 
               {"nombre": "Pedro", "departamento": "IT", "salario": 3800.0}, 
               {"nombre": "Sofia", "departamento": "IT", "salario": 3100.0}, 
               {"nombre": "Diego", "departamento": "Marketing", "salario": 1900.0}, ]
mayor_salario = max(empleados, key=lambda a : a["salario"])
menor_salario = sorted(empleados, key=lambda b : b["salario"],reverse=True)
print(mayor_salario)
print(menor_salario)