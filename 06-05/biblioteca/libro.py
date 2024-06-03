class Libro:
    ultimo_id = 0
    def __init__(self, titulo, autor, año_publicacion, unidades):
        Libro.ultimo_id += 1
        self.id = Libro.ultimo_id        
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.disponible = unidades > 0
        self.unidades = unidades
        
    def a_diccionario(self):
        return {
                "id": self.id,                
                "titulo": self.titulo,
                "autor": self.autor,
                "año_publicacion": self.año_publicacion,
                "disponible": self.disponible,
                "unidades": self.unidades
            }

    #permite crear una instancia de la clase Libro a partir de un diccionario de datos        
    @classmethod    
    def desde_diccionario(cls, data):        
        libro = cls(data["titulo"], data["autor"], data["año_publicacion"], data["unidades"])
        libro.id = data.get("id", Libro.ultimo_id)
        return libro         
    
    def prestar(self):
        if self.unidades > 0:
            self.unidades -= 1
            self.disponible = self.unidades > 0
            return True
        return False
    
    def recibir(self):
        self.unidades += 1    
        self.disponible = True
        return self.disponible 
        