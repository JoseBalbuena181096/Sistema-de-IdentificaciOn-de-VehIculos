#!/usr/bin/env python3
from utilities import *

"""
Mecanismo de Control (interacción y aplicación de reglas)
"""
def main():
    """Función principal para ejecutar el sistema de 
    identificación de vehículos."""
    caracteristicas = obtener_caracteristicas()
    
    if len(caracteristicas) > 4:
        print("Solo puede ingresar un \
              máximo de 4 características.")
        return
    
    print(f"\nCaracterísticas\
            ingresadas: {', '.join(caracteristicas)}")
    
    vehiculos_ordenados = identificar_vehiculo(caracteristicas)
    
    if vehiculos_ordenados:
        print("\nPosibles vehículos basados en las\
               características ingresadas:")
        for vehiculo, puntaje in vehiculos_ordenados:
            probabilidad = "100%" if puntaje == 1.0 \
                else f"{puntaje * 100:.0f}%"
            print(f"- {vehiculo} (Probabilidad: {probabilidad})")
    else:
        print("\nNo se encontraron coincidencias para \
              las características ingresadas.")

# Ejecución del sistema
if __name__ == "__main__":
    main()