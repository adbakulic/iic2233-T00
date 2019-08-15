import menu_de_inicio
import crear_tablero
import menu_de_juego
import turno
import os
import guardar_partida

nombre, decision_usuario_inicio, N, M = menu_de_inicio.decision_usuario_inicio()

### [1] Crear partida nueva
if decision_usuario_inicio == "1":
    tablero_con_legos, tablero_sin_legos, tablero_con_numeros_y_legos = crear_tablero.crear_tablero(N,M)


    while decision_usuario_inicio == "1":
        decision_usuario_juego, letra, numero, letras_posibles = menu_de_juego.menu_de_juego(N,M)

        ### Descubrir una baldosa
        if decision_usuario_juego == "1":
            coordenada_1 = letras_posibles[letra]
            coordenada_2 = numero
            coordenadas = turno.Coordenadas(coordenada_1, coordenada_2)
            coordenadas.turno(tablero_sin_legos, tablero_con_numeros_y_legos)

        ### Guardar la partida
        if decision_usuario_juego == "2":
            guardar_partida.Guardar(nombre, tablero_sin_legos, tablero_con_numeros_y_legos).guardar_partida()

        ### Salir de la partida con guardar
        if decision_usuario_juego == "3":
            pass


        ### Salir de la partida sin guardar
        if decision_usuario_juego == "4":
            exit()




### [0] Salir
elif decision_usuario_inicio == "0":
    exit()


### [2] Cargar partida
elif decision_usuario_inicio == "2":
    print("Hola")


### [3] Ver ranking
else:
    pass

