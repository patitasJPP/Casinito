import tkinter as tk
from tkinter import ttk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos
from modules.ventana_reporte import VentanaReporte


class PanelTodos:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugadores = obtener_todos()
        self._jugadores_filtrados = list(self.jugadores)
        self._orden_col = "gasto_hoy"
        self._orden_rev = True

        PanelBase._crear_header(self.frame, "Todos los Usuarios",
                                f"{len(self.jugadores)} jugadores registrados. Use los filtros para refinar.")
        self._crear_contenido()

    def _crear_contenido(self):
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 0))

        self._crear_barra_filtros(body)

        columnas = ("Nombre", "Edad", "Clasificaci\u00f3n", "Presupuesto", "Gasto Hoy",
                     "Juego Favorito", "Frecuencia", "Perdidas Acum.")
        self.tabla = ttk.Treeview(body, columns=columnas, show="headings", height=12)

        anchos = [120, 50, 100, 100, 100, 130, 90, 120]
        orden_cols = ["nombre", "edad", "clasificacion", "presupuesto_hoy",
                      "gasto_hoy", "juego_favorito", "frecuencia_semanal", "perdidas_acumuladas"]
        for col, ancho, key in zip(columnas, anchos, orden_cols):
            self.tabla.heading(col, text=col,
                               command=lambda k=key: self._ordenar_por(k))
            self.tabla.column(col, width=ancho, anchor=tk.CENTER)

        self._poblar_tabla(self.jugadores)

        scroll_y = ttk.Scrollbar(body, orient=tk.VERTICAL, command=self.tabla.yview)
        scroll_x = ttk.Scrollbar(body, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        body.grid_rowconfigure(2, weight=1)
        body.grid_columnconfigure(0, weight=1)

        self.tabla.grid(row=2, column=0, sticky="nsew")
        scroll_y.grid(row=2, column=1, sticky="ns")
        scroll_x.grid(row=3, column=0, sticky="ew")

        self._frame_detalle = tk.Frame(body, bg=COLORES["fondo"])
        self._frame_detalle.grid(row=4, column=0, columnspan=2, sticky="nsew", pady=(12, 0))

        self.tabla.bind("<<TreeviewSelect>>", self._on_seleccionar)

        if self.jugadores:
            children = self.tabla.get_children()
            if children:
                self.tabla.selection_set(children[0])
                self._mostrar_detalle(self.jugadores[0])

    def _crear_barra_filtros(self, parent):
        frame = tk.Frame(parent, bg=COLORES["fondo"])
        frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        frame.grid_columnconfigure(0, weight=1)

        row1 = tk.Frame(frame, bg=COLORES["fondo"])
        row1.pack(fill=tk.X, pady=(0, 6))

        self.input_busqueda = tk.Entry(row1, bg=COLORES["input_bg"],
                                       fg=COLORES["texto_dim"], font=("Segoe UI", 11),
                                       insertbackground=COLORES["oro"], relief="flat")
        self.input_busqueda.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8), ipady=6)
        self.input_busqueda.insert(0, "Buscar por nombre...")
        self.input_busqueda.bind("<FocusIn>", self._on_focus_in)
        self.input_busqueda.bind("<FocusOut>", self._on_focus_out)
        self.input_busqueda.bind("<KeyRelease>", lambda e: self._aplicar_filtros())

        self.filtro_clasif = tk.StringVar(value="Todas")
        opciones = ["Todas", "VIP", "Retener", "Cuidar", "Servicio_R\u00e1pido"]
        menu = ttk.Combobox(row1, textvariable=self.filtro_clasif, values=opciones,
                            state="readonly", font=("Segoe UI", 10), width=14)
        menu.pack(side=tk.LEFT, padx=(0, 8))
        menu.bind("<<ComboboxSelected>>", lambda e: self._aplicar_filtros())

        row2 = tk.Frame(frame, bg=COLORES["fondo"])
        row2.pack(fill=tk.X)

        tk.Label(row2, text="Gasto m\u00edn:", bg=COLORES["fondo"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=(0, 4))
        self.gasto_min = tk.Entry(row2, bg=COLORES["input_bg"], fg=COLORES["texto"],
                                  font=("Segoe UI", 10), width=8, relief="flat")
        self.gasto_min.pack(side=tk.LEFT, padx=(0, 10), ipady=4)
        self.gasto_min.insert(0, "0")
        self.gasto_min.bind("<KeyRelease>", lambda e: self._aplicar_filtros())

        tk.Label(row2, text="m\u00e1x:", bg=COLORES["fondo"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=(0, 4))
        self.gasto_max = tk.Entry(row2, bg=COLORES["input_bg"], fg=COLORES["texto"],
                                  font=("Segoe UI", 10), width=8, relief="flat")
        self.gasto_max.pack(side=tk.LEFT, padx=(0, 10), ipady=4)
        self.gasto_max.insert(0, "9999")
        self.gasto_max.bind("<KeyRelease>", lambda e: self._aplicar_filtros())

        tk.Label(row2, text="Edad min:", bg=COLORES["fondo"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=(0, 4))
        self.edad_min = tk.Entry(row2, bg=COLORES["input_bg"], fg=COLORES["texto"],
                                 font=("Segoe UI", 10), width=5, relief="flat")
        self.edad_min.pack(side=tk.LEFT, padx=(0, 8), ipady=4)
        self.edad_min.insert(0, "0")
        self.edad_min.bind("<KeyRelease>", lambda e: self._aplicar_filtros())

        tk.Label(row2, text="m\u00e1x:", bg=COLORES["fondo"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=(0, 4))
        self.edad_max = tk.Entry(row2, bg=COLORES["input_bg"], fg=COLORES["texto"],
                                 font=("Segoe UI", 10), width=5, relief="flat")
        self.edad_max.pack(side=tk.LEFT, padx=(0, 8), ipady=4)
        self.edad_max.insert(0, "150")
        self.edad_max.bind("<KeyRelease>", lambda e: self._aplicar_filtros())

        self.lbl_resultados = tk.Label(row2, text="", bg=COLORES["fondo"],
                                       fg=COLORES["texto_sec"], font=("Segoe UI", 10))
        self.lbl_resultados.pack(side=tk.RIGHT, padx=(10, 0))

        btn_limpiar = tk.Button(row2, text="Limpiar Filtros",
                                bg=COLORES["card_alt"], fg=COLORES["texto"],
                                font=("Segoe UI", 9), bd=0, padx=12, pady=4,
                                cursor="hand2", command=self._limpiar_filtros)
        btn_limpiar.pack(side=tk.RIGHT, padx=(0, 8))

    def _aplicar_filtros(self):
        texto = self.input_busqueda.get().strip().lower()
        es_placeholder = texto == "buscar por nombre..."
        clasif_filtro = self.filtro_clasif.get()

        try:
            g_min = float(self.gasto_min.get() or 0)
        except ValueError:
            g_min = 0
        try:
            g_max = float(self.gasto_max.get() or 99999)
        except ValueError:
            g_max = 99999
        try:
            e_min = int(self.edad_min.get() or 0)
        except ValueError:
            e_min = 0
        try:
            e_max = int(self.edad_max.get() or 150)
        except ValueError:
            e_max = 150

        filtrados = []
        for j in self.jugadores:
            if not es_placeholder and texto and texto not in j["nombre"].lower():
                continue
            if clasif_filtro != "Todas":
                if clasif_filtro == "Servicio_R\u00e1pido":
                    if j["clasificacion"] != "Servicio_Rapido":
                        continue
                elif j["clasificacion"] != clasif_filtro:
                    continue
            gasto = j["gasto_hoy"]
            if gasto < g_min or gasto > g_max:
                continue
            edad = j["edad"]
            if edad < e_min or edad > e_max:
                continue
            filtrados.append(j)

        self._jugadores_filtrados = filtrados
        self._ordenar_y_repoblar()

    def _limpiar_filtros(self):
        self.input_busqueda.delete(0, tk.END)
        self.input_busqueda.insert(0, "Buscar por nombre...")
        self.input_busqueda.configure(fg=COLORES["texto_dim"])
        self.filtro_clasif.set("Todas")
        self.gasto_min.delete(0, tk.END); self.gasto_min.insert(0, "0")
        self.gasto_max.delete(0, tk.END); self.gasto_max.insert(0, "9999")
        self.edad_min.delete(0, tk.END); self.edad_min.insert(0, "0")
        self.edad_max.delete(0, tk.END); self.edad_max.insert(0, "150")
        self._jugadores_filtrados = list(self.jugadores)
        self._ordenar_y_repoblar()

    def _ordenar_por(self, key):
        if self._orden_col == key:
            self._orden_rev = not self._orden_rev
        else:
            self._orden_col = key
            self._orden_rev = True
        self._ordenar_y_repoblar()

    def _ordenar_y_repoblar(self):
        ordenados = sorted(self._jugadores_filtrados,
                           key=lambda j: (j.get(self._orden_col, 0) if isinstance(j.get(self._orden_col, ""), (int, float)) else j.get(self._orden_col, "")),
                           reverse=self._orden_rev)
        self._poblar_tabla(ordenados)
        self.lbl_resultados.config(text=f"{len(ordenados)} de {len(self.jugadores)}")

    def _poblar_tabla(self, lista):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        mapa_color = {"VIP": COLORES["oro"], "Retener": COLORES["naranja"],
                      "Cuidar": COLORES["rojo"], "Servicio_Rapido": COLORES["verde"]}
        for j in lista:
            tag, _ = PanelBase._crear_tag(j["clasificacion"])
            self.tabla.insert("", tk.END,
                              values=(j["nombre"], j["edad"], tag,
                                      f"S/ {j['presupuesto_hoy']}", f"S/ {j['gasto_hoy']}",
                                      j["juego_favorito"], f"{j['frecuencia_semanal']}x/sem",
                                      f"S/ {j['perdidas_acumuladas']}"),
                              tags=(j["id"],))
            self.tabla.tag_configure(j["id"],
                                     foreground=mapa_color.get(j["clasificacion"], COLORES["texto"]))

    def _on_focus_in(self, event):
        if self.input_busqueda.get() == "Buscar por nombre...":
            self.input_busqueda.delete(0, tk.END)
            self.input_busqueda.configure(fg=COLORES["texto"])

    def _on_focus_out(self, event):
        if not self.input_busqueda.get().strip():
            self.input_busqueda.delete(0, tk.END)
            self.input_busqueda.insert(0, "Buscar por nombre...")
            self.input_busqueda.configure(fg=COLORES["texto_dim"])

    def _on_seleccionar(self, event):
        seleccion = self.tabla.selection()
        if not seleccion:
            return
        item = self.tabla.item(seleccion[0])
        nombre = item["values"][0]
        jugador = next((j for j in self.jugadores if j["nombre"] == nombre), None)
        if jugador:
            self._mostrar_detalle(jugador)

    def _abrir_reporte(self, jugador):
        VentanaReporte(self.frame, jugador)

    def _mostrar_detalle(self, jugador):
        for w in self._frame_detalle.winfo_children():
            w.destroy()
        PanelBase._detalle_jugador(self._frame_detalle, jugador)
        btn_reporte = tk.Button(self._frame_detalle, text="Abrir Reporte Detallado",
                                bg=COLORES["oro"], fg=COLORES["fondo"],
                                font=("Segoe UI", 10, "bold"), bd=0,
                                padx=16, pady=6, cursor="hand2",
                                command=lambda j=jugador: self._abrir_reporte(j))
        btn_reporte.pack(pady=(8, 0))
