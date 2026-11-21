"""
ModuloTaller  (Biblioteca FacturacionTaller)
Lógica de cálculo para la facturación de los mantenimientos del taller.
Aquí NO hay entrada/salida por pantalla ni archivos: solo parámetros y retornos.
"""

# ---------------------------------------------------------------
# Constantes (evitan "números mágicos" dentro de las fórmulas)
# ---------------------------------------------------------------
TARIFA_PREVENTIVO = 180.00
TARIFA_CORRECTIVO = 320.00
TARIFA_OTRO = 120.00
PORCENTAJE_DESCUENTO = 0.15   # 15% para cliente frecuente
PORCENTAJE_IGV = 0.18         # 18% de IGV


def ObtenerTarifaBase(tipoServicio):
    """Retorna la tarifa base según el tipo de servicio (3 escalas)."""
    tipo = tipoServicio.strip().upper()

    if tipo == "PREVENTIVO":
        return TARIFA_PREVENTIVO      # S/ 180.00
    elif tipo == "CORRECTIVO":
        return TARIFA_CORRECTIVO      # S/ 320.00
    else:                             # "OTRO" o cualquier otro texto
        return TARIFA_OTRO            # S/ 120.00


def CalcularDescuentoCliente(tarifaBase, esFrecuente):
    """Retorna el 15% de descuento si el cliente es frecuente ("SI"); si no, 0."""
    if esFrecuente.strip().upper() == "SI":
        return tarifaBase * PORCENTAJE_DESCUENTO
    else:
        return 0.0


def CalcularImpuestoIGV(tarifabaseConDescuento):
    """Retorna el IGV (18%) sobre la tarifa base luego de restar el descuento."""
    return tarifabaseConDescuento * PORCENTAJE_IGV


def CalcularTotalPagar(tarifaBase, descuento, igv):
    """Retorna el importe final: tarifaBase - descuento + igv."""
    return tarifaBase - descuento + igv


def ConstruirRegistroPipe(placa, propietario, tipoServicio, totalPagar, fecha):
    """
    Genera la trama delimitada por PIPE (|) con los 5 campos.
    El total a pagar se formatea con 2 decimales (F2).
    Ejemplo: ABC-123|Juan Perez|PREVENTIVO|180.54|21-11-2026 14:30:05
    """
    return f"{placa}|{propietario}|{tipoServicio}|{totalPagar:.2f}|{fecha}"
