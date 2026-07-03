class Jugador:
    def __init__(self, nombre, id_jugador, gasto_hoy=0, rondas_jugadas_hoy=0,
                 gasto_maximo_historico=0, frecuencia_semanal=0,
                 perdidas_acumuladas=0, ganancias_acumuladas=0, clasificacion="Normal"):
        self.nombre = nombre
        self.id = id_jugador
        self.gasto_hoy = gasto_hoy
        self.rondas_jugadas_hoy = rondas_jugadas_hoy
        self.gasto_maximo_historico = gasto_maximo_historico
        self.frecuencia_semanal = frecuencia_semanal
        self.perdidas_acumuladas = perdidas_acumuladas
        self.ganancias_acumuladas = ganancias_acumuladas
        self.clasificacion = clasificacion

    def calcular_gasto_promedio(self):
        if self.rondas_jugadas_hoy > 0:
            return round(self.gasto_hoy / self.rondas_jugadas_hoy, 2)
        return 0.0

    def es_vip(self):
        return (self.gasto_maximo_historico >= 100 or
                self.frecuencia_semanal >= 3)

    def es_rentable(self):
        return self.ganancias_acumuladas > self.perdidas_acumuladas

    def en_riesgo(self):
        return self.perdidas_acumuladas > self.ganancias_acumuladas * 2

    def calcular_balance(self):
        return self.ganancias_acumuladas - self.perdidas_acumuladas
