nombres=[]
stocks=[]
precios=[]


def cargarProducto():
    print("Bienvenido a la carga de producto ")
    ccargaP=int(input("Cuantos productos va a cargar "))
    for i in range(ccargaP):
        nombre=input("Ingrese el nombre del producto  ")
        stock=int(input(f"Ingrese el stock de {nombre}  "))
        precio=int(input(f"Ingrese el precio de {nombre}  "))
        nombres.append(nombre)
        stocks.append(stock)
        precios.append(precio)

def listarProducto():
    if (len(nombres)==0):
        print("No hay productos cargado para mostrar. ")
        ejecutarMenu()
    print("Bienvenido al listado de productos  ")
    for i in range(len(nombres)):
        print(f"""
              Producto: {nombres[i]} 
              Stock:    {stocks[i]} 
              Precio:   {precios[i]}""")

def menu():
    print("Bienvenido al programa de stock ")
    print("""
    1) Cargar Producto
    2) Listar Producto
    3) Editar Producto
    4) Eliminar Producto
    5) Salir 
    """)
    
def ejecutarMenu():
    while True:
        menu()        
        eleccion=input("Ingrese una opcion valida ")
        if(eleccion=="1"):
            print("Elegiste Opcion 1 Cargar Producto ")
            cargarProducto()
        elif(eleccion=="2"):
            print("Elegiste Opcion 2 Listar Producto ")
            listarProducto()
        elif(eleccion=="3"):
            print("Elegiste Opcion 3 Editar Producto ")    
        elif(eleccion=="4"):
            print("Elegiste Opcion 4 Eliminar Producto ")
        elif(eleccion=="5"):
            print("Elegiste Opcion 5 Salir ")
            print("Adios ")
            break
        else:
            print("Elegiste Cualquiera ")
    

ejecutarMenu()
