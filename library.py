class Library_management:
    
    
    def __init__(self, libros) -> dict: ##libros es el diccionarios donde estarán los libros.
        self.libros =  libros 

    def lista_libros(self) -> None: ##con esa función veo los libros que están en el diccionario.
        print(f"lista de libros disponibles: {self.libros.values()}")

    def prestar_libros(self, libro : str) -> None: ##función para prestar libros desde la biblioteca.
        if(libro in self.libros):    
            del self.libros[libro]
        else:
            print("no contamos con este libro.")

    def subir_libro(self, lista_libros) -> None: ##función para subir libros desde la biblioteca.
        i=0
        for i in range(len(lista_libros)):
            self.libros[lista_libros[i]] = lista_libros[i]
            i +=1

    def bajar_libro(self, libro : str) -> None: ##función para bajar libros desde la biblioteca.
        if(libro in self.libros):    
            del self.libros[libro]
        else:
            print("no contamos con este libro.")
    
    def entregar_libros(self, libro : str) -> None: ##función para entregar libros.
        self.libros[libro] = libro 
        

class User:

    def __init__(self, name: str) -> None: ## constructor que contiene el nombre del usuario.
        self.name= name

    def prestar_libros(self, objeto,  libro : str):  ## función que le permite a un objeto de la clase usuario prestar un libro.
        
        objeto.prestar_libros(libro)
        print (f"estimado {self.name} ha rentado el libro llamado  {libro} ")
    
    def entregar_libros(self, objeto,  libro : str): ## función que le permite a un objeto de la clase usuario entregar un libro.
        objeto.entregar_libros(libro)
        print (f"estimado {self.name} ha devuelto el libro llamado {libro} ")