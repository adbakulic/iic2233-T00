import texto


class MenuDeInicio:

    def __init__(self, nombre, decision_usuario_inicio):
        self.nombre = nombre
        self.decision_ususario_inicio = decision_usuario_inicio


    def decision_ususario_inicio(self):
        print("Bienvenido a LegoSweeper")
        print("\nPor favor ingrese su nombre de usuario:")
        self.nombre = input()

        print(texto.texto_1)

        while True:
            self.decision_usuario_inicio = input()
            if not self.decision_usuario_inicio.isdigit():
                print("Debe ingresar uno de los dígitos entregado en las opciones")
            else:
                if not int(self.decision_usuario_inicio) in range(4):
                    print("Debe ingresar un dígito entre el 0 y el 3, ambos inclusive")
                else:
                    break

        if self.decision_usuario_inicio == "1":
            print("\nElija el tamaño del tablero")
            print("Por favor ingrese el largo (debe ser un número entero entre 3 y 15, ambos inclusive):")

            while True:
                N = input()
                if not N.isdigit():
                    print("Debe ingresar un número entero \nPor favor ingrese nuevamente el largo del tablero:")
                else:
                    if not int(N) in range(3, 16):
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
                    if not int(M) in range(3, 16):
                        print("Debe ingresar un número entero entre 3 y 15 (ambos inclusive) \
                                \nPor favor ingrese nuevamente el ancho del tablero:")
                    else:
                        break
            return self.nombre, self.decision_usuario_inicio, int(N), int(M)


        elif self.decision_usuario_inicio == "0":
            print("Ha salido del juego")
            exit()
            return self.nombre, self.decision_usuario_inicio, 0, 0


        elif self.decision_usuario_inicio == "2":
            print("...Cargando partida")
            return self.nombre, self.decision_usuario_inicio, 0, 0


        else:
            print("Estos son sus 10 puntajes más altos:")
            return self.nombre, self.decision_usuario_inicio, 0, 0







class MenuDeJuego:

    def __init__(self, decision_usuario_juego, N, M):
        self.decision_usuario_juego = decision_usuario_juego
        self.largo = N
        self.ancho = M

    def menu_de_juego(N, M):
        # estado actual del tablero
        print(texto.texto_2)

        while True:
            decision_usuario_juego = input()
            if not decision_usuario_juego.isdigit():
                print("Debe ingresar uno de los dígitos entregado en las opciones")
            else:
                if not int(decision_usuario_juego) in range(1, 5):
                    print("Debe ingresar un dígito entre el 1 y el 4, ambos inclusive")
                else:
                    break


        ### [1] Descubrir una baldosa ###
        ### Se le piden las coordenadas y que éstas coincidan con las de su tablero

        if decision_usuario_juego == "1":
            print("Ingrese las coordenadas de la baldosa que quiere descubrir \nIngrese la letra de la coordenada")

            while True:
                letra = input()
                letra = str(letra.lower())

                letras_minusculas, letras_mayusculas = string.ascii_letters[0:15], string.ascii_letters[26:41]
                letras_posibles = {l: n for l, n in zip(letras_minusculas, range(0, 16))}
                mayusculas = {l: n for l, n in zip(letras_mayusculas, range(0, 16))}
                letras_posibles.update(mayusculas)
                letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"]

                # letras_posibles['A']
                # retorna 1

                if not letra.isalpha():
                    print("Debe ingresar una letra")
                elif len(letra) != 1:
                    print("Debe ingresar una sola letra")
                elif not letra in letras[:int(M)]:
                    print("Debe ingresar una letra que esté en el tablero")
                else:
                    break

            print("Ingrese el número de la coordenada")
            while True:
                numero = input()
                if not numero.isdigit():
                    print("Debe ingresar un número")
                elif not int(numero) in range(int(N)):
                    print("Debe ingresar un número que esté en el tablero")
                else:
                    break

            return decision_usuario_juego, letra, int(numero), letras_posibles


            ### [2] Guardar la partida ###

        if decision_usuario_juego == "2":
            print("Su partida se ha guardado")
            return decision_usuario_juego, 0, 0, 0


            ### [3] Salir de la partida (con guardar) ###

        if decision_usuario_juego == "3":
            print("Ha salido de la partida con guardar")
            exit()
            return decision_usuario_juego, 0, 0, 0


            ### [4] Salir de la partida (sin guardar) ###

        if decision_usuario_juego == "4":
            print("Ha salido de la partida sin guardar")
            exit()
            return decision_usuario_juego, 0, 0, 0