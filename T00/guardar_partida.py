import os

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

        archivo.write("Tablero actual:\n")
        for i in range(len(self.tablero_actual)):
            linea_sin_legos = " ".join(str(self.tablero_actual[i])) + "\n"
            archivo.write(linea_sin_legos)


        archivo.write("\nTablero original completo:\n")
        for i in range(len(self.tablero_original_completo)):
            linea_con_numeros_y_legos = " ".join(str(self.tablero_original_completo[i])) + "\n"
            archivo.write(linea_con_numeros_y_legos)

        archivo.close()


