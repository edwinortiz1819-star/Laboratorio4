"""
ModuloArchivo  (Biblioteca FacturacionTaller)
Persistencia de las atenciones en el archivo de texto plano atenciones.txt

Formato de cada línea (5 campos separados por PIPE):
    ABC-123|Juan Perez|PREVENTIVO|180.54|21-11-2026 14:30:05
       0         1          2         3          4
    (placa | propietario | tipoServicio | total | fecha)
"""

import os

# Nombre del archivo de texto plano. Program.py fija como carpeta de trabajo
# la carpeta donde está el programa, así que atenciones.txt queda junto a Program.py
# (igual que matriculas.txt en el proyecto de referencia).
NOMBRE_ARCHIVO = "atenciones.txt"


def GuardarAtencion(linea):
    """Almacena el nuevo registro AL FINAL de atenciones.txt."""
    # "a" = append: agrega al final sin borrar lo anterior.
    # 'with' cierra el archivo automáticamente (equivale al Close() del C#).
    with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
        archivo.write(linea + "\n")


def BuscarAtencion(placaBuscada):
    """
    Lee el archivo línea por línea, separa cada línea por '|' y muestra
    TODAS las coincidencias con la placa buscada.
    Retorna la cantidad de atenciones encontradas.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("Todavía no hay atenciones registradas.")
        return 0

    placaBuscada = placaBuscada.strip().upper()
    encontradas = 0

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8-sig") as archivo:
        for linea in archivo:                        # lee línea por línea
            columnas = linea.strip().split("|")      # separa en sub cadenas por |
            if len(columnas) == 5 and columnas[0].upper() == placaBuscada:
                encontradas += 1
                print(f"\nAtención N° {encontradas}")
                print(f"  Placa       : {columnas[0]}")
                print(f"  Propietario : {columnas[1]}")
                print(f"  Servicio    : {columnas[2]}")
                print(f"  Total       : S/ {columnas[3]}")
                print(f"  Fecha       : {columnas[4]}")

    if encontradas == 0:
        print(f"No se encontraron atenciones para la placa {placaBuscada}.")
    else:
        print(f"\nTotal de coincidencias: {encontradas}")

    return encontradas


def ListarTodasLasAtenciones():
    """
    Lee todo atenciones.txt y muestra los vehículos atendidos
    y la suma total recaudada por el taller. Retorna el total recaudado.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("Todavía no hay atenciones registradas.")
        return 0.0

    cantidad = 0
    totalRecaudado = 0.0

    print("\n========== REPORTE GENERAL DE ATENCIONES ==========")
    print(f"{'PLACA':<10}{'PROPIETARIO':<24}{'SERVICIO':<13}{'TOTAL (S/)':>11}   FECHA")
    print("-" * 78)

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8-sig") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("|")
            if len(columnas) != 5:
                continue                              # ignora líneas vacías o dañadas
            try:
                total = float(columnas[3])
            except ValueError:
                continue                              # ignora total no numérico

            cantidad += 1
            totalRecaudado += total                   # acumula lo recaudado
            print(f"{columnas[0]:<10}{columnas[1]:<24}{columnas[2]:<13}{total:>11.2f}   {columnas[4]}")

    print("-" * 78)
    if cantidad == 0:
        print("El archivo no contiene atenciones.")
    else:
        print(f"Vehículos atendidos : {cantidad}")
        print(f"Total recaudado     : S/ {totalRecaudado:.2f}")

    return totalRecaudado
