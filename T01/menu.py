from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self, nombre_menu):
        self.nombre_menu = nombre_menu
        print(f"\nEstás en el {self.nombre_menu}")

    @abstractmethod
    def recibir_input(self):
        pass

    @abstractmethod
    def validar_input(self, input, menu_sesion_o_categoria_vehiculo):
        pass