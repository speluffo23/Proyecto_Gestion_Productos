# validacion_cliente.py - Solución Final TechLab

print("--- REGISTRO, FORMATO Y CLASIFICACIÓN DE CLIENTES ---")

# =======================================================
# 1. SOLICITAR DATOS
# =======================================================
nombre = input("1. Ingrese el nombre: ").strip()
apellido = input("2. Ingrese el apellido: ").strip()
email = input("3. Ingrese el correo electrónico: ").strip()
edad_str = input("4. Ingrese la edad (debe ser un número): ").strip()

# =======================================================
# 2. PROCESO DE VALIDACIÓN Y FORMATO
# =======================================================

# 2.1. FORMATO REQUERIDO
nombre_formateado = nombre.title()
apellido_formateado = apellido.title()

# 2.2. Validación de Edad (Número y Mayor a CERO)
try:
    edad = int(edad_str)
    # ÚNICA VALIDACIÓN DE EDAD: Que sea un número válido y positivo
    es_edad_positiva = (edad >= 1) 
    
except ValueError:
    edad = 0 
    es_edad_positiva = False

# 2.3. Validación de Campos de Texto (No en blanco)
es_nombre_valido = bool(nombre) 
es_apellido_valido = bool(apellido)

# 2.4. VALIDACIÓN DE EMAIL
email_sin_espacios = email.replace(" ", "")
es_email_sin_espacios = (email == email_sin_espacios)
es_una_arroba = (email.count('@') == 1)

# 2.5. Validación Completa (TODOS los campos deben ser válidos)
# Ahora usamos 'es_edad_positiva' en lugar de 'es_mayor_de_edad'
if (es_nombre_valido and es_apellido_valido and 
    es_edad_positiva and es_email_sin_espacios and es_una_arroba):
    
    # ===================================================
    # 3. CLASIFICACIÓN Y MOSTRAR DATOS (Éxito)
    # ===================================================
    
    # CLASIFICACIÓN POR RANGO ETARIO
    if edad <= 13: 
        rango_etario = "Niño/a"
    elif edad < 18: # 14 a 17 años
        rango_etario = "Adolescente"
    else:           # 18 años o más
        rango_etario = "Adulto/a"
        
    print("\n✅ REGISTRO Y FORMATO EXITOSO.")
    print("-" * 45)
    
    # Muestra los datos usando el formato aplicado
    print(f"NOMBRE COMPLETO: {nombre_formateado} {apellido_formateado}")
    print(f"EDAD:            {edad}")
    print(f"RANGO ETARIO:    {rango_etario}")
    print(f"EMAIL:           {email}")
    print("-" * 45)

else:
    # ===================================================
    # 4. MOSTRAR ERROR (Fallo)
    # ===================================================
    print("\nERROR!")
    print("Por favor, revise los requisitos (campos vacíos, edad válida, formato de email).")