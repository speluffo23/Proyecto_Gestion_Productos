import sqlite3

NOMBRE_DB = "inventario.db"

def conectar_db():
    """Establece la conexión a la base de datos y crea el cursor."""
    try:
        # 1. Establecer conexión al archivo (o crearlo si no existe)
        conexion = sqlite3.connect(NOMBRE_DB)
        # 2. Crear un objeto cursor para ejecutar comandos SQL
        cursor = conexion.cursor()
        print(f"✔️ Conexión exitosa a {NOMBRE_DB}.")
        return conexion, cursor
    except sqlite3.Error as e:
        print(f"❌ Error al conectar con la base de datos: {e}")
        return None, None

def crear_tabla(cursor, conexion):
    """Crea la tabla 'articulos' si aún no existe."""
    # Sentencia SQL para definir la estructura de la tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articulos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL)
    ''')
    # Confirmar los cambios
    conexion.commit()
    print("✅ Tabla 'articulos' creada o ya existente.")

def agregar_articulo(cursor, conexion):
    """Solicita datos y realiza la operación INSERT."""
    print("\n--- 1. Agregar Nuevo Artículo (INSERT) ---")
    try:
        nombre = input("Nombre del artículo: ").strip()
        cantidad = int(input("Cantidad en stock (entero): "))
        precio = float(input("Precio unitario (decimal): "))
        
        if not nombre or cantidad < 0 or precio < 0:
            raise ValueError("Datos no válidos. Nombre no puede estar vacío y cantidad/precio deben ser positivos.")
            
        # Sentencia INSERT con parámetros (?)
        cursor.execute('''
            INSERT INTO articulos (nombre, cantidad, precio)
            VALUES (?, ?, ?)
        ''', (nombre, cantidad, precio))
        
        conexion.commit()
        print(f"✔️ Artículo '{nombre}' agregado exitosamente al inventario.")
        
    except ValueError as e:
        print(f"❌ Error de entrada de datos: {e}. Asegúrese de ingresar números válidos.")
    except sqlite3.Error as e:
        print(f"❌ Error de base de datos al insertar: {e}")


def ver_inventario(cursor):
    """Realiza la operación SELECT y muestra todos los registros."""
    print("\n--- 2. Inventario Actual (SELECT) ---")
    
    # Sentencia SELECT para obtener todos los datos
    cursor.execute('SELECT id, nombre, cantidad, precio FROM articulos ORDER BY id ASC')
    articulos = cursor.fetchall() # Recupera todos los resultados
    
    if not articulos:
        print("El inventario está vacío.")
        return

    # Imprimir la tabla de resultados
    print("--------------------------------------------------")
    print(f"| {'ID':<3} | {'Nombre':<15} | {'Stock':<6} | {'Precio':<8} |")
    print("--------------------------------------------------")
    
    for id, nombre, cantidad, precio in articulos:
        print(f"| {id:<3} | {nombre:<15} | {cantidad:<6} | ${precio:<7.2f} |")
        
    print("--------------------------------------------------")


def actualizar_precio(cursor, conexion):
    """Solicita ID y nuevo precio, luego realiza la operación UPDATE."""
    print("\n--- 3. Actualizar Precio (UPDATE) ---")
    try:
        id_articulo = int(input("Ingrese el ID del artículo a actualizar: "))
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        
        if nuevo_precio < 0:
            raise ValueError("El precio debe ser un valor positivo.")
        
        # Sentencia UPDATE con cláusula WHERE
        cursor.execute('UPDATE articulos SET precio = ? WHERE id = ?', (nuevo_precio, id_articulo))
        
        if cursor.rowcount == 0:
            print(f"⚠️ No se encontró ningún artículo con ID: {id_articulo}. No se realizaron cambios.")
        else:
            conexion.commit()
            print(f"🔄 Precio del artículo ID {id_articulo} actualizado a ${nuevo_precio:.2f}.")

    except ValueError:
        print("❌ Error: Debe ingresar números válidos para el ID y el precio.")
    except sqlite3.Error as e:
        print(f"❌ Error de base de datos al actualizar: {e}")


def eliminar_articulo(cursor, conexion):
    """Solicita ID y realiza la operación DELETE."""
    print("\n--- 4. Eliminar Artículo (DELETE) ---")
    try:
        id_articulo = int(input("Ingrese el ID del artículo a eliminar: "))
        
        # Sentencia DELETE con cláusula WHERE
        cursor.execute('DELETE FROM articulos WHERE id = ?', (id_articulo,))
        
        if cursor.rowcount == 0:
            print(f"⚠️ No se encontró ningún artículo con ID: {id_articulo}. No se eliminó nada.")
        else:
            conexion.commit()
            print(f"🗑️ Artículo ID {id_articulo} eliminado exitosamente.")

    except ValueError:
        print("❌ Error: Debe ingresar un ID numérico válido.")
    except sqlite3.Error as e:
        print(f"❌ Error de base de datos al eliminar: {e}")


def mostrar_menu():
    """Función para mostrar el menú de opciones."""
    print("\n====================================")
    print("🚀 SISTEMA DE GESTIÓN DE INVENTARIO")
    print("====================================")
    print("1. Agregar Artículo (INSERT)")
    print("2. Ver Inventario Completo (SELECT)")
    print("3. Actualizar Precio (UPDATE)")
    print("4. Eliminar Artículo (DELETE)")
    print("5. Salir")
    print("------------------------------------")


def main():
    """Función principal que ejecuta el programa."""
    conexion, cursor = conectar_db()
    
    if not conexion:
        return # Sale si falla la conexión

    # Configuración inicial: Asegura que la tabla exista
    crear_tabla(cursor, conexion)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            agregar_articulo(cursor, conexion)
        elif opcion == '2':
            ver_inventario(cursor)
        elif opcion == '3':
            actualizar_precio(cursor, conexion)
        elif opcion == '4':
            eliminar_articulo(cursor, conexion)
        elif opcion == '5':
            print("\n👋 ¡Hasta luego! Cerrando conexión con la base de datos.")
            conexion.close()
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()