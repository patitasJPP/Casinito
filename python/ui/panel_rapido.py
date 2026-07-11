import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import SERVICIO_RAPIDO


class PanelRapido:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        rapidos = SERVICIO_RAPIDO

        PanelBase._crear_header(self.frame, "Servicio R\u00e1pido",
                                f"{len(rapidos)} jugador(es) que prefieren atenci\u00f3n \u00e1gil. Priorizar su experiencia.")
        body = PanelBase._crear_body_scroll(self.frame)
        PanelBase._crear_grid_tarjetas(body, rapidos, 4, self._crear_tarjeta_rapido)

    def _crear_tarjeta_rapido(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["verde"], highlightthickness=1, padx=14, pady=12)
        PanelBase._aplicar_hover_card(card, COLORES["verde"])

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="\u25b6", bg=COLORES["card_bg"], fg=COLORES["verde"],
                 font=("Segoe UI", 14)).pack(side=tk.LEFT, padx=(0, 6))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 13, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="R\u00e1pido", bg=COLORES["verde"], fg=COLORES["blanco"],
                           font=("Segoe UI", 8, "bold"), padx=8, pady=2)
        lbl_tag.pack(side=tk.LEFT, padx=(6, 0))

        razones = []
        if jugador["prefiere_rapido_o_lento"] == "R\u00e1pido":
            razones.append("Prefiere juegos r\u00e1pidos")
        if jugador["cambia_al_perder"] == "S\u00ed":
            razones.append("Cambia r\u00e1pido de juego al perder")
        if jugador["tiempo_promedio_visita"] <= 150:
            razones.append("Visitas cortas - atenci\u00f3n prioritaria")
        if jugador["presupuesto_hoy"] >= 200:
            razones.append("Presupuesto alto - agilizar atenci\u00f3n")

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(6, 0))

        datos = [
            ("Ritmo", jugador["prefiere_rapido_o_lento"]),
            ("Juego Favorito", jugador["juego_favorito"]),
            ("Juego Actual", jugador["juego_actual"]),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Tiempo Prom.", f"{jugador['tiempo_promedio_visita']} min"),
            ("Apuesta Prom.", f"S/ {jugador['gasto_promedio_ronda']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=4, pady=1)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 7)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10, "bold")).pack(anchor="w")

        razon_frame = tk.Frame(card, bg=COLORES["card_alt"], padx=10, pady=6)
        razon_frame.pack(fill=tk.X, pady=(6, 0))
        tk.Label(razon_frame, text="Prioridades:", bg=COLORES["card_alt"],
                 fg=COLORES["verde"], font=("Segoe UI", 8, "bold")).pack(anchor="w")
        for r in razones:
            tk.Label(razon_frame, text=f"  {r}", bg=COLORES["card_alt"],
                     fg=COLORES["texto"], font=("Segoe UI", 8)).pack(anchor="w")

        btn = tk.Button(card, text="Atender Prioritariamente",
                        bg=COLORES["verde"], fg=COLORES["blanco"],
                        font=("Segoe UI", 9, "bold"), bd=0, padx=14, pady=4,
                        activebackground=COLORES["verde_oscuro"],
                        activeforeground=COLORES["blanco"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._atender(n))
        btn.pack(anchor="e", pady=(8, 0))
        return card

    def _atender(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Atenci\u00f3n R\u00e1pida",
                            f"Notificaci\u00f3n enviada: atender a {nombre} con prioridad.")
