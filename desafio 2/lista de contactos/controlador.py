from validaciones import *
""""
contactos = [{"Id": 1, "Nombre": "Juan", "Apellido": "Perez", "Emails": ["mail@mail.com", "otromail@mail.com"], "Teléfonos":["2613215465","2613215547"]},
             {"Id": 2, "Nombre": "Mario", "Apellido": "Kempes", "Emails": ["mimail@mail.com", "unmail@mail.com"], "Teléfonos":["261456465","2614126545"]},
             {"Id": 3, "Nombre": "Mario", "Apellido": "Gonzales", "Emails": ["estemail@mail.com", "cualquiermail@mail.com"], "Teléfonos":["2612126445","261368745"]}
             ]
"""  
contactos = []         
proximo_id = 1  

def buscar_contacto_id(id):
    for contacto in contactos:
        if contacto["Id"] == id:
            return contacto
    
def agregar_contacto():
    global proximo_id 
    nombre = input("Ingrese nombre del contacto: ")
    apellido = input("Ingrese apellido del contacto: ")
    emails = input("Ingrese los correos electrónicos separados por comas: ").split(',')
    emails_validados = validar_correos(emails)            
    telefonos = input("Ingrese los números de teléfono separados por comas: ").split(',')    
        
    nueva_contacto = {
        "Id": proximo_id,
        "Nombre": nombre,
        "Apellido": apellido,
        "Emails": emails_validados,
        "Teléfonos": telefonos
    }
    contactos.append(nueva_contacto)  
    proximo_id += 1 
    
def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos para mostrar.")
        return
            
    print("\n Lista de contactos:")
    for contacto in contactos:
        print(f"ID: {contacto['Id']}")
        print(f"Nombre: {contacto['Nombre']}")
        print(f"Apellido: {contacto['Apellido']}")
        print("Emails:", ', '.join(contacto['Emails']))
        print("Teléfonos:", ', '.join(contacto['Teléfonos']))  
        print()              

                
def modificar_contacto():
    id_contacto_modificar = int(input("Ingrese el ID del contacto que desea modificar: "))
    contacto_encontrado = buscar_contacto_id(id_contacto_modificar)
    
    if contacto_encontrado is None:
        print("No se encontró ningún contacto con ese ID.")
        return
        
    print("Ingrese los nuevos datos para el contacto:")
    nombre = input(f"Nuevo nombre ({contacto_encontrado['Nombre']}): ")
    apellido = input(f"Nuevo apellido ({contacto_encontrado['Apellido']}): ")
    emails = input(f"Nuevos correos electrónicos separados por comas ({', '.join(contacto_encontrado['Emails'])}): ").split(',')    
    emails_validados = validar_correos(emails)
    telefonos = input(f"Nuevos números de teléfono separados por comas ({', '.join(contacto_encontrado['Teléfonos'])}): ").split(',')
    
    nombre = nombre.strip() if nombre.strip() else contacto_encontrado['Nombre']
    apellido = apellido.strip() if apellido.strip() else contacto_encontrado['Apellido']    
    emails_validados = emails_validados if emails_validados else contacto_encontrado['Emails']
    telefonos = telefonos if telefonos else contacto_encontrado["Teléfonos"]
    
    contacto_encontrado['Nombre'] = nombre if nombre else contacto_encontrado['Nombre']
    contacto_encontrado['Apellido'] = apellido if apellido else contacto_encontrado['Apellido']
    contacto_encontrado['Emails'] = emails_validados if emails_validados else contacto_encontrado['Emails']
    contacto_encontrado['Teléfonos'] = telefonos if telefonos else contacto_encontrado['Teléfonos']

    print("Datos del contacto modificados correctamente.")
    
    
def buscar():   
    buscar = input("Ingrese nombre, apellido, email o teléfono a buscar: ")    
    resultados_busqueda = busqueda_texto(buscar)
    mostrar_contactos(resultados_busqueda)
            
def busqueda_texto(texto):
    resultados = []
    for contacto in contactos:
        for valor in contacto.values():
            if isinstance(valor, str) and texto.lower() in valor.lower():
                resultados.append(contacto)
                break
            elif isinstance(valor, list):
                for elemento in valor:
                    if isinstance(elemento, str) and texto.lower() in elemento.lower():
                        resultados.append(contacto)
                        break    
    return resultados

def eliminar_contacto():
    id_contacto_eliminar = int(input("Ingrese el Id del contacto a eliminar: "))
    contacto = buscar_contacto_id(id_contacto_eliminar)
    if contacto:                
        confirmacion = input("¿Está seguro de que desea eliminar este contacto? (s/n): ").lower()
        if confirmacion == 's':
            contactos.remove(contacto)
            print("Contacto eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
    else:
        print("No se encontró ningún contacto con ese ID.")
    