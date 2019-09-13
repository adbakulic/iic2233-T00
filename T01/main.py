from menu_sesion import MenuSesion
from menu_principal import MenuPrincipal

while True:
    menu_sesion = MenuSesion("Menú de Sesión")
    input_sesion = menu_sesion.recibir_input()
    input_sesion = menu_sesion.validar_input(input_sesion, "Menú de Sesión")

    nombre_sesion = ""
    equipo = ""
    if input_sesion == "1":
        nombre_sesion, equipo = menu_sesion.crear_partida()
    elif input_sesion == "2":
        menu_sesion.cargar_partida()
    elif input_sesion == "0":
        continue

    menu_principal = MenuPrincipal("Menú Principal")
    input_usuario_principal = menu_principal.recibir_input()
    input_principal = menu_principal.validar_input(input_usuario_principal, "Menú Principal")

    if input_principal == "3":
        menu_principal.guardar_partida(nombre_sesion, equipo)

    elif input_principal == "0":
        exit()
