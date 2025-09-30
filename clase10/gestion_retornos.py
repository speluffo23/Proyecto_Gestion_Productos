# gestion_retornos.py

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
#               FUNCIONES PRINCIPALES (CON RETORNO)
# =======================================================

def agregar_producto(lista_actual_productos):
    """Permite agregar un producto. Devuelve la lista modificada."""
    print("\n--- AGREGAR PRODUCTO ---")
    
    nombre = validar_entrada_no_vacia("Ingrese el nombre del producto: ")
    precio = validar_precio("Ingrese el precio del producto: $")
    
    # Se agrega el producto a la lista que se pasó como argumento
    lista_actual_productos.append([nombre, precio])
    
    print(f"\n✅ Producto '{nombre}' agregado con éxito.")
    
    # Retorna la lista con el nuevo producto para que el sistema principal la use
    return lista_actual_productos

def consultar_productos(lista_actual_productos):
    """Muestra todos los productos en la lista. No necesita retornar la lista."""
    print("\n--- PRODUCTOS REGISTRADOS ---")
    
    if not lista_actual_productos:
        print("Aún no hay productos registrados.")
        # Simplemente retorna la lista sin cambios
        return lista_actual_productos 

    for i, (nombre, precio) in enumerate(lista_actual_productos):
        print(f"[{i + 1}] Nombre: {nombre} | Precio: ${precio:.2f}")

    print("-" * 50)
    # Retorna la lista (sin cambios, ya que solo es consulta)
    return lista_actual_productos

def eliminar_producto(lista_actual_productos):
    """Elimina un producto de la lista a partir de su nombre. Devuelve la lista modificada."""
    print("\n--- ELIMINAR PRODUCTO ---")
    
    if not lista_actual_productos:
        print("No hay productos para eliminar.")
        return lista_actual_productos # Retorna la lista sin cambios
        
    nombre_a_eliminar = validar_entrada_no_vacia("Ingrese el nombre del producto a eliminar: ").strip().title()
    
    encontrado = False
    
    # Recorremos la lista para buscar el producto
    for producto in lista_actual_productos:
        # product[0] es el nombre del producto en la sublista
        if producto[0].title() == nombre_a_eliminar: 
            
            # Eliminamos el producto de la lista
            lista_actual_productos.remove(producto)
            print(f"\n✅ Producto '{nombre_a_eliminar}' eliminado con éxito.")
            encontrado = True
            break
            
    if not encontrado:
        print(f"❌ Error: Producto '{nombre_a_eliminar}' no encontrado en la lista.")
    
    # Retorna la lista (ya sea modificada o sin cambios)
    return lista_actual_productos

# =======================================================
#               MENÚ INTERACTIVO PRINCIPAL
# =======================================================

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n" + "=" * 40)
    print("  SISTEMA DE GESTIÓN DE PRODUCTOS (Retornos)")
    print("=" * 40)
    print("[1] Agregar Producto")
    print("[2] Consultar Productos")
    print("[3] Eliminar Producto")
    print("[4] Salir del Programa")
    print("-" * 40)

def sistema_gestion():
    """Función principal que maneja la lista y el menú interactivo."""
    
    # La lista de productos se mantiene AQUI (en el scope de la función principal)
    productos_actuales = []
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        # En cada llamada, el sistema ACTUALIZA la lista con el valor retornado
        if opcion == '1':
            productos_actuales = agregar_producto(productos_actuales)
        elif opcion == '2':
            productos_actuales = consultar_productos(productos_actuales)
        elif opcion == '3':
            productos_actuales = eliminar_producto(productos_actuales)
        elif opcion == '4':
            print("\n👋 ¡Gracias por usar el Sistema de Gestión! Saliendo...")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número del 1 al 4.")

# Punto de inicio del programa
if __name__ == "__main__":
    sistema_gestion()