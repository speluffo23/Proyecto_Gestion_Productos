# sistema_gestion.py

import gestion_productos

def sistema_gestion_productos():
    """
    Función principal que ejecuta el menú interactivo para la gestión de productos.
    """
    while True:
        print("\n" + "=" * 50)
        print("  SISTEMA DE GESTIÓN BÁSICA DE PRODUCTOS")
        print("=" * 50)
        print("[01] Agregar Producto")
        print("[02] Visualizar Productos")
        print("[03] Buscar Productos por Nombre")
        print("[04] Eliminar Producto")
        print("[05] Salir del Sistema")
        print("-" * 50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()

        if opcion == '1':
            gestion_productos.agregar_producto()
        elif opcion == '2':
            gestion_productos.visualizar_productos()
        elif opcion == '3':
            gestion_productos.buscar_productos()
        elif opcion == '4':
            gestion_productos.eliminar_producto()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el Sistema de Gestión! Saliendo...")
            break
        else:
            print("\n❌ Opción no válida. Por favor, seleccione un número del 1 al 5.")

if __name__ == "__main__":
    sistema_gestion_productos()