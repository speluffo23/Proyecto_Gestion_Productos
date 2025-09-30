# registro_productos.py

print("--- REGISTRO DE PRODUCTOS Y PRECIOS ---")
print("Escriba 'fin' en el nombre del producto para terminar la carga.")
print("==================================\n")

# Crear el diccionario donde las CLAVES serán los productos y los VALORES los precios
productos = {}

# =======================================================
# 1. Bucle While para la carga continua
# =======================================================

while True:
    
    # 1. Solicitar el nombre del producto (la clave)
    nombre_producto = input("Ingrese el nombre del producto (o 'fin' para salir): ").strip()
    
    # ---------------------------------------------------
    # 2. Condición de Salida
    # ---------------------------------------------------
    if nombre_producto.lower() == "fin":
        print("\nCarga de productos finalizada.")
        break  # Salimos del bucle
        
    # ---------------------------------------------------
    # 3. Validación y Solicitud del Precio (el valor)
    # ---------------------------------------------------
    
    # Bucle anidado para asegurar que el precio sea válido
    while True:
        try:
            precio_str = input(f"Ingrese el precio de '{nombre_producto}': $").strip()
            precio = float(precio_str)
            
            # Asumimos que el precio debe ser positivo para ser válido
            if precio >= 0:
                break # Sale del bucle de validación de precio
            else:
                print("❌ Error: El precio debe ser un número positivo. Intente de nuevo.")
                
        except ValueError:
            print("❌ Error: Por favor, ingrese un valor numérico para el precio.")
            
    # ---------------------------------------------------
    # 4. Agregar al Diccionario
    # ---------------------------------------------------
    
    # Agregar el par clave-valor al diccionario
    productos[nombre_producto] = precio
    print(f"✅ Producto '{nombre_producto}' agregado con precio ${precio:.2f}.\n")


# =======================================================
# 5. Mostrar el Diccionario Final
# =======================================================

print("\n" + "="*50)
print("             LISTA FINAL DE PRODUCTOS")
print("="*50)

if not productos:
    print("No se registró ningún producto.")
else:
    # Recorrer el diccionario y mostrar los datos
    for clave, valor in productos.items():
        print(f"Producto: {clave:<30} | Precio: ${valor:,.2f}") # Formato para alinear y mostrar 2 decimales

print("="*50)