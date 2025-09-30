# gestion_productos.py

# Lista global para almacenar todos los productos
productos = []

# 1. Importa las funciones de validación para poder usarlas
import validaciones 

# =================================================================
#                       FUNCIONES CRUD
# =================================================================

def agregar_producto():
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    # Llama a las funciones importadas
    nombre = validaciones.validar_entrada_no_vacia("Ingrese el nombre del producto: ")
    categoria = validaciones.validar_entrada_no_vacia("Ingrese la categoría del producto: ")
    precio = validaciones.validar_precio_entero("Ingrese el precio del producto (sin centavos): ")
    
    nuevo_producto = [nombre, categoria, precio]
    productos.append(nuevo_producto)
    
    print(f"\n✅ Producto '{nombre}' agregado con éxito.")

def visualizar_productos():
    print("\n--- PRODUCTOS REGISTRADOS ---")
    
    if not productos:
        print("Aún no hay productos registrados.")
        return

    for i in range(len(productos)):
        nombre, categoria, precio = productos[i] 
        print(f"[{i + 1}] Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

    print("-" * 50)

def buscar_productos():
    print("\n--- BUSCAR PRODUCTOS ---")
    
    if not productos:
        print("No hay productos para buscar.")
        return

    termino_busqueda = validaciones.validar_entrada_no_vacia("Ingrese el nombre del producto a buscar: ").lower()
    
    resultados = []
    
    for producto in productos:
        nombre = producto[0]
        if termino_busqueda in nombre.lower():
            resultados.append(producto)
            
    if resultados:
        print("\n✅ Se encontraron los siguientes productos:")
        for nombre, categoria, precio in resultados:
            print(f"-> Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    else:
        print(f"❌ No se encontraron resultados para '{termino_busqueda}'.")

def eliminar_producto():
    visualizar_productos() 
    
    if not productos:
        return 

    print("\n--- ELIMINAR PRODUCTO ---")
    
    while True:
        try:
            posicion_str = input("Ingrese el número del producto a eliminar (o '0' para cancelar): ").strip()
            
            if posicion_str == '0':
                print("Operación cancelada.")
                return

            posicion = int(posicion_str)
            indice = posicion - 1 
            
            if 0 <= indice < len(productos):
                producto_eliminado = productos.pop(indice) 
                nombre_eliminado = producto_eliminado[0]
                print(f"\n✅ Producto N°{posicion} ({nombre_eliminado}) eliminado con éxito.")
                break
            else:
                print(f"❌ Error: El número ingresado ({posicion}) está fuera del rango. Intente de nuevo.")

        except ValueError:
            print("❌ Error: Por favor, ingrese un número válido.")