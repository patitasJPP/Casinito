from consultas import prolog_disponible, obtener_datos_jugador, clasificar_jugador

JUGADORES_MOCK = [
    {
        "id": "j1", "nombre": "Carlos", "edad": 45, "ocupacion": "Ingeniero",
        "presupuesto_hoy": 500, "fichas_actuales": 200, "juego_actual": "Tragamonedas",
        "monto_apuesta": 50, "resultado_ultima_ronda": "Ganó", "tiempo_en_casino_hoy": 2.5,
        "hora_actual": "22:00", "rondas_jugadas_hoy": 15, "gasto_hoy": 300,
        "frecuencia_semanal": 3, "tiempo_promedio_visita": 180, "horario_habitual": "Nocturno",
        "prefiere_azar_o_estrategia": "Azar", "prefiere_rapido_o_lento": "Rápido",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "No", "gasto_promedio_ronda": 50,
        "gasto_maximo_historico": 200, "perdidas_acumuladas": 5000,
        "ganancias_acumuladas": 3000, "variedad_juegos_probados": 3,
        "juego_favorito": "Tragamonedas", "dias_visita": "Vie, Sáb",
        "juega_solo": "No", "reinvierte_ganancias": "Sí", "acepta_recomendaciones": "Sí",
        "total_visitas": 120, "dias_desde_primera_visita": 365, "dias_desde_ultima_visita": 2,
        "clasificacion": "VIP"
    },
    {
        "id": "j2", "nombre": "María", "edad": 28, "ocupacion": "Docente",
        "presupuesto_hoy": 200, "fichas_actuales": 50, "juego_actual": "Ruleta",
        "monto_apuesta": 20, "resultado_ultima_ronda": "Perdió", "tiempo_en_casino_hoy": 1.0,
        "hora_actual": "20:00", "rondas_jugadas_hoy": 8, "gasto_hoy": 150,
        "frecuencia_semanal": 1, "tiempo_promedio_visita": 90, "horario_habitual": "Tarde",
        "prefiere_azar_o_estrategia": "Azar", "prefiere_rapido_o_lento": "Lento",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "Sí", "gasto_promedio_ronda": 20,
        "gasto_maximo_historico": 80, "perdidas_acumuladas": 800,
        "ganancias_acumuladas": 200, "variedad_juegos_probados": 2,
        "juego_favorito": "Ruleta", "dias_visita": "Sáb",
        "juega_solo": "Sí", "reinvierte_ganancias": "No", "acepta_recomendaciones": "Sí",
        "total_visitas": 15, "dias_desde_primera_visita": 60, "dias_desde_ultima_visita": 35,
        "clasificacion": "Retener"
    },
    {
        "id": "j3", "nombre": "Jorge", "edad": 52, "ocupacion": "Empresario",
        "presupuesto_hoy": 1000, "fichas_actuales": 800, "juego_actual": "Blackjack",
        "monto_apuesta": 100, "resultado_ultima_ronda": "Ganó", "tiempo_en_casino_hoy": 3.0,
        "hora_actual": "21:30", "rondas_jugadas_hoy": 20, "gasto_hoy": 200,
        "frecuencia_semanal": 5, "tiempo_promedio_visita": 240, "horario_habitual": "Nocturno",
        "prefiere_azar_o_estrategia": "Estrategia", "prefiere_rapido_o_lento": "Lento",
        "cambia_al_perder": "No", "cambia_al_ganar": "No", "gasto_promedio_ronda": 100,
        "gasto_maximo_historico": 500, "perdidas_acumuladas": 2000,
        "ganancias_acumuladas": 8000, "variedad_juegos_probados": 4,
        "juego_favorito": "Blackjack", "dias_visita": "Lun a Vie",
        "juega_solo": "No", "reinvierte_ganancias": "Sí", "acepta_recomendaciones": "No",
        "total_visitas": 300, "dias_desde_primera_visita": 800, "dias_desde_ultima_visita": 1,
        "clasificacion": "VIP"
    },
    {
        "id": "j4", "nombre": "Lucía", "edad": 22, "ocupacion": "Estudiante",
        "presupuesto_hoy": 50, "fichas_actuales": 5, "juego_actual": "Tragamonedas",
        "monto_apuesta": 5, "resultado_ultima_ronda": "Perdió", "tiempo_en_casino_hoy": 4.5,
        "hora_actual": "23:00", "rondas_jugadas_hoy": 30, "gasto_hoy": 45,
        "frecuencia_semanal": 2, "tiempo_promedio_visita": 120, "horario_habitual": "Noche",
        "prefiere_azar_o_estrategia": "Azar", "prefiere_rapido_o_lento": "Rápido",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "Sí", "gasto_promedio_ronda": 5,
        "gasto_maximo_historico": 20, "perdidas_acumuladas": 300,
        "ganancias_acumuladas": 50, "variedad_juegos_probados": 1,
        "juego_favorito": "Tragamonedas", "dias_visita": "Sáb, Dom",
        "juega_solo": "Sí", "reinvierte_ganancias": "No", "acepta_recomendaciones": "Sí",
        "total_visitas": 20, "dias_desde_primera_visita": 45, "dias_desde_ultima_visita": 1,
        "clasificacion": "Cuidar"
    },
    {
        "id": "j5", "nombre": "Pedro", "edad": 38, "ocupacion": "Abogado",
        "presupuesto_hoy": 300, "fichas_actuales": 100, "juego_actual": "Ruleta",
        "monto_apuesta": 30, "resultado_ultima_ronda": "Ganó", "tiempo_en_casino_hoy": 1.5,
        "hora_actual": "19:00", "rondas_jugadas_hoy": 10, "gasto_hoy": 200,
        "frecuencia_semanal": 2, "tiempo_promedio_visita": 150, "horario_habitual": "Tarde",
        "prefiere_azar_o_estrategia": "Azar", "prefiere_rapido_o_lento": "Rápido",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "No", "gasto_promedio_ronda": 30,
        "gasto_maximo_historico": 100, "perdidas_acumuladas": 1500,
        "ganancias_acumuladas": 2000, "variedad_juegos_probados": 3,
        "juego_favorito": "Ruleta", "dias_visita": "Jue, Vie",
        "juega_solo": "Sí", "reinvierte_ganancias": "No", "acepta_recomendaciones": "Sí",
        "total_visitas": 60, "dias_desde_primera_visita": 180, "dias_desde_ultima_visita": 5,
        "clasificacion": "Servicio_Rapido"
    },
    {
        "id": "j6", "nombre": "Ana", "edad": 48, "ocupacion": "Médico",
        "presupuesto_hoy": 800, "fichas_actuales": 600, "juego_actual": "Blackjack",
        "monto_apuesta": 80, "resultado_ultima_ronda": "Ganó", "tiempo_en_casino_hoy": 0.5,
        "hora_actual": "18:00", "rondas_jugadas_hoy": 3, "gasto_hoy": 200,
        "frecuencia_semanal": 4, "tiempo_promedio_visita": 120, "horario_habitual": "Tarde",
        "prefiere_azar_o_estrategia": "Estrategia", "prefiere_rapido_o_lento": "Lento",
        "cambia_al_perder": "No", "cambia_al_ganar": "No", "gasto_promedio_ronda": 80,
        "gasto_maximo_historico": 300, "perdidas_acumuladas": 500,
        "ganancias_acumuladas": 4000, "variedad_juegos_probados": 2,
        "juego_favorito": "Blackjack", "dias_visita": "Mar, Jue, Sáb",
        "juega_solo": "No", "reinvierte_ganancias": "Sí", "acepta_recomendaciones": "Sí",
        "total_visitas": 200, "dias_desde_primera_visita": 500, "dias_desde_ultima_visita": 1,
        "clasificacion": "VIP"
    },
    {
        "id": "j7", "nombre": "Rosa", "edad": 55, "ocupacion": "Diseñadora",
        "presupuesto_hoy": 400, "fichas_actuales": 250, "juego_actual": "Ruleta",
        "monto_apuesta": 60, "resultado_ultima_ronda": "Perdió", "tiempo_en_casino_hoy": 2.0,
        "hora_actual": "20:30", "rondas_jugadas_hoy": 12, "gasto_hoy": 350,
        "frecuencia_semanal": 3, "tiempo_promedio_visita": 200, "horario_habitual": "Noche",
        "prefiere_azar_o_estrategia": "Estrategia", "prefiere_rapido_o_lento": "Rápido",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "No", "gasto_promedio_ronda": 60,
        "gasto_maximo_historico": 150, "perdidas_acumuladas": 3000,
        "ganancias_acumuladas": 1000, "variedad_juegos_probados": 5,
        "juego_favorito": "Ruleta", "dias_visita": "Mié, Vie, Sáb",
        "juega_solo": "Sí", "reinvierte_ganancias": "Sí", "acepta_recomendaciones": "Sí",
        "total_visitas": 90, "dias_desde_primera_visita": 300, "dias_desde_ultima_visita": 15,
        "clasificacion": "Retener"
    },
    {
        "id": "j8", "nombre": "Luis", "edad": 19, "ocupacion": "Estudiante",
        "presupuesto_hoy": 30, "fichas_actuales": 2, "juego_actual": "Tragamonedas",
        "monto_apuesta": 2, "resultado_ultima_ronda": "Perdió", "tiempo_en_casino_hoy": 5.0,
        "hora_actual": "01:00", "rondas_jugadas_hoy": 25, "gasto_hoy": 25,
        "frecuencia_semanal": 1, "tiempo_promedio_visita": 180, "horario_habitual": "Madrugada",
        "prefiere_azar_o_estrategia": "Azar", "prefiere_rapido_o_lento": "Rápido",
        "cambia_al_perder": "Sí", "cambia_al_ganar": "Sí", "gasto_promedio_ronda": 3,
        "gasto_maximo_historico": 10, "perdidas_acumuladas": 100,
        "ganancias_acumuladas": 10, "variedad_juegos_probados": 1,
        "juego_favorito": "Tragamonedas", "dias_visita": "Dom",
        "juega_solo": "Sí", "reinvierte_ganancias": "No", "acepta_recomendaciones": "Sí",
        "total_visitas": 8, "dias_desde_primera_visita": 30, "dias_desde_ultima_visita": 1,
        "clasificacion": "Cuidar"
    },
]

def obtener_todos():
    if prolog_disponible():
        jugadores = []
        ids = ["j1","j2","j3","j4","j5","j6","j7","j8"]
        for jid in ids:
            datos = obtener_datos_jugador(jid)
            if datos:
                datos["clasificacion"] = clasificar_jugador(jid)
                jugadores.append(datos)
        if jugadores:
            return jugadores
    return JUGADORES_MOCK

def obtener_por_clasificacion(jugadores, clasif):
    return [j for j in jugadores if j["clasificacion"] == clasif]
