import menu_de_inicio
import crear_tablero
import menu_de_juego
import turno
import os
import tablero

from  guardar_partida import Juego

nombre, decision_usuario_inicio, N, M = menu_de_inicio.decision_usuario_inicio()
juego = Juego(nombre, N, M)

### [1] Crear partida nueva
if decision_usuario_inicio == "1":
    tablero_con_legos, tablero_sin_legos, tablero_con_numeros_y_legos = crear_tablero.crear_tablero(N,M)
    juego.tablero_a, juego.tablero_o = tablero_sin_legos, tablero_con_numeros_y_legos


    while decision_usuario_inicio == "1":
        decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N,M)
        juego.letra, juego.numero = letra, numero

        ### Descubrir una baldosa
        if decision_usuario_juego == "1":
            celdas_descubiertas = juego.turno()
            #coordenada_1 = letras_posibles[letra]
            #coordenada_2 = numero
            #coordenadas = turno.Coordenadas(coordenada_1, coordenada_2)
            #coordenadas.turno(tablero_sin_legos, tablero_con_numeros_y_legos)

        ### Guardar la partida
        elif decision_usuario_juego == "2":
            juego.guardar()

            # guardar_partida.Guardar(nombre, tablero_sin_legos, tablero_con_numeros_y_legos).guardar_partida()

        ### Salir de la partida con guardar
        elif decision_usuario_juego == "3":
            juego.guardar()
            exit()


        ### Salir de la partida sin guardar
        elif decision_usuario_juego == "4":
            exit()




### [0] Salir
elif decision_usuario_inicio == "0":
    exit()


### [2] Cargar partida
elif decision_usuario_inicio == "2":
    N, M, tablero_sin_legos, tablero_con_numeros_y_legos = juego.cargar()
    print(tablero_sin_legos)
    tablero.print_tablero(tablero_sin_legos, True)
    tablero.print_tablero(tablero_con_numeros_y_legos, True)


    while decision_usuario_inicio == "2":
        decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N, M)
        if decision_usuario_juego == "1":
            celdas_descubiertas = juego.turno()
        elif decision_usuario_juego == "2":
            juego.guardar()
        elif decision_usuario_juego == "3":
            juego.guardar()
            exit()
        elif decision_usuario_juego == "4":
            exit()

### [3] Ver ranking
else:
    pass


