import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos
from data.analisis import (
    crear_dataframe, analisis_por_clasificacion, correlaciones,
    resumen_estadistico, calcular_promedio_gasto,
    calcular_estadisticas_generales, ejercicio_array_notas,
    ejercicio_ventas, PANDAS_OK
)


class PanelEstadisticas:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugadores = obtener_todos()
        self.df = crear_dataframe(self.jugadores)
        self.stats = resumen_estadistico(self.jugadores)
        self.mostrar_metricas = {"gasto": True, "perdidas": True, "ganancias": True}

        PanelBase._crear_header(self.frame, "Estad\u00edsticas y An\u00e1lisis",
                                "An\u00e1lisis descriptivo de los jugadores usando pandas y numpy.")

        body = PanelBase._crear_body_scroll(self.frame)

        self._crear_selector_analisis(body)
        self._crear_tabla_resumen(body)
        if PANDAS_OK:
            self._crear_exploracion_inicial(body)
        self._crear_analisis_por_clasificacion(body)
        if PANDAS_OK:
            self._crear_correlaciones(body)
        if PANDAS_OK:
            self._crear_ejercicios_numpy(body)
        self._crear_funcional(body, self.jugadores)
        if PANDAS_OK:
            self._crear_graficos(body)

    def _crear_selector_analisis(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Opciones de An\u00e1lisis")
        opts = tk.Frame(frame, bg=COLORES["card_bg"])
        opts.pack(fill=tk.X, pady=(0, 10))

        self.tipo_analisis = tk.IntVar(value=1)
        tk.Radiobutton(opts, text="An\u00e1lisis Individual", variable=self.tipo_analisis,
                       value=1, bg=COLORES["card_bg"], fg=COLORES["texto"],
                       selectcolor=COLORES["fondo"], activebackground=COLORES["card_bg"],
                       activeforeground=COLORES["oro"],
                       font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 20))
        tk.Radiobutton(opts, text="An\u00e1lisis Grupal", variable=self.tipo_analisis,
                       value=2, bg=COLORES["card_bg"], fg=COLORES["texto"],
                       selectcolor=COLORES["fondo"], activebackground=COLORES["card_bg"],
                       activeforeground=COLORES["oro"],
                       font=("Segoe UI", 10)).pack(side=tk.LEFT)

        tk.Label(opts, text="  Mostrar:", bg=COLORES["card_bg"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(30, 6))
        self.cb_gasto = tk.IntVar(value=1)
        tk.Checkbutton(opts, text="Gasto", variable=self.cb_gasto,
                       bg=COLORES["card_bg"], fg=COLORES["texto"],
                       selectcolor=COLORES["fondo"], activebackground=COLORES["card_bg"],
                       activeforeground=COLORES["oro"],
                       font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=4)
        self.cb_perdidas = tk.IntVar(value=1)
        tk.Checkbutton(opts, text="P\u00e9rdidas", variable=self.cb_perdidas,
                       bg=COLORES["card_bg"], fg=COLORES["texto"],
                       selectcolor=COLORES["fondo"], activebackground=COLORES["card_bg"],
                       activeforeground=COLORES["oro"],
                       font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=4)
        self.cb_ganancias = tk.IntVar(value=1)
        tk.Checkbutton(opts, text="Ganancias", variable=self.cb_ganancias,
                       bg=COLORES["card_bg"], fg=COLORES["texto"],
                       selectcolor=COLORES["fondo"], activebackground=COLORES["card_bg"],
                       activeforeground=COLORES["oro"],
                       font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=4)

        self.lbl_sel = tk.Label(opts, text="  [Individual] Gasto+S/ Perd+S/ Gan+S/",
                                bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                                font=("Segoe UI", 9))
        self.lbl_sel.pack(side=tk.LEFT, padx=(10, 0))

        def _actualizar_sel():
            modo = "Individual" if self.tipo_analisis.get() == 1 else "Grupal"
            partes = []
            if self.cb_gasto.get(): partes.append("Gasto")
            if self.cb_perdidas.get(): partes.append("Perd")
            if self.cb_ganancias.get(): partes.append("Gan")
            self.lbl_sel.config(text=f"  [{modo}] {'+'.join(partes) if partes else 'Ninguna'}")

        self.tipo_analisis.trace_add("write", lambda *_: _actualizar_sel())
        self.cb_gasto.trace_add("write", lambda *_: _actualizar_sel())
        self.cb_perdidas.trace_add("write", lambda *_: _actualizar_sel())
        self.cb_ganancias.trace_add("write", lambda *_: _actualizar_sel())

    def _crear_exploracion_inicial(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Exploraci\u00f3n Inicial (pandas)")
        txt = ""
        txt += "df.head():\n" + self.df.head().to_string() + "\n\n"
        import io
        buf = io.StringIO()
        self.df.info(buf=buf)
        txt += "df.info():\n" + buf.getvalue() + "\n"
        txt += "df.describe():\n" + self.df.describe().to_string()
        txt_frame = tk.Frame(frame, bg=COLORES["card_alt"], padx=16, pady=10)
        txt_frame.pack(fill=tk.X, padx=20, pady=(0, 14))
        tk.Label(txt_frame, text=txt, bg=COLORES["card_alt"], fg=COLORES["texto"],
                 font=("Consolas", 8), justify=tk.LEFT, anchor="w").pack(anchor="w")

    def _crear_ejercicios_numpy(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Ejercicios con NumPy")
        ej1 = ejercicio_array_notas(self.jugadores)
        ej2 = ejercicio_ventas(self.jugadores)
        txt = ""
        txt += "Ejercicio 1 - Array de gastos:\n"
        txt += f"  Promedio gasto: S/ {ej1.get('promedio_gasto', 'N/A')}\n"
        txt += f"  Jugadores con gasto alto (>200): {ej1.get('jugadores_gasto_alto', 'N/A')}\n"
        txt += f"  Gastos > 200: {ej1.get('gastos_mayores_200', [])}\n\n"
        txt += "Ejercicio 5 - Array de 'ventas' (gasto_hoy):\n"
        txt += f"  Total gasto hoy: S/ {ej2.get('total_gasto_hoy', 'N/A')}\n"
        txt += f"  Promedio gasto hoy: S/ {ej2.get('promedio_gasto_hoy', 'N/A')}\n"
        txt += f"  Mayor gastador: {ej2.get('mayor_gastador', 'N/A')}\n"
        txt += f"  Menor gastador: {ej2.get('menor_gastador', 'N/A')}"
        txt_frame = tk.Frame(frame, bg=COLORES["card_alt"], padx=16, pady=10)
        txt_frame.pack(fill=tk.X, padx=20, pady=(0, 14))
        tk.Label(txt_frame, text=txt, bg=COLORES["card_alt"], fg=COLORES["texto"],
                 font=("Consolas", 9), justify=tk.LEFT, anchor="w").pack(anchor="w")

    def _crear_tabla_resumen(self, parent):
        frame = PanelBase._crear_card_contenedor(parent, "Estad\u00edsticas Descriptivas")

        grid = tk.Frame(frame, bg=COLORES["card_bg"])
        grid.pack(fill=tk.X, padx=20, pady=(0, 14))

        items = [
            ("Edad Promedio", f"{self.stats['edad_promedio']} a\u00f1os"),
            ("Gasto Promedio", f"S/ {self.stats['gasto_promedio']}"),
            ("P\u00e9rdida Promedio", f"S/ {self.stats['perdida_promedio']}"),
            ("Ganancia Promedio", f"S/ {self.stats['ganancia_promedio']}"),
            ("Frecuencia Promedio", f"{self.stats['frecuencia_promedio']}x/sem"),
            ("Balance Total", f"S/ {self.stats['balance']}"),
        ]
        for i, (label, valor) in enumerate(items):
            c = tk.Frame(grid, bg=COLORES["card_bg"], padx=12, pady=4)
            c.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(c, text=label, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 9)).pack(anchor="w")
            tk.Label(c, text=valor, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 13, "bold")).pack(anchor="w")

    def _crear_analisis_por_clasificacion(self, parent):
        frame = PanelBase._crear_card_contenedor(
            parent, "Agrupaci\u00f3n por Clasificaci\u00f3n (pandas groupby)"
        )

        if not PANDAS_OK:
            self._mostrar_mensaje_sin_pandas(frame)
        else:
            try:
                agrupado = analisis_por_clasificacion(self.df)
                texto = agrupado.to_string()
            except Exception:
                texto = "No hay suficientes datos para agrupar."

            txt_frame = tk.Frame(frame, bg=COLORES["card_alt"], padx=16, pady=10)
            txt_frame.pack(fill=tk.X, padx=20, pady=(0, 14))
            tk.Label(txt_frame, text=texto, bg=COLORES["card_alt"], fg=COLORES["texto"],
                     font=("Consolas", 9), justify=tk.LEFT, anchor="w").pack(anchor="w")

    def _crear_correlaciones(self, parent):
        frame = PanelBase._crear_card_contenedor(
            parent, "Matriz de Correlaci\u00f3n (numpy)"
        )

        try:
            corr = correlaciones(self.df)
            texto = corr.to_string()
        except Exception:
            texto = "No hay suficientes datos num\u00e9ricos."

        txt_frame = tk.Frame(frame, bg=COLORES["card_alt"], padx=16, pady=10)
        txt_frame.pack(fill=tk.X, padx=20, pady=(0, 14))
        tk.Label(txt_frame, text=texto, bg=COLORES["card_alt"], fg=COLORES["texto"],
                 font=("Consolas", 9), justify=tk.LEFT, anchor="w").pack(anchor="w")

    def _crear_funcional(self, parent, jugadores):
        from functools import reduce

        frame = PanelBase._crear_card_contenedor(
            parent, "Python Funcional en Acci\u00f3n"
        )

        vips = list(filter(lambda j: j["clasificacion"] == "VIP", jugadores))
        nombres_vip = list(map(lambda j: j["nombre"], vips))
        total_perdidas = reduce(lambda acc, j: acc + j["perdidas_acumuladas"], jugadores, 0)
        total_ganancias = reduce(lambda acc, j: acc + j["ganancias_acumuladas"], jugadores, 0)

        info_frame = tk.Frame(frame, bg=COLORES["card_alt"], padx=16, pady=10)
        info_frame.pack(fill=tk.X, padx=20, pady=(0, 14))

        func_items = [
            ("filter + lambda  VIPs", f"{', '.join(nombres_vip)}"),
            ("map  Nombres VIP", f"{', '.join(nombres_vip)}"),
            ("reduce  Total P\u00e9rdidas", f"S/ {total_perdidas}"),
            ("reduce  Total Ganancias", f"S/ {total_ganancias}"),
        ]
        for label, valor in func_items:
            row = tk.Frame(info_frame, bg=COLORES["card_alt"])
            row.pack(fill=tk.X, pady=2)
            tk.Label(row, text=label, bg=COLORES["card_alt"], fg=COLORES["texto_sec"],
                     font=("Consolas", 9), width=30, anchor="w").pack(side=tk.LEFT)
            tk.Label(row, text=valor, bg=COLORES["card_alt"], fg=COLORES["texto"],
                     font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(10, 0))

    def _crear_graficos(self, parent):
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        from matplotlib.figure import Figure

        frame = PanelBase._crear_card_contenedor(
            parent, "Visualizaci\u00f3n de Datos (matplotlib)"
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
        orden = self.df.sort_values("gasto_hoy")
        colores_barras = [COLORES["rojo"], COLORES["naranja"], COLORES["oro"],
                          COLORES["verde"], COLORES["verde_oscuro"],
                          COLORES["rojo_oscuro"], COLORES["naranja"], COLORES["oro"]]
        ax2.barh(range(len(orden)), orden["gasto_hoy"].values,
                 color=colores_barras[:len(orden)], edgecolor="none")
        ax2.set_yticks(range(len(orden)))
        ax2.set_yticklabels(orden["nombre"].values, color="white", fontsize=9)
        ax2.set_xlabel("Gasto Hoy (S/)", color="white", fontsize=10)
        ax2.set_title("Gasto por Jugador", color="white", fontsize=11, pad=12)
        ax2.tick_params(colors="white")
        for spine in ax2.spines.values():
            spine.set_color(COLORES["border"])

        canvas = FigureCanvasTkAgg(fig, master=grid_graf)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.X)

    def _mostrar_mensaje_sin_pandas(self, parent):
        msg_frame = tk.Frame(parent, bg=COLORES["card_alt"], padx=16, pady=14)
        msg_frame.pack(fill=tk.X, padx=20, pady=(0, 14))
        tk.Label(msg_frame, text="pandas / numpy no disponibles",
                 bg=COLORES["card_alt"], fg=COLORES["naranja"],
                 font=("Segoe UI", 11, "bold")).pack(anchor="w")
        tk.Label(msg_frame, text="Instala con: pip install pandas numpy",
                 bg=COLORES["card_alt"], fg=COLORES["texto_sec"],
                 font=("Consolas", 10)).pack(anchor="w", pady=(4, 0))
