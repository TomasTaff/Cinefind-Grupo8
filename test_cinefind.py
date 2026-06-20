
from cineFind import existe_pelicula #importo la funcion del programa principal


def test_pelicula_existente(): # tiene que arrancar con la palabra test_ para diferenciarlo de una funcion normal
    catalogo = ["Matrix", "Titanic", "Inception"]
    resultado = existe_pelicula("Matrix", catalogo)
    
    assert resultado == True


def test_pelicula_no_existente():
    catalogo = ["Matrix", "Titanic", "Inception"]
    resultado = existe_pelicula("Avatar", catalogo)
    
    assert resultado == False


def test_pelicula_ignora_mayusculas():
    catalogo = ["Matrix", "Titanic", "Inception"]
    resultado = existe_pelicula("tItAnIc", catalogo)
    
    assert resultado == True