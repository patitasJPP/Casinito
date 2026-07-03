import tkinter as tk
from tkinter import ttk
from pathlib import Path
from config import COLORES


class VentanaReporte:
    def __init__(self, padre, jugador):
        self.ventana = tk.Toplevel(padre)
        self.ventana.title(f"Reporte Detallado - {jugador['nombre']}")
        self.ventana.geometry("550x500")
        self.ventana.configure(bg=COLORES["fondo"])
        self.ventana.resizable(False, False)

        header = tk.Frame(self.ventana, bg=COLORES["card_bg"], padx=20, pady=16)
        header.pack(fill=tk.X)

        tk.Label(header, text=jugador["nombre"],
                 bg=COLORES["card_bg"], fg=COLORES["oro"],
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")

        tag_color = {"VIP": COLORES["oro"], "Retener": COLORES["naranja"],
                     "Cuidar": COLORES["rojo"], "Servicio_Rapido": COLORES["verde"]}
        color = tag_color.get(jugador["clasificacion"], COLORES["texto_sec"])
        tk.Label(header, text=jugador["clasificacion"],
                 bg=color, fg=COLORES["fondo"],
                 font=("Segoe UI", 10, "bold"), padx=14, pady=3).pack(anchor="w", pady=(6, 0))

        canvas = tk.Canvas(self.ventana, bg=COLORES["fondo"], highlightthickness=0)
        scroll = ttk.Scrollbar(self.ventana, orient="vertical", command=canvas.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas.configure(yscrollcommand=scroll.set)

        interior = tk.Frame(canvas, bg=COLORES["fondo"], padx=20, pady=10)
        canvas.create_window((0, 0), window=interior, anchor="nw")

        def _conf(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        interior.bind("<Configure>", _conf)

        categorias = [
            ("Identificacion", [
                ("Edad", jugador["edad"]), ("Ocupacion", jugador["ocupacion"]),
            ]),
            ("Economico", [
                ("Presupuesto Hoy", f"S/ {jugador['presupuesto_hoy']}"),
                ("Gasto Hoy", f"S/ {jugador['gasto_hoy']}"),
                ("Perdidas Acum.", f"S/ {jugador['perdidas_acumuladas']}"),
                ("Ganancias Acum.", f"S/ {jugador['ganancias_acumuladas']}"),
                ("Balance", f"S/ {jugador['ganancias_acumuladas'] - jugador['perdidas_acumuladas']}"),
            ]),
            ("Comportamiento", [
                ("Frecuencia", f"{jugador['frecuencia_semanal']}x/sem"),
                ("Juego Favorito", jugador["juego_favorito"]),
                ("Total Visitas", jugador["total_visitas"]),
            ]),
        ]

        for cat, campos in categorias:
            marco = tk.LabelFrame(interior, text=cat, padx=14, pady=10,
                                  bg=COLORES["card_bg"], fg=COLORES["oro"],
                                  font=("Segoe UI", 10, "bold"),
                                  highlightbackground=COLORES["border"],
                                  highlightthickness=1)
            marco.pack(fill=tk.X, pady=(0, 10))
            for label, valor in campos:
                fila = tk.Frame(marco, bg=COLORES["card_bg"])
                fila.pack(fill=tk.X, pady=2)
                tk.Label(fila, text=label, bg=COLORES["card_bg"],
                         fg=COLORES["texto_sec"], font=("Segoe UI", 9),
                         width=20, anchor="w").pack(side=tk.LEFT)
                tk.Label(fila, text=str(valor), bg=COLORES["card_bg"],
                         fg=COLORES["texto"], font=("Segoe UI", 11, "bold"),
                         anchor="w").pack(side=tk.LEFT, padx=(10, 0))

        btn_cerrar = tk.Button(self.ventana, text="Cerrar",
                               bg=COLORES["oro"], fg=COLORES["fondo"],
                               font=("Segoe UI", 10, "bold"), bd=0,
                               padx=20, pady=6, cursor="hand2",
                               command=self.ventana.destroy)
        btn_cerrar.pack(pady=(0, 14))
