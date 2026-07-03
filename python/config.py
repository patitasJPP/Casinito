COLORES = {
    "fondo": "#0d0d0d",
    "sidebar": "#111111",
    "sidebar_hover": "#1a1a1a",
    "sidebar_selected": "#d4a843",
    "card_bg": "#1a1a1a",
    "card_alt": "#222222",
    "blanco": "#ffffff",
    "oro": "#d4a843",
    "oro_oscuro": "#b8922e",
    "rojo": "#d32f2f",
    "rojo_oscuro": "#b71c1c",
    "verde": "#2e7d32",
    "verde_oscuro": "#1b5e20",
    "naranja": "#e65100",
    "texto": "#f5f5f5",
    "texto_sec": "#aaaaaa",
    "texto_dim": "#666666",
    "border": "#333333",
    "alerta_bg": "#1a0000",
    "toast_bg": "#111111",
    "toast_texto": "#f5f5f5",
    "barra_superior": "#080808",
    "scrollbar_bg": "#111111",
    "scrollbar_fg": "#d4a843",
    "input_bg": "#222222",
    "input_fg": "#f5f5f5",
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
