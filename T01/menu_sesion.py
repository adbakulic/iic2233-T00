import random
from itertools import chain
from piloto import Piloto
from vehiculos import Vehiculo, Automovil, Troncomovil, Bicicleta, Motocicleta
from collections import namedtuple, defaultdict
from parametros import *
from menu import Menu

class MenuSesion(Menu):

    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)

    def recibir_input(self):
        print("\nSeleccione una opción:\n[0] Regresar\n[1] Crear partida\n[2] Cargar partida")
        input_usuario = input("\nIngrese 0, 1 o 2: ")
        return input_usuario

    def validar_input(self, input_usuario, menu_sesion_o_tipo_vehiculo):
        if menu_sesion_o_tipo_vehiculo == "Menú de Sesión":
            while input_usuario not in ["0", "1", "2"]:
                print("\nOpción inválida")
                input_usuario = self.recibir_input()
            return input_usuario
        else:
            while input_usuario not in ["1", "2", "3", "4"]:
                print("\nOpción inválida")
                input_usuario = self.recibir_nombre("vehículo")
            return input_usuario

    def recibir_nombre(self, usuario_vehiculo):
        if usuario_vehiculo == "vehículo":
            print(f"\nSeleccoines una opción de {usuario_vehiculo}:\n[1] Automóvil\n"
                                      f"[2] Troncomóvil\n[3] Bicicleta\n[4] Motocicleta")
            tipo_vehiculo = input("\nIngrese 1, 2, 3 o 4: ")
            tipo_vehiculo = self.validar_input(tipo_vehiculo, "categoría del vehículo")
            nombre = input(f"\nIngrese un nombre de {usuario_vehiculo}: ")
            return tipo_vehiculo, nombre
        if usuario_vehiculo == "usuario":
            nombre = input(f"\nIngrese un nombre de {usuario_vehiculo}: ")
            return nombre

    def obtener_indice(self, ruta, nombre_header):
        with open(ruta, "r", encoding='utf=8') as archivo:
            header = archivo.readline()
            header = header.split(",")
            indice = 0
            while header[indice] != nombre_header and indice < len(header) - 1:
                indice += 1
        return indice

    def obtener_datos_archivo(self, ruta, name_tuple):
        dict_data = defaultdict(list)
        dict_dict_data = {}
        indice_nombre = self.obtener_indice(ruta, "Nombre")
        indice_dinero = self.obtener_indice(ruta, "Dinero")
        indice_personalidad = self.obtener_indice(ruta, "Personalidad")
        indice_contextura = self.obtener_indice(ruta, "Contextura")
        indice_equilibrio = self.obtener_indice(ruta, "Equilibrio")
        indice_experiencia = self.obtener_indice(ruta, "Experiencia")
        indice_equipo = self.obtener_indice(ruta, "Equipo")
        indice_motor_o_zapatillas = self.obtener_indice(PATHS['VEHICULOS'], "Motor o Zapatillas")
        with open(ruta, "r", encoding='utf-8') as archivo:
            header = archivo.readline()
            header = header.strip().split(",")
            if ruta == "vehículos.csv":
                header[indice_motor_o_zapatillas] = "Motor_o_Zapatillas"
            Datos = namedtuple(name_tuple, [*header])

            for linea in archivo:
                data = linea.strip().split(",")
                dict_data[data[indice_nombre]] = Datos(*data)
                dict_dict_data[data[indice_nombre]] = {"Dinero": data[indice_dinero],
                                                        "Personalidad": data[indice_personalidad],
                                                        "Contextura": data[indice_contextura],
                                                        "Equilibrio": data[indice_equilibrio],
                                                        "Experiencia": data[indice_experiencia],
                                                        "Equipo": data[indice_equipo]}
        return dict_data, dict_dict_data

    def validar_composicion_nombre(self, nombre):
        if " " in nombre:
            nombre_unido = nombre.split(" ")
            nombre_unido = "".join(nombre_unido)
            if nombre_unido.isalnum() == False:
                print("Nombre inválido")
                nombre = self.recibir_nombre("usuario")
                nombre = self.validar_composicion_nombre(nombre)
            else:
                nombre = nombre
            return nombre
        elif " " not in nombre:
            if nombre.isalnum() == False:
                print("Nombre inválido")
                nombre = self.recibir_nombre("usuario")
                nombre = self.validar_composicion_nombre(nombre)
            else:
                nombre = nombre
            return nombre

    def validar_existencia_nombre(self, usuario_vehiculo, nombre, ruta, name_tuple):
        # Parámetros: por_revisar--> si se quiere revisar que ya existe o su validez o ambos, usuario_vehiculos-->
                    # si el nombre es de usuario o de vehículo, nombre --> nombre que se quiere validar
        # ruta --> ruta del archivo para buscar si hay nombres repetidos, name_tuple --> nombre de la namedtumple

        ########################################################################################################################
        ############################################################# FALTA EL STR.ISALNUM #####################################
        ########################################################################################################################

        dict_piloto, list_piloto = self.obtener_datos_archivo(ruta, name_tuple)

        nombres_pilotos = set()
        for nombre_piloto in dict_piloto:
            nombres_pilotos.add(nombre_piloto)

        while nombre in nombres_pilotos:
            print("\nNombre existente")
            nombre = self.recibir_nombre(usuario_vehiculo)
        return nombre

    def validar_existencia_vehiculo(self, nuevo_vehiculo, piloto):
        while nuevo_vehiculo in piloto.vehiculos:
            print("Nombre inválido")
            nuevo_vehiculo = self.recibir_nombre("vehículo")
        return nuevo_vehiculo

    def elegir_equipo(self):
        dict_equipo = {"1": "Tareos", "2": "Híbridos", "3": "Docencios"}

        print("\nElija un equipo:\n[1] Tareos\n[2] Híbridos\n[3] Docencios")
        equipo = input("Ingrese 1, 2 o 3: ")

        while equipo not in ["1", "2", "3"]:
            print("\nOpción inválida")
            print("\nElija un equipo:\n[1] Tareos\n[2] Híbridos\n[3]Docencios")
            equipo = input("Ingrese 1, 2 o 3: ")

        return dict_equipo[equipo]

    def crear_partida(self):
        # Pedir NOMBRE --> UNICO y VALIDO
        # Pedir que elija EQUIPO
        # crear nueva ENTRADA en pilotos.csv --> llamar al menu PILOTO (características segun equipo)
        # asignar VEHICULO y NOMBRE --> UNICO y VALIDO
        # crear nueva ENTRADA en vehículos.csv --> llamar a VEHICULO (valores)

        nombre_usuario = self.recibir_nombre("usuario")
        nombre_usuario = self.validar_existencia_nombre("usuario", nombre_usuario, PATHS['PILOTOS'], "Piloto")
        equipo = self.elegir_equipo()

        # Crear entrada en pilotos.csv --> Nombre,Dinero,Personalidad,Contextura,Equilibrio,Experiencia,Equipo
        indice_nombre = self.obtener_indice(PATHS['PILOTOS'], "Nombre")
        indice_dinero = self.obtener_indice(PATHS['PILOTOS'], "Dinero")
        indice_personalidad = self.obtener_indice(PATHS['PILOTOS'], "Personalidad")
        indice_contextura = self.obtener_indice(PATHS['PILOTOS'], "Contextura")
        indice_equilibrio = self.obtener_indice(PATHS['PILOTOS'], "Equilibrio")
        indice_experiencia = self.obtener_indice(PATHS['PILOTOS'], "Experiencia")
        indice_equipo = self.obtener_indice(PATHS['PILOTOS'], "Equipo")

        piloto = Piloto(nombre_usuario, equipo)
        dinero_actual = piloto.obtener_dinero_actual()
        personalidad = piloto.obtener_personalidad()
        contextura = piloto.obtener_contextura()
        equilibrio = piloto.obtener_equilibrio()
        experiencia = piloto.obtener_experiencia()
        dict_indices_piloto = {indice_nombre: nombre_usuario, indice_dinero: dinero_actual, indice_personalidad: personalidad,
                        indice_contextura: contextura, indice_equilibrio: equilibrio,
                            indice_experiencia: experiencia, indice_equipo: equipo}
        with open(PATHS['PILOTOS'], "a", encoding='utf-8') as archivo:
            data_ordenada = list()
            contador = 0
            for indice in dict_indices_piloto:
                if indice == contador:
                    data_ordenada.append(str(dict_indices_piloto[indice]))
                    contador += 1
            nueva_entrada = ",".join(data_ordenada)
            archivo.write(nueva_entrada + "\n")

        tipo_vehiculo, nombre_vehiculo = self.recibir_nombre("vehículo")
        nombre_vehiculo = self.validar_existencia_vehiculo(nombre_vehiculo, piloto)
        nombre_vehiculo = piloto.agregar_vehiculo(nombre_vehiculo)
        #nombre_vehiculo = self.validar_existencia_nombre("vehículo", nombre_vehiculo, PATHS['VEHICULOS'], "Vehículo")

        # Crear entrada en vheículos.csv --> Nombre,Dueño,Categoría,Chasis,Carrocería,Ruedas,Motor o Zapatillas,Peso
        indice_nombre = self.obtener_indice(PATHS['VEHICULOS'], "Nombre")
        indice_dueno = self.obtener_indice(PATHS['VEHICULOS'], "Dueño")
        indice_categoria = self.obtener_indice(PATHS['VEHICULOS'], "Categoría")
        indice_chasis = self.obtener_indice(PATHS['VEHICULOS'], "Chasis")
        indice_carroceria = self.obtener_indice(PATHS['VEHICULOS'], "Carrocería")
        indice_ruedas = self.obtener_indice(PATHS['VEHICULOS'], "Ruedas")
        indice_motor_o_zapatillas = self.obtener_indice(PATHS['VEHICULOS'], "Motor o Zapatillas")
        indice_peso = self.obtener_indice(PATHS['VEHICULOS'], "Peso")

        dict_intancia = {"1": Automovil(nombre_vehiculo, AUTOMOVIL),
                         "2": Troncomovil(nombre_vehiculo, TRONCOMOVIL),
                         "3": Bicicleta(nombre_vehiculo, BICICLETA),
                         "4": Motocicleta(nombre_vehiculo, MOTOCICLETA)}
        dict_categoria = {"1": "automóvil", "2": "troncomóvil", "3": "bicicleta", "4": "motocicleta"}
        vehiculo = dict_intancia[tipo_vehiculo]
        dueno = nombre_usuario
        categoria = dict_categoria[tipo_vehiculo]
        chasis = vehiculo.obtener_chasis()
        carroceria = vehiculo.obtener_carroceria()
        ruedas = vehiculo.obtener_ruedas()
        motor_o_zapatillas = vehiculo.obtener_motor_zapatillas()
        peso = vehiculo.obtener_peso()
        dict_indices_vehiculo = {indice_nombre: nombre_vehiculo, indice_dueno: dueno, indice_categoria: categoria,
                        indice_chasis: chasis, indice_carroceria: carroceria,
                        indice_ruedas: ruedas, indice_motor_o_zapatillas: motor_o_zapatillas,
                        indice_peso: peso}
        with open(PATHS['VEHICULOS'], "a", encoding='utf-8') as archivo:
            data_ordenada = list()
            contador = 0
            for indice in dict_indices_vehiculo:
                if indice == contador:
                    data_ordenada.append(str(dict_indices_vehiculo[indice]))
                    contador += 1
            nueva_entrada = ",".join(data_ordenada)
            archivo.write(nueva_entrada + "\n")

        return nombre_usuario, equipo

    def cargar_partida(self):
        # Pedir NOMBRE --> VALIDO (acceder a la info por el nombre --> difaultdict?)
        # Comprobar si existe nombre:
           # Si no existe: avisar, pedir nuevo nombre, dar opción de volver al menu anterior  ¿¿¿¿¿¿¿¿¿??????????

        nombre = self.recibir_nombre("usuario")
        nombre = self.validar_composicion_nombre(nombre)

        dict_pilotos, list_pilotos = self.obtener_datos_archivo(PATHS['PILOTOS'], "Piloto")
        print("Cargando sus datos...")

        if nombre not in dict_pilotos:
            print("Nombre no existente")
            nombre = self.recibir_nombre("usuario")
            nombre = self.validar_composicion_nombre(nombre)
            print("¿Desea regresar?:\n[0] Regresar\n[1] No regresar")
            while True:
                input_regresar = input("Ingrese 0 o 1: ")
                if input_regresar not in ["0", "1"]:
                    print("Opción inválida")
                else:
                    break
            if input_regresar == "0":
                menu_sesion = MenuSesion("Menú de Sesión")
                input_usuario = menu_sesion.recibir_input()
                input_usuario = menu_sesion.validar_input(input_usuario, "Menú de Sesión")
                if input_usuario == "1":
                    nombre_usuario, equipo = menu_sesion.crear_partida()
                elif input_usuario == "2":
                    menu_sesion.cargar_partida()

            elif input_regresar == "1":
                print("Cargando sus datos...")

class MenuCompraVehiculo(Menu):
    # Mostrar dinero_actual
    # Mostrar vehiculos disponibles para ser comprados con sus respectivos precios
    # opciones:
       # comprar uno de los vehiculos --> asignar NOMBRE UNICO (puede tener muchos vehiculos del mismo tipo)
       # regresar al MenuInicio  ¿¿¿¿¿¿¿¿¿¿¿MenuPrincipal???????????

    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)
        pass

    def mostrar_dinero_actual(self):
        pass

    def mostrar_vehiculos_y_precios(self):
        pass

    def comprar_vehiculo(self):
        pass

    def regresar(self):
        pass

class MenuPreparacionCarrera(Menu):
    # Usuario debe seleccionar PISTA
    # Elegir entre sus VEHICULOS
    # Mostrar MenuCarrera

    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)
        pass

    def seleccionar_pista(self):
        pass

    def elegir_vehiculo(self):
        pass

class MenuCarrera(Menu):
    # MOSTRAR una vez iniciada una carrera y al completar cada vuelta
    # Al completar una vuelta dar opcion de entrar a los PITS:
        # Sí --> MOSTRAR MenuPits
        # No --> Continuar carrera
    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)
        pass

    def entrar_pits(self):
        pass

    def continuar_carrera(self):
        pass

class MenuPits(Menu):
    # MOSTRAR dinero_actual
    # Dar la opción de MEJORAR partes del vehiculo y precios (yo decido si solo se puede mejorar 1 o las que alcance con su dinero_actual)
    # Opcion de VOLVER a la carrera

    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)
        pass

    def mostrar_dinero_actual(self):
        pass

    def mostrar_piezas_mejorables_y_precios(self):
        pass

    def volver_a_carrera(self):
        pass

