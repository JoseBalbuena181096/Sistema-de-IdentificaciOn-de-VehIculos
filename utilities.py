#!/usr/bin/env python3

"""
Definición de hechos (características ingresadas por el usuario)
"""
def obtener_caracteristicas():
    """Solicita al usuario que ingrese entre 1 y\
        4 características para identificar un vehículo."""
    caracteristicas = []
    print("Ingrese entre 1 y 4 características \
          (escriba 'fin' para terminar):")
    
    while len(caracteristicas) < 4:
        caracteristica = input("Característica: ").strip().lower()
        if caracteristica == 'fin':
            break
        if caracteristica and caracteristica\
            not in caracteristicas:
            caracteristicas.append(caracteristica)
        else:
            print("Por favor, ingrese una característica\
                válida que no haya sido ingresada antes.")
    
    if len(caracteristicas) == 0:
        print("Debe ingresar al menos una característica.")
        return obtener_caracteristicas()
    
    return caracteristicas

# Base de conocimientos (reglas para identificar vehículos)
def identificar_vehiculo(caracteristicas):
    """Identifica vehículos basados en las \
        características ingresadas por el usuario."""
    # Base de conocimientos: vehículos y sus características
    vehiculos = {
        "Automóvil": ["cuatro ruedas", "motor\
                      ", "volante", "cuatro asientos"],
        "Motocicleta": ["dos ruedas", "volante\
                        ", "motor", "un asiento"],
        "Bicicleta": ["dos ruedas", "pedales\
                      ", "volante", "un asiento"],
        "Camión": ["carga", "motor\
                   ", "cabina", "ruedas grandes"]
    }
    
    # Registro de qué vehículos tienen cada característica
    vehiculo_por_caracteristica = {}
    for vehiculo, caracteristicas_vehiculo in vehiculos.items():
        for caracteristica in caracteristicas_vehiculo:
            if caracteristica not in vehiculo_por_caracteristica:
                vehiculo_por_caracteristica[caracteristica] = []
            vehiculo_por_caracteristica[caracteristica\
                                        ].append(vehiculo)
    
    # Evaluación de coincidencias
    puntajes = {}
    for vehiculo, caracteristicas_vehiculo in vehiculos.items():
        coincidencias = sum(1 for c in caracteristicas\
                             if c in caracteristicas_vehiculo)
        # Calcular puntaje como proporción de coincidencias
        puntaje = coincidencias / len(caracteristicas_vehiculo)  
        
        # Ajustar el puntaje a 100% si una característica es 
        # exclusiva para este vehículo
        for c in caracteristicas:
            if c in vehiculo_por_caracteristica\
                and len(vehiculo_por_caracteristica[c]) == 1\
                and vehiculo_por_caracteristica[c][0] == vehiculo:
                puntaje = 1.0
                break
        
        puntajes[vehiculo] = puntaje
    
    # Ordenar vehículos por puntaje en orden descendente
    vehiculos_ordenados = sorted(puntajes.items(),\
                                key=lambda x: x[1], reverse=True)
    
    return vehiculos_ordenados