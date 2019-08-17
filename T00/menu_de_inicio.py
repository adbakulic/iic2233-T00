import texto

def decision_usuario_inicio():

    print("Bienvenido a LegoSweeper")
    print("\nPor favor ingrese su nombre de usuario:")
    nombre = input()

    print(texto.texto_1)

    while True:
        decision_usuario_inicio = input()
        if not decision_usuario_inicio.isdigit():
            print("Debe ingresar uno de los dígitos entregado en las opciones")
        else:
            if not int(decision_usuario_inicio) in range(5):
                print("Debe ingresar un dígito entre el 0 y el 3, ambos inclusive")
            else:
                break


### [1] Crear partida nueva ###

    if decision_usuario_inicio == "1":
        print("\nElija el tamaño del tablero")
        print("Por favor ingrese el largo (debe ser un número entero entre 3 y 15, ambos inclusive):")

        while True:
            N = input()
            if not N.isdigit():
                print("Debe ingresar un número entero \nPor favor ingrese nuevamente el largo del tablero:")
            else:
                if not int(N) in range(3,16):
                    print("Debe ingresar un número entero entre 3 y 15 (ambos inclusive) \
                    \nPor favor ingrese nuevamente el largo del tablero:")
                else:
                    break

        print("Por favor ingrese el ancho (debe ser un número entero entre 3 y 15, ambos inclusive):")
        while True:
            M = input()
            if not M.isdigit():
                print("Debe ingresar un número entero \nPor favor ingrese nuevamente el ancho del tablero:")
            else:
                if not int(M) in range (3,16):
                    print("Debe ingresar un número entero entre 3 y 15 (ambos inclusive) \
                    \nPor favor ingrese nuevamente el ancho del tablero:")
                else:
                    break
        return nombre, decision_usuario_inicio, int(N), int(M)


### [0] Salir ###

    elif decision_usuario_inicio == "0":
        print("Ha salido del juego")
        exit()
        return nombre, decision_usuario_inicio, 0, 0


### [2] Cargar partida ###

    elif decision_usuario_inicio == "2":
        print("...Cargando partida")
        return nombre, decision_usuario_inicio, 0, 0


### [3] Ver ranking ###

    elif decision_usuario_inicio == "3":
        print("Estos son sus 10 puntajes más altos:")
        return nombre, decision_usuario_inicio, 0, 0






