# sistema_gestion.py

# 1. Importa todas las funciones del módulo de gestión de productos
import gestion_productos

def sistema_gestion_productos():
    # Inicializa la lista de productos (debe estar en el módulo de gestión)
    # Si la lista estuviera aquí, tendrías que pasarla como argumento a todas las funciones.
    
    while True:
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

        if opcion == '1':
            # Llama a la función del módulo importado
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