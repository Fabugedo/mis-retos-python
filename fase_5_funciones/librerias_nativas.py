import operaciones




cliente_1 = operaciones.generar_ticket(cliente="Fabrizio", monto_base=19500)
cliente_2 = operaciones.generar_ticket(cliente="Carola", monto_base=32450)
print(cliente_1)
print(cliente_2)


transferencia_1 = operaciones.realizar_transferencia(70000, destinatario="Nicolas")
transferencia_2 = operaciones.realizar_transferencia(100000,destinatario="Angela")
print(transferencia_1)
print(transferencia_2)