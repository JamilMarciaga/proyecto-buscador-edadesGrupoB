"""
Programa buscador de edades - Grupo B
Integrantes: Jamil Marciaga, Gilberto Cano, Alexis Lopez, Esequiel Gonzalez
"""

# Lista con los 4 nombres del grupo
nombres_integrantes = ["Jamil", "Gilberto", "Alexis", "Esequiel"]

# Diccionario con edades
edades_integrantes = {
    "Jamil": 25,
    "Gilberto": 22,
    "Alexis": 23,
    "Esequiel": 24
}

# Mostrar integrantes disponibles
print("=== BUSCADOR DE EDADES - GRUPO B ===")
print("Integrantes disponibles:")
for nombre in nombres_integrantes:
    print(f"  - {nombre}")

# Solicitar nombre al usuario
nombre_buscado = input("\nIngresa el nombre de un integrante: ")

# Buscar la edad
if nombre_buscado in edades_integrantes:
    edad_encontrada = edades_integrantes[nombre_buscado]
    print(f"\n✅ {nombre_buscado} tiene {edad_encontrada} años.")
    
    # Dividir la edad entre 4
    edad_dividida = edad_encontrada / 4
    print(f"   📊 Su edad dividida entre 4 es: {edad_dividida:.2f}")
    
    # Cambiar la edad a otro compañero
    for otro_nombre in nombres_integrantes:
        if otro_nombre != nombre_buscado:
            edades_integrantes[otro_nombre] -= 1
            print(f"   🔄 Se restó 1 año a {otro_nombre}. Ahora tiene {edades_integrantes[otro_nombre]} años.")
            break
else:
    print(f"\n❌ La persona '{nombre_buscado}' no fue encontrada en el grupo.")
