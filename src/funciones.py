def limita_entrada(mensaje):
    """Esta funcion muestra el mensaje pasado como argumento
    y devuelve un entero
    """
    seguir = True
    while seguir:
        try:
            numero = int(input(mensaje))
            seguir = False
        except ValueError:
            print("No es un valor válido")
    return numero