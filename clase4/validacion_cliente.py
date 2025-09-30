# validacion_cliente.py - Jornada 4 Actualización

print("--- REGISTRO, FORMATO Y CLASIFICACIÓN DE CLIENTES ---")

# =======================================================
# 1. SOLICITAR DATOS
# =======================================================
# Solicitud de datos, asegurando que se eliminen espacios iniciales/finales
nombre = input("1. Ingrese el nombre: ").strip()
apellido = input("2. Ingrese el apellido: ").strip()
email = input("3. Ingrese el correo electrónico: ").strip()
edad_str = input("4. Ingrese la edad (debe ser un número): ").strip()

# =======================================================
# 2. PROCESO DE VALIDACIÓN Y FORMATO
# =======================================================

# 2.1. FORMATO REQUERIDO (Se aplica antes de la validación para limpieza)
# Convierte la primera letra de cada palabra a mayúscula, el resto a minúscula.
nombre_formateado = nombre.title()
apellido_formateado = apellido.title()

# 2.2. Validación de Edad (Número y Mayor a 18)
try:
    edad = int(edad_str)
    es_mayor_de_edad = (edad >= 18)
except ValueError:
    edad = 0 
    es_mayor_de_edad = False

# 2.3. Validación de Campos de Texto (No en blanco)
es_nombre_valido = bool(nombre) 
es_apellido_valido = bool(apellido)

# 2.4. VALIDACIÓN DE EMAIL (Requisitos nuevos)
# a) Asegurar que NO tenga espacios internos
email_sin_espacios = email.replace(" ", "")
es_email_sin_espacios = (email == email_sin_espacios)

# b) Asegurar que contenga SOLO UNA "@"
es_una_arroba = (email.count('@') == 1)

# 2.5. Validación Completa (Todos los requisitos obligatorios)
if (es_nombre_valido and es_apellido_valido and 
    es_mayor_de_edad and es_email_sin_espacios and es_una_arroba):
    
    # ===================================================
    # 3. CLASIFICACIÓN Y MOSTRAR DATOS (Éxito)
    # ===================================================
    
    # NUEVO REQUISITO: CLASIFICACIÓN POR RANGO ETARIO
    if edad < 13:
        rango_etario = "Niño/a"
    elif edad < 18:
        rango_etario = "Adolescente"
    else:
        rango_etario = "Adulto/a"
        
    print("\n✅ REGISTRO Y FORMATO EXITOSO.")
    print("-" * 45)
    
    # Muestra los datos usando el formato aplicado
    print(f"NOMBRE COMPLETO: {nombre_formateado} {apellido_formateado}")
    print(f"EDAD:            {edad}")
    print(f"RANGO ETARIO:    {rango_etario}") # Nuevo dato
    print(f"EMAIL:           {email}")
    print("-" * 45)

else:
    # ===================================================
    # 4. MOSTRAR ERROR (Fallo)
    # ===================================================
    print("\nERROR!")
    print("Por favor, revise los requisitos (campos vacíos, edad >= 18, formato de email).")