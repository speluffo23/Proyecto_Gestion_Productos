# registro_ingresos.py

print("--- REGISTRO Y CÁLCULO DE INGRESOS MENSUALES ---")
print("Se registrarán los ingresos de 6 meses.\n")

# Variables de control
ingresos_totales = 0.0
mes_actual = 1
NUMERO_MESES = 6

# =======================================================
# 1. Bucle While para registrar los 6 meses
# =======================================================

# El bucle se repite 6 veces (mientras mes_actual sea menor o igual a NUMERO_MESES)
while mes_actual <= NUMERO_MESES:
    
    # ---------------------------------------------------
    # Bucle de validación (Bucle While Anidado)
    # ---------------------------------------------------
    while True:
        try:
            # 1. Solicitar el ingreso
            mensaje = f"Ingrese el ingreso para el Mes {mes_actual}: $"
            ingreso = float(input(mensaje)) # Usamos float para manejar decimales si es necesario
            
            # 2. Validar que el ingreso sea positivo
            if ingreso >= 0:
                # Si es válido, salimos del bucle de validación y continuamos con el registro
                break 
            else:
                # Si es negativo, mostramos el mensaje de error y el bucle True vuelve a solicitar el dato
                print("❌ Error: El ingreso no puede ser un valor negativo. Intente de nuevo.")
                
        except ValueError:
            # Si el usuario ingresa texto, esto maneja el error y el bucle True vuelve a solicitar
            print("❌ Error: Por favor, ingrese un número válido.")
            
    # ---------------------------------------------------
    # Registro de datos
    # ---------------------------------------------------
    
    # 3. Acumular el ingreso al total
    ingresos_totales += ingreso
    
    # 4. Pasar al siguiente mes
    mes_actual += 1

# =======================================================
# 2. CÁLCULO DE RESULTADOS
# =======================================================

# Requisito: Calcular el promedio mensual
promedio_mensual = ingresos_totales / NUMERO_MESES

# =======================================================
# 3. MOSTRAR RESULTADOS
# =======================================================

print("\n" + "="*50)
print("             RESUMEN FINANCIERO")
print("="*50)
print(f"Meses Registrados: {NUMERO_MESES}")
# El formato {:.2f} se usa para mostrar dos decimales (formato monetario)
print(f"Total Acumulado:   ${ingresos_totales:,.2f}") 
print(f"Promedio Mensual:  ${promedio_mensual:,.2f}")
print("="*50)