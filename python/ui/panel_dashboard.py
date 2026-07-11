import tkinter as tk
from tkinter import ttk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos
from data.analisis import resumen_estadistico


def _fmt(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    if num >= 1000:
        return f"{num/1000:.1f}k"
    return str(int(num)) if num == int(num) else f"{num:.1f}"


def _pct(valor, total):
    return f"{valor/max(total,1)*100:.0f}%"


class PanelDashboard:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugadores = obtener_todos()

        PanelBase._crear_header(self.frame, "Dashboard Ejecutivo",
                                "Panorama general del casino en tiempo real")

        body = PanelBase._crear_body_scroll(self.frame)

        stats = resumen_estadistico(self.jugadores)
        self._calc_metricas(stats)

        cards_data = [
            ("\U0001f4b0", "Ingresos del D\u00eda", f"S/ {_fmt(stats['total_gasto'])}",
             COLORES["verde"], f"Meta: S/ 60k - {_pct(stats['total_gasto'], 60000)}"),
            ("\U0001f465", "Jugadores Activos",
             stats["activos_hoy"], COLORES["texto"],
             f"De {stats['total']} registrados"),
            ("\U0001f4c8", "LTV Promedio",
             f"S/ {_fmt(stats['ltv_promedio'])}", COLORES["oro"],
             "Valor neto por jugador"),
            ("\U0001f504", "Tasa Retenci\u00f3n",
             _pct(stats["retenidos_7d"], stats['total']),
             COLORES["verde"] if stats["retenidos_7d"]/max(stats['total'],1) >= 0.4 else COLORES["rojo"],
             "Regresaron en 7 d\u00edas"),
            ("\u26a0", "Riesgo Churn",
             stats["churn_risk"], COLORES["rojo"],
             "Jugadores en riesgo de abandono"),
            ("\U0001f4c9", "Margen Bruto",
             _pct(stats["margen_bruto"], 100) if stats["margen_bruto"] <= 100 else ">100%",
             COLORES["verde"] if stats['margen_bruto'] >= 15 else COLORES["rojo"],
             "Gan. Neta / Gasto"),
        ]
        self._crear_kpi_gallery_4xn(body, cards_data)

        izq = PanelBase._crear_card_contenedor(
            body, "Distribuci\u00f3n de Clasificaciones",
            "Proporci\u00f3n de cada tipo de jugador"
        )
        self._crear_barras_distribucion(izq, stats)

        der = PanelBase._crear_card_contenedor(
            body, "Ingresos vs P\u00e9rdidas",
            "Comparativa financiera por clasificaci\u00f3n"
        )
        self._crear_barras_financieras(der)

        self._crear_tabla_top(body)

        fin = PanelBase._crear_card_contenedor(
            body, "Estado Financiero Detallado",
            "Ingresos, costos y rentabilidad del casino"
        )
        self._crear_resumen_financiero(fin, stats)

        self._crear_mapa_calor(body)

        self._crear_alertas(body, stats)

        export_frame = tk.Frame(body, bg=COLORES["card_bg"],
                                highlightbackground=COLORES["border"], highlightthickness=1)
        export_frame.pack(fill=tk.X, pady=(0, 16), padx=0)

    def _calc_metricas(self, stats):
        j = self.jugadores
        stats["activos_hoy"] = sum(1 for x in j if x["tiempo_en_casino_hoy"] > 0)
        stats["retenidos_7d"] = sum(1 for x in j if x["dias_desde_ultima_visita"] <= 7)

        ltv_total = sum(x["ganancias_acumuladas"] - x["perdidas_acumuladas"] for x in j)
        stats["ltv_promedio"] = ltv_total / max(len(j), 1)

        churn = [x for x in j if x["dias_desde_ultima_visita"] > 30
                 and x["fichas_actuales"] < max(x["presupuesto_hoy"] * 0.1, 10)
                 and x["perdidas_acumuladas"] > x["ganancias_acumuladas"] * 1.5]
        stats["churn_risk"] = len(churn)

        ganancia_neta = stats["total_ganancias"] - stats["total_perdidas"]
        stats["margen_bruto"] = (ganancia_neta / max(stats["total_gasto"], 1)) * 100

        clasifs = ["VIP", "Retener", "Cuidar", "Servicio_Rapido"]
        stats["fin_por_clasif"] = {}
        for c in clasifs:
            pool = [x for x in j if x["clasificacion"] == c]
            stats["fin_por_clasif"][c] = {
                "gasto": sum(x["gasto_hoy"] for x in pool),
                "ganancias": sum(x["ganancias_acumuladas"] for x in pool),
                "perdidas": sum(x["perdidas_acumuladas"] for x in pool),
            }

        juegos = {}
        for x in j:
            jue = x["juego_favorito"]
            if jue not in juegos:
                juegos[jue] = {"count": 0, "gasto": 0, "tiempo": 0}
            juegos[jue]["count"] += 1
            juegos[jue]["gasto"] += x["gasto_hoy"]
            juegos[jue]["tiempo"] += x["tiempo_en_casino_hoy"]
        stats["juegos"] = juegos

    def _crear_kpi_gallery_4xn(self, parent, cards_data):
        body = tk.Frame(parent, bg=COLORES["fondo"])
        body.pack(fill=tk.X)

        _refreshing = [False]
        def _reflow(event=None):
            if _refreshing[0]:
                return
            _refreshing[0] = True
            for i, child in enumerate(body.winfo_children()):
                child.grid_forget()
                row = i // 3
                col = i % 3
                child.grid(row=row, column=col, padx=(0, 14), pady=6, sticky="ew")
            for c in range(3):
                body.grid_columnconfigure(c, weight=1)
            _refreshing[0] = False

        parent.after(50, _reflow)
        for icono, titulo, valor, color, desc in cards_data:
            PanelBase._crear_kpi_card(body, icono, titulo, valor, color, desc)

    def _crear_barras_distribucion(self, parent, stats):
        barras = tk.Frame(parent, bg=COLORES["card_bg"])
        barras.pack(fill=tk.X, padx=10, pady=(0, 14))

        clasifs = [
            ("VIP", stats["vip_count"], COLORES["oro"]),
            ("Retener", stats["retener_count"], COLORES["naranja"]),
            ("Cuidar", stats["cuidar_count"], COLORES["rojo"]),
            ("R\u00e1pido", stats["rapido_count"], COLORES["verde"]),
        ]
        max_val = max((c[1] for c in clasifs), default=1)

        for label, val, color in clasifs:
            row = tk.Frame(barras, bg=COLORES["card_bg"])
            row.pack(fill=tk.X, pady=3)

            tk.Label(row, text=label, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 9, "bold"), width=8, anchor="w").pack(side=tk.LEFT)

            bar_bg = tk.Frame(row, bg=COLORES["card_alt"], height=20)
            bar_bg.pack(side=tk.LEFT, padx=(0, 8), fill=tk.X, expand=True)

            proporcion = val / max_val if max_val > 0 else 0
            ancho_inicial = max(int(200 * proporcion), 1) if val > 0 else 0
            bar_fill = tk.Frame(bar_bg, bg=color, height=20, width=ancho_inicial)
            bar_fill.place(x=0, y=0)

            tk.Label(row, text=str(val), bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 11, "bold"), width=3).pack(side=tk.LEFT)
            tk.Label(row, text=_pct(val, stats["total"]), bg=COLORES["card_bg"],
                     fg=color, font=("Segoe UI", 9, "bold"), width=4).pack(side=tk.LEFT)

    def _crear_barras_financieras(self, parent):
        cont = tk.Frame(parent, bg=COLORES["card_bg"])
        cont.pack(fill=tk.X, padx=10, pady=(0, 14))

        fin = {"VIP": self._fin_por_clasif("VIP"),
               "Retener": self._fin_por_clasif("Retener"),
               "Cuidar": self._fin_por_clasif("Cuidar"),
               "R\u00e1pido": self._fin_por_clasif("Servicio_Rapido")}

        for label, vals in fin.items():
            row = tk.Frame(cont, bg=COLORES["card_bg"])
            row.pack(fill=tk.X, pady=3)

            tk.Label(row, text=label, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 8, "bold"), width=8, anchor="w").pack(side=tk.LEFT)

            mini = tk.Frame(row, bg=COLORES["card_bg"])
            mini.pack(side=tk.LEFT, fill=tk.X, expand=True)
            mini.grid_columnconfigure((0, 1), weight=1)

            g_neto = vals["ganancias"] - vals["perdidas"]
            g_color = COLORES["verde"] if g_neto >= 0 else COLORES["rojo"]
            lbl_neto = f"S/{_fmt(g_neto)}" if abs(g_neto) < 1000000 else f"S/{_fmt(g_neto)}"
            tk.Label(mini, text=f"Gasto: S/{_fmt(vals['gasto'])}",
                     bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(mini, text=f"Neto: {lbl_neto}",
                     bg=COLORES["card_bg"], fg=g_color,
                     font=("Segoe UI", 8, "bold")).pack(anchor="w")

    def _fin_por_clasif(self, clasif):
        pool = [x for x in self.jugadores if x["clasificacion"] == clasif]
        return {
            "gasto": sum(x["gasto_hoy"] for x in pool),
            "ganancias": sum(x["ganancias_acumuladas"] for x in pool),
            "perdidas": sum(x["perdidas_acumuladas"] for x in pool),
        }

    def _crear_tabla_top(self, parent):
        cont = PanelBase._crear_card_contenedor(
            parent, "Top 10 Jugadores por Gasto Hoy",
            "Jugadores con mayor actividad del d\u00eda"
        )
        inner = tk.Frame(cont, bg=COLORES["card_bg"])
        inner.pack(fill=tk.X, padx=10, pady=(0, 14))

        cols = ["#", "Nombre", "Clasif", "Gasto Hoy", "Fichas", "Juego", "\u00daltima Visita", "Riesgo"]
        widths = [30, 150, 70, 80, 60, 100, 90, 50]
        header = tk.Frame(inner, bg=COLORES["card_alt"])
        header.pack(fill=tk.X)
        for c, w in zip(cols, widths):
            tk.Label(header, text=c, bg=COLORES["card_alt"], fg=COLORES["oro"],
                     font=("Segoe UI", 8, "bold"), width=w//7).pack(side=tk.LEFT, padx=2)

        top10 = sorted(self.jugadores, key=lambda x: x["gasto_hoy"], reverse=True)[:10]
        for i, j in enumerate(top10):
            color_fila = COLORES["card_alt"] if i % 2 == 0 else COLORES["card_bg"]
            fila = tk.Frame(inner, bg=color_fila)
            fila.pack(fill=tk.X)

            en_riesgo = (j["dias_desde_ultima_visita"] > 30 and
                         j["fichas_actuales"] < max(j["presupuesto_hoy"] * 0.1, 10) and
                         j["perdidas_acumuladas"] > j["ganancias_acumuladas"] * 1.5)

            tag, tag_color = PanelBase._crear_tag(j["clasificacion"])
            items = [
                str(i + 1),
                j["nombre"][:18],
                tag,
                f"S/{j['gasto_hoy']}",
                str(j["fichas_actuales"]),
                j["juego_actual"],
                f"{j['dias_desde_ultima_visita']}d",
                "\u26a0" if en_riesgo else "",
            ]
            for k, item in enumerate(items):
                fg = tag_color if k == 2 else COLORES["rojo"] if k == 7 and en_riesgo else COLORES["texto"]
                w = widths[k] // 7
                lbl = tk.Label(fila, text=item, bg=color_fila, fg=fg,
                               font=("Segoe UI", 8), width=w, anchor="w")
                lbl.pack(side=tk.LEFT, padx=2)

    def _crear_resumen_financiero(self, parent, stats):
        total_gasto = stats["total_gasto"]
        total_perdidas = stats["total_perdidas"]
        total_ganancias = stats["total_ganancias"]
        ganancia_neta = total_ganancias - total_perdidas
        comisiones = int(total_gasto * 0.05)
        total_ingresos = total_gasto + comisiones + 1200

        premios = int(total_ganancias * 0.08)
        costo_fichas = 500
        costos_vars = premios + int(premios * 0.10) + costo_fichas

        alquiler_dia = 40000 // 30
        sueldos_dia = 30000 // 30
        electricidad = 8000 // 30
        internet = 2000 // 30
        seguros = 5000 // 30
        mantenimiento = 4000 // 30
        licencias = 5000 // 30
        marketing = 10000 // 30
        contador = 5000 // 30
        cctv = 2000 // 30
        suministros = 1000 // 30
        depreciacion = 10000 // 30
        costos_fijos = (alquiler_dia + sueldos_dia + electricidad + internet +
                         seguros + mantenimiento + licencias + marketing +
                         contador + cctv + suministros + depreciacion)

        margen_bruto = total_ingresos - costos_vars - costos_fijos
        impuestos = int(margen_bruto * 0.045)
        margen_neto = margen_bruto - impuestos

        pct_bruto = (margen_bruto / max(total_ingresos, 1)) * 100
        pct_neto = (margen_neto / max(total_ingresos, 1)) * 100
        roi = (margen_bruto / max(costos_fijos, 1)) * 100

        main_frame = tk.Frame(parent, bg=COLORES["card_bg"])
        main_frame.pack(fill=tk.X, padx=10, pady=(0, 14))

        tk.Label(main_frame, text="INGRESOS OPERATIVOS",
                 bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        for lbl, val, color in [
            ("Apuestas del d\u00eda", f"S/ {_fmt(total_gasto)}", COLORES["texto"]),
            ("Comisiones 5%", f"S/ {_fmt(comisiones)}", COLORES["texto"]),
            ("Servicios VIP", "S/ 1.2k", COLORES["texto"]),
        ]:
            fila = tk.Frame(main_frame, bg=COLORES["card_bg"])
            fila.pack(fill=tk.X)
            tk.Label(fila, text=f"  \u2514 {lbl}", bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(side=tk.LEFT)
            tk.Label(fila, text=val, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 8, "bold")).pack(side=tk.RIGHT)
        tk.Label(main_frame, text=f"Total Ingresos: S/ {_fmt(total_ingresos)}",
                 bg=COLORES["card_bg"], fg=COLORES["verde"],
                 font=("Segoe UI", 10, "bold")).pack(anchor="e", pady=(2, 8))

        tk.Label(main_frame, text="COSTOS VARIABLES",
                 bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        for lbl, val in [
            ("Pago de premios", f"S/ {_fmt(premios)}"),
            ("Comisiones dealers", f"S/ {_fmt(int(premios*0.10))}"),
            ("Costo fichas", f"S/ {_fmt(costo_fichas)}"),
        ]:
            fila = tk.Frame(main_frame, bg=COLORES["card_bg"])
            fila.pack(fill=tk.X)
            tk.Label(fila, text=f"  \u2514 {lbl}", bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(side=tk.LEFT)
            tk.Label(fila, text=val, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 8)).pack(side=tk.RIGHT)
        tk.Label(main_frame, text=f"Total Costos Variables: S/ {_fmt(costos_vars)}",
                 bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 10, "bold")).pack(anchor="e", pady=(2, 8))

        tk.Label(main_frame, text="COSTOS FIJOS (por d\u00eda)",
                 bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))

        costos_items = [
            ("Alquiler", f"S/ {_fmt(alquiler_dia)}"),
            ("Sueldos planilla", f"S/ {_fmt(sueldos_dia)}"),
            ("Electricidad/agua", f"S/ {_fmt(electricidad)}"),
            ("Internet/telecom", f"S/ {_fmt(internet)}"),
            ("Seguros", f"S/ {_fmt(seguros)}"),
            ("Mantenimiento", f"S/ {_fmt(mantenimiento)}"),
            ("Licencias/permisos", f"S/ {_fmt(licencias)}"),
            ("Marketing", f"S/ {_fmt(marketing)}"),
            ("Contador/legal", f"S/ {_fmt(contador)}"),
            ("CCTV/seguridad", f"S/ {_fmt(cctv)}"),
            ("Suministros", f"S/ {_fmt(suministros)}"),
            ("Depreciaci\u00f3n", f"S/ {_fmt(depreciacion)}"),
        ]
        for lbl, val in costos_items:
            fila = tk.Frame(main_frame, bg=COLORES["card_bg"])
            fila.pack(fill=tk.X)
            tk.Label(fila, text=f"  \u2514 {lbl}", bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(side=tk.LEFT)
            tk.Label(fila, text=val, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 8)).pack(side=tk.RIGHT)
        tk.Label(main_frame, text=f"Total Costos Fijos: S/ {_fmt(costos_fijos)}",
                 bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 10, "bold")).pack(anchor="e", pady=(2, 8))

        sep = tk.Frame(main_frame, bg=COLORES["border"], height=1)
        sep.pack(fill=tk.X, pady=6)

        margen_color = COLORES["verde"] if margen_bruto >= 0 else COLORES["rojo"]
        tk.Label(main_frame, text=f"MARGEN BRUTO OPERATIVO: S/ {_fmt(margen_bruto)}",
                 bg=COLORES["card_bg"], fg=margen_color,
                 font=("Segoe UI", 11, "bold")).pack(anchor="e", pady=2)
        tk.Label(main_frame, text=f"Impuestos 4.5%: -S/ {_fmt(impuestos)}",
                 bg=COLORES["card_bg"], fg=COLORES["texto_dim"],
                 font=("Segoe UI", 8)).pack(anchor="e")
        tk.Label(main_frame, text=f"MARGEN NETO ESTIMADO: S/ {_fmt(margen_neto)}",
                 bg=COLORES["card_bg"], fg=margen_color,
                 font=("Segoe UI", 12, "bold")).pack(anchor="e", pady=2)

        sep2 = tk.Frame(main_frame, bg=COLORES["border"], height=1)
        sep2.pack(fill=tk.X, pady=6)

        tk.Label(main_frame, text="RENTABILIDAD",
                 bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 9, "bold")).pack(anchor="w")
        for lbl, val in [
            ("Margen Bruto", f"{pct_bruto:.1f}%"),
            ("Margen Neto", f"{pct_neto:.1f}%"),
            ("ROI Diario", f"{roi:.0f}%"),
            ("Ganancia Neta (hist)", f"S/ {_fmt(ganancia_neta)}"),
        ]:
            fila = tk.Frame(main_frame, bg=COLORES["card_bg"])
            fila.pack(fill=tk.X)
            tk.Label(fila, text=f"  {lbl}", bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(side=tk.LEFT)
            tk.Label(fila, text=val, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 8, "bold")).pack(side=tk.RIGHT)

    def _crear_mapa_calor(self, parent):
        cont = PanelBase._crear_card_contenedor(
            parent, "Mapa de Calor por Zona",
            "Tr\u00e1fico e ingresos por \u00e1rea del casino"
        )

        grid = tk.Frame(cont, bg=COLORES["card_bg"])
        grid.pack(fill=tk.X, padx=10, pady=(0, 14))
        grid.grid_columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="zona")

        juegos = {}
        for x in self.jugadores:
            jue = x["juego_favorito"]
            if jue not in juegos:
                juegos[jue] = {"count": 0, "gasto": 0, "tiempo": 0}
            juegos[jue]["count"] += 1
            juegos[jue]["gasto"] += x["gasto_hoy"]
            juegos[jue]["tiempo"] += x["tiempo_en_casino_hoy"]

        zonas = sorted(juegos.items(), key=lambda z: z[1]["count"], reverse=True)

        for i, (zona, datos) in enumerate(zonas):
            intensidad = min(datos["count"] / max(z[1]["count"] for z in zonas), 1.0) if zonas else 0
            if intensidad > 0.7:
                bg_zona = "#3a1515"
                borde = COLORES["rojo"]
            elif intensidad > 0.4:
                bg_zona = "#3a2e15"
                borde = COLORES["naranja"]
            else:
                bg_zona = "#152a15"
                borde = COLORES["verde"]

            card = tk.Frame(grid, bg=bg_zona, highlightbackground=borde,
                            highlightthickness=1, padx=8, pady=10)
            card.grid(row=0, column=i, sticky="nsew", padx=4)

            tk.Label(card, text=zona, bg=bg_zona, fg=COLORES["texto"],
                     font=("Segoe UI", 10, "bold")).pack(anchor="center")
            tk.Label(card, text=f"{datos['count']} jugadores", bg=bg_zona,
                     fg=COLORES["texto_sec"], font=("Segoe UI", 8)).pack(anchor="center")
            tk.Label(card, text=f"S/{_fmt(datos['gasto'])}", bg=bg_zona,
                     fg=borde, font=("Segoe UI", 10, "bold")).pack(anchor="center")
            tk.Label(card, text=f"{datos['tiempo']:.1f} hrs", bg=bg_zona,
                     fg=COLORES["texto_dim"], font=("Segoe UI", 8)).pack(anchor="center")

    def _crear_alertas(self, parent, stats):
        alertas = []

        vips_riesgo = [x for x in self.jugadores if x["clasificacion"] == "VIP"
                       and x["fichas_actuales"] < 50]
        for v in vips_riesgo[:3]:
            alertas.append(("\u26a0", "VIP en riesgo",
                            f"{v['nombre']} - fichas: {v['fichas_actuales']}",
                            COLORES["rojo"]))

        trafico_bajo = [(z, d) for z, d in stats.get("juegos", {}).items() if d["count"] < 3]
        for zona, _ in trafico_bajo[:2]:
            alertas.append(("\u26a0", "Tr\u00e1fico bajo",
                            f"Mesa de {zona} - pocos jugadores",
                            COLORES["naranja"]))

        churn_list = [x for x in self.jugadores
                      if x["dias_desde_ultima_visita"] > 30
                      and x["fichas_actuales"] < max(x["presupuesto_hoy"] * 0.1, 10)
                      and x["perdidas_acumuladas"] > x["ganancias_acumuladas"] * 1.5]
        if churn_list:
            alertas.append(("\u26a0", "Jugadores sin visita",
                            f"{len(churn_list)} jugadores sin visita > 30 d\u00edas",
                            COLORES["naranja"]))

        pct_meta = stats["total_gasto"] / 60000 * 100
        alertas.append(("\u2139", "Meta diaria",
                        f"Ingresos al {pct_meta:.0f}% de la meta (S/ 60k)",
                        COLORES["verde"] if pct_meta >= 100 else COLORES["naranja"]))

        total_ganancias = stats["total_ganancias"]
        total_perdidas = stats["total_perdidas"]
        if total_perdidas > total_ganancias:
            alertas.append(("\u26a0", "Balance negativo",
                            "P\u00e9rdidas acumuladas superan ganancias",
                            COLORES["rojo"]))

        if not alertas:
            return

        cont = PanelBase._crear_card_contenedor(
            parent, "Alertas y Notificaciones",
            "Informaci\u00f3n cr\u00edtica del estado actual"
        )
        inner = tk.Frame(cont, bg=COLORES["card_bg"])
        inner.pack(fill=tk.X, padx=10, pady=(0, 14))

        for icono, titulo, detalle, color in alertas[:6]:
            card = tk.Frame(inner, bg=COLORES["card_alt"],
                            highlightbackground=color, highlightthickness=1,
                            padx=10, pady=6)
            card.pack(fill=tk.X, pady=(0, 6))

            top = tk.Frame(card, bg=COLORES["card_alt"])
            top.pack(fill=tk.X)
            tk.Label(top, text=icono, bg=COLORES["card_alt"], fg=color,
                     font=("Segoe UI", 12)).pack(side=tk.LEFT, padx=(0, 6))
            tk.Label(top, text=titulo, bg=COLORES["card_alt"], fg=color,
                     font=("Segoe UI", 9, "bold")).pack(side=tk.LEFT)
            tk.Label(card, text=detalle, bg=COLORES["card_alt"],
                     fg=COLORES["texto"], font=("Segoe UI", 9),
                     anchor="w", justify=tk.LEFT).pack(fill=tk.X, pady=(4, 0))
