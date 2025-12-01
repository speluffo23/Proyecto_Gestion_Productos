# ===============================================
# SISTEMA DE GESTIÓN DE INVENTARIO BÁSICO EN PYTHON
# ===============================================

# La base de datos de inventario (en memoria)
inventario = [] 
PRODUCTO_ID = 1
UMBRAL_BAJO_STOCK = 10 # Se considera 'bajo stock' si la cantidad es menor o igual a 10

# -----------------------------------------------
# FUNCIONES DE GESTIÓN
# -----------------------------------------------

def registrar_producto():
    """Opción 1: Solicita los datos del producto y lo agrega al inventario."""
    # 🔥 CORRECCIÓN CLAVE: global al inicio, antes de cualquier uso/modificación
    global PRODUCTO_ID, inventario 
    print("\n--- 1. REGISTRAR PRODUCTO ---")
    
    nombre = input("Ingrese el nombre del producto: ").strip().capitalize()
    
    while True:
        try:
            precio = float(input("Ingrese el precio (ej: 10.50): "))
            if precio <= 0:
                print("El precio debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número para el precio.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero para la cantidad.")

    nuevo_producto = {
        'id': PRODUCTO_ID,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    }
    
    inventario.append(nuevo_producto)
    PRODUCTO_ID += 1
    print(f"\n✅ Producto '{nombre}' registrado con ID: {nuevo_producto['id']}.")

def mostrar_todos():
    """Opción 2: Muestra una lista de todos los productos en el inventario."""
    print("\n--- 2. MOSTRAR TODOS LOS PRODUCTOS ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    print("{:<5} | {:<20} | {:<10} | {:<10}".format("ID", "NOMBRE", "PRECIO", "CANTIDAD"))
    print("-" * 50)
    for prod in inventario:
        print("{:<5} | {:<20} | ${:<9.2f} | {:<10}".format(
            prod['id'], prod['nombre'], prod['precio'], prod['cantidad']
        ))
    print("-" * 50)

def actualizar_producto():
    """Opción 3: Permite modificar el precio o la cantidad de un producto por su ID."""
    print("\n--- 3. ACTUALIZAR PRODUCTO ---")
    if not inventario:
        print("El inventario está vacío. Nada para actualizar.")
        return

    mostrar_todos()
    
    try:
        id_a_buscar = int(input("Ingrese el ID del producto a actualizar: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    producto_encontrado = next((p for p in inventario if p['id'] == id_a_buscar), None)

    if producto_encontrado:
        print(f"Producto encontrado: {producto_encontrado['nombre']} | Precio actual: ${producto_encontrado['precio']} | Stock actual: {producto_encontrado['cantidad']}")
        
        # Actualizar Precio
        while True:
            nuevo_precio_str = input(f"Ingrese nuevo precio (o presione Enter para mantener {producto_encontrado['precio']}): ")
            if not nuevo_precio_str:
                break
            try:
                nuevo_precio = float(nuevo_precio_str)
                if nuevo_precio > 0:
                    producto_encontrado['precio'] = nuevo_precio
                    break
                else:
                    print("El precio debe ser un número positivo.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        # Actualizar Cantidad
        while True:
            nueva_cantidad_str = input(f"Ingrese nueva cantidad (o presione Enter para mantener {producto_encontrado['cantidad']}): ")
            if not nueva_cantidad_str:
                break
            try:
                nueva_cantidad = int(nueva_cantidad_str)
                if nueva_cantidad >= 0:
                    producto_encontrado['cantidad'] = nueva_cantidad
                    break
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        print(f"\n✅ Producto con ID {id_a_buscar} actualizado.")
    else:
        print(f"\n❌ Producto con ID {id_a_buscar} no encontrado.")

def eliminar_producto():
    """Opción 4: Elimina un producto del inventario por su ID."""
    
    # 🔥 SOLUCIÓN: DEBE SER LA PRIMERA LÍNEA EJECUTABLE (o después del docstring)
    global inventario 
    
    print("\n--- 4. ELIMINAR PRODUCTO ---")
    if not inventario:
        print("El inventario está vacío. Nada para eliminar.")
        return

    mostrar_todos()

    try:
        id_a_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("El ID debe ser un número entero.")
        return

    # A partir de aquí, el uso de inventario es seguro porque se declaró global arriba.
    inventario_antes = len(inventario)
    inventario = [p for p in inventario if p['id'] != id_a_eliminar]
    inventario_despues = len(inventario)

    if inventario_antes > inventario_despues:
        print(f"\n✅ Producto con ID {id_a_eliminar} eliminado.")
    else:
        print(f"\n❌ Producto con ID {id_a_eliminar} no encontrado.")

def buscar_producto():
    """Opción 5: Busca productos por nombre (coincidencia parcial) o ID."""
    print("\n--- 5. BUSCAR PRODUCTO ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    termino_busqueda = input("Ingrese el nombre o ID del producto a buscar: ").strip()
    resultados = []

    try:
        # Intentar buscar por ID
        id_busqueda = int(termino_busqueda)
        resultados = [p for p in inventario if p['id'] == id_busqueda]
    except ValueError:
        # Si no es un número, buscar por nombre (coincidencia parcial)
        term_lower = termino_busqueda.lower()
        resultados = [p for p in inventario if term_lower in p['nombre'].lower()]

    if resultados:
        print(f"\nSe encontraron {len(resultados)} producto(s):")
        print("{:<5} | {:<20} | {:<10} | {:<10}".format("ID", "NOMBRE", "PRECIO", "CANTIDAD"))
        print("-" * 50)
        for prod in resultados:
            print("{:<5} | {:<20} | ${:<9.2f} | {:<10}".format(
                prod['id'], prod['nombre'], prod['precio'], prod['cantidad']
            ))
        print("-" * 50)
    else:
        print(f"\n❌ No se encontraron productos con el término '{termino_busqueda}'.")

def reporte_bajo_stock():
    """Opción 6: Muestra todos los productos cuya cantidad es <= UMBRAL_BAJO_STOCK."""
    print("\n--- 6. REPORTE BAJO STOCK ---")
    if not inventario:
        print("El inventario está vacío.")
        return

    productos_bajos = [p for p in inventario if p['cantidad'] <= UMBRAL_BAJO_STOCK]

    if productos_bajos:
        print(f"🚨 ¡ATENCIÓN! Productos con stock menor o igual a {UMBRAL_BAJO_STOCK}:")
        print("{:<5} | {:<20} | {:<10} | {:<10}".format("ID", "NOMBRE", "PRECIO", "CANTIDAD"))
        print("-" * 50)
        for prod in productos_bajos:
            print("{:<5} | {:<20} | ${:<9.2f} | {:<10}".format(
                prod['id'], prod['nombre'], prod['precio'], prod['cantidad']
            ))
        print("-" * 50)
    else:
        print("✅ No hay productos con stock bajo. ¡Inventario saludable!")

# -----------------------------------------------
# FUNCIÓN PRINCIPAL (MAIN LOOP)
# -----------------------------------------------

def main():
    """Función principal que ejecuta el menú interactivo."""
    while True:
        print("\n" + "="*30)
        print("  GESTIÓN DE INVENTARIO")
        print("="*30)
        print("1. Registrar Producto")
        print("2. Mostrar Todos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print(f"6. Reporte Bajo Stock (Umbral: {UMBRAL_BAJO_STOCK})")
        print("7. Salir")
        print("-" * 30)

        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            mostrar_todos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print("\n👋 Gracias por usar el sistema. ¡Adiós!")
            break
        else:
            print("\n❌ Opción no válida. Por favor, ingrese un número del 1 al 7.")
            
if __name__ == "__main__":
    main()