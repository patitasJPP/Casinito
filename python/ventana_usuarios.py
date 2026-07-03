import tkinter as tk
from tkinter import ttk

JUGADORES = [
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
]

COLORES = {
    "fondo": "#0a0a0f",
    "sidebar": "#12121e",
    "sidebar_hover": "#1e1e36",
    "sidebar_selected": "#c9a84c",
    "card_bg": "#16162a",
    "card_alt": "#1c1c34",
    "blanco": "#ffffff",
    "oro": "#c9a84c",
    "oro_oscuro": "#a8882e",
    "rojo": "#e94560",
    "rojo_oscuro": "#c0392b",
    "verde": "#2ecc71",
    "verde_oscuro": "#1a9c54",
    "naranja": "#f39c12",
    "texto": "#e8e8f0",
    "texto_sec": "#8888a0",
    "texto_dim": "#5a5a70",
    "border": "#2a2a44",
}

class AplicacionCasino:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Casino Sapiens - Sistema Experto de Gestión")
        self.ventana.configure(bg=COLORES["fondo"])
        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")
        self.ventana.state("zoomed")

        self._estilo = ttk.Style()
        self._estilo.theme_use("clam")

        self.panel_actual = None
        self._crear_layout()
        self._cargar_panel("dashboard")
        self.ventana.mainloop()

    def _crear_layout(self):
        self._crear_barra_superior()
        self._frame_contenido = tk.Frame(self.ventana, bg=COLORES["fondo"])
        self._frame_contenido.pack(fill=tk.BOTH, expand=True)
        self._crear_sidebar()
        self._frame_paneles = tk.Frame(self._frame_contenido, bg=COLORES["fondo"])
        self._frame_paneles.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self._crear_barra_estado()

    def _crear_barra_superior(self):
        barra = tk.Frame(self.ventana, bg="#08080c", height=48)
        barra.pack(fill=tk.X, side=tk.TOP)

        tk.Label(barra, text="◆  CASINO SAPIENS", bg="#08080c",
                 fg=COLORES["oro"], font=("Segoe UI", 15, "bold")).pack(side=tk.LEFT, padx=22, pady=10)

        tk.Label(barra, text="Sistema Experto de Perfilado", bg="#08080c",
                 fg=COLORES["texto_sec"], font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 20), pady=10)

        separador = tk.Frame(self.ventana, bg=COLORES["oro"], height=2)
        separador.pack(fill=tk.X, side=tk.TOP)

    def _crear_sidebar(self):
        self._sidebar = tk.Frame(self._frame_contenido, bg=COLORES["sidebar"], width=230)
        self._sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self._sidebar.pack_propagate(False)

        tk.Label(self._sidebar, text="NAVEGACIÓN", bg=COLORES["sidebar"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 8, "bold")).pack(pady=(22, 12))

        self._nav_btns = {}
        items = [
            ("dashboard", "  Dashboard"),
            ("todos", "  Todos los Usuarios"),
            ("vip", "  Invitar a VIP"),
            ("retener", "  Personas a Retener"),
            ("cuidar", "  Personas a Cuidar"),
            ("rapido", "  Servicio Rápido"),
        ]
        for key, texto in items:
            btn = tk.Button(self._sidebar, text=texto, anchor="w", padx=18,
                            bg=COLORES["sidebar"], fg=COLORES["texto"],
                            font=("Segoe UI", 10), bd=0, relief="flat",
                            activebackground=COLORES["sidebar_hover"],
                            activeforeground=COLORES["oro"],
                            command=lambda k=key: self._cargar_panel(k))
            btn.pack(fill=tk.X, pady=1, padx=8)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=COLORES["sidebar_hover"]))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(
                bg=COLORES["sidebar_selected"] if b == self._nav_btns.get(self.panel_actual) else COLORES["sidebar"]))
            self._nav_btns[key] = btn

    def _crear_barra_estado(self):
        barra = tk.Frame(self.ventana, bg="#08080c", height=30)
        barra.pack(fill=tk.X, side=tk.BOTTOM)
        total = len(JUGADORES)
        vips = sum(1 for j in JUGADORES if j["clasificacion"] == "VIP")
        retener = sum(1 for j in JUGADORES if j["clasificacion"] == "Retener")
        cuidar = sum(1 for j in JUGADORES if j["clasificacion"] == "Cuidar")

        tk.Label(barra, text=f"● {total} jugadores  |  VIP: {vips}  |  Retener: {retener}  |  Cuidar: {cuidar}",
                 bg="#08080c", fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=15, pady=4)
        tk.Label(barra, text="◆ Casino Sapiens v2.0  |  Prolog + Python",
                 bg="#08080c", fg=COLORES["texto_dim"],
                 font=("Segoe UI", 9)).pack(side=tk.RIGHT, padx=15, pady=4)

    def _cargar_panel(self, key):
        self.panel_actual = key
        for k, btn in self._nav_btns.items():
            if k == key:
                btn.configure(bg=COLORES["sidebar_selected"], fg="#12121e")
            else:
                btn.configure(bg=COLORES["sidebar"], fg=COLORES["texto"])
        for w in self._frame_paneles.winfo_children():
            w.destroy()
        if key == "dashboard":
            PanelDashboard(self._frame_paneles)
        elif key == "todos":
            PanelTodos(self._frame_paneles)
        elif key == "vip":
            PanelVIP(self._frame_paneles)
        elif key == "retener":
            PanelRetener(self._frame_paneles)
        elif key == "cuidar":
            PanelCuidar(self._frame_paneles)
        elif key == "rapido":
            PanelRapido(self._frame_paneles)

    @staticmethod
    def _obtener_por_clasificacion(clasif):
        return [j for j in JUGADORES if j["clasificacion"] == clasif]

    @staticmethod
    def _crear_progress(parent, valor, maximo, color, ancho=200):
        pct = min(valor / maximo, 1.0) if maximo > 0 else 0
        frame = tk.Frame(parent, bg=COLORES["card_bg"], height=6, width=ancho)
        frame.pack_propagate(False)
        fill = tk.Frame(frame, bg=color, height=6, width=int(ancho * pct))
        fill.place(x=0, y=0)
        return frame


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
            "Servicio_Rapido": ("Rápido", COLORES["verde"]),
        }
        return etiquetas.get(clasif, (clasif, COLORES["texto_sec"]))

    @staticmethod
    def _crear_kpi_card(parent, icono, titulo, valor, color, desc=""):
        card = tk.Frame(parent, bg=COLORES["card_bg"], padx=18, pady=14,
                        highlightbackground=COLORES["border"], highlightthickness=1)
        card.pack(side=tk.LEFT, padx=(0, 14), pady=8, ipadx=4)
        top = tk.Frame(card, bg=COLORES["card_bg"])
        top.pack(fill=tk.X)
        tk.Label(top, text=icono, bg=COLORES["card_bg"], fg=color,
                 font=("Segoe UI", 20)).pack(side=tk.LEFT, padx=(0, 10))
        tk.Label(top, text=str(valor), bg=COLORES["card_bg"], fg=color,
                 font=("Segoe UI", 26, "bold")).pack(side=tk.LEFT)
        tk.Label(card, text=titulo, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(anchor="w", pady=(2, 0))
        if desc:
            tk.Label(card, text=desc, bg=COLORES["card_bg"], fg=COLORES["texto_dim"],
                     font=("Segoe UI", 8)).pack(anchor="w")
        return card

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
        ventana = canvas.create_window((0, 0), window=interior, anchor="nw")

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
            ("Identificación", [
                ("Edad", jugador["edad"]), ("Ocupación", jugador["ocupacion"])
            ]),
            ("Sesión Actual", [
                ("Juego Actual", jugador["juego_actual"]),
                ("Monto Apuesta", f"S/ {jugador['monto_apuesta']}"),
                ("Resultado Última Ronda", jugador["resultado_ultima_ronda"]),
                ("Rondas Hoy", jugador["rondas_jugadas_hoy"]),
                ("Tiempo en Casino", f"{jugador['tiempo_en_casino_hoy']} hrs"),
                ("Hora Actual", jugador["hora_actual"]),
            ]),
            ("Económico", [
                ("Presupuesto Hoy", f"S/ {jugador['presupuesto_hoy']}"),
                ("Fichas Actuales", jugador["fichas_actuales"]),
                ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
                ("Gasto Promedio/Ronda", f"S/ {jugador['gasto_promedio_ronda']}"),
                ("Gasto Máximo Hist.", f"S/ {jugador['gasto_maximo_historico']}"),
                ("Pérdidas Acumuladas", f"S/ {jugador['perdidas_acumuladas']}"),
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
                ("Días de Visita", jugador["dias_visita"]),
                ("Total Visitas", jugador["total_visitas"]),
                ("Días desde 1ra Visita", jugador["dias_desde_primera_visita"]),
                ("Días desde Última", jugador["dias_desde_ultima_visita"]),
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

        # Progress bar for budget usage
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


class PanelDashboard:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)

        PanelBase._crear_header(self.frame, "Dashboard",
                                "Resumen general del estado del casino y los jugadores.")

        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(8, 28))

        total = len(JUGADORES)
        vips = len(AplicacionCasino._obtener_por_clasificacion("VIP"))
        retener = len(AplicacionCasino._obtener_por_clasificacion("Retener"))
        cuidar = len(AplicacionCasino._obtener_por_clasificacion("Cuidar"))
        rapido = len(AplicacionCasino._obtener_por_clasificacion("Servicio_Rapido"))
        total_gasto = sum(j["gasto_hoy"] for j in JUGADORES)
        total_perdidas = sum(j["perdidas_acumuladas"] for j in JUGADORES)
        total_ganancias = sum(j["ganancias_acumuladas"] for j in JUGADORES)

        cards = tk.Frame(body, bg=COLORES["fondo"])
        cards.pack(fill=tk.X, pady=(0, 20))

        PanelBase._crear_kpi_card(cards, "👥", "Total Jugadores", total, COLORES["texto"])
        PanelBase._crear_kpi_card(cards, "👑", "VIP", vips, COLORES["oro"],
                                  f"{vips/total*100:.0f}% del total" if total > 0 else "")
        PanelBase._crear_kpi_card(cards, "⚠️", "En Riesgo", retener, COLORES["naranja"])
        PanelBase._crear_kpi_card(cards, "🛡️", "A Cuidar", cuidar, COLORES["rojo"])
        PanelBase._crear_kpi_card(cards, "⚡", "Serv. Rápido", rapido, COLORES["verde"])
        PanelBase._crear_kpi_card(cards, "💰", "Gasto Hoy", f"S/{total_gasto}", COLORES["texto"])

        graf = tk.Frame(body, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["border"], highlightthickness=1)
        graf.pack(fill=tk.X, pady=(0, 16))

        tk.Label(graf, text="Distribución de Clasificaciones", bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(14, 4))
        tk.Label(graf, text="Proporción de cada tipo de jugador en el sistema",
                 bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(anchor="w", padx=20, pady=(0, 12))

        barras = tk.Frame(graf, bg=COLORES["card_bg"])
        barras.pack(fill=tk.X, padx=20, pady=(0, 18))

        clasifs = [
            ("VIP", vips, COLORES["oro"]),
            ("Retener", retener, COLORES["naranja"]),
            ("Cuidar", cuidar, COLORES["rojo"]),
            ("Rápido", rapido, COLORES["verde"]),
        ]
        max_val = max((c[1] for c in clasifs), default=1)
        for label, val, color in clasifs:
            row = tk.Frame(barras, bg=COLORES["card_bg"])
            row.pack(fill=tk.X, pady=3)
            tk.Label(row, text=label, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10), width=10, anchor="w").pack(side=tk.LEFT)
            bar_bg = tk.Frame(row, bg=COLORES["card_alt"], height=22, width=300)
            bar_bg.pack(side=tk.LEFT, padx=(0, 10))
            bar_w = int(300 * (val / max_val)) if max_val > 0 else 0
            bar_fill = tk.Frame(bar_bg, bg=color, height=22, width=max(bar_w, 1) if bar_w > 0 else 0)
            bar_fill.place(x=0, y=0)
            tk.Label(row, text=str(val), bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 12, "bold"), width=3).pack(side=tk.LEFT)

        resumen = tk.Frame(body, bg=COLORES["card_bg"],
                           highlightbackground=COLORES["border"], highlightthickness=1)
        resumen.pack(fill=tk.X)

        tk.Label(resumen, text="Resumen Financiero", bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 13, "bold")).pack(anchor="w", padx=20, pady=(14, 4))

        fin_data = tk.Frame(resumen, bg=COLORES["card_bg"])
        fin_data.pack(fill=tk.X, padx=20, pady=(8, 16))

        cols = tk.Frame(fin_data, bg=COLORES["card_bg"])
        cols.pack(fill=tk.X)
        items_fin = [
            ("Gasto Total Hoy", f"S/ {total_gasto}", COLORES["texto"]),
            ("Pérdidas Totales", f"S/ {total_perdidas}", COLORES["rojo"]),
            ("Ganancias Totales", f"S/ {total_ganancias}", COLORES["verde"]),
            ("Balance", f"S/ {total_ganancias - total_perdidas}",
             COLORES["verde"] if total_ganancias >= total_perdidas else COLORES["rojo"]),
        ]
        for i, (lbl, val, color) in enumerate(items_fin):
            c = tk.Frame(cols, bg=COLORES["card_bg"], padx=12)
            c.grid(row=0, column=i, sticky="w")
            tk.Label(c, text=lbl, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 9)).pack(anchor="w")
            tk.Label(c, text=val, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 16, "bold")).pack(anchor="w")


class PanelTodos:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugador_seleccionado = None

        PanelBase._crear_header(self.frame, "Todos los Usuarios",
                                f"{len(JUGADORES)} jugadores registrados. Seleccione uno para ver detalles completos.")
        self._crear_contenido()

    def _crear_contenido(self):
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 0))

        columnas = ("Nombre", "Edad", "Ocupación", "Presupuesto", "Fichas",
                     "Gasto Hoy", "Juego Favorito", "Frecuencia", "Clasificación")
        self.tabla = ttk.Treeview(body, columns=columnas, show="headings", height=10)

        self._estilo = ttk.Style()
        self._estilo.configure("Treeview", background=COLORES["card_bg"],
                               foreground=COLORES["texto"], rowheight=34,
                               fieldbackground=COLORES["card_bg"], font=("Segoe UI", 10),
                               bordercolor=COLORES["border"])
        self._estilo.configure("Treeview.Heading", background=COLORES["sidebar"],
                               foreground=COLORES["oro"], font=("Segoe UI", 10, "bold"),
                               bordercolor=COLORES["border"])
        self._estilo.map("Treeview", background=[("selected", COLORES["sidebar_hover"])],
                         foreground=[("selected", COLORES["oro"])])
        self._estilo.map("Treeview.Heading", background=[("active", COLORES["sidebar_hover"])])

        anchos = [100, 50, 100, 90, 70, 80, 120, 90, 110]
        for col, ancho in zip(columnas, anchos):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor=tk.CENTER)

        for j in JUGADORES:
            tag, _ = PanelBase._crear_tag(j["clasificacion"])
            self.tabla.insert("", tk.END,
                              values=(j["nombre"], j["edad"], j["ocupacion"],
                                      f"S/ {j['presupuesto_hoy']}", j["fichas_actuales"],
                                      f"S/ {j['gasto_hoy']}", j["juego_favorito"],
                                      f"{j['frecuencia_semanal']}x/sem", tag),
                              tags=(j["id"],))
            color_tag = {"VIP": COLORES["oro"], "Retener": COLORES["naranja"],
                         "Cuidar": COLORES["rojo"], "Servicio_Rapido": COLORES["verde"]}
            self.tabla.tag_configure(j["id"], foreground=color_tag.get(j["clasificacion"], COLORES["texto"]))

        scroll_y = ttk.Scrollbar(body, orient=tk.VERTICAL, command=self.tabla.yview)
        scroll_x = ttk.Scrollbar(body, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        self._frame_detalle = tk.Frame(body, bg=COLORES["fondo"], height=300)
        self._frame_detalle.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(15, 0))
        body.grid_rowconfigure(2, weight=1)

        self.tabla.bind("<<TreeviewSelect>>", self._on_seleccionar)

        if JUGADORES:
            children = self.tabla.get_children()
            if children:
                self.tabla.selection_set(children[0])
                self._mostrar_detalle(JUGADORES[0])

    def _on_seleccionar(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        item = self.tabla.item(seleccion[0])
        nombre = item["values"][0]
        jugador = next((j for j in JUGADORES if j["nombre"] == nombre), None)
        if jugador:
            self._mostrar_detalle(jugador)

    def _mostrar_detalle(self, jugador):
        for w in self._frame_detalle.winfo_children():
            w.destroy()
        PanelBase._detalle_jugador(self._frame_detalle, jugador)


class PanelVIP:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        vips = AplicacionCasino._obtener_por_clasificacion("VIP")

        PanelBase._crear_header(self.frame, "Invitar a VIP",
                                f"{len(vips)} jugadores de alto valor. Clientes premium que merecen atención exclusiva.")
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 28))

        if not vips:
            tk.Label(body, text="No hay jugadores VIP en este momento.", bg=COLORES["fondo"],
                     fg=COLORES["texto_sec"], font=("Segoe UI", 12)).pack()
            return

        for vip in vips:
            self._crear_tarjeta_vip(body, vip)

    def _crear_tarjeta_vip(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["oro"], highlightthickness=1, padx=22, pady=16)
        card.pack(fill=tk.X, pady=(0, 12))

        superior = tk.Frame(card, bg=COLORES["card_bg"])
        superior.pack(fill=tk.X)
        tk.Label(superior, text="👑", bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 18)).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(superior, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["oro"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(superior, text="VIP", bg=COLORES["oro"], fg=COLORES["fondo"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(10, 0))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(10, 0))

        datos = [
            ("Edad", jugador["edad"]),
            ("Ocupación", jugador["ocupacion"]),
            ("Presupuesto Hoy", f"S/ {jugador['presupuesto_hoy']}"),
            ("Frecuencia", f"{jugador['frecuencia_semanal']}x/sem"),
            ("Gasto Máx. Hist.", f"S/ {jugador['gasto_maximo_historico']}"),
            ("Total Visitas", jugador["total_visitas"]),
            ("Juego Favorito", jugador["juego_favorito"]),
            ("Ganancias Acum.", f"S/ {jugador['ganancias_acumuladas']}"),
        ]
        for i, (label, valor) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=8, pady=2)
            sub.grid(row=i // 4, column=i % 4, sticky="w")
            tk.Label(sub, text=label, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=str(valor), bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        btn = tk.Button(card, text="Enviar Invitación VIP",
                        bg=COLORES["oro"], fg=COLORES["fondo"],
                        font=("Segoe UI", 10, "bold"), bd=0, padx=18, pady=6,
                        activebackground=COLORES["oro_oscuro"],
                        activeforeground=COLORES["fondo"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._invitar(n))
        btn.pack(anchor="e", pady=(12, 0))

    def _invitar(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Invitación Enviada",
                            f"Se ha enviado la invitación VIP a {nombre}.")


class PanelRetener:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        retener = AplicacionCasino._obtener_por_clasificacion("Retener")

        PanelBase._crear_header(self.frame, "Personas a Retener",
                                f"{len(retener)} jugador(es) en riesgo de abandono. Aplicar incentivos para retenerlos.")
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 28))

        if not retener:
            tk.Label(body, text="No hay jugadores en riesgo de irse.", bg=COLORES["fondo"],
                     fg=COLORES["texto_sec"], font=("Segoe UI", 12)).pack()
            return

        for j in retener:
            self._crear_tarjeta_retener(body, j)

    def _crear_tarjeta_retener(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["naranja"], highlightthickness=1, padx=22, pady=16)
        card.pack(fill=tk.X, pady=(0, 12))

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="⚠️", bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 16)).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="Retener", bg=COLORES["naranja"], fg=COLORES["fondo"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(10, 0))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(10, 0))

        datos = [
            ("Días sin venir", f"{jugador['dias_desde_ultima_visita']} días"),
            ("Total Visitas", jugador["total_visitas"]),
            ("Frecuencia", f"{jugador['frecuencia_semanal']}x/sem"),
            ("Último Juego", jugador["juego_actual"]),
            ("Gasto Promedio", f"S/ {jugador['gasto_promedio_ronda']}"),
            ("Perdidas Acum.", f"S/ {jugador['perdidas_acumuladas']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        # Días sin venir como progress bar
        dias_max = 60
        dias_pct = min(jugador["dias_desde_ultima_visita"] / dias_max, 1.0)
        dias_frame = tk.Frame(card, bg=COLORES["card_bg"])
        dias_frame.pack(fill=tk.X, pady=(8, 0))
        tk.Label(dias_frame, text="Riesgo de pérdida:", bg=COLORES["card_bg"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 9)).pack(anchor="w")
        bar_bg = tk.Frame(dias_frame, bg=COLORES["card_alt"], height=8, width=300)
        bar_bg.pack(anchor="w", pady=(3, 0))
        color_riesgo = COLORES["verde"] if dias_pct < 0.3 else COLORES["naranja"] if dias_pct < 0.6 else COLORES["rojo"]
        bar_fill = tk.Frame(bar_bg, bg=color_riesgo, height=8, width=int(300 * dias_pct))
        bar_fill.place(x=0, y=0)

        btn = tk.Button(card, text="Ofrecer Bono de Retorno",
                        bg=COLORES["naranja"], fg=COLORES["fondo"],
                        font=("Segoe UI", 10, "bold"), bd=0, padx=18, pady=6,
                        activebackground=COLORES["sidebar_hover"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._ofrecer_bono(n))
        btn.pack(anchor="e", pady=(12, 0))

    def _ofrecer_bono(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Bono Ofrecido",
                            f"Bono de retorno ofrecido a {nombre}.")


class PanelCuidar:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        cuidar = AplicacionCasino._obtener_por_clasificacion("Cuidar")

        PanelBase._crear_header(self.frame, "Personas a Cuidar",
                                f"{len(cuidar)} jugador(es) que requieren supervisión. Intervenir para juego responsable.")
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 28))

        if not cuidar:
            tk.Label(body, text="No hay jugadores que requieran supervisión.", bg=COLORES["fondo"],
                     fg=COLORES["texto_sec"], font=("Segoe UI", 12)).pack()
            return

        for j in cuidar:
            self._crear_tarjeta_cuidar(body, j)

    def _crear_tarjeta_cuidar(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["rojo"], highlightthickness=1, padx=22, pady=16)
        card.pack(fill=tk.X, pady=(0, 12))

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="🛡️", bg=COLORES["card_bg"], fg=COLORES["rojo"],
                 font=("Segoe UI", 16)).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="Cuidar", bg=COLORES["rojo"], fg=COLORES["blanco"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(10, 0))

        alertas = []
        if jugador["edad"] <= 22:
            alertas.append(("Edad joven", "Monitorear tiempo de juego", COLORES["rojo"]))
        if jugador["tiempo_en_casino_hoy"] >= 4:
            alertas.append((f"Tiempo excesivo", f"{jugador['tiempo_en_casino_hoy']} hrs hoy - sugerir descanso", COLORES["rojo"]))
        if jugador["gasto_hoy"] >= jugador["presupuesto_hoy"] * 0.8:
            alertas.append(("Presupuesto agotado", "Gastó más del 80% - monitorear", COLORES["naranja"]))
        if jugador["perdidas_acumuladas"] > jugador["ganancias_acumuladas"] * 2:
            alertas.append(("Pérdidas altas", "Pérdidas superan ganancias significativamente", COLORES["naranja"]))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(8, 0))

        datos = [
            ("Edad", jugador["edad"]),
            ("Tiempo Hoy", f"{jugador['tiempo_en_casino_hoy']} hrs"),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
            ("Rondas Hoy", jugador["rondas_jugadas_hoy"]),
            ("Perdidas Acum.", f"S/ {jugador['perdidas_acumuladas']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        if alertas:
            alert_frame = tk.Frame(card, bg="#2a0a0a", padx=14, pady=10)
            alert_frame.pack(fill=tk.X, pady=(10, 0))
            for icono, msg, color in alertas:
                row_a = tk.Frame(alert_frame, bg="#2a0a0a")
                row_a.pack(fill=tk.X, pady=1)
                tk.Label(row_a, text="●", bg="#2a0a0a", fg=color,
                         font=("Segoe UI", 8)).pack(side=tk.LEFT, padx=(0, 6))
                tk.Label(row_a, text=msg, bg="#2a0a0a", fg=COLORES["texto"],
                         font=("Segoe UI", 9), anchor="w").pack(side=tk.LEFT)

        btn_frame = tk.Frame(card, bg=COLORES["card_bg"])
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        tk.Button(btn_frame, text="Sugerir Descanso",
                  bg=COLORES["rojo"], fg=COLORES["blanco"],
                  font=("Segoe UI", 9, "bold"), bd=0, padx=14, pady=5,
                  cursor="hand2",
                  command=lambda n=jugador["nombre"]: self._sugerir_descanso(n)).pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(btn_frame, text="Registrar Intervención",
                  bg=COLORES["texto_dim"], fg=COLORES["texto"],
                  font=("Segoe UI", 9), bd=0, padx=14, pady=5,
                  cursor="hand2",
                  command=lambda n=jugador["nombre"]: self._registrar_intervencion(n)).pack(side=tk.LEFT)

    def _sugerir_descanso(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Descanso Sugerido",
                            f"Notificación enviada a {nombre}: sugerencia de descanso.")

    def _registrar_intervencion(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Intervención Registrada",
                            f"Intervención con {nombre} registrada en el sistema.")


class PanelRapido:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        rapidos = AplicacionCasino._obtener_por_clasificacion("Servicio_Rapido")

        PanelBase._crear_header(self.frame, "Servicio Rápido",
                                f"{len(rapidos)} jugador(es) que prefieren atención ágil. Priorizar su experiencia.")
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 28))

        if not rapidos:
            tk.Label(body, text="No hay jugadores para servicio rápido.", bg=COLORES["fondo"],
                     fg=COLORES["texto_sec"], font=("Segoe UI", 12)).pack()
            return

        for j in rapidos:
            self._crear_tarjeta_rapido(body, j)

    def _crear_tarjeta_rapido(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["verde"], highlightthickness=1, padx=22, pady=16)
        card.pack(fill=tk.X, pady=(0, 12))

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="⚡", bg=COLORES["card_bg"], fg=COLORES["verde"],
                 font=("Segoe UI", 18)).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="Rápido", bg=COLORES["verde"], fg=COLORES["fondo"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(10, 0))

        razones = []
        if jugador["prefiere_rapido_o_lento"] == "Rápido":
            razones.append("Prefiere juegos rápidos")
        if jugador["cambia_al_perder"] == "Sí":
            razones.append("Cambia rápido de juego al perder")
        if jugador["tiempo_promedio_visita"] <= 150:
            razones.append("Visitas cortas - atención prioritaria")
        if jugador["presupuesto_hoy"] >= 200:
            razones.append("Presupuesto alto - agilizar atención")

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(10, 0))

        datos = [
            ("Ritmo", jugador["prefiere_rapido_o_lento"]),
            ("Juego Favorito", jugador["juego_favorito"]),
            ("Juego Actual", jugador["juego_actual"]),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Tiempo Prom.", f"{jugador['tiempo_promedio_visita']} min"),
            ("Apuesta Prom.", f"S/ {jugador['gasto_promedio_ronda']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        razon_frame = tk.Frame(card, bg=COLORES["card_alt"], padx=12, pady=8)
        razon_frame.pack(fill=tk.X, pady=(8, 0))
        tk.Label(razon_frame, text="Prioridades:", bg=COLORES["card_alt"],
                 fg=COLORES["verde"], font=("Segoe UI", 9, "bold")).pack(anchor="w")
        for r in razones:
            tk.Label(razon_frame, text=f"  ▶ {r}", bg=COLORES["card_alt"],
                     fg=COLORES["texto"], font=("Segoe UI", 9)).pack(anchor="w")

        btn = tk.Button(card, text="Atender Prioritariamente",
                        bg=COLORES["verde"], fg=COLORES["fondo"],
                        font=("Segoe UI", 10, "bold"), bd=0, padx=18, pady=6,
                        activebackground=COLORES["verde_oscuro"],
                        activeforeground=COLORES["fondo"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._atender(n))
        btn.pack(anchor="e", pady=(12, 0))

    def _atender(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Atención Rápida",
                            f"Notificación enviada: atender a {nombre} con prioridad.")


if __name__ == "__main__":
    AplicacionCasino()
