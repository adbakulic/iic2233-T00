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

        for i in range(len(self.tablero_a)):
            linea_sin_legos = " ".join(str(self.tablero_a[i])) + "\n"
            archivo.write(linea_sin_legos)

        for i in range(len(self.tablero_o)):
            linea_con_numeros_y_legos = " ".join(str(self.tablero_o[i])) + "\n"
            archivo.write(linea_con_numeros_y_legos)

        archivo.close()


    def turno(self):
        letras_minusculas, letras_mayusculas = string.ascii_letters[0:15], string.ascii_letters[26:41]
        letras_posibles = {l: n for l, n in zip(letras_minusculas, range(0, 16))}
        mayusculas = {l: n for l, n in zip(letras_mayusculas, range(0, 16))}
        letras_posibles.update(mayusculas)
        letra_convertida = letras_posibles[self.letra]

        if self.tablero_a[self.numero][letra_convertida] == "L":
            print("Haz perdido")
            tablero.print_tablero(self.tablero_o, True)
            exit()
        else:
            self.tablero_a[self.numero][letra_convertida] = self.tablero_o[self.numero][letra_convertida]
            tablero.print_tablero(self.tablero_a, True)


    def cargar(self):
        nombre_archivo = os.path.join("partidas", self.nombre + ".txt")

        #archivo = open(nombre_archivo, "r")
        #self.N = archivo.readline()
        #tablero_a = []
        #tablero_o = []
        #for linea in archivo:
            #linea = linea.strip()
        #archivo.close()

        #return tablero_a, tablero_o


        with open(nombre_archivo, "r") as archivo:

            lista_lineas = []
            for linea in archivo:
                linea = linea.strip()
                linea = linea.split("\n")
                lista_lineas.append(linea)
            print(lista_lineas)

            self.N = lista_lineas.pop(0)

