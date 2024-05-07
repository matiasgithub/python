def validar_menu():
    while True:
        try:
            seleccion = int(input("Ingrese opción: "))   
            if seleccion not in [1, 2, 3, 4, 5, 6]:
                print("Opción inválida. Por favor, elige una opción válida.")
            else:
                return seleccion
        except ValueError:
            print("Por favor, ingrese un número válido.")
            
def validar_correos(emails):
    while True:
        if all(valida_mail(email) for email in emails):
            return emails
        else:
            print("Al menos uno de los correos electrónicos ingresados no es válido. Inténtalo de nuevo.")
            emails = input("Ingrese los correos electrónicos separados por comas: ").split(',')
def valida_mail(email):
    if not email:
        return True        
    partes = email.split('@')
            
    if len(partes) != 2:
        return False
    
    nombre_usuario, dominio = partes
        
    if not nombre_usuario or not dominio:
        return False
    if '.' not in dominio:
        return False    
    return True
