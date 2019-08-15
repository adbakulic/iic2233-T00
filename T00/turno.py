# En cada turno, el jugador debe ingresar coordenadas que indiquen la casilla que quiere despejar
import tablero

class Coordenadas:

    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero

    def turno(self, tablero_sin_legos, tablero_con_numeros_y_legos):
        coordenada_1 = self.numero
        coordenada_2 = self.letra

        if tablero_con_numeros_y_legos[coordenada_1][coordenada_2] == "L":
            print("Haz perdido")
            tablero.print_tablero(tablero_con_numeros_y_legos, True)
            exit()
        else:
            tablero_sin_legos[coordenada_1][coordenada_2] = tablero_con_numeros_y_legos[coordenada_1][coordenada_2]
            tablero.print_tablero(tablero_sin_legos, True)




