import random
import parametros
import math
import tablero

# Función retorna 3 lista de listas: solo de espacios, de espacios y L, de números y L

def crear_tablero(N,M):
    # N: largo tablero (filas)
    # M: ancho tablero (columnas)

    cantidad_celdas = int(N) * int(M)
    cantidad_legos = math.ceil(int(N) * int(M) * parametros.PROB_LEGO)

    lista_de_legos_y_espacios = []
    indice = 0
    while indice < cantidad_legos:
        lista_de_legos_y_espacios.append("L")
        indice += 1

    indice = 0
    while indice < (cantidad_celdas - cantidad_legos):
        lista_de_legos_y_espacios.append(" ")
        indice +=1


    random.shuffle(lista_de_legos_y_espacios)

    lista_de_espacios = []
    for indice in lista_de_legos_y_espacios:
        if indice == "L":
            lista_de_espacios.append(" ")
        else:
            lista_de_espacios.append(" ")


### Lista de listas de espacios y L

    tablero_con_legos = []
    i = 0
    while i < (int(N) * int(M)):
        tablero_con_legos.append(lista_de_legos_y_espacios[i:i + int(M)])
        i += int(M)


### Lista de listas de solo espacios

    tablero_sin_legos = []
    i = 0
    while i < (int(N) * int(M)):
        tablero_sin_legos.append(lista_de_espacios[i:i + int(M)])
        i += int(M)


### Cuántos legos hay alrededor de cada baldosa, exceptuando las baldosas que tienen un lego
    lista_con_numeros_y_legos = []

    i = 0
    for i in range(int(N)):
        j = 0
        for j in range(int(M)):
            #esquina superioir izquierda:
            if i == 0 and j  == 0:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #esquina superior derecha:
            if i == 0 and j == int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #esquina inferior izquierda:
            if i == int(N) - 1 and j == 0:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #esquina inferior derecha:
            if i == int(N) - 1 and j == int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #barra lateral izquierda:
            if i != 0 and i != int(N) - 1 and j == 0:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #barra lateral derecha:
            if i != 0 and i != int(N) - 1 and j == int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #barra superior:
            if i == 0 and j != 0 and j != int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #barra inferior:
            if i == int(N) - 1 and j != 0 and j != int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            #centro sin bordes:
            if i != 0 and i != int(N) - 1 and j != 0 and j != int(M) - 1:
                legos_alrededor = 0
                if tablero_con_legos[i][j] == " ":
                    if tablero_con_legos[i - 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i - 1][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i][j + 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j - 1] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j] == "L":
                        legos_alrededor += 1
                    if tablero_con_legos[i + 1][j + 1] == "L":
                        legos_alrededor += 1
                    else:
                        legos_alrededor = legos_alrededor

                    lista_con_numeros_y_legos.append(str(legos_alrededor))
                else:
                    lista_con_numeros_y_legos.append("L")

            j += 1
        i += 1


### Lista de listas con los números y L correspondientes

    tablero_con_numeros_y_legos = []
    i = 0
    while i < (int(N) * int(M)):
        tablero_con_numeros_y_legos.append(lista_con_numeros_y_legos[i:i + int(M)])
        i += int(M)


    tablero.print_tablero(tablero_sin_legos, True)

    return tablero_con_legos, tablero_sin_legos, tablero_con_numeros_y_legos














