from colorama import Fore, init, Style
init(autoreset=True)
import funciones_SQL
from datetime import datetime


#main

#extra = []
generos = ["Terror", "Comedia", "Romance", "Fantasia", "Drama", "Accion", "Ciencia ficcion", "Infantil", "Documental"]
idiomas = ["Español españa", "Español latinoamerica", "Ingles", "Aleman", "Frances"]
plataformas =["Hbo", "Netflix", "Prime video", "Paramount", "Disney"]
#Bienvenido
fecha_hora_actual = datetime.now()
print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}{fecha_hora_actual}")
print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}BIENVENIDO")
funciones_SQL.mostrar_menu()
opcion = funciones_SQL.comprobar_opcion()

while opcion != 8:
    match opcion:
        case 1: #✅
            funciones_SQL.cargar_producto(generos, plataformas, idiomas)
        case 2:
            funciones_SQL.menu_busqueda()
            opcion_busqueda = funciones_SQL.comprobar_opcion()
            match opcion_busqueda:
                case 1: 
                    funciones_SQL.buscar_por_nombre_SQL()
                case 2:
                    funciones_SQL.buscar_por_genero_SQL()
                case _:
                    print(f"{Fore.RED}Opcion erronea")
        case 3: #✅
            funciones_SQL.menu_ver()
            opcion_ver = funciones_SQL.comprobar_opcion()
            match opcion_ver:
                case 1:
                    funciones_SQL.ver_productos_SQL()
                case 2:
                    funciones_SQL.ver_productos_nombre()
                case 3:
                    funciones_SQL.ver_productos_plataforma()
                case 4:
                    funciones_SQL.ver_productos_precio()
                case _:
                    print(f"{Fore.RED}Opcion erronea")
        case 4:
            existe, id_elegido = funciones_SQL.modificar_producto_SQL()
            if existe:
                opcion_modificar = funciones_SQL.comprobar_opcion()
                match opcion_modificar:
                    case 1:
                        funciones_SQL.modificar_genero(id_elegido, generos)
                    case 2:
                        funciones_SQL.modificar_nombre(id_elegido)
                    case 3:
                        funciones_SQL.modificar_plataforma(id_elegido, plataformas)
                    case 4:
                        funciones_SQL.modificar_idioma(id_elegido, idiomas)
                    case _:
                        print(f"{Fore.RED}Opcion erronea")
        case 5: #✅
            funciones_SQL.eliminar_producto_SQL()
        case 6: #✅
            funciones_SQL.vaciar_productos_SQL()
        case 7:
            funciones_SQL.cantidad_peliculas_SQL()
        case _: 
            print(f"{Fore.RED}Opcion erronea")
    funciones_SQL.mostrar_menu()
    opcion = funciones_SQL.comprobar_opcion()


print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Gracias por usar este programa")