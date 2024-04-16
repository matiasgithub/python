def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")

def verificar_ganador(tablero, jugador):   
    for fila in tablero:#verifico columnas
        todas_iguales = True
        for casilla in fila:
            if casilla != jugador:
                todas_iguales = False
                break            
            if todas_iguales:
                return True
        return False
        
    for columna in range(3):#verifico columnas
        todas_iguales = True
        for fila in range(3):
            if tablero[fila][columna] != jugador:
                todas_iguales = False
                break
            if todas_iguales:
                return True
        return False
    
    for i in range(3):#verifico diagonales
        if tablero[i][i] != jugador:
            diagonal1_iguales = False
        if tablero[i][2 - i] != jugador:
            diagonal2_iguales = False
            
    if diagonal1_iguales or diagonal2_iguales:
        return True

    return False        

tablero = [[" "," "," "],[" "," "," "],[" "," "," "]];        
jugadores = ["X", "O"]
indice = 0
i = 0

while True:
    imprimir_tablero(tablero)    
    jugador_actual = jugadores[indice]
    posicion = input(f"Jugador {jugador_actual}, ingrese fila y columna separadas por espacio(por ejemplo, 1 2): ")
    fila, columna = map(int, posicion.split())   
    
    try:
        fila, columna = map(int, posicion.split())
        if fila < 1 or fila > 3 or columna < 1 or columna > 3:
            print("Los valores de fila y columna deben estar entre 1 y 3. Intenta nuevamente.")
            continue
    except ValueError:
        print("Por favor, ingrese valores numéricos para fila y columna. Intenta nuevamente.")
        continue 
    
    if tablero[fila-1][columna-1] != " ":
            print("Esa casilla ya está ocupada. Intenta nuevamente.")
            continue
        
    tablero[fila-1][columna-1] = jugador_actual #coloco la pieza
    
    if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

    if all([casilla != " " for fila in tablero for casilla in fila]):
            imprimir_tablero(tablero)
            print("¡Empate!")
            break    
    indice = 1 - indice #cambio de jugador    