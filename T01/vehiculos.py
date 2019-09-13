from parametros import *

class Vehiculo():
    def __init__(self, nombre_vehiculo, tipo_vehiculo):
        self.nombre = nombre_vehiculo
        self.tipo_vehiculo = tipo_vehiculo
        self.chasis = 0
        self.carroceria = 0
        self.ruedas = 0
        self.peso = 0



    def obtener_chasis(self):
        inferior = self.tipo_vehiculo['CHASIS']['MIN'] + 1
        superior = self.tipo_vehiculo['CHASIS']['MAX'] - 1
        self.chasis = random.randint(inferior, superior)
        return self.chasis

    def obtener_carroceria(self):
        inferior = self.tipo_vehiculo['CARROCERIA']['MIN'] + 1
        superior = self.tipo_vehiculo['CARROCERIA']['MAX'] - 1
        self.carroceria = random.randint(inferior, superior)
        return self.carroceria

    def obtener_ruedas(self):
        inferior = self.tipo_vehiculo['RUEDAS']['MIN'] + 1
        superior = self.tipo_vehiculo['RUEDAS']['MAX'] - 1
        self.ruedas = random.randint(inferior, superior)
        return self.ruedas

    def obtener_peso(self):
        inferior = self.tipo_vehiculo['PESO']['MIN'] + 1
        superior = self.tipo_vehiculo['PESO']['MAX'] - 1
        self.peso = random.randint(inferior, superior)
        return self.peso

class Automovil(Vehiculo):
    def __init__(self, nombre_vehiculo, tipo_vehiculo):
        super().__init__(nombre_vehiculo, tipo_vehiculo)
        self.motor = 0

    def obtener_motor_zapatillas(self):
        inferior = self.tipo_vehiculo['MOTOR']['MIN'] + 1
        superior = self.tipo_vehiculo['MOTOR']['MAX'] - 1
        self.motor = random.randint(inferior, superior)
        return self.motor

class Troncomovil(Vehiculo):
    def __init__(self, nombre_vehiculo, tipo_vehiculo):
        super().__init__(nombre_vehiculo, tipo_vehiculo)
        self.zapatillas = 0

    def obtener_motor_zapatillas(self):
        inferior = self.tipo_vehiculo['ZAPATILLAS']['MIN'] + 1
        superior = self.tipo_vehiculo['ZAPATILLAS']['MAX'] - 1
        self.zapatillas = random.randint(inferior, superior)
        return self.zapatillas

class Bicicleta(Vehiculo):
    def __init__(self, nombre_vehiculo, tipo_vehiculo):
        super().__init__(nombre_vehiculo, tipo_vehiculo)
        self.zapatillas = 0

    def obtener_motor_zapatillas(self):
        inferior = self.tipo_vehiculo['ZAPATILLAS']['MIN'] + 1
        superior = self.tipo_vehiculo['ZAPATILLAS']['MAX'] - 1
        self.zapatillas = random.randint(inferior, superior)
        return self.zapatillas

class Motocicleta(Vehiculo):
    def __init__(self, nombre_vehiculo, tipo_vehiculo):
        super().__init__(nombre_vehiculo, tipo_vehiculo)
        self.motor = 0

    def obtener_motor_zapatillas(self):
        inferior = self.tipo_vehiculo['MOTOR']['MIN'] + 1
        superior = self.tipo_vehiculo['MOTOR']['MAX'] - 1
        self.motor = random.randint(inferior, superior)
        return self.motor


