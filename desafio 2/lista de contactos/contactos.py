from controlador import *

#Estructura de un contacto: {"Id": 1, "Nombre": "nombre", "Apellido": "apellido", "Emails": ["email1", "email2"], "Teléfonos":["3234234","123123123"] }
opcion = None
while True:
    menu = """ 
            MENU CONTACTOS
            1) Agregar        2) Eliminar 
            3) Modificar      4) Mostrar contactos
            5) Buscar         6) Salir                
            """
    if(opcion != 5): mostrar_contactos(contactos)       
    print(menu)
    opcion = validar_menu()
        
    if opcion == 1:
        print("Seleccionaste Agregar")
        agregar_contacto()
    elif opcion == 2:
        print("Seleccionaste Eliminar")
        eliminar_contacto()
    elif opcion == 3:
        print("Seleccionaste Modificar")
        modificar_contacto()
    elif opcion == 4:
        print("Seleccionaste Mostrar")
        mostrar_contactos(contactos)
    elif opcion == 5:
        print("Seleccionaste Buscar")
        buscar()
    elif opcion == 6:
        print("Seleccionaste Salir")
        break  
    