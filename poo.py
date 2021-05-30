class Book():
    
    """
    aqui esta una clase de libros
    """
    electronico = False

libro1 = Book()

print(libro1.electronico)


print(Book.__doc__)




class Book2():
    
    def __init__(self, titulo, autor, electronico):
        
        self.titulo = titulo
        self.autor = autor
        self.electronico = electronico
        
        
book2 = Book2("Cementerio de Animales", "Stephen King", True)


print(book2.titulo)

print(book2.autor)

print(book2.electronico)


print(book2.__dict__)
