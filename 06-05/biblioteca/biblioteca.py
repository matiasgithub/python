import os
import json
from libro import Libro
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro) 
        
    def quitar_libro(self, libro_id):
        libro_encontrado = False
        for libro in self.libros:
            if libro.id == libro_id:
                self.libros.remove(libro)
                libro_encontrado = True
                print(f"Libro '{libro.titulo}' quitado con éxito.")
                break
        if not libro_encontrado:
            print(f"Error: No existe un libro con el ID {libro_id}.")       
        
    def mostrar_libros(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        for libro in self.libros:            
            estado = "Disponible" if libro.disponible else "No disponible"
            print(f"{libro.id} {libro.titulo} por {libro.autor}, {libro.año_publicacion} - Unidades: {libro.unidades} ({estado})")
            
    def prestar_libro(self, titulo):
        libro_encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo:
                libro_encontrado = True
                if libro.prestar():
                    print(f"Libro '{titulo}' prestado con éxito.")
                else:
                    print(f"Libro '{titulo}' no está disponible.")
                return
        if not libro_encontrado:
            print(f"Libro '{titulo}' no encontrado en la biblioteca.")
            
                    
    def recibir_libro(self, titulo):
        libro_encontrado = False
        for libro in self.libros:
            if libro.titulo == titulo:
                libro_encontrado = True
                if libro.recibir():
                    print(f"Se recibió el libro '{titulo}'.")
                else:
                    print(f"El libro '{titulo}' ya estaba disponible en la biblioteca.")
                return
        if not libro_encontrado:
            print(f"Libro '{titulo}' no encontrado en la biblioteca.")       
                    
    def guardar_libros_json(self, nombre_archivo):
        libros_dict = [libro.a_diccionario() for libro in self.libros]
        ruta = os.path.join(os.path.dirname(__file__), nombre_archivo)
        try:
            with open(ruta, 'w') as f:
                json.dump(libros_dict, f, ensure_ascii=False, indent=4)
            print("Libros guardados correctamente en:", ruta)
        except Exception as e:
            print("Error al guardar libros:", e)
            
    @classmethod
    def cargar_desde_json(cls, nombre, archivo):
        biblioteca = cls(nombre)
        ruta = os.path.join(os.path.dirname(__file__), archivo)        
        try:
            with open(ruta, 'r') as file:
                libros_data = json.load(file)
                for libro_data in libros_data:
                    biblioteca.agregar_libro(Libro.desde_diccionario(libro_data))
        except FileNotFoundError:
            print(f"Archivo '{archivo}' no encontrado.")
        return biblioteca          