import tkinter as tk
from config import COLORES
from ui.panel_base import PanelBase
from data.jugadores import obtener_todos
from data.analisis import resumen_estadistico


class PanelDashboard:
    def __init__(self, padre):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.jugadores = obtener_todos()

        PanelBase._crear_header(self.frame, "Dashboard",
                                "Resumen general del estado del casino y los jugadores.")

        body = PanelBase._crear_body_scroll(self.frame)

        stats = resumen_estadistico(self.jugadores)

        cards_data = [
            ("\u25c9", "Total Jugadores", stats["total"], COLORES["texto"], ""),
            ("\u2605", "VIP", stats["vip_count"], COLORES["oro"],
             f"{stats['vip_count']/max(stats['total'],1)*100:.0f}% del total"),
            ("\u25b2", "En Riesgo", stats["retener_count"], COLORES["naranja"],
             f"{stats['retener_count']/max(stats['total'],1)*100:.0f}% del total"),
            ("\u25a0", "A Cuidar", stats["cuidar_count"], COLORES["rojo"],
             f"{stats['cuidar_count']/max(stats['total'],1)*100:.0f}% del total"),
            ("\u25b6", "Serv. R\u00e1pido", stats["rapido_count"], COLORES["verde"],
             f"{stats['rapido_count']/max(stats['total'],1)*100:.0f}% del total"),
            ("$", "Gasto Hoy", f"S/ {stats['total_gasto']}", COLORES["texto"], ""),
        ]
        PanelBase._crear_kpi_cards_grid(body, cards_data)

        graf = PanelBase._crear_card_contenedor(
            body, "Distribuci\u00f3n de Clasificaciones",
            "Proporci\u00f3n de cada tipo de jugador en el sistema"
        )
        self._crear_barras_distribucion(graf, stats)

        fin = PanelBase._crear_card_contenedor(
            body, "Resumen Financiero",
            "M\u00e9tricas econ\u00f3micas generales del casino"
        )
        self._crear_resumen_financiero(fin, stats)

    def _crear_barras_distribucion(self, parent, stats):
        barras = tk.Frame(parent, bg=COLORES["card_bg"])
        barras.pack(fill=tk.X, padx=20, pady=(0, 18))

        clasifs = [
            ("VIP", stats["vip_count"], COLORES["oro"]),
            ("Retener", stats["retener_count"], COLORES["naranja"]),
            ("Cuidar", stats["cuidar_count"], COLORES["rojo"]),
            ("R\u00e1pido", stats["rapido_count"], COLORES["verde"]),
        ]
        max_val = max((c[1] for c in clasifs), default=1)

        rows = []
        for label, val, color in clasifs:
            row = tk.Frame(barras, bg=COLORES["card_bg"])
            row.pack(fill=tk.X, pady=4)
            rows.append(row)

            tk.Label(row, text=label, bg=COLORES["card_bg"], fg=COLORES["texto"],
                     font=("Segoe UI", 10), width=10, anchor="w").pack(side=tk.LEFT)

            bar_bg = tk.Frame(row, bg=COLORES["card_alt"], height=24)
            bar_bg.pack(side=tk.LEFT, padx=(0, 12), fill=tk.X, expand=True)

            proporcion = val / max_val if max_val > 0 else 0
            ancho_inicial = max(int(400 * proporcion), 1) if val > 0 else 0
            bar_fill = tk.Frame(bar_bg, bg=color, height=24, width=ancho_inicial)
            bar_fill.place(x=0, y=0)

            tk.Label(row, text=str(val), bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 12, "bold"), width=3).pack(side=tk.LEFT)

            pct = proporcion * 100
            tk.Label(row, text=f"{pct:.0f}%", bg=COLORES["card_bg"],
                     fg=COLORES["texto_dim"], font=("Segoe UI", 9), width=4).pack(side=tk.LEFT)

            row.bar_bg = bar_bg
            row.val = val
            row.max_val = max_val

        def _reflow_barras(event=None):
            ancho = barras.winfo_width()
            ancho_barra = max(200, min(400, ancho - 160))
            for row in rows:
                if row.max_val > 0:
                    bar_w = int(ancho_barra * (row.val / row.max_val))
                    row.bar_bg.configure(width=ancho_barra)
                    for child in row.bar_bg.winfo_children():
                        child.configure(width=max(bar_w, 1) if bar_w > 0 else 0)

        barras.after(100, _reflow_barras)
        barras.bind("<Configure>", _reflow_barras)

    def _crear_resumen_financiero(self, parent, stats):
        fin_data = tk.Frame(parent, bg=COLORES["card_bg"])
        fin_data.pack(fill=tk.X, padx=20, pady=(8, 16))
        fin_data.grid_columnconfigure((0, 1, 2, 3), weight=1, uniform="fin")

        items_fin = [
            ("Gasto Total Hoy", f"S/ {stats['total_gasto']}", COLORES["texto"]),
            ("P\u00e9rdidas Totales", f"S/ {stats['total_perdidas']}", COLORES["rojo"]),
            ("Ganancias Totales", f"S/ {stats['total_ganancias']}", COLORES["verde"]),
            ("Balance", f"S/ {stats['balance']}",
             COLORES["verde"] if stats['balance'] >= 0 else COLORES["rojo"]),
        ]
        for i, (lbl, val, color) in enumerate(items_fin):
            c = tk.Frame(fin_data, bg=COLORES["card_bg"], padx=12)
            c.grid(row=0, column=i, sticky="nsew")
            tk.Label(c, text=lbl, bg=COLORES["card_bg"], fg=COLORES["texto_sec"],
                     font=("Segoe UI", 9)).pack(anchor="center")
            tk.Label(c, text=val, bg=COLORES["card_bg"], fg=color,
                     font=("Segoe UI", 18, "bold")).pack(anchor="center")
