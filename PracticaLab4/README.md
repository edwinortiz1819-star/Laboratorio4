# Práctica de Laboratorio 4 – Taller Mecánico (Python)

**Curso:** Fundamentos de Programación – UPN
**Tema 6:** Registro y facturación de mantenimientos de un centro de servicio técnico mecánico
**Alumno:** _(escribe aquí tu nombre y código)_

Sistema de consola que registra y factura los mantenimientos de vehículos. La lógica de cálculo está separada en una **biblioteca independiente** (`FacturacionTaller`), los datos se guardan en un **archivo de texto plano** (`atenciones.txt`) y la fecha/hora de cada atención se obtiene con `datetime` (biblioteca estándar de Python).

## Estructura del proyecto

```
PracticaLab4/
├── Program.py                    # Programa principal (menú interactivo)
├── atenciones.txt                # Archivo de datos (formato PIPE)
└── FacturacionTaller/            # Biblioteca
    ├── __init__.py
    ├── ModuloTaller.py           # Lógica de cálculo
    └── ModuloArchivo.py          # Manejo del archivo de texto
```

## Cómo ejecutar

Requiere Python 3.6 o superior. Abre una terminal **dentro de la carpeta del proyecto** (donde está `Program.py`) y ejecuta:

```bash
python Program.py        # Windows también: py Program.py   |   Mac/Linux: python3 Program.py
```

> Importante: la carpeta `FacturacionTaller/` debe estar junto a `Program.py`, tal como se muestra arriba.

## Módulo `ModuloTaller`

| Función | Descripción |
|---|---|
| `ObtenerTarifaBase(tipoServicio)` | PREVENTIVO = S/ 180.00 · CORRECTIVO = S/ 320.00 · cualquier otro = S/ 120.00 |
| `CalcularDescuentoCliente(tarifaBase, esFrecuente)` | 15 % de la tarifa si el cliente es frecuente ("SI"); si no, 0 |
| `CalcularImpuestoIGV(tarifabaseConDescuento)` | 18 % sobre la tarifa luego de restar el descuento |
| `CalcularTotalPagar(tarifaBase, descuento, igv)` | `tarifaBase - descuento + igv` |
| `ConstruirRegistroPipe(placa, propietario, tipoServicio, totalPagar, fecha)` | Trama de 5 campos separados por `\|`, con el total en 2 decimales |

## Módulo `ModuloArchivo`

| Función | Descripción |
|---|---|
| `GuardarAtencion(linea)` | Agrega el registro al final de `atenciones.txt` |
| `BuscarAtencion(placaBuscada)` | Lee línea por línea, separa por `\|` y muestra todas las coincidencias de la placa |
| `ListarTodasLasAtenciones()` | Muestra todos los vehículos atendidos y la suma total recaudada |

## Menú principal

```
1. Registrar atención
2. Buscar atención por Placa
3. Reporte general de atenciones
4. Salir
```

El menú se repite hasta elegir la opción 4 y está protegido con `try-except` (entradas no numéricas, opciones fuera de rango, errores de archivo, etc.).

## Ejemplo de cálculo

Servicio **PREVENTIVO** para un **cliente frecuente**:

| Concepto | Monto |
|---|---|
| Tarifa base | S/ 180.00 |
| Descuento (15 %) | S/ 27.00 |
| IGV (18 % de 153.00) | S/ 27.54 |
| **Total a pagar** | **S/ 180.54** |

## Formato de `atenciones.txt`

Cada línea tiene 5 campos separados por `|`:

```
placa|propietario|tipoServicio|total|fecha
ABC-123|Juan Perez|PREVENTIVO|180.54|14-11-2026 09:15:42
```

> Las 5 líneas incluidas en `atenciones.txt` son datos de ejemplo para probar las opciones 2 y 3.
