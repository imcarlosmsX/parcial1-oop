from library import Library_management, User

lista_libros = {"el mundo de sofia" : "el mundo de sofia", "el mar" : "el mar"} ## se le dan valores al diccionario libros.
lista_subir_libros = ["dios", "el naufrago", "la odisea"] ## acá hay una lista, que es la que se agregará a los libros.

libreria1 = Library_management(libros= lista_libros) ## se le asigna el diccionario 
libreria1.subir_libro(lista_libros = lista_subir_libros)  ## acá se usa la función para agregar libro del objeto tipo libros que ya creamos.


libreria1.lista_libros() ##esta función muestra los libros disponibles.

usuario1 = User("carlos mendoza") ##definimos un usuario.

libreria1.prestar_libros("cualquiera") ##prestamos un libro desde la clase Library_management


usuario1.prestar_libros(libreria1, "dios") ## prestamos un libro desde la clase User, con el usuario que ya definimos antes.

libreria1.lista_libros() 

usuario1.entregar_libros(libreria1, "dios") ##regresamos el mismo libro que prestamos con el usuario anterior.

libreria1.lista_libros()

