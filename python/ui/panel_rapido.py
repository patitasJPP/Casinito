import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos, obtener_por_clasificacion


class PanelRapido:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        jugadores = obtener_todos()
        rapidos = obtener_por_clasificacion(jugadores, "Servicio_Rapido")

        PanelBase._crear_header(self.frame, "Servicio R\u00e1pido",
                                f"{len(rapidos)} jugador(es) que prefieren atenci\u00f3n \u00e1gil. Priorizar su experiencia.")
        body = PanelBase._crear_body_scroll(self.frame)

        if not rapidos:
            tk.Label(body, text="No hay jugadores para servicio r\u00e1pido.", bg=COLORES["fondo"],
                     fg=COLORES["texto_sec"], font=("Segoe UI", 12)).pack()
            return

        for j in rapidos:
            self._crear_tarjeta_rapido(body, j)

    def _crear_tarjeta_rapido(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["verde"], highlightthickness=1, padx=22, pady=16)
        card.pack(fill=tk.X, pady=(0, 12))
        PanelBase._aplicar_hover_card(card, COLORES["verde"])

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="\u25b6", bg=COLORES["card_bg"], fg=COLORES["verde"],
                 font=("Segoe UI", 16)).pack(side=tk.LEFT, padx=(0, 8))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 16, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="R\u00e1pido", bg=COLORES["verde"], fg=COLORES["blanco"],
                           font=("Segoe UI", 9, "bold"), padx=12, pady=3)
        lbl_tag.pack(side=tk.LEFT, padx=(10, 0))

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
            tk.Label(razon_frame, text=f"  {r}", bg=COLORES["card_alt"],
                     fg=COLORES["texto"], font=("Segoe UI", 9)).pack(anchor="w")

        btn = tk.Button(card, text="Atender Prioritariamente",
                        bg=COLORES["verde"], fg=COLORES["blanco"],
                        font=("Segoe UI", 10, "bold"), bd=0, padx=18, pady=6,
                        activebackground=COLORES["verde_oscuro"],
                        activeforeground=COLORES["blanco"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._atender(n))
        btn.pack(anchor="e", pady=(12, 0))
        btn.bind("<FocusIn>", lambda e: btn.configure(highlightbackground=COLORES["oro"], highlightthickness=2))
        btn.bind("<FocusOut>", lambda e: btn.configure(highlightthickness=0))

    def _atender(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Atenci\u00f3n R\u00e1pida",
                            f"Notificaci\u00f3n enviada: atender a {nombre} con prioridad.")
