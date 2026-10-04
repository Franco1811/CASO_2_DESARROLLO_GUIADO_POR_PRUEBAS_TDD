"""Módulo de cálculo de edad siguiendo TDD."""
from datetime import date

MENSAJE_FECHA_FUTURA = "La fecha de nacimiento no puede ser posterior a la fecha actual"


def validar_fecha_nacimiento(fecha_nacimiento: date, fecha_actual: date) -> None:
    """Valida que la fecha de nacimiento no sea posterior a la fecha actual."""
    if fecha_nacimiento > fecha_actual:
        raise ValueError(MENSAJE_FECHA_FUTURA)


def ya_cumplio_anios(fecha_nacimiento: date, fecha_actual: date) -> bool:
    """Verifica si en el año actual la persona ya cumplió años o si es su cumpleaños hoy."""
    return (fecha_actual.month, fecha_actual.day) >= (fecha_nacimiento.month, fecha_nacimiento.day)


def calcular_edad(fecha_nacimiento: date, fecha_actual: date) -> int:
    """Calcula la edad exacta en años cumplidos a partir de una fecha de nacimiento y fecha actual dada."""
    validar_fecha_nacimiento(fecha_nacimiento, fecha_actual)

    diferencia_anios = fecha_actual.year - fecha_nacimiento.year
    if not ya_cumplio_anios(fecha_nacimiento, fecha_actual):
        return diferencia_anios - 1

    return diferencia_anios
