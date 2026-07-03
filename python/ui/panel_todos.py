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
        self._items_filtrados = set()

        PanelBase._crear_header(self.frame, "Todos los Usuarios",
                                f"{len(self.jugadores)} jugadores registrados. Seleccione uno para ver detalles.")
        self._crear_contenido()

    def _crear_contenido(self):
        body = tk.Frame(self.frame, bg=COLORES["fondo"])
        body.pack(fill=tk.BOTH, expand=True, padx=28, pady=(10, 0))

        self._crear_barra_busqueda(body)

        columnas = ("Nombre", "Edad", "Ocupaci\u00f3n", "Presupuesto", "Fichas",
                     "Gasto Hoy", "Juego Favorito", "Frecuencia", "Clasificaci\u00f3n")
        self.tabla = ttk.Treeview(body, columns=columnas, show="headings")

        anchos = [100, 50, 100, 90, 70, 80, 120, 90, 110]
        for col, ancho in zip(columnas, anchos):
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=ancho, anchor=tk.CENTER)

        mapa_color = {"VIP": COLORES["oro"], "Retener": COLORES["naranja"],
                      "Cuidar": COLORES["rojo"], "Servicio_Rapido": COLORES["verde"]}
        for j in self.jugadores:
            tag, _ = PanelBase._crear_tag(j["clasificacion"])
            self.tabla.insert("", tk.END,
                              values=(j["nombre"], j["edad"], j["ocupacion"],
                                      f"S/ {j['presupuesto_hoy']}", j["fichas_actuales"],
                                      f"S/ {j['gasto_hoy']}", j["juego_favorito"],
                                      f"{j['frecuencia_semanal']}x/sem", tag),
                              tags=(j["id"],))
            self.tabla.tag_configure(j["id"],
                                     foreground=mapa_color.get(j["clasificacion"], COLORES["texto"]))

        scroll_y = ttk.Scrollbar(body, orient=tk.VERTICAL, command=self.tabla.yview)
        scroll_x = ttk.Scrollbar(body, orient=tk.HORIZONTAL, command=self.tabla.xview)
        self.tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        body.grid_rowconfigure(1, weight=1)
        body.grid_columnconfigure(0, weight=1)

        self.tabla.grid(row=1, column=0, sticky="nsew")
        scroll_y.grid(row=1, column=1, sticky="ns")
        scroll_x.grid(row=2, column=0, sticky="ew")

        self._frame_detalle = tk.Frame(body, bg=COLORES["fondo"])
        self._frame_detalle.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(15, 0))

        self.tabla.bind("<<TreeviewSelect>>", self._on_seleccionar)

        if self.jugadores:
            children = self.tabla.get_children()
            if children:
                self.tabla.selection_set(children[0])
                self._mostrar_detalle(self.jugadores[0])

    def _crear_barra_busqueda(self, parent):
        frame = tk.Frame(parent, bg=COLORES["fondo"])
        frame.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 10))

        self.input_busqueda = tk.Entry(frame, bg=COLORES["input_bg"],
                                       fg=COLORES["texto_dim"], font=("Segoe UI", 11),
                                       insertbackground=COLORES["oro"], relief="flat")
        self.input_busqueda.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=6)
        self.input_busqueda.insert(0, "Buscar jugador...")
        self.input_busqueda.bind("<FocusIn>", self._on_focus_in)
        self.input_busqueda.bind("<FocusOut>", self._on_focus_out)
        self.input_busqueda.bind("<KeyRelease>", self._on_filtrar)

        self.filtro_clasif = tk.StringVar(value="Todas")
        opciones = ["Todas", "VIP", "Retener", "Cuidar", "Servicio_R\u00e1pido"]
        menu = ttk.Combobox(frame, textvariable=self.filtro_clasif, values=opciones,
                            state="readonly", font=("Segoe UI", 10))
        menu.pack(side=tk.RIGHT)
        menu.bind("<<ComboboxSelected>>", self._on_filtrar)

    def _on_focus_in(self, event):
        if self.input_busqueda.get() == "Buscar jugador...":
            self.input_busqueda.delete(0, tk.END)
            self.input_busqueda.configure(fg=COLORES["texto"])

    def _on_focus_out(self, event):
        if not self.input_busqueda.get().strip():
            self.input_busqueda.delete(0, tk.END)
            self.input_busqueda.insert(0, "Buscar jugador...")
            self.input_busqueda.configure(fg=COLORES["texto_dim"])

    def _on_filtrar(self, event=None):
        texto = self.input_busqueda.get().strip().lower()
        es_placeholder = texto == "buscar jugador..."
        clasif_filtro = self.filtro_clasif.get()

        for item in self.tabla.get_children():
            self.tabla.detach(item)

        for j in self.jugadores:
            items = self.tabla.get_children()
            item_id = None
            for it in items:
                vals = self.tabla.item(it, "values")
                if vals and vals[0] == j["nombre"]:
                    item_id = it
                    break
            if item_id is None:
                tag, _ = PanelBase._crear_tag(j["clasificacion"])
                item_id = self.tabla.insert("", tk.END,
                                            values=(j["nombre"], j["edad"], j["ocupacion"],
                                                    f"S/ {j['presupuesto_hoy']}", j["fichas_actuales"],
                                                    f"S/ {j['gasto_hoy']}", j["juego_favorito"],
                                                    f"{j['frecuencia_semanal']}x/sem", tag),
                                            tags=(j["id"],))

            nombre = j["nombre"].lower()
            clasif = j["clasificacion"]
            coincide_texto = True if (not texto or es_placeholder) else texto in nombre
            coincide_clasif = (clasif_filtro == "Todas" or
                               clasif == clasif_filtro or
                               (clasif == "Servicio_Rapido" and clasif_filtro == "Servicio_R\u00e1pido"))

            if coincide_texto and coincide_clasif:
                self.tabla.move(item_id, "", tk.END)

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
