from menu import Menu
from piloto import Piloto
from menu_sesion import MenuSesion
from parametros import *

class MenuPrincipal(Menu):
    def __init__(self, nombre_menu):
        super().__init__(nombre_menu)

    def recibir_input(self):
        print("\nSeleccione una opción:\n[0] Salir del programa\n[1] Comprar nuevo vehículo\n"
              "[2] Iniciar carrera\n[3] Guardar partida")
        input_usuario = input("\nIngrese 0, 1, 2 o 3: ")
        return input_usuario

    def validar_input(self, input_usuario, menu):
        while input_usuario not in ["0", "1", "2", "3"]:
            print("\nOpción inválida")
            input_usuario = self.recibir_input()
        return input_usuario

    def comprar_nuevos_vehiculos(self):
        # mostrar MenuCompraVehiculo
        pass

    def iniciar_carrera(self):
        # mostrar MenuPreparacionCarrera
        pass

    def guardar_partida(self, nombre_piloto, equipo):
        # Cambiar valores en pilotos.csv --> ACTUALIZAR (escribir archivo con "a")
        # Cambiar valores en vehiculos.csv --> ACTUALIZAR (escribir archivo con "a")
        # respetar mayusculas y minusculas
        menus_sesion = MenuSesion("Menú Principal/Guardar Partida")
        dict_pilotos, dict_dict_pilotos = menus_sesion.obtener_datos_archivo(PATHS['PILOTOS'], "Piloto")
        print(dict_dict_pilotos)
        piloto = Piloto(nombre_piloto, equipo)
        piloto.dinero_actual = '300'
        dict_dict_pilotos[nombre_piloto]["Dinero"] =  piloto.dinero_actual
        print(dict_dict_pilotos)
        dict_dict_pilotos[nombre_piloto]["Personalidad"] = piloto.personalidad
        dict_dict_pilotos[nombre_piloto]["Contextura"] = piloto.contextura
        dict_dict_pilotos[nombre_piloto]["Equilibrio"] = piloto.equilibrio
        dict_dict_pilotos[nombre_piloto]["Experiencia"] = piloto.experiencia
        dict_dict_pilotos[nombre_piloto]["Equipo"] = piloto.equipo
        with open (PATHS['PILOTOS'], "w", encoding='utf-8') as archivo:
            for usuario in dict_dict_pilotos:
                print(usuario)
                print(dict_dict_pilotos[usuario]["Dinero"])
