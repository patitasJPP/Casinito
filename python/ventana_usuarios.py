import tkinter as tk
from tkinter import ttk

# ============================================================
# DATOS: 30 campos por jugador (simulando datos de Prolog)
# ============================================================
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

# ============================================================
# COLORES: rojos análogos minimalistas
# ============================================================
C = {
    "sidebar_fondo": "#1e0e0e",
    "sidebar_texto": "#e8d5d0",
    "sidebar_selected": "#b3382c",
    "sidebar_hover": "#3d1c1c",
    "fondo": "#f4f1ee",
    "blanco": "#ffffff",
    "rojo_primario": "#c0392b",
    "rojo_secundario": "#e74c3c",
    "rojo_claro": "#fadbd8",
    "rojo_oscuro": "#a93226",
    "texto_principal": "#2c3e50",
    "texto_secundario": "#7f8c8d",
    "border": "#e0d8d4",
    "success": "#27ae60",
    "warning": "#e67e22",
    "danger": "#c0392b",
}

# ============================================================
# APLICACIÓN PRINCIPAL
# ============================================================
class AplicacionCasino:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Casino Sapiens - Sistema de Gestión")
        self.ventana.configure(bg=C["fondo"])
        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")
        self.ventana.state("zoomed")

        self.panel_actual = None
        self._crear_layout()
        self._cargar_panel("todos")
        self.ventana.mainloop()

    # ----------------------------------------------------------
    # Layout principal: barra + sidebar + contenido + barra_estado
    # ----------------------------------------------------------
    def _crear_layout(self):
        self._crear_barra_superior()
        self._frame_contenido = tk.Frame(self.ventana, bg=C["fondo"])
        self._frame_contenido.pack(fill=tk.BOTH, expand=True)
        self._crear_sidebar()
        self._frame_paneles = tk.Frame(self._frame_contenido, bg=C["fondo"])
        self._frame_paneles.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self._crear_barra_estado()

    def _crear_barra_superior(self):
        barra = tk.Frame(self.ventana, bg=C["sidebar_fondo"], height=44)
        barra.pack(fill=tk.X, side=tk.TOP)
        tk.Label(barra, text="CASINO SAPIENS", bg=C["sidebar_fondo"],
                 fg=C["rojo_claro"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT, padx=20, pady=8)
        tk.Label(barra, text="Sistema Experto de Gestión", bg=C["sidebar_fondo"],
                 fg=C["sidebar_texto"], font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 20), pady=8)

        separador = tk.Frame(self.ventana, bg=C["rojo_primario"], height=3)
        separador.pack(fill=tk.X, side=tk.TOP)

    def _crear_sidebar(self):
        self._sidebar = tk.Frame(self._frame_contenido, bg=C["sidebar_fondo"], width=220)
        self._sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self._sidebar.pack_propagate(False)

        tk.Label(self._sidebar, text="NAVEGACIÓN", bg=C["sidebar_fondo"],
                 fg=C["sidebar_texto"], font=("Segoe UI", 9, "bold")).pack(pady=(20, 10))

        self._nav_btns = {}
        items = [
            ("todos", "Todos los Usuarios"),
            ("vip", "Invitar a VIP"),
            ("retener", "Personas a Retener"),
            ("cuidar", "Personas a Cuidar"),
            ("rapido", "Servicio Rápido"),
        ]
        for key, texto in items:
            btn = tk.Button(self._sidebar, text=texto, anchor="w", padx=15,
                            bg=C["sidebar_fondo"], fg=C["sidebar_texto"],
                            font=("Segoe UI", 11), bd=0, relief="flat",
                            activebackground=C["sidebar_hover"],
                            activeforeground=C["rojo_claro"],
                            command=lambda k=key: self._cargar_panel(k))
            btn.pack(fill=tk.X, pady=2, padx=8)
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg=C["sidebar_hover"]))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg=C["sidebar_fondo"]))
            self._nav_btns[key] = btn

    def _crear_barra_estado(self):
        barra = tk.Frame(self.ventana, bg=C["sidebar_fondo"], height=28)
        barra.pack(fill=tk.X, side=tk.BOTTOM)
        total = len(JUGADORES)
        vips = sum(1 for j in JUGADORES if j["clasificacion"] == "VIP")
        tk.Label(barra, text=f"Total: {total} jugadores  |  VIP: {vips}",
                 bg=C["sidebar_fondo"], fg=C["sidebar_texto"],
                 font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=15, pady=3)
        tk.Label(barra, text="Datos simulados | Prolog conectado próximamente",
                 bg=C["sidebar_fondo"], fg=C["texto_secundario"],
                 font=("Segoe UI", 9)).pack(side=tk.RIGHT, padx=15, pady=3)

    # ----------------------------------------------------------
    # Navegación: cargar panel según selección
    # ----------------------------------------------------------
    def _cargar_panel(self, key):
        for k, btn in self._nav_btns.items():
            btn.configure(bg=C["sidebar_selected"] if k == key else C["sidebar_fondo"])
        for w in self._frame_paneles.winfo_children():
            w.destroy()
        if key == "todos":
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


# ============================================================
# PANEL BASE (utilidades compartidas)
# ============================================================
class PanelBase:
    @staticmethod
    def _crear_header(frame, titulo, subtitulo=""):
        header = tk.Frame(frame, bg=C["blanco"], padx=25, pady=18)
        header.pack(fill=tk.X)
        tk.Label(header, text=titulo, bg=C["blanco"], fg=C["rojo_primario"],
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")
        if subtitulo:
            tk.Label(header, text=subtitulo, bg=C["blanco"], fg=C["texto_secundario"],
                     font=("Segoe UI", 10)).pack(anchor="w", pady=(3, 0))

    @staticmethod
    def _crear_card(frame, titulo, valor, color=C["texto_principal"], ancho=180):
        card = tk.Frame(frame, bg=C["blanco"], highlightbackground=C["border"],
                        highlightthickness=1, padx=15, pady=12)
        card.pack(side=tk.LEFT, padx=(0, 15), pady=10)
        tk.Label(card, text=titulo, bg=C["blanco"], fg=C["texto_secundario"],
                 font=("Segoe UI", 9)).pack(anchor="w")
        tk.Label(card, text=str(valor), bg=C["blanco"], fg=color,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")
        return card

    @staticmethod
    def _crear_tag(clasif):
        etiquetas = {
            "VIP": ("VIP", C["rojo_primario"]),
            "Retener": ("Retener", C["warning"]),
            "Cuidar": ("Cuidar", C["rojo_secundario"]),
            "Servicio_Rapido": ("Rápido", C["success"]),
        }
        return etiquetas.get(clasif, (clasif, C["texto_secundario"]))

    @staticmethod
    def _detalle_jugador(frame, jugador):
        """Muestra todos los 30 datos de un jugador en un panel lateral."""
        detalle = tk.Frame(frame, bg=C["blanco"], highlightbackground=C["border"],
                           highlightthickness=1)
        detalle.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 25))

        canvas = tk.Canvas(detalle, bg=C["blanco"], highlightthickness=0)
        scroll = ttk.Scrollbar(detalle, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scroll.set)

        interior = tk.Frame(canvas, bg=C["blanco"], padx=20, pady=15)
        ventana = canvas.create_window((0, 0), window=interior, anchor="nw")

        def _configurar_inner(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        interior.bind("<Configure>", _configurar_inner)

        tag, color_tag = PanelBase._crear_tag(jugador["clasificacion"])

        # Encabezado del detalle
        enc = tk.Frame(interior, bg=C["blanco"])
        enc.pack(fill=tk.X, pady=(0, 15))
        tk.Label(enc, text=f"{jugador['nombre']}", bg=C["blanco"],
                 fg=C["texto_principal"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        tk.Label(enc, text=tag, bg=color_tag, fg=C["blanco"],
                 font=("Segoe UI", 9, "bold"), padx=10, pady=2).pack(side=tk.LEFT, padx=(10, 0))

        # Categorías de datos
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
            # Separador de categoría
            sep = tk.Frame(interior, bg=C["border"], height=1)
            sep.pack(fill=tk.X, pady=(5, 8))
            tk.Label(interior, text=cat_nombre, bg=C["blanco"],
                     fg=C["rojo_primario"], font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(0, 6))
            grid = tk.Frame(interior, bg=C["blanco"])
            grid.pack(fill=tk.X)
            for i, (label, valor) in enumerate(campos):
                fila = i // 3
                col = i % 3
                sub = tk.Frame(grid, bg=C["blanco"], padx=10, pady=3)
                sub.grid(row=fila, column=col, sticky="w")
                tk.Label(sub, text=label, bg=C["blanco"], fg=C["texto_secundario"],
                         font=("Segoe UI", 9)).pack(anchor="w")
                tk.Label(sub, text=str(valor), bg=C["blanco"], fg=C["texto_principal"],
                         font=("Segoe UI", 11, "bold")).pack(anchor="w")


# ============================================================
# PANEL: Todos los Usuarios
# ============================================================
class PanelTodos:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=C["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugador_seleccionado = None

        PanelBase._crear_header(self.frame, "Todos los Usuarios",
                                f"{len(JUGADORES)} jugadores registrados. Seleccione uno para ver detalles.")
        self._crear_contenido()

    def _crear_contenido(self):
        body = tk.Frame(self.frame, bg=C["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=(10, 0))

        # Tabla con columnas principales
        columnas = ("Nombre", "Edad", "Ocupación", "Presupuesto", "Fichas",
                     "Gasto Hoy", "Juego Favorito", "Frecuencia", "Clasificación")
        self.tabla = ttk.Treeview(body, columns=columnas, show="headings", height=10)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=C["blanco"], foreground=C["texto_principal"],
                        rowheight=32, fieldbackground=C["blanco"], font=("Segoe UI", 10))
        style.configure("Treeview.Heading", background=C["rojo_primario"],
                        foreground=C["blanco"], font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[("selected", C["rojo_claro"])],
                  foreground=[("selected", C["rojo_oscuro"])])
        style.map("Treeview.Heading", background=[("active", C["rojo_secundario"])])

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
            if j["clasificacion"] == "VIP":
                self.tabla.tag_configure(j["id"], foreground=C["rojo_primario"])
            elif j["clasificacion"] == "Retener":
                self.tabla.tag_configure(j["id"], foreground=C["warning"])
            elif j["clasificacion"] == "Cuidar":
                self.tabla.tag_configure(j["id"], foreground=C["rojo_secundario"])
            elif j["clasificacion"] == "Servicio_Rapido":
                self.tabla.tag_configure(j["id"], foreground=C["success"])

        scroll_y = ttk.Scrollbar(body, orient=tk.VERTICAL, command=self.tabla.yview)
        scroll_x = ttk.Scrollbar(body, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")
        body.grid_rowconfigure(0, weight=1)
        body.grid_columnconfigure(0, weight=1)

        # Área de detalle: se llena al seleccionar una fila
        self._frame_detalle = tk.Frame(body, bg=C["fondo"], height=300)
        self._frame_detalle.grid(row=2, column=0, columnspan=2, sticky="nsew", pady=(15, 0))
        body.grid_rowconfigure(2, weight=1)

        self.tabla.bind("<<TreeviewSelect>>", self._on_seleccionar)

        # Mostrar detalle del primer jugador por defecto
        if JUGADORES:
            self.tabla.selection_set(self.tabla.get_children()[0])
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


# ============================================================
# PANEL: Invitar a VIP
# ============================================================
class PanelVIP:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=C["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        vips = AplicacionCasino._obtener_por_clasificacion("VIP")

        PanelBase._crear_header(self.frame, "Invitar a VIP",
                                f"{len(vips)} jugadores VIP. Clientes de alto valor que merecen atención especial.")
        body = tk.Frame(self.frame, bg=C["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=(10, 25))

        if not vips:
            tk.Label(body, text="No hay jugadores VIP.", bg=C["fondo"],
                     fg=C["texto_secundario"], font=("Segoe UI", 12)).pack()
            return

        for vip in vips:
            self._crear_tarjeta_vip(body, vip)

    def _crear_tarjeta_vip(self, padre, jugador):
        card = tk.Frame(padre, bg=C["blanco"], highlightbackground=C["border"],
                        highlightthickness=1, padx=20, pady=15)
        card.pack(fill=tk.X, pady=(0, 10))

        superior = tk.Frame(card, bg=C["blanco"])
        superior.pack(fill=tk.X)

        tk.Label(superior, text=jugador["nombre"], bg=C["blanco"],
                 fg=C["rojo_primario"], font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT)
        tk.Label(superior, text="👑 VIP", bg=C["rojo_primario"], fg=C["blanco"],
                 font=("Segoe UI", 9, "bold"), padx=10, pady=2).pack(side=tk.LEFT, padx=(10, 0))

        info = tk.Frame(card, bg=C["blanco"])
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
            sub = tk.Frame(info, bg=C["blanco"], padx=8, pady=2)
            sub.grid(row=i // 4, column=i % 4, sticky="w")
            tk.Label(sub, text=label, bg=C["blanco"], fg=C["texto_secundario"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=str(valor), bg=C["blanco"], fg=C["texto_principal"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        btn = tk.Button(card, text="📨 Invitar a Evento VIP",
                        bg=C["rojo_primario"], fg=C["blanco"],
                        font=("Segoe UI", 10, "bold"), bd=0, padx=15, pady=5,
                        activebackground=C["rojo_secundario"],
                        activeforeground=C["blanco"],
                        command=lambda n=jugador["nombre"]: self._invitar(n))
        btn.pack(anchor="e", pady=(10, 0))

    def _invitar(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Invitación Enviada",
                            f"Se ha enviado invitación VIP a {nombre}.")


# ============================================================
# PANEL: Personas a Retener
# ============================================================
class PanelRetener:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=C["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        retener = AplicacionCasino._obtener_por_clasificacion("Retener")

        PanelBase._crear_header(self.frame, "Personas a Retener",
                                f"{len(retener)} jugador(es) en riesgo de irse. Aplicar incentivos.")
        body = tk.Frame(self.frame, bg=C["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=(10, 25))

        if not retener:
            tk.Label(body, text="No hay jugadores en riesgo de irse.", bg=C["fondo"],
                     fg=C["texto_secundario"], font=("Segoe UI", 12)).pack()
            return

        for j in retener:
            self._crear_tarjeta_retener(body, j)

    def _crear_tarjeta_retener(self, padre, jugador):
        card = tk.Frame(padre, bg=C["blanco"], highlightbackground=C["warning"],
                        highlightthickness=1, padx=20, pady=15)
        card.pack(fill=tk.X, pady=(0, 10))

        sup = tk.Frame(card, bg=C["blanco"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text=jugador["nombre"], bg=C["blanco"],
                 fg=C["texto_principal"], font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT)
        tk.Label(sup, text="⚠ Retener", bg=C["warning"], fg=C["blanco"],
                 font=("Segoe UI", 9, "bold"), padx=10, pady=2).pack(side=tk.LEFT, padx=(10, 0))

        info = tk.Frame(card, bg=C["blanco"])
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
            sub = tk.Frame(info, bg=C["blanco"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=C["blanco"], fg=C["texto_secundario"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=C["blanco"], fg=C["texto_principal"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        tk.Button(card, text="🎁 Ofrecer Bono de Retorno",
                  bg=C["warning"], fg=C["blanco"], font=("Segoe UI", 10, "bold"),
                  bd=0, padx=15, pady=5,
                  activebackground=C["sidebar_hover"],
                  command=lambda n=jugador["nombre"]: self._ofrecer_bono(n)).pack(anchor="e", pady=(10, 0))

    def _ofrecer_bono(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Bono Ofrecido",
                            f"Bono de retorno ofrecido a {nombre}.")


# ============================================================
# PANEL: Personas a Cuidar
# ============================================================
class PanelCuidar:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=C["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        cuidar = AplicacionCasino._obtener_por_clasificacion("Cuidar")

        PanelBase._crear_header(self.frame, "Personas a Cuidar",
                                f"{len(cuidar)} jugador(es) que requieren supervisión o límites.")
        body = tk.Frame(self.frame, bg=C["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=(10, 25))

        if not cuidar:
            tk.Label(body, text="No hay jugadores que requieran cuidado.", bg=C["fondo"],
                     fg=C["texto_secundario"], font=("Segoe UI", 12)).pack()
            return

        for j in cuidar:
            self._crear_tarjeta_cuidar(body, j)

    def _crear_tarjeta_cuidar(self, padre, jugador):
        card = tk.Frame(padre, bg=C["blanco"], highlightbackground=C["rojo_secundario"],
                        highlightthickness=1, padx=20, pady=15)
        card.pack(fill=tk.X, pady=(0, 10))

        sup = tk.Frame(card, bg=C["blanco"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text=jugador["nombre"], bg=C["blanco"],
                 fg=C["texto_principal"], font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT)
        tk.Label(sup, text="🛡 Cuidar", bg=C["rojo_secundario"], fg=C["blanco"],
                 font=("Segoe UI", 9, "bold"), padx=10, pady=2).pack(side=tk.LEFT, padx=(10, 0))

        alertas = []
        if jugador["edad"] <= 22:
            alertas.append("Edad joven - monitorear tiempo de juego")
        if jugador["tiempo_en_casino_hoy"] >= 4:
            alertas.append(f"Lleva {jugador['tiempo_en_casino_hoy']} hrs jugando - sugerir descanso")
        if jugador["gasto_hoy"] >= jugador["presupuesto_hoy"] * 0.8:
            alertas.append("Gastó más del 80% de su presupuesto - monitorear")
        if jugador["perdidas_acumuladas"] > jugador["ganancias_acumuladas"] * 2:
            alertas.append("Pérdidas acumuladas altas comparado a ganancias")
        if not alertas:
            alertas.append("Sin alertas críticas por ahora")

        info = tk.Frame(card, bg=C["blanco"])
        info.pack(fill=tk.X, pady=(5, 0))

        datos = [
            ("Edad", jugador["edad"]),
            ("Tiempo Hoy", f"{jugador['tiempo_en_casino_hoy']} hrs"),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
            ("Rondas Hoy", jugador["rondas_jugadas_hoy"]),
            ("Pérdidas Totales", f"S/ {jugador['perdidas_acumuladas']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=C["blanco"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=C["blanco"], fg=C["texto_secundario"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=C["blanco"], fg=C["texto_principal"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        alert_frame = tk.Frame(card, bg=C["rojo_claro"], padx=12, pady=8)
        alert_frame.pack(fill=tk.X, pady=(10, 0))
        for alerta in alertas:
            tk.Label(alert_frame, text=f"⚠ {alerta}", bg=C["rojo_claro"],
                     fg=C["rojo_oscuro"], font=("Segoe UI", 9),
                     anchor="w").pack(fill=tk.X)

        btn_frame = tk.Frame(card, bg=C["blanco"])
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        tk.Button(btn_frame, text="🔇 Sugerir Descanso",
                  bg=C["rojo_secundario"], fg=C["blanco"],
                  font=("Segoe UI", 9, "bold"), bd=0, padx=12, pady=4,
                  command=lambda n=jugador["nombre"]: self._sugerir_descanso(n)).pack(side=tk.LEFT, padx=(0, 10))
        tk.Button(btn_frame, text="📋 Registrar Intervención",
                  bg=C["texto_secundario"], fg=C["blanco"],
                  font=("Segoe UI", 9), bd=0, padx=12, pady=4,
                  command=lambda n=jugador["nombre"]: self._registrar_intervencion(n)).pack(side=tk.LEFT)

    def _sugerir_descanso(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Descanso Sugerido",
                            f"Notificación enviada a {nombre}: sugerencia de descanso.")

    def _registrar_intervencion(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Intervención Registrada",
                            f"Intervención con {nombre} registrada en el sistema.")


# ============================================================
# PANEL: Servicio Rápido
# ============================================================
class PanelRapido:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=C["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        rapidos = AplicacionCasino._obtener_por_clasificacion("Servicio_Rapido")

        PanelBase._crear_header(self.frame, "Servicio Rápido",
                                f"{len(rapidos)} jugador(es) que prefieren atención ágil y eficiente.")
        body = tk.Frame(self.frame, bg=C["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=25, pady=(10, 25))

        if not rapidos:
            tk.Label(body, text="No hay jugadores para servicio rápido.", bg=C["fondo"],
                     fg=C["texto_secundario"], font=("Segoe UI", 12)).pack()
            return

        for j in rapidos:
            self._crear_tarjeta_rapido(body, j)

    def _crear_tarjeta_rapido(self, padre, jugador):
        card = tk.Frame(padre, bg=C["blanco"], highlightbackground=C["success"],
                        highlightthickness=1, padx=20, pady=15)
        card.pack(fill=tk.X, pady=(0, 10))

        sup = tk.Frame(card, bg=C["blanco"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text=jugador["nombre"], bg=C["blanco"],
                 fg=C["texto_principal"], font=("Segoe UI", 14, "bold")).pack(side=tk.LEFT)
        tk.Label(sup, text="⚡ Rápido", bg=C["success"], fg=C["blanco"],
                 font=("Segoe UI", 9, "bold"), padx=10, pady=2).pack(side=tk.LEFT, padx=(10, 0))

        razones = []
        if jugador["prefiere_rapido_o_lento"] == "Rápido":
            razones.append("Prefiere juegos rápidos")
        if jugador["cambia_al_perder"] == "Sí":
            razones.append("Cambia rápido de juego al perder")
        if jugador["tiempo_promedio_visita"] <= 150:
            razones.append("Visitas cortas - atención prioritaria")
        if jugador["presupuesto_hoy"] >= 200:
            razones.append("Presupuesto alto - agilizar atención")

        info = tk.Frame(card, bg=C["blanco"])
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
            sub = tk.Frame(info, bg=C["blanco"], padx=8, pady=2)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=C["blanco"], fg=C["texto_secundario"],
                     font=("Segoe UI", 8)).pack(anchor="w")
            tk.Label(sub, text=v, bg=C["blanco"], fg=C["texto_principal"],
                     font=("Segoe UI", 11, "bold")).pack(anchor="w")

        razon_frame = tk.Frame(card, bg=C["blanco"], padx=8, pady=5)
        razon_frame.pack(fill=tk.X, pady=(5, 0))
        tk.Label(razon_frame, text="Prioridad:", bg=C["blanco"],
                 fg=C["texto_secundario"], font=("Segoe UI", 9)).pack(anchor="w")
        for r in razones:
            tk.Label(razon_frame, text=f"  • {r}", bg=C["blanco"],
                     fg=C["texto_principal"], font=("Segoe UI", 10)).pack(anchor="w")

        tk.Button(card, text="⚡ Atender Prioritariamente",
                  bg=C["success"], fg=C["blanco"], font=("Segoe UI", 10, "bold"),
                  bd=0, padx=15, pady=5,
                  activebackground=C["sidebar_hover"],
                  command=lambda n=jugador["nombre"]: self._atender(n)).pack(anchor="e", pady=(10, 0))

    def _atender(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Atención Rápida",
                            f"Notificación enviada: atender a {nombre} con prioridad.")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    AplicacionCasino()
