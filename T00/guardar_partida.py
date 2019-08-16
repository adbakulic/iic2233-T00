import os
import tablero
import string


class Juego:

    def __init__(self, nombre, N, M, tablero_a=None, tablero_o=None, letra=None, numero=None):
        self.nombre = nombre
        self.N = N
        self.M = M
        self.tablero_a = tablero_a
        self.tablero_o = tablero_o
        self.letra = letra
        self.numero = numero

    def guardar(self):

        if not os.path.isdir("partidas"):
            os.mkdir("partidas")

        nombre_archivo = os.path.join("partidas", self.nombre + ".txt")

        archivo = open(nombre_archivo, "w")
        archivo.write(str(self.N) + "\n")
        archivo.write(str(self.M) + "\n")

        for i in self.tablero_a:
            linea_sin_legos = ",".join(i) + "\n"
            archivo.write(linea_sin_legos)

        for i in self.tablero_o:
            linea_con_numeros_y_legos = ",".join(i) + "\n"
            archivo.write(linea_con_numeros_y_legos)

        archivo.close()


    def turno(self):
        letras_minusculas, letras_mayusculas = string.ascii_letters[0:15], string.ascii_letters[26:41]
        letras_posibles = {l: n for l, n in zip(letras_minusculas, range(0, 16))}
        mayusculas = {l: n for l, n in zip(letras_mayusculas, range(0, 16))}
        letras_posibles.update(mayusculas)
        letra_convertida = letras_posibles[self.letra]
        celdas_descubiertas = 0

        if self.tablero_a[self.numero][letra_convertida] == "L":
            print("Haz perdido")
            tablero.print_tablero(self.tablero_o, True)
            exit()

        else:
            self.tablero_a[self.numero][letra_convertida] = self.tablero_o[self.numero][letra_convertida]
            tablero.print_tablero(self.tablero_a, True)
            celdas_descubiertas += 1

        return celdas_descubiertas


    def cargar(self):
        nombre_archivo = os.path.join("partidas", self.nombre + ".txt")

        with open(nombre_archivo, "r") as archivo:

            lista_lineas = []
            for linea in archivo:
                linea = linea.strip()
                linea = linea.split(",")
                lista_lineas.append(linea)

            self.N = lista_lineas.pop(0)[0]
            self.M = lista_lineas.pop(0)[0]

            lista_a = lista_lineas[: int(self.N)]
            lista_o = lista_lineas[int(self.N) : int(self.N) * 2]



            return self.N, self.M, lista_a, lista_o






