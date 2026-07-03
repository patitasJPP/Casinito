import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from data.jugadores import JUGADORES_MOCK, obtener_por_clasificacion
from data.analisis import (
    crear_dataframe, filtrar_por_clasificacion, total_metricas,
    nombres_clasificados, resumen_estadistico
)
from functools import reduce


class TestJugadores:

    def test_total_jugadores(self):
        assert len(JUGADORES_MOCK) == 8

    def test_campos_completos(self):
        """Cada jugador debe tener todos los campos requeridos."""
        requeridos = ["id", "nombre", "edad", "ocupacion", "presupuesto_hoy",
                      "fichas_actuales", "gasto_hoy", "clasificacion"]
        for j in JUGADORES_MOCK:
            for campo in requeridos:
                assert campo in j, f"Falta campo {campo} en {j['id']}"

    def test_clasificaciones_validas(self):
        validas = {"VIP", "Retener", "Cuidar", "Servicio_Rapido"}
        for j in JUGADORES_MOCK:
            assert j["clasificacion"] in validas, f"Clasificación inválida: {j['clasificacion']}"

    def test_vips_existen(self):
        vips = obtener_por_clasificacion(JUGADORES_MOCK, "VIP")
        assert len(vips) >= 1

    def test_cuidar_existen(self):
        cuidar = obtener_por_clasificacion(JUGADORES_MOCK, "Cuidar")
        assert len(cuidar) >= 1

    def test_edades_positivas(self):
        for j in JUGADORES_MOCK:
            assert j["edad"] > 0


class TestAnalisis:

    def test_dataframe_creado(self):
        df = crear_dataframe(JUGADORES_MOCK)
        assert len(df) == 8
        assert "nombre" in df.columns
        assert "clasificacion" in df.columns

    def test_filtrar_por_clasificacion(self):
        vips = filtrar_por_clasificacion(JUGADORES_MOCK, "VIP")
        assert all(j["clasificacion"] == "VIP" for j in vips)

    def test_nombres_clasificados(self):
        nombres = nombres_clasificados(JUGADORES_MOCK, "VIP")
        for n in nombres:
            assert isinstance(n, str)

    def test_total_metricas_reduce(self):
        """Verifica que reduce suma correctamente."""
        total = total_metricas(JUGADORES_MOCK)
        esperado = sum(j["gasto_hoy"] for j in JUGADORES_MOCK)
        assert total["gasto_hoy"] == esperado

    def test_resumen_estadistico(self):
        resumen = resumen_estadistico(JUGADORES_MOCK)
        assert resumen["total"] == 8
        assert resumen["vip_count"] >= 1
        assert "balance" in resumen


class TestFuncional:

    def test_filter_lambda(self):
        """Demostración de programación funcional: filter + lambda."""
        vips = list(filter(lambda j: j["clasificacion"] == "VIP", JUGADORES_MOCK))
        assert all(j["clasificacion"] == "VIP" for j in vips)

    def test_map_lambda(self):
        """Demostración de programación funcional: map."""
        nombres = list(map(lambda j: j["nombre"], JUGADORES_MOCK))
        assert len(nombres) == 8
        assert all(isinstance(n, str) for n in nombres)

    def test_reduce(self):
        """Demostración de programación funcional: reduce."""
        total = reduce(lambda acc, j: acc + j["gasto_hoy"], JUGADORES_MOCK, 0)
        esperado = sum(j["gasto_hoy"] for j in JUGADORES_MOCK)
        assert total == esperado

    def test_list_comprehension(self):
        """Demostración de list comprehension."""
        nombres_vip = [j["nombre"] for j in JUGADORES_MOCK if j["clasificacion"] == "VIP"]
        assert len(nombres_vip) >= 1
