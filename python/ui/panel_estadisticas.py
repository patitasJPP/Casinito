import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos, VIP, RETENER, CUIDAR, SERVICIO_RAPIDO
from data.analisis import (
    crear_dataframe, analisis_por_clasificacion,
    resumen_estadistico, PANDAS_OK
)


class PanelEstadisticas:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugadores = obtener_todos()
        self.stats = resumen_estadistico(self.jugadores)
        self.df = crear_dataframe(self.jugadores) if PANDAS_OK else None

        PanelBase._crear_header(self.frame, "Estad\u00edsticas del Casino",
                                "M\u00e9tricas clave y comparativas por clasificaci\u00f3n de jugadores.")

        body = PanelBase._crear_body_scroll(self.frame)

        self._crear_resumen_general(body)
        self._crear_comparativa_clasificacion(body)
        self._crear_top_gastadores(body)
        if PANDAS_OK and self.df is not None:
            self._crear_graficos(body)

    def _crear_resumen_general(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Resumen General")

        grid = tk.Frame(frame, bg=COLORES["card_bg"])
        grid.pack(fill=tk.X, padx=20, pady=(0, 14))

        items = [
            ("Total Jugadores", f"{len(self.jugadores)}", COLORES["texto"]),
            ("Gasto Total Hoy", f"S/ {self.stats['gasto_promedio'] * len(self.jugadores):,.0f}", COLORES["oro"]),
            ("Gasto Promedio", f"S/ {self.stats['gasto_promedio']}", COLORES["oro"]),
            ("P\u00e9rdida Promedio", f"S/ {self.stats['perdida_promedio']}", COLORES["rojo"]),
            ("Ganancia Promedio", f"S/ {self.stats['ganancia_promedio']}", COLORES["verde"]),
            ("Balance Total", f"S/ {self.stats['balance']}", COLORES["verde"] if self.stats['balance'] >= 0 else COLORES["rojo"]),
            ("Edad Promedio", f"{self.stats['edad_promedio']} a\u00f1os", COLORES["texto"]),
            ("Frecuencia Prom.", f"{self.stats['frecuencia_promedio']}x/sem", COLORES["texto"]),
        ]
        for i, (label, valor, color) in enumerate(items):
            c = tk.Frame(grid, bg=COLORES["card_bg"], padx=12, pady=4)
            c.grid(row=i // 4, column=i % 4, sticky="w")
            tk.Label(c, text=label, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(c, text=valor, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 14, "bold")).pack(anchor="w")

        clasifs = [
            ("VIP", len(VIP), COLORES["oro"]),
            ("Retener", len(RETENER), COLORES["naranja"]),
            ("Cuidar", len(CUIDAR), COLORES["rojo"]),
            ("Servicio R\u00e1pido", len(SERVICIO_RAPIDO), COLORES["verde"]),
        ]
        sep = tk.Frame(grid, bg=COLORES["border"], height=1)
        sep.grid(row=2, column=0, columnspan=4, sticky="ew", pady=8)
        for i, (nombre, cantidad, color) in enumerate(clasifs):
            c = tk.Frame(grid, bg=COLORES["card_bg"], padx=12, pady=2)
            c.grid(row=3, column=i, sticky="w")
            tk.Label(c, text=nombre, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 9, "bold")).pack(anchor="w")
            tk.Label(c, text=str(cantidad), bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 18, "bold")).pack(anchor="w")

    def _crear_comparativa_clasificacion(self, parent):
        frame = PanelBase._crear_card_contenedor(
            parent, "Comparativa por Clasificaci\u00f3n"
        )

        if not PANDAS_OK or self.df is None:
            tk.Label(frame, text="Requiere pandas: pip install pandas",
                     bg=COLORES["card_bg"], fg=COLORES["naranja"],
                     font=("Segoe UI", 10)).pack(pady=10)
            return

        try:
            agrupado = analisis_por_clasificacion(self.df)
        except Exception:
            agrupado = None

        if agrupado is None or agrupado.empty:
            tk.Label(frame, text="No hay datos suficientes.",
                     bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 10)).pack(pady=10)
            return

        cols_mostrar = [("gasto_hoy", "mean"), ("perdidas", "mean"), ("ganancias", "mean")]
        etiquetas = ["Gasto Prom.", "P\u00e9rdida Prom.", "Ganancia Prom."]
        colores_fila = {
            "VIP": COLORES["oro"],
            "Retener": COLORES["naranja"],
            "Cuidar": COLORES["rojo"],
            "Servicio_Rapido": COLORES["verde"],
        }

        tabla = tk.Frame(frame, bg=COLORES["card_bg"])
        tabla.pack(fill=tk.X, padx=20, pady=(0, 14))

        conteos = self.df["clasificacion"].value_counts()
        encabezados = ["Clasificaci\u00f3n", "Cantidad"] + etiquetas
        for j, h in enumerate(encabezados):
            tk.Label(tabla, text=h, bg=COLORES["card_bg"], fg=COLORES["oro"],
                     font=("Segoe UI", 10, "bold"), padx=12, pady=4,
                     width=14 if j > 0 else 18, anchor="w").grid(row=0, column=j)

        for i, (clasif, row) in enumerate(agrupado.iterrows()):
            color = colores_fila.get(clasif, COLORES["texto"])
            bg_fila = COLORES["card_alt"] if i % 2 == 0 else COLORES["card_bg"]
            tk.Label(tabla, text=clasif.replace("_", " "), bg=bg_fila, fg=color,
                     font=("Segoe UI", 10, "bold"), padx=12, pady=3,
                     width=18, anchor="w").grid(row=i + 1, column=0)
            cant = int(conteos.get(clasif, 0))
            tk.Label(tabla, text=str(cant), bg=bg_fila, fg=COLORES["texto"],
                     font=("Segoe UI", 10), padx=12, pady=3,
                     width=14, anchor="w").grid(row=i + 1, column=1)
            for j, col in enumerate(cols_mostrar):
                val = float(row[col])
                texto = f"S/ {val:,.1f}"
                tk.Label(tabla, text=texto, bg=bg_fila, fg=COLORES["texto"],
                         font=("Segoe UI", 10), padx=12, pady=3,
                         width=14, anchor="w").grid(row=i + 1, column=j + 2)

    def _crear_top_gastadores(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Top 10 Gastadores del D\u00eda")

        ordenados = sorted(self.jugadores, key=lambda j: j["gasto_hoy"], reverse=True)[:10]

        tabla = tk.Frame(frame, bg=COLORES["card_bg"])
        tabla.pack(fill=tk.X, padx=20, pady=(0, 14))

        colores_fila = {
            "VIP": COLORES["oro"], "Retener": COLORES["naranja"],
            "Cuidar": COLORES["rojo"], "Servicio_Rapido": COLORES["verde"],
        }

        encabezados = ["#", "Nombre", "Clasificaci\u00f3n", "Gasto Hoy", "Juego", "Frecuencia"]
        anchos = [4, 20, 16, 12, 18, 12]
        for j, h in enumerate(encabezados):
            tk.Label(tabla, text=h, bg=COLORES["card_bg"], fg=COLORES["oro"],
                     font=("Segoe UI", 10, "bold"), padx=10, pady=4,
                     width=anchos[j], anchor="w").grid(row=0, column=j)

        for i, j in enumerate(ordenados):
            color = colores_fila.get(j["clasificacion"], COLORES["texto"])
            bg_fila = COLORES["card_alt"] if i % 2 == 0 else COLORES["card_bg"]
            valores = [
                str(i + 1), j["nombre"],
                j["clasificacion"].replace("_", " "),
                f"S/ {j['gasto_hoy']}",
                j["juego_favorito"],
                f"{j['frecuencia_semanal']}x/sem",
            ]
            for k, v in enumerate(valores):
                fg = color if k == 2 else COLORES["texto"]
                tk.Label(tabla, text=v, bg=bg_fila, fg=fg,
                         font=("Segoe UI", 10), padx=10, pady=3,
                         width=anchos[k], anchor="w").grid(row=i + 1, column=k)

    def _crear_graficos(self, parent):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from matplotlib.figure import Figure

        frame = PanelBase._crear_card_contenedor(
            parent, "Distribuci\u00f3n y Tendencias"
        )

        grid_graf = tk.Frame(frame, bg=COLORES["card_bg"])
        grid_graf.pack(fill=tk.X, padx=20, pady=(0, 14))

        fig = Figure(figsize=(10, 5), dpi=100, facecolor=COLORES["card_bg"])
        fig.subplots_adjust(wspace=0.3, hspace=0.4)

        ax1 = fig.add_subplot(121)
        counts = self.df["clasificacion"].value_counts()

        orden_clasifs = ["VIP", "Retener", "Cuidar", "Servicio_Rapido"]
        orden_etiquetas = ["VIP", "Retener", "Cuidar", "R\u00e1pido"]
        colores_pie = [COLORES["oro"], COLORES["naranja"], COLORES["rojo"], COLORES["verde"]]
        valores_ordenados = [counts.get(c, 0) for c in orden_clasifs]
        valores_positivos = [v for v in valores_ordenados if v > 0]
        etiquetas_positivas = [orden_etiquetas[i] for i, v in enumerate(valores_ordenados) if v > 0]
        colores_positivos = [colores_pie[i] for i, v in enumerate(valores_ordenados) if v > 0]

        if valores_positivos:
            wedges, texts, autotexts = ax1.pie(
                valores_positivos, labels=etiquetas_positivas, autopct="%1.1f%%",
                colors=colores_positivos, startangle=90,
                textprops={"color": "white", "fontsize": 9}
            )
            for t in autotexts:
                t.set_color("black")
                t.set_fontweight("bold")
        ax1.set_title("Distribuci\u00f3n de Clasificaciones", color="white", fontsize=11, pad=12)

        ax2 = fig.add_subplot(122)
        top10 = self.df.nlargest(10, "gasto_hoy")
        ax2.barh(range(len(top10)), top10["gasto_hoy"].values,
                 color=[COLORES["oro"], COLORES["naranja"], COLORES["rojo"],
                        COLORES["verde"], COLORES["verde_oscuro"]],
                 edgecolor="none")
        ax2.set_yticks(range(len(top10)))
        ax2.set_yticklabels(top10["nombre"].values, color="white", fontsize=9)
        ax2.set_xlabel("Gasto Hoy (S/)", color="white", fontsize=10)
        ax2.set_title("Top 10 Gastadores", color="white", fontsize=11, pad=12)
        ax2.tick_params(colors="white")
        for spine in ax2.spines.values():
            spine.set_color(COLORES["border"])

        canvas = FigureCanvasTkAgg(fig, master=grid_graf)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.X)
