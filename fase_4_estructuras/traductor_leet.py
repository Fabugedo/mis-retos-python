
def traducir_a_leet(texto):
    convertir = {
        "a" : "4",
        "e" : "3",
        "i" : "1",
        "o" : "0",
        "s" : "5",
        "A" : "4",
        "E" : "3",
        "I" : "1",
        "O" : "0",
        "S" : "5"
    }

    convertido = ""

    for i in texto:
        if i in convertir:
            convertido += convertir[i]
        else:
            convertido += i

    return convertido

traducir = input("ingresa acá: ")
prueba = traducir_a_leet(traducir)
print(prueba)
