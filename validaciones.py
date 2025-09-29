# validaciones.py

def validar_entrada_no_vacia(mensaje):
    """Solicita una entrada y se asegura de que no esté vacía."""
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        else:
            print("❌ Error: La entrada no puede estar vacía. Intente de nuevo.")

def validar_precio_entero(mensaje):
    """Solicita un precio y se asegura de que sea un número entero positivo."""
    while True:
        entrada = input(mensaje).strip()
        
        if entrada.isdigit() and int(entrada) >= 0:
            return int(entrada)
        else:
            print("❌ Error: El precio debe ser un número entero positivo (sin centavos). Intente de nuevo.")