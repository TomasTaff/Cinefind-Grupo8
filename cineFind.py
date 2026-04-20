# ---------------- FUNCIONES DE PEDIDO ----------------
 
import re
from functools import reduce
def pedir_nombre():
 """Solicita y valida que el nombre de la película no sea un string vacío."""
    nombre = input("Nombre de la película: ")
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre de la película: ")
    return nombre

def pedir_genero():
 """Solicita el genero de la pelicula y valida que no sea un campo vacio."""
    genero = input("Género: ")
    while genero == "":
        print("El género no puede estar vacío.")
        genero = input("Género: ")
    return genero

def pedir_puntaje():
 """
    Solicita un puntaje (0-10). Usa re.fullmatch para asegurar que sean numeros 
    y verifica que el valor este en el rango permitido.
    """
    puntaje_str = input("Puntaje (0 a 10): ")
    
    while not re.fullmatch(r"^\d{1,2}$", puntaje_str) or float(puntaje_str) < 0 or float(puntaje_str) > 10:
        print("Puntaje inválido.")
        puntaje_str = input("Puntaje (0 a 10): ")
        
    puntaje = float(puntaje_str)
    return puntaje

def pedir_año():
 """
    Solicita el anio de estreno. Valida que sea un numero de 4 digitos 
    entre 1888 y 2025 mediante expresiones regulares y comparaciones logicas.
    """
    año_str = input("Año de estreno: ")
    while not re.fullmatch(r"^\d{4}$", año_str) or int(año_str) < 1888 or int(año_str) > 2025:
        print("Año inválido o fuera de rango. Ingrese 4 números (ej. 2001).")
        año_str = input("Año de estreno: ")
        
    año = int(año_str) 
    return año

# ---------------- FUNCIONES PRINCIPALES ----------------
def existe_pelicula(nombre, peliculas):
 """
    Recorre la lista de titulos para verificar si el nombre ingresado ya existe.
    Usa re.IGNORECASE para evitar duplicados por diferencias de mayusculas.
    """
    i = 0
    while i < len(peliculas):
        if re.fullmatch(nombre, peliculas[i], flags=re.IGNORECASE):
            return True
        i += 1
    return False

def agregar_pelicula(peliculas, generos, puntajes, años):
 """
    Coordina la carga de una nueva pelicula. Verifica existencia previa y 
    actualiza las cuatro listas (nombres, generos, puntajes, anios).
    """
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
 """
    Busca una pelicula por nombre y permite al usuario modificar 
    especificamente su genero o su puntaje.
    """
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
 """
    Calcula el promedio aritmetico de todos los puntajes registrados 
    utilizando la funcion de orden superior 'reduce'.
    """
    if len(puntajes) == 0:
        print("No hay películas cargadas.\n")
        return
 
    total = reduce(lambda a, b: a + b, puntajes, 0)
 
    promedio = total / len(puntajes)
    print("Puntaje promedio general:", round(promedio, 2), "\n")
def copiar_lista(lista):
 """Crea y retorna una copia superficial (shallow copy) de la lista ingresada."""
    copia_lista=lista.copy()
    return copia_lista
def ordenar_por_puntaje(peliculas, generos, puntajes, años):
 """
    Aplica el algoritmo de Bubble Sort para ordenar las listas de forma descendente 
    basandose en el puntaje, manteniendo la integridad de los datos en paralelo.
    """
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

def buscar_pelicula(peliculas, generos, puntajes, años):
 """
    Realiza una busqueda por nombre y, de encontrar coincidencia, 
    imprime toda la ficha tecnica de la pelicula (Genero, Puntaje, Anio).
    """
    nombre = input("Ingrese el nombre de la película: ")
    for i in range(len(peliculas)):
        if re.fullmatch(nombre, peliculas[i], flags=re.IGNORECASE):
            print("Película encontrada:")
            print("Película:", peliculas[i])
            print("Género:", generos[i])
            print("Puntaje:", puntajes[i])
            print("Año:", años[i])
            return
    print("No se encontró la película.\n")

def estadisticas(puntajes):
 """
    Muestra un resumen estadistico rapido: puntaje mas alto, 
    mas bajo y el promedio general.
    """
    if len(puntajes) == 0:
        print("No hay películas cargadas.\n")
        return
    maximo = max(puntajes)
    minimo = min(puntajes)
    promedio = sum(puntajes) / len(puntajes)
    print("Puntaje máximo:", maximo)
    print("Puntaje mínimo:", minimo)
    print("Promedio:", round(promedio, 2), "\n")

# ---------------- MATRIZ ----------------
def matriz_peliculas(filas, columnas,peliculas):
 """
    Organiza la lista de nombres de peliculas en una estructura bidimensional 
    (matriz) de dimensiones dadas, rellenando con 'VACIO' si sobran espacios.
    """
 

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
 """Recorre e imprime cualquier matriz en consola con un formato visual de rejilla (|)."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")
        print()
 
def mostrar_pelucula_en_matriz(filas, columnas,peliculas,generos,puntajes,años):
 """
    Genera una matriz donde cada celda contiene una lista con toda la informacion 
    agrupada de cada pelicula (Estructura compleja dentro de matriz).
    """
 

    matriz = []
    indice = 0
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if indice < len(peliculas):
                fila.append([peliculas[indice],generos[indice],puntajes[indice],años[indice]])
                indice += 1
            else:
                fila.append("VACIO")
        matriz.append(fila)
    return matriz

def mostrar_destacadas(peliculas, puntajes):
 """
    Filtra y muestra por consola los nombres de las peliculas cuya calificacion 
    es estrictamente superior a 8 puntos usando 'filter'.
    """
    print("\n=== PELÍCULAS DESTACADAS ===")
    # arma una lista con todas las posiciones de las peliculas.  
    posiciones = list(range(len(puntajes)))
    
    pos_destacadas = list(filter(lambda i: puntajes[i] > 8, posiciones))
    #pos_destacadas filtra las peliculas segun su numero de pos. con puntajes mayores a 8.
    if len(pos_destacadas) == 0:
        print("No hay películas destacadas aún.")
    else:
        for i in pos_destacadas:
            print(f"- {peliculas[i]}: {puntajes[i]} estrellas")
    print()
# ---------------- MENU ----------------
def menu():
 """Muestra la interfaz de opciones al usuario y valida que la entrada sea una opcion valida."""
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
 """
    Valida la entrada de un correo electronico mediante una expresion regular 
    que verifica la estructura estandar (usuario@dominio.com).
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    mail = input("Ingrese su mail: ")
    while not re.match(patron, mail):
        print("Formato de mail inválido (ejemplo: usuario@dominio.com).")
        mail = input("Ingrese su mail: ")
    return mail


# ---------------- MAIN ----------------
def main():
    peliculas = ["Matrix", "Titanic", "Inception", "Gladiador", "Interestelar"]
    generos = ["Ciencia ficción", "Romance", "Ciencia ficción", "Acción", "Ciencia ficción"]
    puntajes = [9, 8, 9.5, 8.5, 9.8]
    años = [1999, 1997, 2010, 2000, 2014]
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
        elif opcion == "2":
            m=mostrar_pelucula_en_matriz(4, 4,peliculas,generos,puntajes,años)
            imprimir_matriz(m)
        elif opcion == "3":
            actualizar_pelicula(peliculas, generos, puntajes, años)
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
            print("Fin del programa.")
            band=False
            
            print("Desea ingresar su mail para que le mandemos notificaciones?")
            opcion_mail=input("1=Si   2=No: ")
            if opcion_mail=="1":
                pedir_mail()
                print("Mail valido se le mandaran las notificaciones ")
            else:
                print ("Gracias por usar CineFind")

main()
