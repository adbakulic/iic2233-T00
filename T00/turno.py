# En cada turno, el jugador debe ingresar coordenadas que indiquen la casilla que quiere despejar
import tablero
import os

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




class Guardar:

    def __init__(self, nombre_usuario, tablero_actual, tablero_original_completo):
        self.nombre_usuario = nombre_usuario
        self.tablero_actual = tablero_actual
        self.tablero_original_completo = tablero_original_completo

    def guardar_partida(self):

        if not os.path.isdir("partidas"):
            os.mkdir("partidas")

        nombre_archivo = os.path.join("partidas", self.nombre_usuario + ".txt")

        archivo = open(nombre_archivo, "w")

        for i in range(len(self.tablero_actual)):
            linea_sin_legos = " ".join(str(self.tablero_actual[i])) + "\n"
            archivo.write(linea_sin_legos)

        for i in range(len(self.tablero_original_completo)):
            linea_con_numeros_y_legos = " ".join(str(self.tablero_original_completo[i])) + "\n"
            archivo.write(linea_con_numeros_y_legos)

        archivo.close()