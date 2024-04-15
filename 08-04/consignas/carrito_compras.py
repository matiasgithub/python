
lista_compras = []
i=0

def calcula_total(lista):
    total = 0
    for elemento in lista:
       # print(elemento)
        total += float(elemento[2])
    return total 

def muestra_lista(lista):
    print(  """
                Carrito:
                Id     Nombre     Precio 
            """)
    for producto in lista:
        print("""     
        {}      {}          {}
        """.format(producto[0], producto[1], producto[2]))
        
total_compra = 0         
while True:   
   
    menu=   """ \n
                MENU PRODUCTOS
                1) Agregar        2) Eliminar 
                3) Ver            4) Finalizar compra
                5) Salir
            """
    muestra_lista(lista_compras)
    print("Total: ",total_compra)
    print(menu)    
    try:
        seleccion = int(input("Ingrese opción:"))   
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue    
    if seleccion not in [1,2,3,4,5]:
        print("Opción inválida. Por favor, elige una opción válida.")
        continue
    if seleccion == 1 :
        i+=1
        producto_id = i
        producto_nombre = input("Ingrese nombre de producto: ")
        producto_precio = float(input("Ingrese precio: "))
        lista_compras.append([i, producto_nombre, producto_precio])
        total_compra = calcula_total(lista_compras)
    if seleccion == 2:
        id_producto_eliminar = int(input("Ingrese el id de producto a eliminar: "))   
        for elemento in lista_compras:
            if elemento[0] == id_producto_eliminar:
                lista_compras.remove(elemento)   
                total_compra = calcula_total(lista_compras) 
    if seleccion == 3:               
        muestra_lista(lista_compras)
    if seleccion == 4:
        print("Compra Finalizada")
        muestra_lista(lista_compras)
        total_compra = calcula_total(lista_compras)
        print("Total: ",total_compra)
        break
    if seleccion == 5:
        break
    
        