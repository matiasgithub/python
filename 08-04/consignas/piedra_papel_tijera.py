import random
ppt = {1 : "Piedra", 2 :"Papel", 3:"Tijera"}

while True:
    eleccion_maquina = random.choice(list(ppt.keys()))
    eleccion_usuario= int (input("""    
        Elija una opción\n
        1-Piedra  2-Papel  3-Tijera \n
        Ingrese el número correspondiente:
        """))
    
    if eleccion_usuario not in ppt:
        print("Opción inválida. Por favor, elige una opción válida.")
        continue
    
    print("La máquina ha elegido:", ppt[eleccion_maquina])
    print("Tú has elegido:", ppt[eleccion_usuario])
    
    if eleccion_usuario == eleccion_maquina:
        print("Empate")
    elif (eleccion_usuario == 1 and eleccion_maquina == 3) or \
            (eleccion_usuario == 2 and eleccion_maquina == 1) or \
            (eleccion_usuario == 3 and eleccion_maquina == 2):
            print("¡Has ganado!")
    else:
            print("¡La máquina gana!")
            
    continuar = input("¿Quieres volver a jugar? (s/n): ")
    
    if continuar.lower() != 's':
        break       
