try:
    import pandas as pd
    import numpy as np
    PANDAS_OK = True
except ImportError:
    PANDAS_OK = False
    pd = None
    np = None

from functools import reduce


def crear_dataframe(jugadores):
    if not PANDAS_OK:
        return None
    return pd.DataFrame([{
        "id": j["id"],
        "nombre": j["nombre"],
        "edad": j["edad"],
        "presupuesto": j["presupuesto_hoy"],
        "gasto_hoy": j["gasto_hoy"],
        "gasto_promedio": j["gasto_promedio_ronda"],
        "gasto_max_historico": j["gasto_maximo_historico"],
        "perdidas": j["perdidas_acumuladas"],
        "ganancias": j["ganancias_acumuladas"],
        "frecuencia": j["frecuencia_semanal"],
        "tiempo_promedio": j["tiempo_promedio_visita"],
        "total_visitas": j["total_visitas"],
        "clasificacion": j["clasificacion"]
    } for j in jugadores])


def analisis_por_clasificacion(df):
    if df is None:
        return None
    return df.groupby("clasificacion").agg({
        "edad": ["mean", "min", "max"],
        "gasto_hoy": ["mean", "sum"],
        "perdidas": "mean",
        "ganancias": "mean",
        "frecuencia": "mean",
        "total_visitas": "mean"
    }).round(2)


def top_jugadores_riesgo(df, umbral_perdidas=0.75):
    if df is None or not PANDAS_OK:
        return None
    limite = np.percentile(df["perdidas"], umbral_perdidas * 100)
    return df[df["perdidas"] > limite][["nombre", "perdidas", "clasificacion"]]


def correlaciones(df):
    if df is None or not PANDAS_OK:
        return None
    nums = df.select_dtypes(include=[np.number])
    return nums.corr().round(3)


def filtrar_por_clasificacion(jugadores, clasif):
    return list(filter(lambda j: j["clasificacion"] == clasif, jugadores))


def total_metricas(jugadores):
    return reduce(lambda acc, j: {
        "perdidas": acc["perdidas"] + j["perdidas_acumuladas"],
        "ganancias": acc["ganancias"] + j["ganancias_acumuladas"],
        "gasto_hoy": acc["gasto_hoy"] + j["gasto_hoy"]
    }, jugadores, {"perdidas": 0, "ganancias": 0, "gasto_hoy": 0})


def nombres_clasificados(jugadores, clasif):
    return list(map(lambda j: j["nombre"],
                    filtrar_por_clasificacion(jugadores, clasif)))


def resumen_estadistico(jugadores):
    df = crear_dataframe(jugadores)
    if df is None:
        return _resumen_sin_pandas(jugadores)
    return {
        "total": len(jugadores),
        "gasto_promedio": round(df["gasto_hoy"].mean(), 2),
        "perdida_promedio": round(df["perdidas"].mean(), 2),
        "ganancia_promedio": round(df["ganancias"].mean(), 2),
        "edad_promedio": round(df["edad"].mean(), 1),
        "frecuencia_promedio": round(df["frecuencia"].mean(), 1),
        "total_gasto": int(df["gasto_hoy"].sum()),
        "total_perdidas": int(df["perdidas"].sum()),
        "total_ganancias": int(df["ganancias"].sum()),
        "balance": int(df["ganancias"].sum() - df["perdidas"].sum()),
        "vip_count": int((df["clasificacion"] == "VIP").sum()),
        "retener_count": int((df["clasificacion"] == "Retener").sum()),
        "cuidar_count": int((df["clasificacion"] == "Cuidar").sum()),
        "rapido_count": int((df["clasificacion"] == "Servicio_Rapido").sum()),
    }


def _resumen_sin_pandas(jugadores):
    total = len(jugadores)
    if total == 0:
        return {k: 0 for k in ["total", "gasto_promedio", "perdida_promedio",
                               "ganancia_promedio", "edad_promedio",
                               "frecuencia_promedio", "total_gasto",
                               "total_perdidas", "total_ganancias", "balance",
                               "vip_count", "retener_count", "cuidar_count",
                               "rapido_count"]}
    gastos = [j["gasto_hoy"] for j in jugadores]
    perdidas = [j["perdidas_acumuladas"] for j in jugadores]
    ganancias = [j["ganancias_acumuladas"] for j in jugadores]
    edades = [j["edad"] for j in jugadores]
    frecuencias = [j["frecuencia_semanal"] for j in jugadores]
    clasifs = [j["clasificacion"] for j in jugadores]
    return {
        "total": total,
        "gasto_promedio": round(sum(gastos) / total, 2),
        "perdida_promedio": round(sum(perdidas) / total, 2),
        "ganancia_promedio": round(sum(ganancias) / total, 2),
        "edad_promedio": round(sum(edades) / total, 1),
        "frecuencia_promedio": round(sum(frecuencias) / total, 1),
        "total_gasto": int(sum(gastos)),
        "total_perdidas": int(sum(perdidas)),
        "total_ganancias": int(sum(ganancias)),
        "balance": int(sum(ganancias) - sum(perdidas)),
        "vip_count": clasifs.count("VIP"),
        "retener_count": clasifs.count("Retener"),
        "cuidar_count": clasifs.count("Cuidar"),
        "rapido_count": clasifs.count("Servicio_Rapido"),
    }
