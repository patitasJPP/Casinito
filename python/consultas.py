from pathlib import Path
from functools import lru_cache

RUTA_PROLOG = str(Path(__file__).resolve().parent.parent / "prolog" / "casino.pl")

_prolog = None

def _get_prolog():
    global _prolog
    if _prolog is None:
        try:
            from pyswip import Prolog
            _prolog = Prolog()
            _prolog.consult(RUTA_PROLOG)
        except ImportError:
            _prolog = None
    return _prolog

def prolog_disponible():
    return _get_prolog() is not None

def obtener_vips():
    p = _get_prolog()
    if p is None:
        return []
    return list(p.query("lista_vip(Lista)"))

def obtener_retener():
    p = _get_prolog()
    if p is None:
        return []
    return list(p.query("lista_retener(Lista)"))

def obtener_cuidar():
    p = _get_prolog()
    if p is None:
        return []
    return list(p.query("lista_cuidar(Lista)"))

def obtener_recomendacion(jugador_id):
    p = _get_prolog()
    if p is None:
        return []
    return list(p.query(f"recomendar({jugador_id}, Juego)"))

def obtener_datos_jugador(jugador_id):
    p = _get_prolog()
    if p is None:
        return None
    q = list(p.query(
        "datos_jugador(Id, Nombre, Edad, Ocupacion, "
        "Presupuesto, Fichas, GastoHoy, GastoProm, GastoMax, "
        "Perdidas, Ganancias, JuegoActual, MontoApuesta, Resultado, "
        "RondasHoy, TiempoCasino, HoraActual, Frecuencia, TiempoProm, "
        "Horario, TotalVisitas, DiasPrimera, DiasUltima, "
        "JuegoFav, Variedad, PrefJuego, Ritmo, "
        "CambiaPierde, CambiaGana, JuegaSolo, Reinvierte, AceptaRec)",
        Id=jugador_id
    ))
    if not q:
        return None
    r = q[0]
    return {
        "id": r["Id"], "nombre": r["Nombre"], "edad": r["Edad"],
        "ocupacion": r["Ocupacion"], "presupuesto_hoy": r["Presupuesto"],
        "fichas_actuales": r["Fichas"], "gasto_hoy": r["GastoHoy"],
        "gasto_promedio_ronda": r["GastoProm"],
        "gasto_maximo_historico": r["GastoMax"],
        "perdidas_acumuladas": r["Perdidas"],
        "ganancias_acumuladas": r["Ganancias"],
        "juego_actual": r["JuegoActual"], "monto_apuesta": r["MontoApuesta"],
        "resultado_ultima_ronda": r["Resultado"],
        "rondas_jugadas_hoy": r["RondasHoy"],
        "tiempo_en_casino_hoy": r["TiempoCasino"],
        "hora_actual": r["HoraActual"], "frecuencia_semanal": r["Frecuencia"],
        "tiempo_promedio_visita": r["TiempoProm"],
        "horario_habitual": r["Horario"],
        "total_visitas": r["TotalVisitas"],
        "dias_desde_primera_visita": r["DiasPrimera"],
        "dias_desde_ultima_visita": r["DiasUltima"],
        "juego_favorito": r["JuegoFav"],
        "variedad_juegos_probados": r["Variedad"],
        "prefiere_azar_o_estrategia": r["PrefJuego"],
        "prefiere_rapido_o_lento": r["Ritmo"],
        "cambia_al_perder": r["CambiaPierde"],
        "cambia_al_ganar": r["CambiaGana"],
        "juega_solo": r["JuegaSolo"],
        "reinvierte_ganancias": r["Reinvierte"],
        "acepta_recomendaciones": r["AceptaRec"],
    }

def clasificar_jugador(jugador_id):
    p = _get_prolog()
    if p is None:
        return "Normal"
    q = list(p.query(f"clasificacion({jugador_id}, Clase)"))
    if not q:
        return "Normal"
    mapa = {"vip": "VIP", "retener": "Retener", "cuidar": "Cuidar"}
    return mapa.get(q[0]["Clase"], "Normal")
