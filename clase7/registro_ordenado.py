# registro_ordenado.py

print("--- REGISTRO DE CLIENTES ---")
print("Escriba 'fin' en cualquier momento para terminar la carga.")
print("==================================\n")

# Lista donde se guardarán los nombres válidos
lista_clientes = []

# Variable de control del bucle. Inicialmente la ponemos vacía.
nombre_ingresado = ""

# =======================================================
# 1. Bucle While para la carga continua
# =======================================================
# El bucle se repite mientras el nombre ingresado NO sea "fin"
while nombre_ingresado.lower() != "fin":
    
    # Solicita la entrada de nombre
    nombre_ingresado = input("Ingrese el nombre del cliente/a: ").strip()
    
    # ---------------------------------------------------
    # 2. Condición de Salida
    # ---------------------------------------------------
    # Verifica la condición de salida inmediatamente después de la entrada
    if nombre_ingresado.lower() == "fin":
        print("\nCarga finalizada por el usuario.")
        break  # Sale del bucle while
        
    # ---------------------------------------------------
    # 3. Validación de Nombre No Vacío
    # ---------------------------------------------------
    
    # Si el nombre_ingresado NO está vacío después de limpiar espacios (.strip())
    if nombre_ingresado: 
        
        # Guardar cada nombre válido en la lista con .append()
        lista_clientes.append(nombre_ingresado)
        print(f"✅ Cliente '{nombre_ingresado}' agregado.")
        
    else:
        # Muestra la advertencia y el bucle while vuelve a empezar automáticamente
        print("⚠️ Advertencia: El nombre no puede estar vacío. Intente de nuevo.")


# =======================================================
# 4. Procesamiento y Salida Final
# =======================================================

print("\n" + "="*50)
print("       LISTA DE CLIENTES REGISTRADOS Y ORDENADOS")
print("="*50)

if not lista_clientes:
    print("No se registraron clientes.")
else:
    # Ordenar alfabéticamente los nombres
    lista_clientes.sort() # El método .sort() ordena la lista in-place (la modifica directamente)
    
    # Mostrar la lista ordenada utilizando un bucle for
    print("Nombres ordenados alfabéticamente:")
    for nombre in lista_clientes:
        print(f"- {nombre}")

print("==================================\n")