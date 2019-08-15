# Debe mostrarse luego de cada jugada efectuada
# Primero debe mostrar el estado actual del tablero y luego mostrar la lista de acciones que el jugador puede ejecutar
# Acciones: descubrir una baldosa, guardar la partida, y salir de la partida, con o sin guardar
import string
import texto

def menu_de_juego(N,M):
    #estado actual del tablero
    print(texto.texto_2)


    while True:
        decision_usuario_juego = input()
        if not decision_usuario_juego.isdigit():
            print("Debe ingresar uno de los dígitos entregado en las opciones")
        else:
            if not int(decision_usuario_juego) in range(1,5):
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
            letras_posibles = {l:n for l, n in zip(letras_minusculas, range(0, 16))}
            mayusculas = {l:n for l, n in zip(letras_mayusculas, range(0, 16))}
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