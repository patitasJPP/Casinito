import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ventana_principal import AplicacionCasino
from modules.operaciones import sumar, restar, multiplicar, dividir, promedio
from modules.jugador import Jugador
from modules.casino import Casino
from modules.cargar_datos import leer_csv, csv_a_diccionarios
from modules.reportes import generar_reporte_simple, generar_reporte_csv
from data.jugadores import JUGADORES_MOCK


def demo_modulos():
    print("=" * 60)
    print("CASINO SAPIENS - DEMO DE MODULOS")
    print("=" * 60)

    print("\n[operaciones.py]")
    print(f"  sumar(10, 5) = {sumar(10, 5)}")
    print(f"  restar(10, 5) = {restar(10, 5)}")
    print(f"  multiplicar(10, 5) = {multiplicar(10, 5)}")
    print(f"  dividir(10, 5) = {dividir(10, 5)}")
    print(f"  promedio([1,2,3,4,5]) = {promedio([1,2,3,4,5])}")

    print("\n[jugador.py - Clase Jugador]")
    j = Jugador("Carlos", "j1", gasto_hoy=300, rondas_jugadas_hoy=15,
                gasto_maximo_historico=200, frecuencia_semanal=3,
                perdidas_acumuladas=5000, ganancias_acumuladas=3000,
                clasificacion="VIP")
    print(f"  Jugador: {j.nombre}")
    print(f"  Gasto promedio: S/ {j.calcular_gasto_promedio()}")
    print(f"  Es VIP? {j.es_vip()}")
    print(f"  Es rentable? {j.es_rentable()}")
    print(f"  En riesgo? {j.en_riesgo()}")
    print(f"  Balance: S/ {j.calcular_balance()}")

    print("\n[casino.py - Clase Casino]")
    c = Casino()
    for d in JUGADORES_MOCK[:3]:
        c.agregar_jugador(Jugador(d["nombre"], d["id"],
                                   gasto_hoy=d["gasto_hoy"],
                                   gasto_maximo_historico=d["gasto_maximo_historico"],
                                   frecuencia_semanal=d["frecuencia_semanal"],
                                   clasificacion=d["clasificacion"]))
    print(f"  Gasto promedio general: S/ {c.calcular_gasto_promedio_general()}")
    print(f"  VIPs: {c.contar_por_clasificacion('VIP')}")
    print(f"  Top gastadores: {[j.nombre for j in c.top_gastadores(2)]}")

    print("\n[cargar_datos.py - Lectura CSV]")
    try:
        jugadores_csv = leer_csv()
        print(f"  Leidos {len(jugadores_csv)} jugadores desde CSV")
    except Exception as e:
        print(f"  Error al leer CSV: {e}")

    print("\n[reportes.py]")
    generar_reporte_simple(JUGADORES_MOCK)
    generar_reporte_csv(JUGADORES_MOCK)

    print("\n" + "=" * 60)
    print("DEMO COMPLETADA")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        demo_modulos()
    else:
        AplicacionCasino()
