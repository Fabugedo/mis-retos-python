usuario_a = ["#python", "#coding", "#developer", "#python", "#code", "#python"]
usuario_b = ["#developer", "#web", "#python", "#backend", "#code"]

usuario_a_sorted = set(usuario_a)
usuario_b_sorted = set(usuario_b)


usuario_a_prelista = usuario_a_sorted - usuario_b_sorted
usuario_b_prelista = usuario_a_sorted & usuario_b_sorted

usuario_a_lista = list(usuario_a_prelista)
usuario_b_lista = list(usuario_b_prelista)

print(usuario_a_lista)
print(usuario_b_lista)
print(f"Más especifico: Diferencias: {usuario_a_lista}. Intereses comunes: {usuario_b_lista}"  )
