import csv
from pathlib import Path


def generar_reporte_simple(jugadores):
    if not jugadores:
        print("=" * 60)
        print("No hay jugadores registrados.")
        print("=" * 60)
        return
    print("=" * 60)
    print(f"REPORTE DE JUGADORES ({len(jugadores)} total)")
    print("=" * 60)
    for j in jugadores:
        balance = j["ganancias_acumuladas"] - j["perdidas_acumuladas"]
        estado = "VIP" if j["clasificacion"] == "VIP" else j["clasificacion"]
        print(f"  {j['nombre']:20s} | Gasto: S/{j['gasto_hoy']:>4d} | "
              f"Balance: S/{balance:>4d} | {estado}")
    print("=" * 60)


def generar_reporte_csv(jugadores, nombre_archivo=None):
    if nombre_archivo is None:
        nombre_archivo = str(Path(__file__).resolve().parent.parent /
                             "data" / "reporte_generado.csv")
    campos = ["id", "nombre", "edad", "clasificacion", "gasto_hoy",
              "perdidas_acumuladas", "ganancias_acumuladas", "balance"]
    try:
        with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            for j in jugadores:
                writer.writerow({
                    "id": j["id"],
                    "nombre": j["nombre"],
                    "edad": j["edad"],
                    "clasificacion": j["clasificacion"],
                    "gasto_hoy": j["gasto_hoy"],
                    "perdidas_acumuladas": j["perdidas_acumuladas"],
                    "ganancias_acumuladas": j["ganancias_acumuladas"],
                    "balance": j["ganancias_acumuladas"] - j["perdidas_acumuladas"],
                })
        print(f"Reporte exportado a: {nombre_archivo}")
    except Exception as e:
        print(f"Error al exportar reporte: {e}")
