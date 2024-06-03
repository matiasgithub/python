from biblioteca import Biblioteca
from libro import Libro

def mostrar_menu_principal():
    print("\nSeleccione una opción:")
    print("1. Seleccionar biblioteca")
    print("2. Cargar biblioteca desde archivo JSON")
    print("3. Salir")
    
def mostrar_menu_biblioteca(nombre):
    print(f"\n {nombre} \nSeleccione una opción:")
    print("1. Mostrar libros")
    print("2. Agregar libro")
    print("3. Quitar libro")
    print("4. Prestar libro")
    print("5. Recibir libro")
    print("6. Guardar biblioteca en archivo JSON")       
    print("7. Volver menú anterior")
def seleccionar_biblioteca(bibliotecas):
    print("\nSeleccione una biblioteca:")
    for i, biblioteca in enumerate(bibliotecas):
        print(f"{i + 1}. {biblioteca.nombre}")
    seleccion = int(input("Ingrese el número de la biblioteca: ")) - 1
    return bibliotecas[seleccion]
def main():
            
    biblioteca1 = Biblioteca("Biblioteca Central")
    biblioteca2 = Biblioteca("Biblioteca del Barrio")
    bibliotecas = [biblioteca1, biblioteca2]
    
    while True:
        mostrar_menu_principal()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            biblioteca_actual = seleccionar_biblioteca(bibliotecas)
            while biblioteca_actual:
                mostrar_menu_biblioteca(biblioteca_actual.nombre)
                opcion_biblioteca = input("Ingrese una opción: ")

                if opcion_biblioteca == "1":
                    biblioteca_actual.mostrar_libros()
                elif opcion_biblioteca == "2":
                    titulo = input("Ingrese el título del libro: ")
                    autor = input("Ingrese el autor del libro: ")
                    año_publicacion = int(input("Ingrese el año de publicación: "))
                    unidades = int(input("Ingrese la cantidad de unidades: "))
                    libro = Libro(titulo, autor, año_publicacion, unidades)
                    biblioteca_actual.agregar_libro(libro)
                    print(f"Libro '{titulo}' agregado con éxito.")
                elif opcion_biblioteca == "3":
                    biblioteca_actual.mostrar_libros()
                    libro_id = int(input("Ingrese el ID del libro a quitar: "))
                    biblioteca_actual.quitar_libro(libro_id)
                elif opcion_biblioteca == "4":
                    titulo = input("Ingrese el título del libro a prestar: ")
                    biblioteca_actual.prestar_libro(titulo)
                elif opcion_biblioteca == "5":
                    titulo = input("Ingrese el título del libro a recibir: ")
                    biblioteca_actual.recibir_libro(titulo)
                elif opcion_biblioteca == "6":
                    archivo = input("Ingrese el nombre del archivo JSON para guardar: ")
                    biblioteca_actual.guardar_libros_json(archivo)
                    print(f"Biblioteca guardada en '{archivo}'.")
                elif opcion_biblioteca == "7":
                    break                
                else:
                    print("Opción no válida. Intente de nuevo.")
        elif opcion == "2":
            archivo = input("Ingrese el nombre del archivo JSON para cargar: ")
            nombre = input("Ingrese el nombre de la biblioteca: ")
            biblioteca_nueva = Biblioteca.cargar_desde_json(nombre, archivo)
            if biblioteca_nueva:
                bibliotecas.append(biblioteca_nueva)
                print(f"Biblioteca '{nombre}' cargada desde '{archivo}'.")
            else:
                print("Error al cargar la biblioteca.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
if __name__ == "__main__":
    main()
    
""" biblioteca1 = Biblioteca("Biblioteca Central")
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
    """            