# Importar colorama para la estética
from colorama import Fore, Back, Style, init
from datetime import datetime

# Inicializar colorama (necesario en algunos sistemas)
init(autoreset=True)

# 1. Función para agregar producto con fecha/hora
def agregar_producto(lista_productos, nombre_producto):
    # Obtener la fecha y hora actuales
    fecha_compra = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crear el registro del producto
    producto = {
        "nombre": nombre_producto,
        "fecha_compra": fecha_compra
    }
    lista_productos.append(producto)

    # 2. Usar colorama para una mejor interacción
    mensaje = f"\n{Fore.GREEN}{Style.BRIGHT}✅ Producto '{nombre_producto}' agregado con fecha: {fecha_compra}{Style.RESET_ALL}"
    print(mensaje)

# Ejemplo de uso en tu programa principal
productos = []
agregar_producto(productos, "Leche")
agregar_producto(productos, "Pan")

print(f"\nLista actual de productos: {productos}")