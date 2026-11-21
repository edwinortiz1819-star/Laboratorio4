"""
Program.py  -  Programa principal (Main)
Práctica de Laboratorio 4 - Fundamentos de Programación
Tema 6: Registro y facturación de mantenimientos de un taller mecánico.
"""

import os
from datetime import datetime                      # fecha/hora del sistema (biblioteca estándar)

try:
    from FacturacionTaller import ModuloTaller, ModuloArchivo   # llamada a mi biblioteca
except ImportError as ex:
    print("ERROR: no se pudo cargar la biblioteca FacturacionTaller.")
    print(f"Detalle: {ex}")
    print("La carpeta 'FacturacionTaller' debe estar junto a Program.py:")
    print("    Program.py")
    print("    FacturacionTaller/")
    print("        __init__.py")
    print("        ModuloTaller.py")
    print("        ModuloArchivo.py")
    raise SystemExit(1)


def PrepararCarpetaDeTrabajo():
    """Hace que atenciones.txt se cree/lea siempre junto a Program.py."""
    if "__file__" in globals():
        os.chdir(os.path.dirname(os.path.abspath(__file__)))


def PedirTexto(mensaje):
    """Pide un texto que no esté vacío. Quita '|' para no romper el formato PIPE."""
    while True:
        texto = input(mensaje).strip().replace("|", "")
        if texto != "":
            return texto
        print("  El dato no puede estar vacío.")


def PedirSiNo(mensaje):
    """Pide SI o NO hasta recibir una respuesta válida."""
    while True:
        respuesta = input(mensaje).strip().upper()
        if respuesta == "SI" or respuesta == "NO":
            return respuesta
        print("  Responda SI o NO.")


def RegistrarAtencion():
    print("\n--- REGISTRAR ATENCIÓN ---")
    placa = PedirTexto("PLACA: ").upper()
    propietario = PedirTexto("PROPIETARIO: ")
    tipoServicio = PedirTexto("TIPO DE SERVICIO (PREVENTIVO / CORRECTIVO / OTRO): ").upper()
    esFrecuente = PedirSiNo("CLIENTE FRECUENTE? (SI/NO): ")

    # Fecha y hora exacta de la atención (DateTime.Now en C#)
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Cálculos con ModuloTaller
    tarifaBase = ModuloTaller.ObtenerTarifaBase(tipoServicio)
    descuento = ModuloTaller.CalcularDescuentoCliente(tarifaBase, esFrecuente)
    igv = ModuloTaller.CalcularImpuestoIGV(tarifaBase - descuento)
    total = ModuloTaller.CalcularTotalPagar(tarifaBase, descuento, igv)

    print("\n--- DETALLE DE FACTURACIÓN ---")
    print(f"Tarifa base : S/ {tarifaBase:>8.2f}")
    print(f"Descuento   : S/ {descuento:>8.2f}")
    print(f"IGV (18%)   : S/ {igv:>8.2f}")
    print(f"TOTAL       : S/ {total:>8.2f}")
    print(f"Fecha       : {fecha}")

    # Construir la trama PIPE y guardarla en atenciones.txt
    nuevoRegistro = ModuloTaller.ConstruirRegistroPipe(placa, propietario, tipoServicio, total, fecha)
    ModuloArchivo.GuardarAtencion(nuevoRegistro)
    print("¡Atención registrada!")


def BuscarPorPlaca():
    print("\n--- BUSCAR ATENCIÓN POR PLACA ---")
    placa = PedirTexto("Ingrese la PLACA a buscar: ")
    ModuloArchivo.BuscarAtencion(placa)


def MostrarMenu():
    print("\n===== TALLER MECÁNICO =====")
    print("1. Registrar atención")
    print("2. Buscar atención por Placa")
    print("3. Reporte general de atenciones")
    print("4. Salir")


def Main():
    PrepararCarpetaDeTrabajo()
    opcion = 0
    while opcion != 4:
        MostrarMenu()
        try:                                                # podría ocurrir un error
            opcion = int(input("Seleccione una opción: "))  # error si no es número

            if opcion == 1:
                RegistrarAtencion()
            elif opcion == 2:
                BuscarPorPlaca()
            elif opcion == 3:
                ModuloArchivo.ListarTodasLasAtenciones()
            elif opcion == 4:
                print("Fin del programa. ¡Hasta pronto!")
            else:
                print("Opción fuera de rango. Elija del 1 al 4.")

        except ValueError:                                  # el usuario no escribió un número
            print("Entrada no válida: ingrese un número del 1 al 4.")
            opcion = 0
        except (KeyboardInterrupt, EOFError):               # Ctrl+C o entrada cerrada
            print("\nEntrada interrumpida. Saliendo del sistema...")
            break
        except Exception as ex:                             # cualquier otro error (ej. archivo)
            print(f"Ocurrió un error: {ex}")
            opcion = 0


if __name__ == "__main__":
    Main()
