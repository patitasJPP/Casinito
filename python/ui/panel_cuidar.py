import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import CUIDAR


class PanelCuidar:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        cuidar = CUIDAR

        PanelBase._crear_header(self.frame, "Personas a Cuidar",
                                f"{len(cuidar)} jugador(es) que requieren supervisi\u00f3n. Intervenir para juego responsable.")
        body = PanelBase._crear_body_scroll(self.frame)
        PanelBase._crear_grid_tarjetas(body, cuidar, 3, self._crear_tarjeta_cuidar)

    def _crear_tarjeta_cuidar(self, padre, jugador):
        card = tk.Frame(padre, bg=COLORES["card_bg"],
                        highlightbackground=COLORES["rojo"], highlightthickness=1, padx=14, pady=12)
        PanelBase._aplicar_hover_card(card, COLORES["rojo"])

        sup = tk.Frame(card, bg=COLORES["card_bg"])
        sup.pack(fill=tk.X)
        tk.Label(sup, text="\u25a0", bg=COLORES["card_bg"], fg=COLORES["rojo"],
                 font=("Segoe UI", 14)).pack(side=tk.LEFT, padx=(0, 6))
        tk.Label(sup, text=jugador["nombre"], bg=COLORES["card_bg"],
                 fg=COLORES["texto"], font=("Segoe UI", 13, "bold")).pack(side=tk.LEFT)
        lbl_tag = tk.Label(sup, text="Cuidar", bg=COLORES["rojo"], fg=COLORES["blanco"],
                           font=("Segoe UI", 8, "bold"), padx=8, pady=2)
        lbl_tag.pack(side=tk.LEFT, padx=(6, 0))

        alertas = []
        if jugador["edad"] <= 22:
            alertas.append(("Edad joven", "Monitorear tiempo de juego", COLORES["rojo"]))
        if jugador["tiempo_en_casino_hoy"] >= 4:
            alertas.append(("Tiempo excesivo", f"{jugador['tiempo_en_casino_hoy']} hrs hoy - sugerir descanso", COLORES["rojo"]))
        if jugador["gasto_hoy"] >= jugador["presupuesto_hoy"] * 0.8:
            alertas.append(("Presupuesto agotado", "Gast\u00f3 m\u00e1s del 80% - monitorear", COLORES["naranja"]))
        if jugador["perdidas_acumuladas"] > jugador["ganancias_acumuladas"] * 2:
            alertas.append(("P\u00e9rdidas altas", "P\u00e9rdidas superan ganancias significativamente", COLORES["naranja"]))

        info = tk.Frame(card, bg=COLORES["card_bg"])
        info.pack(fill=tk.X, pady=(6, 0))

        datos = [
            ("Edad", jugador["edad"]),
            ("Tiempo Hoy", f"{jugador['tiempo_en_casino_hoy']} hrs"),
            ("Presupuesto", f"S/ {jugador['presupuesto_hoy']}"),
            ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
            ("Rondas Hoy", jugador["rondas_jugadas_hoy"]),
            ("Perdidas Acum.", f"S/ {jugador['perdidas_acumuladas']}"),
        ]
        for i, (l, v) in enumerate(datos):
            sub = tk.Frame(info, bg=COLORES["card_bg"], padx=4, pady=1)
            sub.grid(row=i // 3, column=i % 3, sticky="w")
            tk.Label(sub, text=l, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 7)).pack(anchor="w")
            tk.Label(sub, text=v, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10, "bold")).pack(anchor="w")

        if alertas:
            alert_frame = tk.Frame(card, bg=COLORES["alerta_bg"], padx=10, pady=8)
            alert_frame.pack(fill=tk.X, pady=(6, 0))
            for titulo, msg, color in alertas:
                row_a = tk.Frame(alert_frame, bg=COLORES["alerta_bg"])
                row_a.pack(fill=tk.X, pady=1)
                tk.Label(row_a, text="\u25cf", bg=COLORES["alerta_bg"], fg=color,
                         font=("Segoe UI", 7)).pack(side=tk.LEFT, padx=(0, 4))
                tk.Label(row_a, text=f"{titulo}: {msg}", bg=COLORES["alerta_bg"], fg=COLORES["texto"],
                         font=("Segoe UI", 8), anchor="w").pack(side=tk.LEFT)

        btn_frame = tk.Frame(card, bg=COLORES["card_bg"])
        btn_frame.pack(fill=tk.X, pady=(6, 0))
        tk.Button(btn_frame, text="Sugerir Descanso",
                  bg=COLORES["rojo"], fg=COLORES["blanco"],
                  font=("Segoe UI", 8, "bold"), bd=0, padx=10, pady=4,
                  cursor="hand2",
                  command=lambda n=jugador["nombre"]: self._sugerir_descanso(n)).pack(side=tk.LEFT, padx=(0, 6))
        tk.Button(btn_frame, text="Registrar Interv.",
                  bg=COLORES["texto_dim"], fg=COLORES["texto"],
                  font=("Segoe UI", 8), bd=0, padx=10, pady=4,
                  cursor="hand2",
                  command=lambda n=jugador["nombre"]: self._registrar_intervencion(n)).pack(side=tk.LEFT)
        return card

    def _sugerir_descanso(self, nombre):
        from tkinter import messagebox
        messagebox.showwarning("Alerta de Juego Responsable",
                                f"{nombre} ha estado jugando por mucho tiempo. Sugerencia de descanso enviada.")

    def _registrar_intervencion(self, nombre):
        from tkinter import messagebox
        messagebox.showinfo("Intervenci\u00f3n Registrada",
                            f"Intervenci\u00f3n con {nombre} registrada en el sistema.")
