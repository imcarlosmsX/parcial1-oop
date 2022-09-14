class Library_management:
    
    
    def __init__(self, libros) -> dict:
        self.libros =  libros 

    def lista_libros(self) -> None:
        print(f"lista de libros disponibles: {self.libros.values()}")

    def prestar_libros(self, libro : str) -> None:
        if(libro in self.libros):    
            del self.libros[libro]
        else:
            print("no contamos con este libro.")

    def subir_libro(self, lista_libros) -> None:
        i=0
        for i in range(len(lista_libros)):
            self.libros[lista_libros[i]] = lista_libros[i]
            i +=1

    def bajar_libro(self, libro : str) -> None:
        if(libro in self.libros):    
            del self.libros[libro]
        else:
            print("no contamos con este libro.")
    
    def entregar_libros(self, libro : str) -> None:
        self.libros[libro] = libro 
        

class User:

    def __init__(self, name: str) -> None:
        self.name= name

    def prestar_libros(self, objeto,  libro : str):
        
        objeto.prestar_libros(libro)
        print (f"estimado {self.name} ha rentado el libro llamado  {libro} ")
    
    def entregar_libros(self, objeto,  libro : str):
        objeto.entregar_libros(libro)
        print (f"estimado {self.name} ha devuelto el libro llamado {libro} ")