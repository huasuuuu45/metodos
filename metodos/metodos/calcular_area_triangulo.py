# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        return "Error: Base y altura deben ser mayores que cero"
    else:
        area = (base * altura) / 2
        return area

# Casos de prueba
def prueba_calcular_area_triangulo():
    # Caso 1: Base y altura válidas
    assert calcular_area_triangulo(5, 4) == 10.0

    # Caso 2: Base negativa
    assert calcular_area_triangulo(-5, 4) == "Error: Base y altura deben ser mayores que cero"

    # Caso 3: Altura negativa
    assert calcular_area_triangulo(5, -4) == "Error: Base y altura deben ser mayores que cero"

    # Caso 4: Base y altura negativas
    assert calcular_area_triangulo(-5, -4) == "Error: Base y altura deben ser mayores que cero"

    # Caso 5: Base cero
    assert calcular_area_triangulo(0, 4) == "Error: Base y altura deben ser mayores que cero"

    # Caso 6: Altura cero
    assert calcular_area_triangulo(5, 0) == "Error: Base y altura deben ser mayores que cero"

    # Caso 7: Base y altura cero
    assert calcular_area_triangulo(0, 0) == "Error: Base y altura deben ser mayores que cero"

# Ejecutar casos de prueba
prueba_calcular_area_triangulo()
