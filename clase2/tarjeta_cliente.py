# tarjeta_cliente.py


print("--- RECOPILACIÓN DE DATOS DE LA CLIENTE ---")


nombre = input("Ingrese el nombre completo de la cliente: ").strip()
profesion = input("Ingrese la profesión o cargo de la cliente: ").strip()
email = input("Ingrese la dirección de correo electrónico: ").strip()
telefono = input("Ingrese el número de teléfono: ").strip()



print("\n" + "="*50)
print("     TARJETA DE PRESENTACIÓN DIGITAL - TECHLAB")
print("="*50)


print(f"CLIENTE: {nombre.upper()}") 
print(f"CARGO:   {profesion}")
print("-" * 50)
print(f"EMAIL:   {email}")
print(f"TEL:     {telefono}")
print("="*50)

# Nota: El uso de .strip() al final de cada input elimina espacios en blanco innecesarios.