# procesamiento_clientes.py

print("--- PROCESAMIENTO DE CLIENTES TECHLAB ---")
print("========================================\n")

# 1. Crear la lista de clientes (incluyendo una cadena vacía para la prueba)
clientes = [
    "Mariana",
    "Luis",
    "",           # Cadena vacía para probar la validación
    "Elena",
    "Diego",
    "Sofía",
    " "           # Cadena con solo espacios (también se considera vacío al usar .strip())
]

# =======================================================
# 2. Recorrer la lista y mostrar posición + nombre
# =======================================================

# Usamos enumerate() para obtener el índice (index) y el nombre (nombre_cliente)
# El 'start=1' hace que la numeración empiece en 1 (Cliente 1), en lugar de 0 (índice real).
for index, nombre_cliente in enumerate(clientes, start=1):
    
    # Eliminamos espacios en blanco innecesarios para la validación
    nombre_limpio = nombre_cliente.strip()
    
    # ---------------------------------------------------
    # 3. Validar si la cadena está vacía
    # ---------------------------------------------------
    
    if nombre_limpio: # Esto evalúa a True si la cadena no está vacía
        
        # Muestra el nombre y su posición
        print(f"✅ Cliente {index}: {nombre_limpio}")
        
    else:
        
        # Muestra el mensaje de alerta si está vacío (o solo tiene espacios)
        print(f"⚠️ Cliente {index}: [ALERTA] Dato no válido (Nombre vacío).")

print("\n========================================")
print("Procesamiento de lista finalizado.")