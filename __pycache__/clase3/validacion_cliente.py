# validacion_cliente.py

print("--- REGISTRO Y VALIDACIÓN DE DATOS DEL CLIENTE ---")

# =======================================================
# 1. SOLICITAR DATOS
# =======================================================
# Usamos .strip() para eliminar espacios en blanco al inicio o final.
nombre = input("1. Ingrese el nombre: ").strip()
apellido = input("2. Ingrese el apellido: ").strip()
email = input("3. Ingrese el correo electrónico: ").strip()
edad_str = input("4. Ingrese la edad (debe ser un número): ").strip()

# =======================================================
# 2. PROCESO DE VALIDACIÓN
# =======================================================

# 2.1. Validación de Edad (Número y Mayor a 18)
try:
    # Intenta convertir la edad a un entero
    edad = int(edad_str)
    
    # Valida que la edad sea mayor o igual a 18
    es_mayor_de_edad = (edad >= 18)
    
except ValueError:
    # Si la conversión a int falla (ej: ingresó texto), la edad es inválida
    edad = 0 
    es_mayor_de_edad = False

# 2.2. Validación de Campos de Texto (No en blanco)
es_nombre_valido = bool(nombre) # bool('') es False, bool('algo') es True
es_apellido_valido = bool(apellido)
es_email_valido = bool(email)

# 2.3. Condición General: Todos los campos deben ser válidos
if es_nombre_valido and es_apellido_valido and es_email_valido and es_mayor_de_edad:
    
    # ===================================================
    # 3. MOSTRAR DATOS (Éxito)
    # ===================================================
    print("\n✅ DATOS VÁLIDOS. REGISTRO EXITOSO.")
    print("-" * 30)
    print(nombre)
    print(apellido)
    print(edad)
    print(email)
    print("-" * 30)

else:
    # ===================================================
    # 3. MOSTRAR ERROR (Fallo)
    # ===================================================
    print("\nERROR!")