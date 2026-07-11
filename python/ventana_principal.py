import tkinter as tk
from config import COLORES, configurar_estilos
from ui.panel_dashboard import PanelDashboard
from ui.panel_todos import PanelTodos
from ui.panel_vip import PanelVIP
from ui.panel_retener import PanelRetener
from ui.panel_cuidar import PanelCuidar
from ui.panel_rapido import PanelRapido
from ui.panel_estadisticas import PanelEstadisticas
from data.jugadores import obtener_todos


class AplicacionCasino:
    def __init__(self):
        self.ventana = tk.Tk()
        configurar_estilos()
        self.ventana.title("Casino Sapiens - Sistema Experto de Gestión")
        self.ventana.configure(bg=COLORES["fondo"])
        self.ventana.resizable(False, False)
        try:
            self.ventana.iconbitmap("assets/icono.ico")
        except Exception:
            pass
        ancho = self.ventana.winfo_screenwidth()
        alto = self.ventana.winfo_screenheight()
        self.ventana.geometry(f"{ancho}x{alto}+0+0")
        self.ventana.state("zoomed")

        self.panel_actual = None
        self._crear_layout()
        self._cargar_panel("dashboard")
        self._bind_atajos()
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
        barra = tk.Frame(self.ventana, bg=COLORES["barra_superior"], height=48)
        barra.pack(fill=tk.X, side=tk.TOP)

        tk.Label(barra, text="CASINO SAPIENS", bg=COLORES["barra_superior"],
                 fg=COLORES["oro"], font=("Segoe UI", 15, "bold")).pack(side=tk.LEFT, padx=22, pady=10)
        tk.Label(barra, text="Sistema Experto de Perfilado", bg=COLORES["barra_superior"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 10)).pack(side=tk.LEFT, padx=(0, 20), pady=10)

        separador = tk.Frame(barra, bg=COLORES["oro"], height=2)
        separador.pack(fill=tk.X, side=tk.BOTTOM)

    def _crear_sidebar(self):
        self._sidebar = tk.Frame(self._frame_contenido, bg=COLORES["sidebar"], width=230)
        self._sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self._sidebar.pack_propagate(False)

        tk.Label(self._sidebar, text="NAVEGACIÓN", bg=COLORES["sidebar"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 8, "bold")).pack(pady=(22, 12))

        self._nav_btns = {}
        items = [
            ("dashboard", "Dashboard"),
            ("todos", "Todos los Usuarios"),
            ("vip", "Invitar a VIP"),
            ("retener", "Personas a Retener"),
            ("cuidar", "Personas a Cuidar"),
            ("rapido", "Servicio Rápido"),
            ("estadisticas", "Estadísticas"),
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
        barra = tk.Frame(self.ventana, bg=COLORES["barra_superior"], height=30)
        barra.pack(fill=tk.X, side=tk.BOTTOM)
        jugadores = obtener_todos()
        total = len(jugadores)
        vips = sum(1 for j in jugadores if j["clasificacion"] == "VIP")
        retener = sum(1 for j in jugadores if j["clasificacion"] == "Retener")
        cuidar = sum(1 for j in jugadores if j["clasificacion"] == "Cuidar")

        tk.Label(barra, text=f"{total} jugadores  |  VIP: {vips}  |  Retener: {retener}  |  Cuidar: {cuidar}",
                 bg=COLORES["barra_superior"], fg=COLORES["texto_sec"],
                 font=("Segoe UI", 9)).pack(side=tk.LEFT, padx=15, pady=4)
        tk.Label(barra, text="Casino Sapiens v2.0  |  Prolog + Python  |  Multiparadigma",
                 bg=COLORES["barra_superior"], fg=COLORES["texto_dim"],
                 font=("Segoe UI", 9)).pack(side=tk.RIGHT, padx=15, pady=4)

    def _cargar_panel(self, key):
        self.panel_actual = key
        for k, btn in self._nav_btns.items():
            if k == key:
                btn.configure(bg=COLORES["sidebar_selected"], fg=COLORES["fondo"])
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
        elif key == "estadisticas":
            PanelEstadisticas(self._frame_paneles)

    def _bind_atajos(self):
        self.ventana.bind("<Control-1>", lambda e: self._cargar_panel("dashboard"))
        self.ventana.bind("<Control-2>", lambda e: self._cargar_panel("todos"))
        self.ventana.bind("<Control-3>", lambda e: self._cargar_panel("vip"))
        self.ventana.bind("<Control-4>", lambda e: self._cargar_panel("retener"))
        self.ventana.bind("<Control-5>", lambda e: self._cargar_panel("cuidar"))
        self.ventana.bind("<Control-6>", lambda e: self._cargar_panel("rapido"))
        self.ventana.bind("<Control-7>", lambda e: self._cargar_panel("estadisticas"))
