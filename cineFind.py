import re
import json
import os
from functools import reduce
import doctest

ARCHIVO_BD = "cinefind_db.json"

# ================ FUNCIONES PARA JSON ================

def cargar_datos():
    '''
    Verifica si existe el archivo JSON. Si existe, lo lee y devuelve las listas.
    Si no existe, devuelve las listas predeterminadas para empezar.
    '''
    if os.path.exists(ARCHIVO_BD):
        with open(ARCHIVO_BD, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            # Retornamos las 4 listas guardadas
            return datos["peliculas"], datos["generos"], datos["puntajes"], datos["años"]
    else:
        # Si es la primera vez que se ejecuta el programa y no hay JSON
        peliculas = ["Matrix", "Titanic", "Inception", "Gladiador", "Interestelar"]
        generos = ["Ciencia ficción", "Romance", "Ciencia ficción", "Acción", "Ciencia ficción"]
        puntajes = [9.0, 8.0, 9.5, 8.5, 9.8]
        años = [1999, 1997, 2010, 2000, 2014]
        return peliculas, generos, puntajes, años

def guardar_datos(peliculas, generos, puntajes, años):
    '''
    Empaqueta las 4 listas paralelas en un diccionario y lo guarda en el JSON.
    '''
    datos = {
        "peliculas": peliculas,
        "generos": generos,
        "puntajes": puntajes,
        "años": años
    }
    with open(ARCHIVO_BD, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)

# ================ FUNCIONES DE VALIDACIÓN ================

def pedir_nombre():
    ''' 
    Solicita el nombre de la pelicula y valida que no sea un campo vacio
    '''
    nombre = input("Nombre de la película: ")
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre de la película: ")
    return nombre

def pedir_genero():
    '''
    Solicita el genero de la pelicula y valida que no sea un campo vacio
    '''
    genero = input("Género: ")
    while genero == "":
        print("El género no puede estar vacío.")
        genero = input("Género: ")
    return genero

def pedir_puntaje():
    '''
    Le pide el puntaje al usuario (0-10). 
    Usa excepciones (ValueError) para validar que sea un número válido.
    '''
    while True:
        puntaje_str = input("Puntaje (0 a 10): ")
        try:
            puntaje = float(puntaje_str)
            if puntaje < 0 or puntaje > 10:
                print("Puntaje inválido. Debe estar entre 0 y 10.")
            else:
                return puntaje
        except ValueError:
            print("Error: Por favor ingresa un número válido (ej. 8 o 8.5).")

def pedir_año():
    '''
    Usuario ingresa el año de estreno de la pelicula. Con re.fullmatch valida que sean 4 digitos. 
    Tambien se valida que sea entre 1888 y 2026 mediante expresiones regulares y comparaciones logicas.
    '''
    año_str = input("Año de estreno: ")
    while not re.fullmatch(r"^\d{4}$", año_str) or int(año_str) < 1888 or int(año_str) > 2026:
        print("Año inválido o fuera de rango. Ingrese 4 números (ej. 2001).")
        año_str = input("Año de estreno: ")
        
    año = int(año_str) 
    return año

# ---------------- FUNCIONES PRINCIPALES ----------------

def existe_pelicula(nombre, peliculas):
    '''
    Verifica si el nombre ingresado ya existe en el catálogo.
    Usa re.IGNORECASE para evitar duplicados por diferencias de mayúsculas. 
    
    --- PRUEBAS UNITARIAS (doctest) ---
    
    Escenario 1: La película existe exactamente igual
    >>> existe_pelicula("Matrix", ["Matrix", "Titanic", "Inception"])
    True
    
    Escenario 2: La película no existe en la lista
    >>> existe_pelicula("Avatar", ["Matrix", "Titanic", "Inception"])
    False
    
    Escenario 3: La película existe pero escrita en minúsculas (Prueba de re.IGNORECASE)
    >>> existe_pelicula("titanic", ["Matrix", "Titanic", "Inception"])
    True
    '''
    i = 0
    while i < len(peliculas):
        if re.fullmatch(nombre, peliculas[i], flags=re.IGNORECASE):
            return True
        i += 1
    return False

def agregar_pelicula(peliculas, generos, puntajes, años):
    '''
    Coordina la carga de una nueva pelicula. 
    Verifica existencia previa y actualiza las cuatro listas (nombres, generos, puntajes,años)
    '''
    nombre = pedir_nombre()
    if existe_pelicula(nombre, peliculas):
        print("Esa película ya fue cargada.\n")
        return
    genero = pedir_genero()
    puntaje = pedir_puntaje()
    año = pedir_año()
    peliculas.append(nombre)
    generos.append(genero)
    puntajes.append(puntaje)
    años.append(año)
    print("Película agregada.\n")

def actualizar_pelicula(peliculas, generos, puntajes, años):
    '''
    Busca una pelicula por nombre y permite al usuario modificar especificamente su genero o puntaje. 
    '''
    if len(peliculas) == 0:
        print("No hay películas para actualizar.\n")
        return
    nombre = input("Nombre de la película a actualizar: ")
    pos = -1
    for i in range(len(peliculas)):
        if peliculas[i] == nombre:
            pos = i
    if pos == -1:
        print("Esa película no está en la lista.\n")
        return
    print("1. Cambiar género")
    print("2. Cambiar puntaje")
    opcion = input("Opción: ")
    if opcion == "1":
        nuevo_genero = pedir_genero()
        generos[pos] = nuevo_genero
        print("Género actualizado.\n")
    elif opcion == "2":
        nuevo_puntaje = pedir_puntaje()
        puntajes[pos] = nuevo_puntaje
        print("Puntaje actualizado.\n")
    else:
        print("Opción inválida.\n")

def promedio_puntajes(puntajes):
    try:
        total = reduce(lambda a, b: a + b, puntajes, 0)
        promedio = total / len(puntajes) #si no hay películas, len es 0
        print("Puntaje promedio general:", round(promedio, 2), "\n")
        
    except ZeroDivisionError:
        print("No hay películas cargadas para calcular el promedio.\n")

def copiar_lista(lista):
    """
    Crea y retorna una copia superficial (shallow copy) de la lista ingresada.
    """
    copia_lista=lista.copy()
    return copia_lista

def ordenar_por_puntaje(peliculas, generos, puntajes, años):
    '''
    Aplica el algoritmo de Bubble Sort para ordenar las listas de forma descendente 
    basandose en el puntaje, manteniendo la integridad de los datos en paralelo.
    '''
    n = len(puntajes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if puntajes[j] < puntajes[j + 1]:
                # intercambio
                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]
                peliculas[j], peliculas[j+1] = peliculas[j+1], peliculas[j]
                generos[j], generos[j+1] = generos[j+1], generos[j]
                años[j], años[j+1] = años[j+1], años[j]
    print("Películas ordenadas por puntaje.\n")

def diccionarioPelicula(peliculas,pelicula,genero,puntaje,año):
    for i in range(len(peliculas)):
        if re.fullmatch(pelicula,peliculas[i],flags=re.IGNORECASE):
            peliculaD={"pelicula":pelicula,"genero":genero[i],"puntaje":puntaje[i],"anio":año[i]}
            print(peliculaD)
            return
            
    print("pelicula no encontrada")
            
def buscar_pelicula(peliculas, generos, puntajes, años):
    nombre = input("Ingrese el nombre de la película: ")
    d=diccionarioPelicula(peliculas,nombre,generos,puntajes,años)
    return d

def estadisticas(puntajes):
    '''
    Muestra un resumen estadistico rapido.
    Usa Excepciones para atajar listas vacías en lugar de contar los elementos con un IF.
    '''
    try:
        maximo = max(puntajes) # Riesgo de ValueError
        minimo = min(puntajes)
        promedio = sum(puntajes) / len(puntajes) # Riesgo de ZeroDivisionError
        
        print("Puntaje máximo:", maximo)
        print("Puntaje mínimo:", minimo)
        print("Promedio:", round(promedio, 2), "\n")
        
    except (ZeroDivisionError, ValueError):
        # Atrapamos los dos errores posibles en una sola linea
        print("No hay películas cargadas para calcular estadísticas.\n")

# ---------------- MATRIZ ----------------

def matriz_peliculas(filas, columnas,peliculas):
    '''
    Organiza la lista de nombres de peliculas en una estructura bidimensional 
    (matriz) de dimensiones dadas, rellenando con 'VACIO' si sobran espacios.
    '''
    matriz = []
    indice = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if indice < len(peliculas):
                fila.append(peliculas[indice])
                indice += 1
            else:
                fila.append("VACIO")
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    '''
    Recorre e imprime cualquier matriz en consola con un formato visual de rejilla (|)
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")
        print()
 
def mostrar_pelicula(peliculas,generos,puntajes,años):
    for i in range (len(peliculas)):
        pelicula={f"pelicula":peliculas[i],"genero":generos[i],"puntaje":puntajes[i],"anio":años[i]}
        print(pelicula)

def mostrar_destacadas(peliculas, puntajes):
    '''
    Filtra y muestra por consola los nombres de las peliculas cuya calificacion 
    es estrictamente superior a 8 puntos usando 'filter'.
    '''
    print("\n=== PELÍCULAS DESTACADAS ===")                           
 
    posiciones = list(range(len(puntajes)))
    pos_destacadas = list(filter(lambda i: puntajes[i] > 8, posiciones))

    if len(pos_destacadas) == 0:
        print("No hay películas destacadas aún.")
    else:
        for i in pos_destacadas:
            print(f"- {peliculas[i]}: {puntajes[i]} estrellas")
    print()

# ---------------- MENU ----------------

def menu():
    '''
    Muestra la intefaz de opciones al usuario y valida que la entrada sea una opcion valida. 
    '''
    print("=== MENÚ CINEFIND ===")
    print("1. Agregar película")
    print("2. Mostrar películas")
    print("3. Actualizar película")
    print("4. Calcular promedio")
    print("5. Ordenar por puntaje")
    print("6. Buscar película")
    print("7. Ver estadísticas")
    print("8. Ver peliculas destacadas")
    print("0. Salir")
    opcion = input("Opción: ")
    while opcion not in ["0","1","2","3","4","5","6","7","8"]:
        print("Opción inválida.")
        opcion = input("Opción: ")
    return opcion
    
def pedir_mail():
    '''
    Valida la entrada de un correo electronico mediante una expresion regular 
    que verifica la estructura estandar (usuario@dominio.com).
    '''
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mail = input("Ingrese su mail: ")
    while not re.match(patron, mail):
        print("Formato de mail inválido (ejemplo: usuario@dominio.com).")
        mail = input("Ingrese su mail: ")
    return mail

# ---------------- MAIN ----------------

def main():
    peliculas, generos, puntajes, años = cargar_datos()
    
    matriz = matriz_peliculas(3, 5,peliculas)
    print("=== CINEFIND ===\n")
    opcion = ""
    band=True
    
    while band :
        opcion = menu()
        
        if opcion == "1":
            print("estas son las peliculas que ya estan cargadas ")
            imprimir_matriz(matriz)
            agregar_pelicula(peliculas, generos, puntajes, años)
            matriz = matriz_peliculas(3, 5,peliculas)
            guardar_datos(peliculas, generos, puntajes, años)
            
        elif opcion == "2":
            mostrar_pelicula(peliculas,generos,puntajes,años)
            
        elif opcion == "3":
            actualizar_pelicula(peliculas, generos, puntajes, años)
            guardar_datos(peliculas, generos, puntajes, años)
            
        elif opcion == "4":
            promedio_puntajes(puntajes)
            
        elif opcion == "5":
            copia_peliculas=copiar_lista(peliculas)
            copia_generos=copiar_lista(generos)
            copia_puntajes=copiar_lista( puntajes)
            copia_años=copiar_lista(años)
            ordenar_por_puntaje(copia_peliculas, copia_generos,copia_puntajes, copia_años)
            
        elif opcion == "6":
            buscar_pelicula(peliculas, generos, puntajes, años)
            
        elif opcion == "7":
            estadisticas(puntajes)
            
        elif opcion == "8":
            mostrar_destacadas(peliculas, puntajes)
                 
        elif opcion == "0":
            band=False
            print("Desea ingresar su mail para que le mandemos notificaciones?")
            opcion_mail=input("1:Si   2:No ")
            if opcion_mail=="1":
                pedir_mail()
                print("Mail valido se le mandaran las notificaciones ")
            else:
                print ("Gracias por usar CineFind")
                
            print("Fin del programa.")

if __name__ == "__main__":
    doctest.testmod()
    
    main()