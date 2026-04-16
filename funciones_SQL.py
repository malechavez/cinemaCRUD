from colorama import Fore, init, Style
import json
import sqlite3
import datetime
init(autoreset=True)

try:
    conexion = sqlite3.connect("cinema.db")
    print("Conexion establecida")

    cursor = conexion.cursor()

    #crear tabla
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS peliculas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        genero TEXT NOT NULL,
                        precio FLOAT,
                        plataforma TEXT NOT NULL,
                        idioma TEXT NOT NULL,
                        fecha_registro DATETIME NOT NULL
                    )
    """
    )
    print("Tabla creada")
except sqlite3.Error as e:
    print(f"Error {e}")
finally:
    if conexion:
        conexion.close()
        print("conexion cerrada")

def mostrar_menu():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"\n{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cartelera de peliculas")
    print(f"{Fore.LIGHTMAGENTA_EX}1.Cargar pelicula")
    print(f"{Fore.LIGHTMAGENTA_EX}2.Buscar pelicula")
    print(f"{Fore.LIGHTMAGENTA_EX}3.Ver peliculas")
    print(f"{Fore.LIGHTMAGENTA_EX}4.Modificar pelicula")
    print(f"{Fore.LIGHTMAGENTA_EX}5.Eliminar pelicula")
    print(f"{Fore.LIGHTMAGENTA_EX}6.Vaciar lista de peliculas")
    print(f"{Fore.LIGHTMAGENTA_EX}7.Cantidad de peliculas registradas")
    print(f"{Fore.LIGHTMAGENTA_EX}8.Salir\n")
    print(f'{Fore.MAGENTA}~'*42)

def menu_busqueda():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Busqueda de peliculas")
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}1.Buscar por nombre de pelicula")
    print(f"{Fore.LIGHTMAGENTA_EX}2.Busqueda por genero")

def menu_modificar():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Busqueda de peliculas")
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}1.Modificar genero")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}2.Modificar nombre")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}3.Modificar plataforma")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}4.Modificar idioma")

def menu_ver():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Ver peliculas")
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}1.Ordenadas por ID")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}2.Ordenadas por nombre")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}3.Ordenadas por plataforma")
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}4.Ordenadas por precio")

def comprobar_opcion():
    opcion = input(f"{Fore.LIGHTWHITE_EX}Ingrese una opcion: ")
    while opcion.isdigit() == False:
        print("Ingrese un digito")
        opcion = input(f"{Fore.LIGHTWHITE_EX}Ingrese una opcion: ")
    opcion = int(opcion)
    return opcion

def recorrer(lista):
    for indice, i in enumerate(lista, start=1):
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}{indice}.{i}")

def recorrer_peliculas(peliculas):
    for i, pelicula in enumerate(peliculas, start=1):
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.DIM}{i}. {pelicula[0]} - {pelicula[1]} - ${pelicula[2]}")


def cargar_producto_SQL(nombre, genero, precio, plataforma, idioma, fecha):
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "INSERT INTO peliculas(nombre,genero,precio,plataforma, idioma,fecha_registro) VALUES (?,?,?,?,?,?)"
    cursor.execute(query, (nombre, genero, precio, plataforma, idioma, fecha))
    conexion.commit()
    conexion.close()

def cargar_producto(generos, plataformas, idiomas):
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Carga de producto")
    print(f'{Fore.MAGENTA}~'*42)
    nombre = input(f"{Style.BRIGHT}Ingrese el nombre de la pelicula: ")
    nombre = nombre.strip().capitalize()
    while nombre == "":
        nombre = input(f"{Style.BRIGHT}Ingrese el nombre de la pelicula: ")
    
    print(f"{Fore.MAGENTA}Lista de generos permitidos")
    recorrer(generos)
    genero = input(f"{Style.BRIGHT}Ingrese el genero: ").strip().capitalize()
    while genero not in generos:
        print(f"{Fore.RED}Genero incorrecto")
        genero = input(f"{Style.BRIGHT}Ingrese el genero: ").strip().capitalize()
    
    precio = input(f"{Style.BRIGHT}Ingrese el precio: ")
    while precio.isdigit() == False:
        print(f"{Fore.RED}Ingrese correctamente el precio")
        precio = input(f"{Style.BRIGHT}Ingrese el precio: ")
    precio = float(precio)

    print(f"{Fore.LIGHTMAGENTA_EX}Lista de plataformas permitidas")
    recorrer(plataformas)
    plataforma = input(f"{Style.BRIGHT}Ingrese la plataforma: ").strip().capitalize()
    while plataforma not in plataformas:
        print(f"{Fore.RED}Plataforma incorrecta")
        plataforma = input(f"{Style.BRIGHT}Ingrese la plataforma: ").strip().capitalize()

    print(f"{Fore.LIGHTMAGENTA_EX}Lista de idiomas: ")
    recorrer(idiomas)
    idioma = input(f"{Style.BRIGHT}Ingrese el idioma:").strip().capitalize()
    while idioma not in idiomas:
        print(f"{Fore.RED}Idioma incorrecto")
        idioma = input(f"{Style.BRIGHT}Ingrese el idioma:").strip().capitalize()

    fecha_registro = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cargar_producto_SQL(nombre,genero,precio, plataforma, idioma, fecha_registro)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}¡Pelicula {nombre} agregada con exito!")


def buscar_por_nombre_SQL():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Buscar por nombre de pelicula")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    nombreBuscado = input(f"{Style.BRIGHT}Ingrese el nombre de la pelicula a buscar: ").strip()
    query = "SELECT * FROM peliculas WHERE LOWER(nombre) LIKE ?"
    cursor.execute(query, (f"%{nombreBuscado.lower()}%",))
    peliculas = cursor.fetchall()
    conexion.close()
    encontrado=0
    if not peliculas:
        print(f"{Fore.RED}No se encontro ninguna pelicula con ese nombre")
    else:
        for pelicula in peliculas:
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT} {pelicula[0]} - {pelicula[1]} - {pelicula[2]} - ${pelicula[3]} - {pelicula[4]} - {pelicula[5]}")

def buscar_por_genero_SQL():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Buscar por genero")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    generoBuscado = input(f"{Style.BRIGHT}Ingrese el genero a buscar: ").strip()
    query = "SELECT * FROM peliculas WHERE LOWER(genero) LIKE ?"
    cursor.execute(query, (f"%{generoBuscado.lower()}%",))
    peliculas = cursor.fetchall()
    conexion.close()
    encontrado=0
    if not peliculas:
        print(f"{Fore.RED}No se encontro un genero")
    else:
        for pelicula in peliculas:
            print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT} {pelicula[0]} - {pelicula[1]} - {pelicula[2]} - ${pelicula[3]} - {pelicula[4]} - {pelicula[5]}")


def ver_productos_SQL():
    #ID
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Visualizacion de peliculas segun ID")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM peliculas"
    cursor.execute(query)
    peliculas = cursor.fetchall()
    conexion.close()

    if not peliculas: 
        print(f"{Fore.RED}No hay peliculas")
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista de peliculas")
        print(f"ID \t|  nombre \t\t|  genero \t|  precio  \t|  plataforma \t| idioma\t|\t fecha |")
        for pelicula in peliculas:
            print(f"{pelicula[0]:<3} | {pelicula[1]:<25} | {pelicula[2]:<12} | {pelicula[3]:<8} | {pelicula[4]:<12} | {pelicula[5]:<9} | {pelicula[6]:<14}")

def ver_productos_nombre():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Visualizacion de peliculas segun nombre")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM peliculas ORDER BY nombre"
    cursor.execute(query)
    peliculas = cursor.fetchall()
    conexion.close()

    if not peliculas: 
        print(f"{Fore.RED}No hay peliculas")
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista de peliculas")
        print(f"ID \t|  nombre \t\t|  genero \t|  precio  \t|  plataforma \t| idioma\t|\t fecha |")
        for pelicula in peliculas:
            print(f"{pelicula[0]:<3} | {pelicula[1]:<25} | {pelicula[2]:<12} | {pelicula[3]:<8} | {pelicula[4]:<12} | {pelicula[5]:<9} | {pelicula[6]:<14}")

def ver_productos_plataforma():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Visualizacion de peliculas segun plataforma")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM peliculas ORDER BY plataforma"
    cursor.execute(query)
    peliculas = cursor.fetchall()
    conexion.close()

    if not peliculas: 
        print(f"{Fore.RED}No hay peliculas")
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista de peliculas")
        print(f"ID \t|  nombre \t\t|  genero \t|  precio  \t|  plataforma \t| idioma\t|\t fecha |")
        for pelicula in peliculas:
            print(f"{pelicula[0]:<3} | {pelicula[1]:<25} | {pelicula[2]:<12} | {pelicula[3]:<8} | {pelicula[4]:<12} | {pelicula[5]:<9} | {pelicula[6]:<14}")

def ver_productos_precio():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Visualizacion de peliculas segun precio")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "SELECT * FROM peliculas ORDER BY precio"
    cursor.execute(query)
    peliculas = cursor.fetchall()
    conexion.close()

    if not peliculas: 
        print(f"{Fore.RED}No hay peliculas")
    else:
        print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Lista de peliculas")
        print(f"ID \t|  nombre \t\t|  genero \t|  precio  \t|  plataforma \t| idioma\t|\t fecha |")
        for pelicula in peliculas:
            print(f"{pelicula[0]:<3} | {pelicula[1]:<25} | {pelicula[2]:<12} | {pelicula[3]:<8} | {pelicula[4]:<12} | {pelicula[5]:<9} | {pelicula[6]:<14}")


def modificar_producto_SQL():
    ver_productos_SQL()
    id = input(f"{Fore.LIGHTMAGENTA_EX}Ingrese el ID del producto a modificar: ").strip()
    while id.isdigit() == False:
        id = input(f"{Fore.LIGHTMAGENTA_EX}Ingrese el ID del producto a modificar: ").strip()
    id = int(id)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    # verificar si existe
    cursor.execute("SELECT * FROM peliculas WHERE id = ?", (id,))
    pelicula = cursor.fetchone()
    if not pelicula:
        print("❌ No existe una pelicula con ese ID")
        conexion.close()
        return False, None
    else:
        menu_modificar()
        conexion.close()
        return True, id

def modificar_genero(id_elegido, generos):
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Modificar genero")
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.MAGENTA}Lista de generos permitidos")
    recorrer(generos)
    nuevo_genero = input(f"{Style.BRIGHT}Ingrese el nuevo genero: ").strip().capitalize()
    while nuevo_genero not in generos:
        print(f"{Fore.RED}Nuevo genero incorrecto")
        nuevo_genero = input(f"{Style.BRIGHT}Ingrese el nuevo genero: ").strip().capitalize()
    
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "UPDATE peliculas SET genero = ? WHERE id = ?"
    cursor.execute(query, (nuevo_genero, id_elegido))
    conexion.commit()
    conexion.close()

def modificar_nombre(id_elegido):
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Modificar nombre")
    print(f'{Fore.MAGENTA}~'*42)
    nuevo_nombre = input(f"{Style.BRIGHT}Ingrese el nuevo nombre de la pelicula: ")
    nuevo_nombre = nuevo_nombre.strip().capitalize()
    while nuevo_nombre == "":
        nuevo_nombre = input(f"{Style.BRIGHT}Ingrese el nuevo nombre de la pelicula: ")
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "UPDATE peliculas SET nombre = ? WHERE id = ?"
    cursor.execute(query, (nuevo_nombre, id_elegido))
    conexion.commit()
    conexion.close()

def modificar_plataforma(id_elegido, plataformas):
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Modificar plataforma")
    print(f'{Fore.MAGENTA}~'*42)

    print(f"{Fore.LIGHTMAGENTA_EX}Lista de plataformas permitidas")
    recorrer(plataformas)
    nuevo_plataforma = input(f"{Style.BRIGHT}Ingrese la nueva plataforma: ").strip().capitalize()
    while nuevo_plataforma not in plataformas:
        print(f"{Fore.RED} nueva plataforma incorrecta")
        nuevo_plataforma = input(f"{Style.BRIGHT}Ingrese la nueva plataforma: ").strip().capitalize()

    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "UPDATE peliculas SET plataforma = ? WHERE id = ?"
    cursor.execute(query, (nuevo_plataforma, id_elegido))
    conexion.commit()
    conexion.close()

def modificar_idioma(id_elegido, idiomas):
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Modificar idioma")
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}Lista de idiomas: ")
    recorrer(idiomas)
    nuevo_idioma = input(f"{Style.BRIGHT}Ingrese el nuevo idioma:").strip().capitalize()
    while nuevo_idioma not in idiomas:
        print(f"{Fore.RED}Nuevo idioma incorrecto")
        nuevo_idioma = input(f"{Style.BRIGHT}Ingrese el nuevo idioma:").strip().capitalize()
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    query = "UPDATE peliculas SET idioma = ? WHERE id = ?"
    cursor.execute(query, (nuevo_idioma, id_elegido))
    conexion.commit()
    conexion.close()


def eliminar_producto_SQL():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Eliminar una pelicula")
    print(f'{Fore.MAGENTA}~'*42)
    ver_productos_SQL()
    id = input(f"{Fore.LIGHTMAGENTA_EX}Ingrese el ID del producto a eliminar: ").strip()
    while id.isdigit() == False:
        id = input(f"{Fore.LIGHTMAGENTA_EX}Ingrese el ID del producto a eliminar: ").strip()
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    # verificar si existe
    cursor.execute("SELECT * FROM peliculas WHERE id = ?", (id,))
    pelicula = cursor.fetchone()

    if not pelicula:
        print("❌ No existe una pelicula con ese ID")

    else:
        confirmacion = input(f"{Fore.LIGHTMAGENTA_EX}Esta seguro de querer borrar {pelicula[1]}? Si/No ").title()
        while confirmacion != "Si" and confirmacion != "No":
            print(f"{Fore.RED}Por favor ingrese datos validos")
            confirmacion = input(f"{Fore.LIGHTMAGENTA_EX}¿Esta seguro que desea vaciar la lista? Si/No ").title()
        if confirmacion == "Si":
            cursor.execute("DELETE FROM peliculas WHERE id = ?", (id,))
            conexion.commit()
            print(f"✅ Pelicula con ID {id} eliminada")
    conexion.close()


def vaciar_productos_SQL():

    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Vaciar lista en SQL")
    print(f'{Fore.MAGENTA}~'*42)
    ver_productos_SQL()
    confirmacion = input(f"{Fore.RED}¿Esta seguro que desea vaciar la lista? Si/No ").title()
    while confirmacion != "Si" and confirmacion != "No":
            print(f"{Fore.RED}Por favor ingrese datos validos")
            confirmacion = input(f"{Fore.RED}¿Esta seguro que desea vaciar la lista? Si/No ").title()
    if confirmacion == "Si":
        conexion = sqlite3.connect("cinema.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM peliculas")
        conexion.commit()
        conexion.close()
        print(f"{Fore.GREEN}{Style.BRIGHT}Lista vaciada")

def cantidad_peliculas_SQL():
    print(f'{Fore.MAGENTA}~'*42)
    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}Cantidad de peliculas registradas")
    print(f'{Fore.MAGENTA}~'*42)
    conexion = sqlite3.connect("cinema.db")
    cursor = conexion.cursor()
    # por genero
    query = "SELECT genero, COUNT(*) FROM peliculas GROUP BY genero"
    cursor.execute(query)
    cantidad_genero = cursor.fetchall()

    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nPor genero:")
    for genero, cantidad in cantidad_genero:
        print(f"{Fore.LIGHTMAGENTA_EX}{genero}: {cantidad} peliculas")

    # por plataforma
    query = "SELECT plataforma, COUNT(*) FROM peliculas GROUP BY plataforma"
    cursor.execute(query)
    cantidad_plataforma = cursor.fetchall()

    print(f"{Fore.LIGHTMAGENTA_EX}{Style.BRIGHT}\nPor plataforma:")
    for plataforma, cantidad in cantidad_plataforma:
        print(f"{Fore.LIGHTMAGENTA_EX}{plataforma}: {cantidad} peliculas")

    conexion.close()