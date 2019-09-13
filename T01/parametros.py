import random
# Valores máximos y mínimos de las partes y el peso de los vehículos

AUTOMOVIL = {
    'CHASIS': {
        'MIN': (-1),
        'MAX': 101
    },
    'CARROCERIA': {
        'MIN': (-1),
        'MAX': 201
    },
    'RUEDAS': {
        'MIN': 49,
        'MAX': 301
    },
    'MOTOR': {
        'MIN': 99,
        'MAX': 501
    },
    'ZAPATILLAS': {
        'MIN': (-1),
        'MAX': 1
    },
    'PESO': {
        'MIN': 999,
        'MAX': 5001
    }
}

TRONCOMOVIL = {
    'CHASIS': {
        'MIN': (-1),
        'MAX': 51
    },
    'CARROCERIA': {
        'MIN': (-1),
        'MAX': 101
    },
    'RUEDAS': {
        'MIN': 49,
        'MAX': 101
    },
    'MOTOR': {
        'MIN': (-1),
        'MAX': 1
    },
    'ZAPATILLAS': {
        'MIN': 69,
        'MAX': 101
    },
    'PESO': {
        'MIN': 1999,
        'MAX': 7001
    }
}

MOTOCICLETA = {
    'CHASIS': {
        'MIN': (-1),
        'MAX': 81
    },
    'CARROCERIA': {
        'MIN': (-1),
        'MAX': 151
    },
    'RUEDAS': {
        'MIN': 49,
        'MAX': 201
    },
    'MOTOR': {
        'MIN': 89,
        'MAX': 451
    },
    'ZAPATILLAS': {
        'MIN': (-1),
        'MAX': 1
    },
    'PESO': {
        'MIN': 499,
        'MAX': 1001
    }
}

BICICLETA = {
    'CHASIS': {
        'MIN': (-1),
        'MAX': 71
    },
    'CARROCERIA': {
        'MIN': (-1),
        'MAX': 101
    },
    'RUEDAS': {
        'MIN': 19,
        'MAX': 71
    },
    'MOTOR': {
        'MIN': (-1),
        'MAX': 1
    },
    'ZAPATILLAS': {
        'MIN': 49,
        'MAX': 91
    },
    'PESO': {
        'MIN': 199,
        'MAX': 501
    }
}


# Mejoras de las partes de los vehículos

MEJORAS = {
    'CHASIS': {
        'COSTO': 800,
        'EFECTO': 2
    },
    'CARROCERIA': {
        'COSTO': 500,
        'EFECTO': 4
    },
    'RUEDAS': {
        'COSTO': 500,
        'EFECTO': 4
    },
    'MOTOR': {
        'COSTO': 300,
        'EFECTO': 3
    },
    'ZAPATILLAS': {
        'COSTO': 300,
        'EFECTO': 3
    }
}


# Características de los pilotos de los diferentes equipos

EQUIPOS = {
    'TAREOS': {
        'CONTEXTURA': {
            'MIN': 26,
            'MAX': 45
        },
        'EQUILIBRIO': {
            'MIN': 36,
            'MAX': 55
        },
        'PERSONALIDAD': "precavido"
    },
    'HIBRIDOS': {
        'CONTEXTURA': {
            'MIN': 35,
            'MAX': 54
        },
        'EQUILIBRIO': {
            'MIN': 20,
            'MAX': 38
        },
        'PERSONALIDAD': random.choice(["precavido", "osado"])
    },
    'DOCENCIOS': {
        'CONTEXTURA': {
            'MIN': 44,
            'MAX': 60
        },
        'EQUILIBRIO': {
            'MIN': 4,
            'MAX': 10
        },
        'PERSONALIDAD': "osado"
    }
}


# Las constantes de las formulas

# Velocidad real
VELOCIDAD_MINIMA = None

# Velocidad intencional
EFECTO_OSADO = None
EFECTO_PRECAVIDO = None

# Dificultad de control del vehículo
PESO_MEDIO = None
EQUILIBRIO_PRECAVIDO = None

# Tiempo pits
TIEMPO_MINIMO_PITS = None
VELOCIDAD_PITS = None

# Experiencia por ganar
BONIFICACION_PRECAVIDO = None
BONIFICACION_OSADO = None


# Paths de los archivos

PATHS = {
    'PISTAS': "pistas.csv",
    'CONTRINCANTES': "contrincantes.csv",
    'PILOTOS': "pilotos.csv",
    'VEHICULOS': "vehículos.csv",
}


# Power-ups

# Caparazon
DMG_CAPARAZON = None

# Relámpago
SPD_RELAMPAGO = None
