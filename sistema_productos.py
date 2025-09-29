# Lista global para almacenar todos los productos
# Formato de cada sublista: [nombre, categoría, precio]
productos = []

# =================================================================
#                         FUNCIONES DE VALIDACIÓN
# =================================================================

def validar_entrada_no_vacia(mensaje):
    """Solicita una entrada y se asegura de que no esté vacía."""
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("❌ Error: La entrada no puede estar vacía. Intente de nuevo.")

def validar_precio_entero(mensaje):
    """Solicita un precio y se asegura de que sea un número entero positivo."""
    while True:
        entrada = input(mensaje).strip()
        
        # Validación de que sean dígitos y que sea positivo
        if entrada.isdigit() and int(entrada) >= 0:
            return int(entrada)
        else:
            print("❌ Error: El precio debe ser un número entero positivo (sin centavos). Intente de nuevo.")

# =================================================================
#                       1. AGREGAR PRODUCTO
# =================================================================

def agregar_producto():
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    
    # Requisito: Usar validación
    nombre = validar_entrada_no_vacia("Ingrese el nombre del producto: ")
    categoria = validar_entrada_no_vacia("Ingrese la categoría del producto: ")
    precio = validar_precio_entero("Ingrese el precio del producto (sin centavos): ")
    
    # Requisito: Almacenar como sublista
    nuevo_producto = [nombre, categoria, precio]
    
    # Requisito: Usar lista para almacenar datos
    productos.append(nuevo_producto)
    
    print(f"\n✅ Producto '{nombre}' agregado con éxito.")

# =================================================================
#                       2. VISUALIZAR PRODUCTOS
# =================================================================

def visualizar_productos():
    print("\n--- PRODUCTOS REGISTRADOS ---")
    
    # Condicional para manejar lista vacía
    if not productos:
        print("Aún no hay productos registrados.")
        return

    # Requisito: Usar bucle 'for' para recorrer y presentar ordenado y numerado
    for i in range(len(productos)):
        nombre, categoria, precio = productos[i] # Desempaquetado para claridad
        
        # Mostrar cada producto numerado (i + 1)
        print(f"[{i + 1}] Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")

    print("-" * 50)

# =================================================================
#                       3. BÚSQUEDA DE PRODUCTOS
# =================================================================

def buscar_productos():
    print("\n--- BUSCAR PRODUCTOS ---")
    
    if not productos:
        print("No hay productos para buscar.")
        return

    termino_busqueda = validar_entrada_no_vacia("Ingrese el nombre del producto a buscar: ").lower()
    
    resultados = []
    
    # Requisito: Usar bucle 'for' para revisar cada producto
    for producto in productos:
        nombre = producto[0]
        
        # Condicional para la coincidencia (búsqueda parcial e insensible a mayúsculas)
        if termino_busqueda in nombre.lower():
            resultados.append(producto)
            
    if resultados:
        print("\n✅ Se encontraron los siguientes productos:")
        # Bucle 'for' para mostrar resultados
        for nombre, categoria, precio in resultados:
            print(f"-> Nombre: {nombre} | Categoría: {categoria} | Precio: ${precio}")
    else:
        # Requisito: Informar si no hay coincidencias
        print(f"❌ No se encontraron resultados para '{termino_busqueda}'.")

# =================================================================
#                       4. ELIMINACIÓN DE PRODUCTOS
# =================================================================

def eliminar_producto():
    visualizar_productos() # Muestra la lista para que el usuario elija el número
    
    if not productos:
        return # Sale si no hay productos

    print("\n--- ELIMINAR PRODUCTO ---")
    
    # Requisito: Usar bucle 'while' para la validación de entrada
    while True:
        try:
            posicion_str = input("Ingrese el número del producto a eliminar (o '0' para cancelar): ").strip()
            
            if posicion_str == '0':
                print("Operación cancelada.")
                return

            posicion = int(posicion_str)
            
            # La posición del usuario es 1-basada, el índice de la lista es 0-basado
            indice = posicion - 1 
            
            # Requisito: Usar condicional para validar el índice
            if 0 <= indice < len(productos):
                producto_eliminado = productos.pop(indice) 
                nombre_eliminado = producto_eliminado[0]
                print(f"\n✅ Producto N°{posicion} ({nombre_eliminado}) eliminado con éxito.")
                break
            else:
                print(f"❌ Error: El número ingresado ({posicion}) está fuera del rango. Intente de nuevo.")

        except ValueError:
            print("❌ Error: Por favor, ingrese un número válido.")
            
# =================================================================
#                        MENÚ PRINCIPAL
# =================================================================

def sistema_gestion_productos():
    
    # Requisito: El programa debe continuar funcionando hasta que se elija una opción para salir
    while True: # Bucle 'while' principal
        print("\n" + "=" * 50)
        print("  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
        print("=" * 50)
        print("[1] Agregar Producto")
        print("[2] Visualizar Productos")
        print("[3] Buscar Productos por Nombre")
        print("[4] Eliminar Producto")
        print("[5] Salir del Sistema")
        print("-" * 50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        # Requisito: Usar condicionales para gestionar las opciones del menú
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            visualizar_productos()
        elif opcion == '3':
            buscar_productos()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el Sistema de Gestión! Saliendo...")
            break # Sale del bucle 'while'
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número del 1 al 5.")

# Punto de inicio de la aplicación
if __name__ == "__main__":
    sistema_gestion_productos()