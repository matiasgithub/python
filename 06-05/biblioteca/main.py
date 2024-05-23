from biblioteca import Biblioteca
from libro import Libro
def main():
    biblioteca1 = Biblioteca("Biblioteca Central")
    biblioteca2 = Biblioteca("Biblioteca del Barrio")
    biblioteca1.agregar_libro(Libro("1984", "George Orwell", 1949, 3))
    biblioteca1.agregar_libro(Libro("Hamlet", "William Shakespeare ", 1603, 2))
    
    biblioteca2.agregar_libro(Libro("El Hobbit", "J.R.R. Tolkien", 1937, 4))
    biblioteca2.agregar_libro(Libro("Don Quijote", "Miguel de Cervantes", 1605, 1))
    
    biblioteca1.mostrar_libros()
    biblioteca1.prestar_libros("1984")
    biblioteca1.prestar_libros("1984")
    biblioteca1.prestar_libros("1984")
    biblioteca1.prestar_libros("1984")
    biblioteca1.recibir_libros("1984")
    biblioteca1.prestar_libros("1984")
    biblioteca1.mostrar_libros()

    biblioteca3 = Biblioteca.cargar_desde_json("Biblioteca Municipal", "biblioteca_municipal.json")
    biblioteca3.mostrar_libros()
    #biblioteca1.guardar_libros_json("biblioteca_central_libros.json")        

if __name__ == "__main__":
    main()
    