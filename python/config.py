COLORES = {
    "fondo": "#0a0e17",
    "sidebar": "#0f1420",
    "sidebar_hover": "#1a2340",
    "sidebar_selected": "#f0c040",
    "card_bg": "#141a2b",
    "card_alt": "#1a2340",
    "blanco": "#ffffff",
    "oro": "#f0c040",
    "oro_oscuro": "#d4a830",
    "rojo": "#ef5350",
    "rojo_oscuro": "#c62828",
    "verde": "#66bb6a",
    "verde_oscuro": "#2e7d32",
    "naranja": "#ffa726",
    "texto": "#e8eaf6",
    "texto_sec": "#9ea7c3",
    "texto_dim": "#5c6a8a",
    "border": "#2a3355",
    "alerta_bg": "#1a0a0a",
    "toast_bg": "#0f1420",
    "toast_texto": "#e8eaf6",
    "barra_superior": "#060a12",
    "scrollbar_bg": "#0f1420",
    "scrollbar_fg": "#f0c040",
    "input_bg": "#1a2340",
    "input_fg": "#e8eaf6",
}


def configurar_estilos():
    from tkinter import ttk
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview",
                     background=COLORES["card_bg"],
                     foreground=COLORES["texto"],
                     rowheight=34,
                     fieldbackground=COLORES["card_bg"],
                     font=("Segoe UI", 10),
                     bordercolor=COLORES["border"])
    estilo.configure("Treeview.Heading",
                     background=COLORES["sidebar"],
                     foreground=COLORES["oro"],
                     font=("Segoe UI", 10, "bold"),
                     bordercolor=COLORES["border"])
    estilo.map("Treeview",
               background=[("selected", COLORES["sidebar_hover"])],
               foreground=[("selected", COLORES["oro"])])
    estilo.map("Treeview.Heading",
               background=[("active", COLORES["sidebar_hover"])])
    estilo.configure("Vertical.TScrollbar",
                     background=COLORES["scrollbar_fg"],
                     troughcolor=COLORES["fondo"],
                     bordercolor=COLORES["border"],
                     arrowcolor=COLORES["oro"])
