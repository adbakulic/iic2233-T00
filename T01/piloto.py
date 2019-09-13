from parametros import *
from collections import defaultdict

class Piloto:
    def __init__(self, nombre_usuario, equipo):
        self.nombre = nombre_usuario
        self.dinero_actual = 0
        self.personalidad = ""
        self.contextura = 0
        self.equilibrio = 0
        self.experiencia = 0
        self.equipo = equipo
        self.vehiculos = []

    def agregar_vehiculo(self, nuevo_vehiculo):
        if nuevo_vehiculo in self.vehiculos:
            self.vehiculos.append(nuevo_vehiculo)
        else:
            self.vehiculos.append(nuevo_vehiculo)
        return nuevo_vehiculo

    def obtener_dinero_actual(self):
        return self.dinero_actual

    def obtener_personalidad(self):
        if self.equipo == "Tareos":
            self.personalidad = EQUIPOS['TAREOS']['PERSONALIDAD']
        elif self.equipo == "Híbridos":
            self.personalidad = EQUIPOS['HIBRIDOS']['PERSONALIDAD']
        else:
            self.personalidad = EQUIPOS['DOCENCIOS']['PERSONALIDAD']
        return self.personalidad

    def obtener_contextura(self):
        if self.equipo == "Tareos":
            inferior = EQUIPOS['TAREOS']['CONTEXTURA']['MIN'] + 1
            superior = EQUIPOS['TAREOS']['CONTEXTURA']['MAX'] - 1
            self.contextura = random.randint(inferior, superior )
        elif self.equipo == "Híbridos":
            inferior = EQUIPOS['HIBRIDOS']['CONTEXTURA']['MIN'] + 1
            superior = EQUIPOS['HIBRIDOS']['CONTEXTURA']['MAX'] - 1
            self.contextura = random.randint(inferior, superior)
        else:
            inferior = EQUIPOS['DOCENCIOS']['CONTEXTURA']['MIN'] + 1
            superior = EQUIPOS['DOCENCIOS']['CONTEXTURA']['MAX'] - 1
            self.contextura = random.randint(inferior, superior)
        return self.contextura

    def obtener_equilibrio(self):
        if self.equipo == "Tareos":
            inferior = EQUIPOS['TAREOS']['EQUILIBRIO']['MIN'] + 1
            superior = EQUIPOS['TAREOS']['EQUILIBRIO']['MAX'] - 1
            self.equilibrio = random.randint(inferior, superior )
        elif self.equipo == "Híbridos":
            inferior = EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MIN'] + 1
            superior = EQUIPOS['HIBRIDOS']['EQUILIBRIO']['MAX'] - 1
            self.equilibrio = random.randint(inferior, superior)
        else:
            inferior = EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN'] + 1
            superior = EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MAX'] - 1
            self.equilibrio = random.randint(inferior, superior)
        return self.equilibrio

    def obtener_experiencia(self):
        return self.experiencia


print(EQUIPOS['DOCENCIOS']['EQUILIBRIO']['MIN'])