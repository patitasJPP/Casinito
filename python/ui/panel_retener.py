import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import RETENER


class PanelRetener:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        retener = RETENER

        PanelBase._crear_header(self.frame, "Personas a Retener",
                                f"{len(retener)} jugador(es) en riesgo de abandono. Aplicar incentivos para retenerlos.")
        body = PanelBase._crear_body_scroll(self.frame)
        PanelBase._crear_grid_tarjetas(body, retener, 4, self._crear_tarjeta_retener)

    def _crear_tarjeta_retener(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["naranja"], highlightthickness=1, padx=14, pady=12)
        PanelBase._aplicar_hover_card(card, COLORES["naranja"])

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="\u25b2", bg=COLORES["card_bg"], fg=COLORES["naranja"],
                 font=("Segoe UI", 14)).pack(side=tk.LEFT, padx=(0, 6))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 13, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="Retener", bg=COLORES["naranja"], fg=COLORES["fondo"],
                           font=("Segoe UI", 8, "bold"), padx=8, pady=2)
        lbl_tag.pack(side=tk.LEFT, padx=(6, 0))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(6, 0))

        datos = [
            ("D\u00edas sin venir", f"{jugador['dias_desde_ultima_visita']} d\u00edas"),
            ("Total Visitas", jugador["total_visitas"]),
            ("Frecuencia", f"{jugador['frecuencia_semanal']}x/sem"),
            ("\u00daltimo Juego", jugador["juego_actual"]),
            ("Gasto Prom.", f"S/ {jugador['gasto_promedio_ronda']}"),
            ("Perdidas Acum.", f"S/ {jugador['perdidas_acumuladas']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=4, pady=1)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 7)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10, "bold")).pack(anchor="w")

        dias_max = 60
        dias_pct = min(jugador["dias_desde_ultima_visita"] / dias_max, 1.0)
        dias_frame = tk.Frame(card, bg=COLORES["card_bg"])
        dias_frame.pack(fill=tk.X, pady=(6, 0))
        tk.Label(dias_frame, text="Riesgo de p\u00e9rdida:", bg=COLORES["card_bg"],
                 fg=COLORES["texto_sec"], font=("Segoe UI", 8)).pack(anchor="w")
        bar_bg = tk.Frame(dias_frame, bg=COLORES["card_alt"], height=6, width=200)
        bar_bg.pack(anchor="w", pady=(2, 0))
        color_riesgo = COLORES["verde"] if dias_pct < 0.3 else COLORES["naranja"] if dias_pct < 0.6 else COLORES["rojo"]
        bar_fill = tk.Frame(bar_bg, bg=color_riesgo, height=6, width=int(200 * dias_pct))
        bar_fill.place(x=0, y=0)

        btn = tk.Button(card, text="Ofrecer Bono de Retorno",
                        bg=COLORES["naranja"], fg=COLORES["fondo"],
                        font=("Segoe UI", 9, "bold"), bd=0, padx=14, pady=4,
                        activebackground=COLORES["sidebar_hover"],
                        cursor="hand2",
                        command=lambda n=jugador["nombre"]: self._ofrecer_bono(n))
        btn.pack(anchor="e", pady=(8, 0))
        return card

    def _ofrecer_bono(self, nombre):
        from tkinter import messagebox
        confirmar = messagebox.askquestion("Confirmar Bono",
                                            f"\u00bfEst\u00e1 seguro de ofrecer bono de retorno a {nombre}?")
        if confirmar == "yes":
            messagebox.showinfo("Bono Ofrecido",
                                f"Bono de retorno ofrecido a {nombre}.")
