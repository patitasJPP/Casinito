import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import VIP


class PanelVIP:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        vips = VIP

        PanelBase._crear_header(self.frame, "Invitar a VIP",
                                f"{len(vips)} jugadores de alto valor. Clientes premium que merecen atenci\u00f3n exclusiva.")
        body = PanelBase._crear_body_scroll(self.frame)
        PanelBase._crear_grid_tarjetas(body, vips, 3, self._crear_tarjeta_vip)

    def _crear_tarjeta_vip(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["oro"], highlightthickness=1, padx=14, pady=12)
        PanelBase._aplicar_hover_card(card, COLORES["oro"])

        superior = tk.Frame(card, bg=COLORES["card_bg"])
        superior.pack(fill=tk.X)
        tk.Label(superior, text="\u2605", bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 14)).pack(side=tk.LEFT, padx=(0, 6))
        tk.Label(superior, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["oro"], font=("Segoe UI", 13, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(superior, text="VIP", bg=COLORES["oro"], fg=COLORES["fondo"],
                           font=("Segoe UI", 8, "bold"), padx=8, pady=2)
        lbl_tag.pack(side=tk.LEFT, padx=(6, 0))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(6, 0))

        datos = [
            ("Edad", jugador["edad"]),
            ("Ocupaci\u00f3n", jugador["ocupacion"]),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Frecuencia", f"{jugador['frecuencia_semanal']}x/sem"),
            ("Gasto M\u00e1x.", f"S/ {jugador['gasto_maximo_historico']}"),
            ("Visitas", jugador["total_visitas"]),
            ("Juego", jugador["juego_favorito"]),
            ("Ganancias", f"S/ {jugador['ganancias_acumuladas']}"),
        ]
        for i, (label, valor) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=4, pady=1)
            sub.grid(row=i // 4, column=i % 4, sticky="w")
            tk.Label(sub, text=label, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 7)).pack(anchor="w")
            tk.Label(sub, text=str(valor), bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10, "bold")).pack(anchor="w")

        btn = tk.Button(card, text="Enviar Invitaci\u00f3n VIP",
                        bg=COLORES["oro"], fg=COLORES["fondo"],
                        font=("Segoe UI", 9, "bold"), bd=0, padx=14, pady=4,
                        activebackground=COLORES["oro_oscuro"],
                        activeforeground=COLORES["fondo"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._invitar(n))
        btn.pack(anchor="e", pady=(8, 0))
        return card

    def _invitar(self, nombre):
        from tkinter import messagebox
        confirmar = messagebox.askquestion("Confirmar Invitaci\u00f3n",
                                            f"\u00bfEst\u00e1 seguro de enviar invitaci\u00f3n VIP a {nombre}?")
        if confirmar == "yes":
            messagebox.showinfo("Invitaci\u00f3n Enviada",
                                f"Se ha enviado la invitaci\u00f3n VIP a {nombre}.")
