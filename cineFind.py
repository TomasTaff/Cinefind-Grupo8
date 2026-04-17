# ---------------- FUNCIONES DE PEDIDO ----------------
 
import re
from functools import reduce
def pedir_nombre():
    nombre = input("Nombre de la película: ")
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre de la película: ")
    return nombre

def pedir_genero():
    genero = input("Género: ")
    while genero == "":
        print("El género no puede estar vacío.")
        genero = input("Género: ")
    return genero

def pedir_puntaje():
    puntaje_str = input("Puntaje (0 a 10): ")
    
    while not re.fullmatch(r"^\d{1,2}$", puntaje_str) or float(puntaje_str) < 0 or float(puntaje_str) > 10:
        print("Puntaje inválido.")
        puntaje_str = input("Puntaje (0 a 10): ")
        
    puntaje = float(puntaje_str)
    return puntaje

def pedir_año():
    año = int(input("Año de estreno: "))
    if validacionFecha(año ):

        while año < 1888 or año > 2025:
            print("Año fuera de rango.")
            año = int(input("Año de estreno: "))
    else:
        return año

# ---------------- FUNCIONES PRINCIPALES ----------------
def existe_pelicula(nombre, peliculas):
    i = 0
    while i < len(peliculas):
        if peliculas[i] == nombre:
            return True
        i += 1
    return False

def agregar_pelicula(peliculas, generos, puntajes, años):
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
    if len(puntajes) == 0:
        print("No hay películas cargadas.\n")
        return
 
    total = reduce(lambda a, b: a + b, puntajes, 0)
 
    promedio = total / len(puntajes)
    print("Puntaje promedio general:", round(promedio, 2), "\n")
def copiar_lista(lista):
    copia_lista=lista.copy()
    return copia_lista
def ordenar_por_puntaje(peliculas, generos, puntajes, años):
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
    nombre = input("Ingrese el nombre de la película: ")
    for i in range(len(peliculas)):
        if peliculas[i] == nombre:
            print("Película encontrada:")
            print("Película:", peliculas[i])
            print("Género:", generos[i])
            print("Puntaje:", puntajes[i])
            print("Año:", años[i])
            return
    print("No se encontró la película.\n")

def estadisticas(puntajes):
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
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" | ")
        print()
 
def mostrar_pelucula_en_matriz(filas, columnas,peliculas,generos,puntajes,años):
 

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

# ---------------- MENU ----------------
def menu():
    print("=== MENÚ CINEFIND ===")
    print("1. Agregar película")
    print("2. Mostrar películas")
    print("3. Actualizar película")
    print("4. Calcular promedio")
    print("5. Ordenar por puntaje")
    print("6. Buscar película")
    print("7. Ver estadísticas")
    print("0. Salir")
    opcion = input("Opción: ")
    while opcion not in ["0","1","2","3","4","5","6","7"]:
        print("Opción inválida.")
        opcion = input("Opción: ")
    return opcion
 
def validacionFecha(anio_estreno ):
    if re.match(r"^\d{4}$",anio_estreno):
        return True
    else:
        return False #FALTA IMPLEMENTAR 

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
            mostrar_peliculas(copia_peliculas, copia_generos,copia_puntajes, copia_años)
        elif opcion == "6":
            buscar_pelicula(peliculas, generos, puntajes, años)
        elif opcion == "7":
            estadisticas(puntajes)

        elif opcion == "0":
            print("Fin del programa.")
            band=False

main()
