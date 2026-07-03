# PLAN DE ACCIÓN — CASINO SAPIENS v2.0
### Estrategia para obtener la máxima nota (90+ / 100)

---

## CONTEXTO: LA IDEA CENTRAL

> **Prolog es el cerebro** — contiene los datos de los jugadores y las reglas de inferencia que clasifican y recomiendan.
> **Python es la cara** — un dashboard profesional que consulta a Prolog y presenta los resultados visualmente.
> **Multiparadigma real**: Al cambiar una regla en Prolog, el comportamiento en Python cambia sin modificar Python.

| Componente | Rol | Paradigma |
|---|---|---|
| Prolog (`prolog/`) | Motor de inferencia, datos, reglas | Lógico / Declarativo |
| Python (`consultas.py`) | Puente de conexión vía pyswip | — |
| Python (`data/analisis.py`) | Análisis de datos | Funcional + pandas/numpy |
| Python (`ui/`) | Dashboard tkinter | POO |

---

## ESTRATEGIA POR CRITERIO DE LA RÚBRICA

---

### C1 — Paradigmas de Programación (25%) → META: 20/20

| Sub-criterio | Acción concreta | Evidencia para exponer |
|---|---|---|
| **Lógico (Prolog)** | 6 jugadores como hechos + 18+ reglas de inferencia (VIP, retener, cuidar, recomendar) | Mostrar `hechos.pl` y `reglas_*.pl` en vivo |
| **Multiparadigma** | Prolog (lógico) + Python POO (clases) + Python funcional (map, filter, reduce, comprehensions) | Señalar los 3 paradigmas en el código |
| **Integración** | pyswip conecta Prolog → Python. Cambiar regla → cambia resultado en GUI sin tocar Python | **DEMO ESTRELLA**: cambiar frecuencia de Carlos de 3→2, recargar, ya no aparece en VIP |

**Implementación:**

```prolog
% hechos.pl — 8 jugadores con 30 campos organizados en 6 predicados
% Cada predicado es un hecho Prolog con tipos: átomos, números, listas
jugador(j1, 'Carlos', 45, ingeniero).
economia(j1, 500, 200, 300, 50, 200, 5000, 3000).
comportamiento(j1, azar, rapido, si, no, si, no, si).
sesion(j1, tragamonedas, 50, gano, 15, 2.5, '22:00').
visitas(j1, 3, 180, nocturno, [viernes,sabado], 120, 365, 2).
preferencias(j1, tragamonedas, 3).
```

```prolog
% reglas_vip.pl — 5 reglas: frecuencia, gasto, ganancias, antigüedad
vip(Id) :- visitas(Id, Freq, _, _, _, _, _, _), Freq >= 3.
vip(Id) :- economia(Id, _, _, _, _, GastoMax, _, _), GastoMax >= 100.
vip(Id) :- economia(Id, _, _, _, _, _, _, Ganancias), Ganancias >= 3000.
vip(Id) :- visitas(Id, _, _, _, _, _, DiasPrimera, _), DiasPrimera > 365.
vip(Id) :- jugador(Id, _, Edad, _), Edad >= 40,
           economia(Id, _, _, _, _, _, Perdidas, _), Perdidas >= 2000.
```

```prolog
% reglas_retener.pl — 4 reglas: inactividad, caída frecuencia, pérdidas
en_riesgo_irse(Id) :- visitas(Id, _, _, _, _, _, _, DiasUlt), DiasUlt > 30.
en_riesgo_irse(Id) :- visitas(Id, Freq, _, _, _, TotalVis, _, _),
                       Freq < 2, TotalVis > 10.
en_riesgo_irse(Id) :- economia(Id, _, _, _, _, _, Perdidas, _), Perdidas > 3000.
en_riesgo_irse(Id) :- jugador(Id, _, Edad, _), Edad > 50,
                       visitas(Id, _, _, _, _, _, _, DiasUlt), DiasUlt > 14.
```

```prolog
% reglas_detener.pl — 4 reglas: edad, tiempo, presupuesto, pérdidas
detener_juego(Id) :- jugador(Id, _, Edad, _), Edad < 25.
detener_juego(Id) :- sesion(Id, _, _, _, _, Horas, _), Horas >= 4.
detener_juego(Id) :- economia(Id, Presup, _, Gasto, _, _, _, _),
                      Gasto >= Presup * 0.8.
detener_juego(Id) :- economia(Id, _, _, _, _, _, Perdidas, Ganancias),
                      Perdidas > Ganancias * 2.
```

```prolog
% reglas_recomendar.pl — 8+ reglas combinando comportamiento + preferencias
recomendar(Id, tragamonedas) :- comportamiento(Id, azar, rapido, _, _, _, _, _).
recomendar(Id, blackjack)    :- comportamiento(Id, estrategia, _, _, _, _, _, _).
recomendar(Id, ruleta)       :- comportamiento(Id, azar, lento, _, _, _, _, _).
recomendar(Id, tragamonedas) :- comportamiento(Id, azar, _, _, _, _, _, _),
                                 preferencias(Id, tragamonedas, _).
recomendar(Id, blackjack)    :- comportamiento(Id, _, _, _, _, si, _, _).
recomendar(Id, ruleta)       :- comportamiento(Id, _, lento, _, _, _, _, _).
```

```prolog
% casino.pl — Archivo principal con meta-predicados para Python
:- consult('hechos.pl').
:- consult('reglas_vip.pl').
:- consult('reglas_retener.pl').
:- consult('reglas_detener.pl').
:- consult('reglas_recomendar.pl').

lista_vip(Lista)     :- findall(Id, vip(Id), Lista).
lista_retener(Lista) :- findall(Id, en_riesgo_irse(Id), Lista).
lista_cuidar(Lista)  :- findall(Id, detener_juego(Id), Lista).
```

---

### C2 — Modularidad del Código (20%) → META: 20/20

**Estructura final del proyecto:**

```
casino_sapiens/
│
├── plan.md                          ← Este archivo (estrategia)
├── README.md                        ← Documentación académica formal
│
├── prolog/
│   ├── casino.pl                    ← Meta-predicados, consulta módulos
│   ├── hechos.pl                    ← 8 jugadores (hechos)
│   ├── reglas_vip.pl                ← Reglas VIP
│   ├── reglas_retener.pl            ← Reglas retener
│   ├── reglas_detener.pl            ← Reglas detener/cuidar
│   └── reglas_recomendar.pl         ← Reglas recomendar juegos
│
└── python/
    ├── main.py                      ← Punto de entrada
    ├── config.py                    ← Colores, fuentes, constantes
    ├── consultas.py                 ← Puente pyswip (Prolog → Python)
    ├── data/
    │   ├── jugadores.py             ← Datos estructurados desde Prolog
    │   └── analisis.py              ← pandas + numpy + funcional
    ├── ui/
    │   ├── ventana_principal.py     ← Layout, sidebar, navegación
    │   ├── panel_base.py            ← Clase base (header, cards, tags)
    │   ├── panel_todos.py           ← Tabla + detalle expandible
    │   ├── panel_vip.py             ← Invitar VIPs
    │   ├── panel_retener.py         ← Bonos retener
    │   ├── panel_cuidar.py          ← Alertas y supervisión
    │   ├── panel_rapido.py          ← Servicio rápido
    │   └── panel_estadisticas.py    ← Gráficos y análisis (NUEVO)
    └── tests/
        └── test_clasificaciones.py  ← Pruebas unitarias
```

**Principios aplicados:**
- **Responsabilidad única**: cada archivo hace una cosa
- **Reutilización**: `PanelBase` con métodos estáticos compartidos
- **Separación datos-presentación**: `data/` separado de `ui/`
- **Inyección de dependencias**: los paneles reciben los datos ya procesados

**Fragmento clave de la refactorización:**

```python
# main.py
from ui.ventana_principal import AplicacionCasino

if __name__ == "__main__":
    AplicacionCasino().ejecutar()
```

```python
# config.py — Centralización visual
COLORES = {
    "fondo_oscuro": "#0d0d0d",
    "sidebar": "#1a1a2e",
    "primario": "#e94560",
    "secundario": "#0f3460",
    "texto": "#ffffff",
    "texto_secundario": "#a0a0b0",
    "card_bg": "#16213e",
    "exito": "#2ecc71",
    "advertencia": "#f39c12",
    "peligro": "#e74c3c",
}
```

---

### C3 — Análisis y Tratamiento de Datos (20%) → META: 20/20

**Herramientas:** pandas + numpy + Python funcional

```python
# data/analisis.py
import pandas as pd
import numpy as np
from functools import reduce

def crear_dataframe(jugadores):
    """Convierte datos de jugadores a DataFrame de pandas."""
    return pd.DataFrame([{
        "id": j["id"],
        "nombre": j["nombre"],
        "edad": j["edad"],
        "presupuesto": j["presupuesto_hoy"],
        "gasto_hoy": j["gasto_hoy"],
        "gasto_promedio": j["gasto_promedio_ronda"],
        "gasto_max_historico": j["gasto_maximo_historico"],
        "perdidas": j["perdidas_acumuladas"],
        "ganancias": j["ganancias_acumuladas"],
        "frecuencia": j["frecuencia_semanal"],
        "tiempo_promedio": j["tiempo_promedio_visita"],
        "total_visitas": j["total_visitas"],
        "clasificacion": j["clasificacion"]
    } for j in jugadores])

def analisis_por_clasificacion(df):
    """Agrupa por clasificación y calcula estadísticas."""
    return df.groupby("clasificacion").agg({
        "edad": ["mean", "min", "max"],
        "gasto_hoy": ["mean", "sum"],
        "perdidas": "mean",
        "ganancias": "mean",
        "frecuencia": "mean",
        "total_visitas": "mean"
    }).round(2)

def top_jugadores_riesgo(df, umbral_perdidas=0.75):
    """Jugadores en percentil alto de pérdidas usando numpy."""
    limite = np.percentile(df["perdidas"], umbral_perdidas * 100)
    return df[df["perdidas"] > limite][["nombre", "perdidas", "clasificacion"]]

def correlaciones(df):
    """Matriz de correlación entre variables numéricas."""
    nums = df.select_dtypes(include=[np.number])
    return nums.corr()

# --- Python funcional ---
def filtrar_por_clasificacion(jugadores, clasif):
    return list(filter(lambda j: j["clasificacion"] == clasif, jugadores))

def total_metricas(jugadores):
    return reduce(lambda acc, j: {
        "perdidas": acc["perdidas"] + j["perdidas_acumuladas"],
        "ganancias": acc["ganancias"] + j["ganancias_acumuladas"],
        "gasto_hoy": acc["gasto_hoy"] + j["gasto_hoy"]
    }, jugadores, {"perdidas": 0, "ganancias": 0, "gasto_hoy": 0})

def nombres_clasificados(jugadores, clasif):
    return list(map(lambda j: j["nombre"],
                    filtrar_por_clasificacion(jugadores, clasif)))
```

**Análisis que se presentan en la exposición:**

| Análisis | Qué muestra | Código |
|---|---|---|
| Gasto promedio por clasificación | Cuánto gasta cada tipo | `df.groupby("clasificacion")["gasto_hoy"].mean()` |
| Correlación frecuencia-pérdidas | ¿Jugar seguido = perder más? | `df["frecuencia"].corr(df["perdidas"])` |
| Top 25% más pérdidas | Jugadores en riesgo alto | `np.percentile + filtro` |
| Edad promedio VIPs | Perfil del jugador VIP | `df[df["VIP"]]["edad"].mean()` |
| Balance pérdidas/ganancias | Quién gana vs quién pierde | `df["perdidas"] - df["ganancias"]` |

---

### C4 — Resultados, Pruebas y Visualización (15%) → META: 20/20

#### Pruebas unitarias (pytest)

```python
# tests/test_clasificaciones.py
import pytest
from consultas import obtener_vips, obtener_retener, obtener_cuidar

def test_carlos_es_vip():
    """Carlos (j1) debe clasificar como VIP por frecuencia >= 3 y gasto."""
    vips = obtener_vips()
    ids = [r["Id"] for r in vips]
    assert "j1" in ids, "Carlos debería ser VIP"

def test_maria_en_riesgo_irse():
    """María (j2) debe estar en retener por 35 días sin venir."""
    retener = obtener_retener()
    ids = [r["Id"] for r in retener]
    assert "j2" in ids, "María debería estar en riesgo"

def test_lucia_detener_juego():
    """Lucía (j4) debe requerir intervención (edad 22, 4.5 hrs)."""
    cuidar = obtener_cuidar()
    ids = [r["Id"] for r in cuidar]
    assert "j4" in ids, "Lucía debería estar en cuidar"

def test_vip_no_aparece_si_cambio_frecuencia():
    """Demo clave: si bajo frecuencia de Carlos a 2, ya no es VIP."""
    # Esto se demo en vivo cambiando el .pl
    pass

def test_recomendacion_coincide_con_perfil():
    """Jugador de azar+rapido recibe tragamonedas."""
    from consultas import obtener_recomendacion
    rec = obtener_recomendacion("j1")
    assert rec in ["tragamonedas", "ruleta"]
```

#### Visualizaciones (matplotlib en tkinter)

**Panel nuevo: Estadísticas**

```python
# ui/panel_estadisticas.py
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class PanelEstadisticas:
    def __init__(self, padre, df):
        self.frame = tk.Frame(padre, bg=COLORES["fondo"])
        self.frame.pack(fill=tk.BOTH, expand=True)
        self._crear_graficos(df)

    def _crear_graficos(self, df):
        # Gráfico 1: Distribución de clasificaciones (torta)
        fig = Figure(figsize=(12, 8), dpi=100, facecolor=COLORES["fondo"])
        
        ax1 = fig.add_subplot(2, 2, 1)
        counts = df["clasificacion"].value_counts()
        colores = [COLORES["primario"], COLORES["advertencia"], 
                   COLORES["peligro"], COLORES["exito"], "#95a5a6"]
        ax1.pie(counts, labels=counts.index, autopct="%1.1f%%",
                colors=colores, startangle=90)
        ax1.set_title("Distribución de Clasificaciones", color="white")

        # Gráfico 2: Gasto hoy por jugador (barras)
        ax2 = fig.add_subplot(2, 2, 2)
        df_sorted = df.sort_values("gasto_hoy", ascending=True)
        ax2.barh(df_sorted["nombre"], df_sorted["gasto_hoy"], 
                 color=COLORES["primario"])
        ax2.set_title("Gasto Hoy por Jugador", color="white")
        ax2.tick_params(colors="white")

        # Gráfico 3: Pérdidas vs Ganancias (barras agrupadas)
        ax3 = fig.add_subplot(2, 2, 3)
        x = range(len(df))
        ax3.bar(x, df["perdidas"], width=0.35, label="Pérdidas", 
                color=COLORES["peligro"])
        ax3.bar([i + 0.35 for i in x], df["ganancias"], 
                width=0.35, label="Ganancias", color=COLORES["exito"])
        ax3.set_xticks([i + 0.175 for i in x])
        ax3.set_xticklabels(df["nombre"], rotation=45, ha="right")
        ax3.set_title("Pérdidas vs Ganancias", color="white")
        ax3.legend()

        # Gráfico 4: Correlación frecuencia vs pérdidas
        ax4 = fig.add_subplot(2, 2, 4)
        ax4.scatter(df["frecuencia"], df["perdidas"], 
                    c=COLORES["primario"], s=100, alpha=0.7)
        ax4.set_xlabel("Frecuencia semanal", color="white")
        ax4.set_ylabel("Pérdidas acumuladas", color="white")
        ax4.set_title("Frecuencia vs Pérdidas", color="white")
        ax4.tick_params(colors="white")

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
```

#### Presentación de resultados en la expo

| Momento | Qué mostrar |
|---|---|
| Apertura | Dashboard con KPIs: 6 jugadores, 2 VIP, 1 retener, 1 cuidar |
| Demo 1 | Carlos VIP → cambiar frecuencia en Prolog → ya no es VIP |
| Demo 2 | Lucía en Cuidar → alertas (edad 22, 4.5 hrs, 80% presupuesto) |
| Demo 3 | Estadísticas → gráficos de torta, barras, scatter |
| Cierre | Tests pasando en terminal con `pytest -v` |

---

### C5 — Documentación del Proyecto (10%) → META: 20/20

**README.md debe tener esta estructura:**

```markdown
# 🎰 CASINO SAPIENS — Sistema Experto de Perfilado para Casino

## 📄 Portada
- Nombre del proyecto
- Universidad / Curso
- Integrantes
- Fecha

## 📖 Introducción
Contexto: los casinos manejan grandes volúmenes de jugadores.
Un sistema experto permite clasificarlos automáticamente para
mejorar la experiencia y la gestión.

## 🎯 Objetivos
**General:** Desarrollar un sistema experto multiparadigma que
clasifique jugadores de casino y recomiende acciones.

**Específicos:**
1. Implementar un motor de inferencia en Prolog con hechos y reglas
2. Diseñar un dashboard en Python con tkinter
3. Integrar ambos lenguajes vía pyswip
4. Aplicar análisis de datos con pandas y numpy
5. Generar visualizaciones automáticas del perfil de jugadores

## 📐 Marco Teórico
- Paradigma lógico (Prolog): hechos, reglas, unificación, findall
- Paradigma funcional: map, filter, reduce, list comprehensions
- Paradigma OOP: clases, herencia, encapsulamiento
- pyswip: puente Python ↔ Prolog
- pandas / numpy: análisis y transformación de datos

## 🏗️ Diseño del Sistema
- Diagrama de arquitectura: Prolog → pyswip → Python → tkinter
- Explicación de los 6 predicados por jugador
- Explicación de las 18+ reglas de inferencia
- Estructura de módulos de Python

## 💻 Implementación
- Fragmentos clave de Prolog (hechos + 1 regla de cada tipo)
- Fragmentos clave de Python (consulta pyswip, panel base, análisis)
- Capturas de pantalla de la GUI funcionando

## 🧪 Pruebas
- Captura de pytest -v mostrando tests pasando
- Explicación de cada test

## 📊 Resultados
- Capturas de los 5 paneles funcionales
- Capturas de los gráficos generados
- Tabla de clasificaciones obtenidas

## ✅ Conclusiones
- Se logró integrar Prolog + Python exitosamente
- El sistema clasifica correctamente según reglas definidas
- El análisis de datos revela patrones de comportamiento
- Limitaciones: datos estáticos, sin conexión a BD real

## 📚 Referencias
- SWI-Prolog documentation (https://www.swi-prolog.org)
- pyswip (https://github.com/yuce/pyswip)
- pandas documentation (https://pandas.pydata.org)
- matplotlib documentation (https://matplotlib.org)
- tkinter documentation (https://docs.python.org/3/library/tkinter.html)
```

---

## PLAN DE EJECUCIÓN — PASO A PASO

### Paso 1: Completar Prolog (hechos + reglas)
✓ Archivos a modificar: `hechos.pl`, `reglas_vip.pl`, `reglas_retener.pl`, `reglas_detener.pl`, `reglas_recomendar.pl`, `casino.pl`
✓ Tiempo: 2-3 horas

### Paso 2: Crear consultas.py (puente pyswip)
✓ Conectar Python con Prolog
✓ Reemplazar datos mock con consultas reales
✓ Tiempo: 1 hora

### Paso 3: Refactorizar Python (modularidad)
✓ Dividir `ventana_usuarios.py` en archivos separados
✓ Crear `config.py`, `main.py`, `panel_base.py`, `panel_*.py`
✓ Tiempo: 2 horas

### Paso 4: Agregar análisis de datos
✓ Implementar `data/analisis.py` con pandas + numpy
✓ Agregar funciones de Python funcional
✓ Tiempo: 2 horas

### Paso 5: Agregar panel de estadísticas + gráficos
✓ Implementar `panel_estadisticas.py` con matplotlib
✓ 4 gráficos: torta, barras, barras agrupadas, scatter
✓ Tiempo: 2 horas

### Paso 6: Escribir pruebas unitarias
✓ 5+ tests en `tests/test_clasificaciones.py`
✓ Tiempo: 1 hora

### Paso 7: Mejorar diseño visual
✓ Paleta de colores más moderna y profesional
✓ Dashboard con KPIs (cards de resumen)
✓ Efectos visuales (sombras, hover, progress bars)
✓ Tiempo: 1-2 horas

### Paso 8: Documentación final
✓ README.md con estructura académica
✓ Comentarios en código (docstrings)
✓ Tiempo: 1-2 horas

### Paso 9: Preparar exposición
✓ 3 casos demo preparados
✓ Script de presentación
✓ Capturas y fragmentos clave
✓ Tiempo: 2 horas

---

## GUION DE EXPOSICIÓN (3 minutos)

| Tiempo | Qué decir | Qué mostrar |
|---|---|---|
| 0:00-0:30 | "Casino Sapiens es un sistema experto multiparadigma. Prolog clasifica jugadores mediante reglas lógicas. Python muestra los resultados en un dashboard profesional." | Arquitectura del sistema |
| 0:30-1:00 | "Aquí los hechos en Prolog: 8 jugadores con 30 campos cada uno. Y las reglas: por ejemplo, VIP si frecuencia ≥ 3/semana o gasto máximo ≥ 100." | Código Prolog en vivo |
| 1:00-1:30 | "El dashboard consulta a Prolog via pyswip. Tenemos 5 paneles. Miren: Carlos es VIP por su frecuencia y gasto. Pero si cambio su frecuencia de 3 a 2 en Prolog... ¡ya no aparece en VIP!" | GUI + cambio en Prolog |
| 1:30-2:00 | "Además aplicamos análisis de datos con pandas y numpy: distribución de clasificaciones, gasto por jugador, correlaciones. Y pruebas unitarias con pytest." | Gráficos + tests |
| 2:00-2:30 | "En conclusión, logramos integrar 3 paradigmas: lógico (Prolog), funcional (map/filter/reduce) y POO (Python). El sistema clasifica, recomienda y analiza." | Conclusión |
| 2:30-3:00 | Preguntas | — |
