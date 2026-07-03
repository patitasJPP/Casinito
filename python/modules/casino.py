from modules.jugador import Jugador


class Casino:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        if isinstance(jugador, Jugador):
            self.jugadores.append(jugador)

    def calcular_gasto_promedio_general(self):
        if not self.jugadores:
            return 0.0
        total = sum(j.gasto_hoy for j in self.jugadores)
        return round(total / len(self.jugadores), 2)

    def contar_por_clasificacion(self, clasificacion):
        return sum(1 for j in self.jugadores if j.clasificacion == clasificacion)

    def obtener_vips(self):
        return [j for j in self.jugadores if j.es_vip()]

    def obtener_en_riesgo(self):
        return [j for j in self.jugadores if j.en_riesgo()]

    def total_gasto(self):
        return sum(j.gasto_hoy for j in self.jugadores)

    def top_gastadores(self, n=3):
        ordenados = sorted(self.jugadores, key=lambda j: j.gasto_hoy, reverse=True)
        return ordenados[:n]
