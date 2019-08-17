import os
import tablero
import string
import parametros
import math


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

        if self.tablero_o[self.numero][letra_convertida] == "L":
            print("Haz perdido")
            tablero.print_tablero(self.tablero_o, True)

            os.remove(os.path.join("partidas", self.nombre + ".txt"))

            return False

        else:
            self.tablero_a[self.numero][letra_convertida] = self.tablero_o[self.numero][letra_convertida]
            tablero.print_tablero(self.tablero_a, True)

            return True

    def puntaje(self):
        celdas_descubiertas = 0
        legos = 0
        i = 0
        while i < (int(self.N)):
            j = 0
            while j < (int(self.M)):
                if self.tablero_a[i][j] != " ":
                    celdas_descubiertas += 1
                if self.tablero_o[i][j] == "L":
                    legos += 1
                    j += 1
                else:
                    j += 1
            i += 1


        return celdas_descubiertas * legos * parametros.POND_PUNT

    def cargar(self):
        nombre_archivo = os.path.join("partidas", self.nombre + ".txt")

        if not os.path.isfile(nombre_archivo):
            return 0, 0, 0, 0

        else:
            with open(nombre_archivo, "r") as archivo:

                lista_lineas = []
                for linea in archivo:
                    linea = linea.strip("\n")
                    linea = linea.split(",")
                    lista_lineas.append(linea)

                self.N = lista_lineas.pop(0)[0]
                self.M = lista_lineas.pop(0)[0]

                lista_a = lista_lineas[: int(self.N)]
                lista_o = lista_lineas[int(self.N) : int(self.N) * 2]

                return self.N, self.M, lista_a, lista_o


    def guardar_ranking(self, puntaje):
        with open("puntajes.txt", "a") as archivo:
            archivo.write(self.nombre + "," + puntaje + "\n")

    def ver_ranking(self):
        lista_rankings = []
        with open("puntajes.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip("\n")
                linea = linea.split(",")
                lista_rankings.append(linea)

        lista_rankings_sin_usuario = []
        for i in range(len(lista_rankings)):
            lista_rankings_sin_usuario.append(int(lista_rankings[i][1]))


        lista_rankings_sin_usuario.sort(reverse=True)

        return lista_rankings_sin_usuario[:10]

    def ganador(self):
        contador = 0
        for i in range(len(self.tablero_o)):
            for j in range(len(self.tablero_o)):
                if self.tablero_o[i][j] != "L":
                    if self.tablero_a[i][j] == self.tablero_o[i][j]:
                        contador += 1
                        j += 1
                    else:
                        j += 1
            i += 1

        if contador == int(self.N) * int(self.M) - (math.ceil(int(self.N) * int(self.M) * parametros.PROB_LEGO)):
            print("¡Felicitaciones!" + "\n" + "Haz ganado el juego")
            return True
        elif contador != int(self.N) * int(self.M) - (math.ceil(int(self.N) * int(self.M) * parametros.PROB_LEGO)):
            return False


