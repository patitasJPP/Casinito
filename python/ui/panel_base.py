import tkinter as tk
from tkinter import ttk
from config import COLORES


class PanelBase:

    @staticmethod
    def _crear_header(frame, titulo, subtitulo=""):
        header = tk.Frame(frame, bg=COLORES["card_bg"], padx=28, pady=20)
        header.pack(fill=tk.X, pady=(0, 2))
        tk.Label(header, text=titulo, bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 20, "bold")).pack(anchor="w")
        if subtitulo:
            tk.Label(header, text=subtitulo, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 10)).pack(anchor="w", pady=(4, 0))

    @staticmethod
    def _crear_tag(clasif):
        etiquetas = {
            "VIP": ("VIP", COLORES["oro"]),
            "Retener": ("Retener", COLORES["naranja"]),
            "Cuidar": ("Cuidar", COLORES["rojo"]),
            "Servicio_Rapido": ("R\u00e1pido", COLORES["verde"]),
        }
        return etiquetas.get(clasif, (clasif, COLORES["texto_sec"]))

    @staticmethod
    def _crear_kpi_cards_grid(parent, cards_data, ancho_card=220):
        body = tk.Frame(parent, bg=COLORES["fondo"])
        body.pack(fill=tk.X)

        _refreshing = [False]
        def _reflow(event=None):
            if _refreshing[0]:
                return
            _refreshing[0] = True
            ancho_disp = parent.winfo_width() - 56
            cols = max(1, ancho_disp // ancho_card)
            for i, child in enumerate(body.winfo_children()):
                child.grid_forget()
                row = i // cols
                col = i % cols
                child.grid(row=row, column=col, padx=(0, 14), pady=6, sticky="ew")
            for c in range(cols):
                body.grid_columnconfigure(c, weight=1)
            _refreshing[0] = False

        parent.after(50, _reflow)
        for icono, titulo, valor, color, desc in cards_data:
            PanelBase._crear_kpi_card(body, icono, titulo, valor, color, desc)

    @staticmethod
    def _crear_kpi_card(parent, icono, titulo, valor, color, desc=""):
        card = tk.Frame(parent, bg=COLORES["card_bg"], padx=18, pady=14,
                        highlightbackground=COLORES["border"], highlightthickness=1)
        card.grid_propagate(False)

        card.bind("<Enter>", lambda e: card.configure(highlightbackground=color))
        card.bind("<Leave>", lambda e: card.configure(highlightbackground=COLORES["border"]))

        top = tk.Frame(card, bg=COLORES["card_bg"])
        top.pack(fill=tk.X)
        if icono:
            tk.Label(top, text=icono, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 20)).pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(top, text=str(valor), bg=COLORES["card_bg"], fg=color,
                 font=("Segoe UI", 26, "bold")).pack(side=tk.LEFT)
        tk.Label(card, text=titulo, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 0))
        if desc:
            tk.Label(card, text=desc, bg=COLORES["card_bg"], fg=COLORES["texto_dim"],
                     font=("Segoe UI", 8)).pack(anchor="w")

    @staticmethod
    def _crear_card_contenedor(parent, titulo, subtitulo=""):
        frame = tk.LabelFrame(parent, text=titulo, padx=20, pady=14,
                              bg=COLORES["card_bg"], fg=COLORES["texto"],
                              font=("Segoe UI", 13, "bold"),
                              highlightbackground=COLORES["border"],
                              highlightthickness=1)
        frame.pack(fill=tk.X, pady=(0, 16))
        if subtitulo:
            tk.Label(frame, text=subtitulo, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 9)).pack(anchor="w", pady=(0, 8))
        return frame

    @staticmethod
    def _aplicar_hover_card(card, color_borde):
        card.bind("<Enter>", lambda e: card.configure(highlightbackground=color_borde))
        card.bind("<Leave>", lambda e: card.configure(highlightbackground=COLORES["border"]))

    @staticmethod
    def _detalle_jugador(frame, jugador):
        detalle = tk.Frame(frame, bg=COLORES["card_bg"],
                           highlightbackground=COLORES["border"], highlightthickness=1)
        detalle.pack(fill=tk.BOTH, expand=True, padx=28, pady=(0, 28))

        canvas = tk.Canvas(detalle, bg=COLORES["card_bg"], highlightthickness=0)
        scroll = ttk.Scrollbar(detalle, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scroll.set)

        interior = tk.Frame(canvas, bg=COLORES["card_bg"], padx=22, pady=18)
        canvas.create_window((0, 0), window=interior, anchor="nw")

        def _configurar_inner(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        interior.bind("<Configure>", _configurar_inner)

        tag, color_tag = PanelBase._crear_tag(jugador["clasificacion"])

        enc = tk.Frame(interior, bg=COLORES["card_bg"])
        enc.pack(fill=tk.X, pady=(0, 15))
        tk.Label(enc, text=f"{jugador['nombre']}", bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 18, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(enc, text=tag, bg=color_tag, fg=COLORES["fondo"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(12, 0))

        categorias = [
            ("Identificaci\u00f3n", [
                ("Edad", jugador["edad"]), ("Ocupaci\u00f3n", jugador["ocupacion"])
            ]),
            ("Sesi\u00f3n Actual", [
                ("Juego Actual", jugador["juego_actual"]),
                ("Monto Apuesta", f"S/ {jugador['monto_apuesta']}"),
                ("Resultado \u00daltima Ronda", jugador["resultado_ultima_ronda"]),
                ("Rondas Hoy", jugador["rondas_jugadas_hoy"]),
                ("Tiempo en Casino", f"{jugador['tiempo_en_casino_hoy']} hrs"),
                ("Hora Actual", jugador["hora_actual"]),
            ]),
            ("Econ\u00f3mico", [
                ("Presupuesto Hoy", f"S/ {jugador['presupuesto_hoy']}"),
                ("Fichas Actuales", jugador["fichas_actuales"]),
                ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
                ("Gasto Promedio/Ronda", f"S/ {jugador['gasto_promedio_ronda']}"),
                ("Gasto M\u00e1ximo Hist.", f"S/ {jugador['gasto_maximo_historico']}"),
                ("P\u00e9rdidas Acumuladas", f"S/ {jugador['perdidas_acumuladas']}"),
                ("Ganancias Acumuladas", f"S/ {jugador['ganancias_acumuladas']}"),
            ]),
            ("Comportamiento", [
                ("Prefiere", jugador["prefiere_azar_o_estrategia"]),
                ("Ritmo", jugador["prefiere_rapido_o_lento"]),
                ("Cambia al Perder", jugador["cambia_al_perder"]),
                ("Cambia al Ganar", jugador["cambia_al_ganar"]),
                ("Juega Solo", jugador["juega_solo"]),
                ("Reinvierte Ganancias", jugador["reinvierte_ganancias"]),
                ("Acepta Recomendaciones", jugador["acepta_recomendaciones"]),
            ]),
            ("Historial de Visitas", [
                ("Frecuencia Semanal", f"{jugador['frecuencia_semanal']}x"),
                ("Tiempo Promedio", f"{jugador['tiempo_promedio_visita']} min"),
                ("Horario Habitual", jugador["horario_habitual"]),
                ("D\u00edas de Visita", jugador["dias_visita"]),
                ("Total Visitas", jugador["total_visitas"]),
                ("D\u00edas desde 1ra Visita", jugador["dias_desde_primera_visita"]),
                ("D\u00edas desde \u00daltima", jugador["dias_desde_ultima_visita"]),
            ]),
            ("Preferencias", [
                ("Juego Favorito", jugador["juego_favorito"]),
                ("Variedad Probada", f"{jugador['variedad_juegos_probados']} juegos"),
            ]),
        ]

        for cat_nombre, campos in categorias:
            sep = tk.Frame(interior, bg=COLORES["border"], height=1)
            sep.pack(fill=tk.X, pady=(6, 10))
            tk.Label(interior, text=cat_nombre, bg=COLORES["card_bg"],
                     fg=COLORES["oro"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))
            grid = tk.Frame(interior, bg=COLORES["card_bg"])
            grid.pack(fill=tk.X)
            for i, (label, valor) in enumerate(campos):
                fila = i // 3
                col = i % 3
                sub = tk.Frame(grid, bg=COLORES["card_bg"], padx=10, pady=3)
                sub.grid(row=fila, column=col, sticky="w")
                tk.Label(sub, text=label, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                         font=("Segoe UI", 9)).pack(anchor="w")
                tk.Label(sub, text=str(valor), bg=COLORES["card_bg"], fg=COLORES["texto"],
                         font=("Segoe UI", 12, "bold")).pack(anchor="w")

        sep2 = tk.Frame(interior, bg=COLORES["border"], height=1)
        sep2.pack(fill=tk.X, pady=(6, 10))
        tk.Label(interior, text="Uso de Presupuesto", bg=COLORES["card_bg"],
                 fg=COLORES["oro"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))
        pb_frame = tk.Frame(interior, bg=COLORES["card_bg"])
        pb_frame.pack(fill=tk.X)
        tk.Label(pb_frame, text="Hoy:", bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(anchor="w")
        pct = min(jugador["gasto_hoy"] / jugador["presupuesto_hoy"], 1.0) if jugador["presupuesto_hoy"] > 0 else 0
        pb_color = COLORES["verde"] if pct < 0.5 else COLORES["naranja"] if pct < 0.8 else COLORES["rojo"]
        bar_frame = tk.Frame(pb_frame, bg=COLORES["card_alt"], height=8, width=300)
        bar_frame.pack(anchor="w", pady=(4, 0))
        bar_fill = tk.Frame(bar_frame, bg=pb_color, height=8, width=int(300 * pct))
        bar_fill.place(x=0, y=0)
        tk.Label(pb_frame, text=f"{jugador['gasto_hoy']} / {jugador['presupuesto_hoy']} ({int(pct*100)}%)",
                 bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(4, 0))

    @staticmethod
    def _crear_body_scroll(padre):
        canvas = tk.Canvas(padre, bg=COLORES["fondo"], highlightthickness=0)
        scroll = ttk.Scrollbar(padre, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scroll.set)
        interior = tk.Frame(canvas, bg=COLORES["fondo"])
        canvas.create_window((0, 0), window=interior, anchor="nw")

        def _conf(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        interior.bind("<Configure>", _conf)

        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def _on_mousewheel_linux_up(event):
            canvas.yview_scroll(-3, "units")

        def _on_mousewheel_linux_down(event):
            canvas.yview_scroll(3, "units")

        canvas.bind("<MouseWheel>", _on_mousewheel)
        canvas.bind("<Button-4>", _on_mousewheel_linux_up)
        canvas.bind("<Button-5>", _on_mousewheel_linux_down)
        return interior
