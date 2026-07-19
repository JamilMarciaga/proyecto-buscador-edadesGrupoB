"""
Programa buscador de edades - Grupo B
Integrantes: Jamil Marciaga, Gilberto Cano, Alexis Lopez, Esequiel Gonzalez
"""

# Lista con los nombres del grupo
nombres_integrantes = ["Jamil", "Gilberto", "Alexis", "Esequiel", "Ana", "Carlos"]

# Diccionario con edades
edades_integrantes = {
    "Jamil": 25,
    "Gilberto": 22,
    "Alexis": 23,
    "Esequiel": 24,
    "Ana": 30,
    "Carlos"
}
# ==========================
# PARTE DE ESEQUIEL
# Estadísticas del grupo
# ==========================

cantidad_integrantes = len(edades_integrantes)
promedio_edades = sum(edades_integrantes.values()) / cantidad_integrantes

integrante_mayor = max(edades_integrantes, key=edades_integrantes.get)
integrante_menor = min(edades_integrantes, key=edades_integrantes.get)

print("\n=== ESTADÍSTICAS DEL GRUPO ===")
print(f"Cantidad de integrantes: {cantidad_integrantes}")
print(f"Promedio de edades: {promedio_edades:.2f}")
print(f"Mayor edad: {integrante_mayor} ({edades_integrantes[integrante_mayor]} años)")
print(f"Menor edad: {integrante_menor} ({edades_integrantes[integrante_menor]} años)")
# Mostrar integrantes disponibles
print("=== BUSCADOR DE EDADES - GRUPO B ===")
print("Integrantes disponibles:")
for nombre in nombres_integrantes:
    print(f"  - {nombre}")

# Solicitar un nombre válido
while True:
    nombre_buscado = input("\nIngresa el nombre de un integrante: ").strip()
    if nombre_buscado:
        break
    print("El nombre no puede estar vacío. Inténtalo de nuevo.")

# Buscar el nombre sin distinguir mayúsculas y minúsculas
nombre_encontrado = None
for nombre in nombres_integrantes:
    if nombre.casefold() == nombre_buscado.casefold():
        nombre_encontrado = nombre
        break

# Buscar la edad
if nombre_encontrado:
    edad_encontrada = edades_integrantes[nombre_encontrado]
    print(f"\nHola, {nombre_encontrado}. Tu edad registrada es {edad_encontrada} años.")
    
    # Dividir la edad entre 4
    edad_dividida = edad_encontrada / 4
    print(f"   📊 Su edad dividida entre 4 es: {edad_dividida:.2f}")
    
    # Cambiar la edad a otro compañero
    for otro_nombre in nombres_integrantes:
        if otro_nombre != nombre_encontrado:
            edades_integrantes[otro_nombre] -= 1
            print(f"   🔄 Se restó 1 año a {otro_nombre}. Ahora tiene {edades_integrantes[otro_nombre]} años.")
            break

# ==========================
# PARTE DE GILBERTO
# ==========================

if nombre_encontrado:
    print("\n--- Cambio especial de Gilberto ---")

    # Calcular el doble de la edad
    doble_edad = edades_integrantes[nombre_encontrado] * 2
    print(f"El doble de la edad de {nombre_encontrado} es: {doble_edad} años.")
    
else:
    print(f"\nLo sentimos, '{nombre_buscado}' no fue encontrado en el grupo.")
    print("Nombres disponibles:", ", ".join(nombres_integrantes))
