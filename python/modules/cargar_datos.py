import csv
import sys
from pathlib import Path
from modules.jugador import Jugador


def leer_csv(ruta=None):
    if ruta is None:
        ruta = str(Path(__file__).resolve().parent.parent.parent / "data" / "jugadores.csv")
    jugadores = []
    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    j = Jugador(
                        nombre=fila["nombre"],
                        id_jugador=fila["id"],
                        gasto_hoy=int(fila["gasto_hoy"]),
                        rondas_jugadas_hoy=int(fila["rondas_jugadas_hoy"]),
                        gasto_maximo_historico=int(fila["gasto_maximo_historico"]),
                        frecuencia_semanal=int(fila["frecuencia_semanal"]),
                        perdidas_acumuladas=int(fila["perdidas_acumuladas"]),
                        ganancias_acumuladas=int(fila["ganancias_acumuladas"]),
                        clasificacion=fila["clasificacion"],
                    )
                    jugadores.append(j)
                except (KeyError, ValueError) as e:
                    print(f"Error en fila {fila.get('id', 'desconocido')}: {e}")
                    continue
    except FileNotFoundError:
        print(f"ERROR: Archivo no encontrado: {ruta}")
        sys.exit(1)
    except PermissionError:
        print(f"ERROR: Permiso denegado al leer: {ruta}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR inesperado al leer CSV: {e}")
        sys.exit(1)
    return jugadores


def csv_a_diccionarios(ruta=None):
    if ruta is None:
        ruta = str(Path(__file__).resolve().parent.parent.parent / "data" / "jugadores.csv")
    datos = []
    try:
        with open(ruta, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                datos.append(dict(fila))
    except FileNotFoundError:
        print(f"ERROR: Archivo no encontrado: {ruta}")
    return datos
