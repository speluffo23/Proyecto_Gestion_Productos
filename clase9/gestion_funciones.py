# gestion_funciones.py

# Lista global para almacenar los productos. Formato: [[nombre, precio], [nombre, precio], ...]
productos = []

# =======================================================
#               FUNCIONES DE UTILIDAD/VALIDACIÓN
# =======================================================

def validar_entrada_no_vacia(mensaje):
    """Solicita una entrada y se asegura de que no esté vacía."""
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("❌ Error: La entrada no puede estar vacía. Intente de nuevo.")

def validar_precio(mensaje):
    """Solicita un precio y se asegura de que sea un número positivo."""
    while True:
        try:
            precio = float(input(mensaje).strip())
            if precio >= 0:
                return precio
            else:
                print("❌ Error: El precio debe ser positivo. Intente de nuevo.")
        except ValueError:
            print("❌ Error: Por favor, ingrese un valor numérico válido.")

# =======================================================
#               FUNCIONES PRINCIPALES (CRUD)
# =======================================================

def agregar_producto():
    """Permite agregar un nuevo producto (nombre y precio) a la lista."""
    print("\n--- AGREGAR PRODUCTO ---")
    
    # Usamos la función de validación para el nombre
    nombre = validar_entrada_no_vacia("Ingrese el nombre del producto: ")
    
    # Usamos la función de validación para el precio
    precio = validar_precio("Ingrese el precio del producto: $")
    
    # Agregar el producto a la lista como una sublista [nombre, precio]
    productos.append([nombre, precio])
    
    print(f"\n✅ Producto '{nombre}' agregado con éxito.")

def consultar_productos():
    """Muestra todos los productos en la lista con sus precios."""
    print("\n--- PRODUCTOS REGISTRADOS ---")
    
    if not productos:
        print("Aún no hay productos registrados.")
        return

    # Usamos enumerate para mostrar la posición (i + 1)
    for i, (nombre, precio) in enumerate(productos):
        # Usamos :.2f para mostrar el precio con dos decimales
        print(f"[{i + 1}] Nombre: {nombre} | Precio: ${precio:.2f}")

    print("-" * 50)

def eliminar_producto():
    """Elimina un producto de la lista a partir de su nombre."""
    print("\n--- ELIMINAR PRODUCTO ---")
    
    if not productos:
        print("No hay productos para eliminar.")
        return
        
    # Usamos la función de validación para el nombre
    nombre_a_eliminar = validar_entrada_no_vacia("Ingrese el nombre del producto a eliminar: ").strip().title()
    
    encontrado = False
    
    # Recorremos la lista para buscar el producto
    for producto in productos:
        # product[0] es el nombre del producto en la sublista
        if producto[0].title() == nombre_a_eliminar: 
            
            # Eliminamos el producto de la lista
            productos.remove(producto)
            print(f"\n✅ Producto '{nombre_a_eliminar}' eliminado con éxito.")
            encontrado = True
            break
            
    if not encontrado:
        print(f"❌ Error: Producto '{nombre_a_eliminar}' no encontrado en la lista.")


# =======================================================
#               MENÚ INTERACTIVO PRINCIPAL
# =======================================================

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "=" * 40)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("=" * 40)
    print("[1] Agregar Producto")
    print("[2] Consultar Productos")
    print("[3] Eliminar Producto")
    print("[4] Salir del Programa")
    print("-" * 40)

def sistema_gestion():
    """Función principal que contiene el menú interactivo."""
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            consultar_productos()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            print("\n👋 ¡Gracias por usar el Sistema de Gestión! Saliendo...")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número del 1 al 4.")

# Punto de inicio del programa
if __name__ == "__main__":
    sistema_gestion()