import os
import json
from libro import Libro
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)        
    def mostrar_libros(self):
        for libro in self.libros:            
            print(f"{libro.titulo} por {libro.autor}, {libro.año_publicacion} - Unidades: {libro.unidades}")    
            
    def prestar_libros(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.prestar():
                    print(f"Se prestó el libro {titulo} ")
                else:    
                    print(f"{titulo} No está disponible ")
            
                    
    def recibir_libros(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                if libro.recibir():
                    print(f"Se recibio el libro {titulo} ")        
                    
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