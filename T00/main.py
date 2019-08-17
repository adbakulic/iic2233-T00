import menu_de_inicio
import crear_tablero
import menu_de_juego
import turno
import os
import tablero
from  guardar_partida import Juego



nombre, decision_usuario_inicio, N, M = menu_de_inicio.decision_usuario_inicio()

juego = Juego(nombre, N, M)

puntaje = 0
# [1] Crear partida nueva.
if decision_usuario_inicio == "1":
    tablero_con_legos, tablero_sin_legos, tablero_con_numeros_y_legos = crear_tablero.crear_tablero(N,M)
    juego.tablero_a, juego.tablero_o = tablero_sin_legos, tablero_con_numeros_y_legos

    while decision_usuario_inicio == "1":
        decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N,M)
        juego.letra, juego.numero = letra, numero

        # Descubrir una baldosa.
        if decision_usuario_juego == "1":
            turno = juego.turno()
            ganador = juego.ganador()
            puntaje = juego.puntaje()
            if turno == False:
                juego.guardar_ranking(str(puntaje))
                exit()
            if ganador == True:
                juego.guardar_ranking(str(puntaje))
                tablero.print_tablero(tablero_con_numeros_y_legos, True)
                exit()

        # Guardar la partida.
        if decision_usuario_juego == "2":
            juego.guardar()
            puntaje = juego.puntaje()

        # Salir de la partida con guardar.
        if decision_usuario_juego == "3":
            juego.guardar()
            puntaje = juego.puntaje()
            exit()

        # Salir de la partida sin guardar.
        if decision_usuario_juego == "4":
            juego.guardar_ranking(str(puntaje))
            exit()

# [0] Salir.
elif decision_usuario_inicio == "0":
    juego.guardar_ranking(str(puntaje))
    exit()

# [2] Cargar partida.
elif decision_usuario_inicio == "2":

    N, M, tablero_sin_legos, tablero_con_numeros_y_legos = juego.cargar()

    while N == 0 and M == 0 and tablero_sin_legos == 0 and tablero_con_numeros_y_legos == 0:
        print("\nEsta partida no existe\n")
        nombre, decision_usuario_inicio, N, M = menu_de_inicio.decision_usuario_inicio()
        juego = Juego(nombre, N, M)

        if decision_usuario_inicio == "1":
            tablero_con_legos, tablero_sin_legos, tablero_con_numeros_y_legos = crear_tablero.crear_tablero(N, M)
            juego.tablero_a, juego.tablero_o = tablero_sin_legos, tablero_con_numeros_y_legos

            while decision_usuario_inicio == "1":
                decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N, M)
                juego.letra, juego.numero = letra, numero

                # Descubrir una baldosa.
                if decision_usuario_juego == "1":
                    turno = juego.turno()
                    ganador = juego.ganador()
                    puntaje = juego.puntaje()
                    if turno == False:
                        juego.guardar_ranking(str(puntaje))
                        exit()
                    if ganador == True:
                        juego.guardar_ranking(str(puntaje))
                        tablero.print_tablero(tablero_con_numeros_y_legos, True)
                        exit()

                # Guardar la partida.
                if decision_usuario_juego == "2":
                    juego.guardar()
                    puntaje = juego.puntaje()

                # Salir de la partida con guardar.
                if decision_usuario_juego == "3":
                    juego.guardar()
                    puntaje = juego.puntaje()
                    exit()

                # Salir de la partida sin guardar.
                if decision_usuario_juego == "4":
                    juego.guardar_ranking(str(puntaje))
                    exit()


        elif decision_usuario_inicio == "0":
            juego.guardar_ranking(str(puntaje))
            exit()

        elif decision_usuario_inicio == "3":
            print(juego.ver_ranking())
            exit()



    tablero.print_tablero(tablero_sin_legos, True)

    while N != 0 and M != 0 and tablero_sin_legos != 0 and tablero_con_numeros_y_legos != 0:

        decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N, M)
        juego.letra, juego.numero = letra, numero
        juego.tablero_a, juego.tablero_o = tablero_sin_legos, tablero_con_numeros_y_legos

        if decision_usuario_juego == "1":
            turno = juego.turno()
            ganador = juego.ganador()
            puntaje = juego.puntaje()
            if turno == False:
                juego.guardar_ranking(str(puntaje))
                exit()
            if ganador == True:
                tablero.print_tablero(tablero_con_numeros_y_legos, True)
                juego.guardar_ranking(str(puntaje))
                exit()
        elif decision_usuario_juego == "2":
            juego.guardar()
            puntaje = juego.puntaje()
        elif decision_usuario_juego == "3":
            juego.guardar()
            puntaje = juego.puntaje()
            exit()
        elif decision_usuario_juego == "4":
            juego.guardar_ranking(str(puntaje))
            exit()




# [3] Ver ranking.
elif decision_usuario_inicio == "3":
    print(juego.ver_ranking())
    exit()

# [4] Volver atrás.
else:
    pass
