# ◆ CASINO SAPIENS — Sistema Experto de Perfilado para Casino

**Universidad:** [Nombre de la universidad]  
**Curso:** [Nombre del curso]  
**Integrantes:** [Nombres de los integrantes]  
**Fecha:** Junio 2026  

---

## 📖 Introducción

Los casinos manejan grandes volúmenes de jugadores con perfiles, comportamientos y necesidades muy distintas. Clasificarlos manualmente es ineficiente y propenso a errores. **Casino Sapiens** es un sistema experto multiparadigma que automatiza la clasificación de jugadores usando un motor de inferencia en Prolog y un dashboard interactivo en Python, demostrando la integración de los paradigmas lógico, funcional y orientado a objetos.

---

## 🎯 Objetivos

### General
Desarrollar un sistema experto multiparadigma que clasifique jugadores de casino en categorías (VIP, Retener, Cuidar, Servicio Rápido) y recomiende acciones personalizadas, integrando Prolog como motor de inferencia y Python como interfaz de visualización.

### Específicos
1. Implementar una base de hechos en Prolog con 8 jugadores y 30 campos descriptivos cada uno.
2. Codificar 22+ reglas de inferencia en Prolog para clasificación y recomendación.
3. Diseñar un dashboard profesional en Python con tkinter y tema oscuro premium.
4. Integrar ambos lenguajes mediante pyswip para que Python consulte a Prolog en tiempo real.
5. Aplicar análisis de datos con pandas y numpy sobre los perfiles de jugadores.
6. Incorporar programación funcional (map, filter, reduce, comprehensions) en el pipeline de datos.
7. Generar visualizaciones y pruebas unitarias que validen el comportamiento del sistema.

---

## 📐 Marco Teórico

### Paradigmas de Programación

| Paradigma | Lenguaje | Aplicación en el proyecto |
|---|---|---|
| **Lógico / Declarativo** | Prolog | Hechos, reglas, unificación, backtracking, findall |
| **Funcional** | Python | map, filter, reduce, lambda, list comprehensions |
| **Orientado a Objetos** | Python | Clases, herencia (PanelBase), encapsulamiento |

### Herramientas

| Herramienta | Versión | Propósito |
|---|---|---|
| SWI-Prolog | 9.x | Motor de inferencia lógica |
| Python | 3.13+ | Dashboard y análisis |
| pyswip | 0.3+ | Puente Python ↔ Prolog |
| pandas | 2.x | Análisis y transformación de datos |
| numpy | 1.x | Cálculos estadísticos y percentiles |
| tkinter | — | Interfaz gráfica de usuario |
| pytest | 8.x | Pruebas unitarias |

### Conceptos Clave

- **Hechos Prolog**: Predicados con argumentos que representan datos inmutables (`jugador/4`, `economia/8`).
- **Reglas**: Cláusulas `:-` que definen condiciones lógicas para inferir nuevas verdades.
- **Unificación**: Mecanismo de matching de patrones de Prolog.
- **findall**: Meta-predicado que recolecta todas las soluciones de una consulta.
- **map/filter/reduce**: Funciones de orden superior del paradigma funcional.
- **pandas groupby**: Agregación de datos por categorías.

---

## 🏗️ Diseño del Sistema

### Arquitectura

```
┌─────────────────────────────────────────────────────────┐
│                     PROLOG (cerebro)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │ hechos.pl │  │ reglas_*.│  │ casino.pl            │  │
│  │ 8 jug.    │  │ pl       │  │ (meta-predicados,    │  │
│  │ 30 campos │  │ VIP,     │  │  findall, consultas) │  │
│  │ c/u       │  │ Retener, │  │                      │  │
│  │           │  │ Cuidar,  │  │                      │  │
│  │           │  │ Recom.   │  │                      │  │
│  └──────────┘  └──────────┘  └──────────────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │ pyswip
                     ▼
┌─────────────────────────────────────────────────────────┐
│                     PYTHON (cara)                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│  │consultas │  │ data/    │  │ ui/                  │  │
│  │.py       │  │ jugadores│  │ panel_base.py        │  │
│  │(puente)  │  │ analisis │  │ panel_dashboard.py   │  │
│  │          │  │ .py      │  │ panel_*.py           │  │
│  │          │  │ (pandas, │  │ (tkinter)            │  │
│  │          │  │  numpy,  │  │                      │  │
│  │          │  │  func.)  │  │                      │  │
│  └──────────┘  └──────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Módulos de Prolog

| Archivo | Contenido |
|---|---|
| `hechos.pl` | 8 jugadores × 6 predicados (30 campos c/u) |
| `reglas_vip.pl` | 5 reglas: frecuencia, gasto, ganancias, antigüedad, edad |
| `reglas_retener.pl` | 5 reglas: inactividad, caída frecuencia, pérdidas, perfil |
| `reglas_detener.pl` | 5 reglas: edad, tiempo excesivo, presupuesto, pérdidas, solitario |
| `reglas_recomendar.pl` | 8 reglas: combinaciones azar/estrategia × rápido/lento |
| `casino.pl` | Meta-predicados findall + datos_jugador/32 |

### Módulos de Python

| Módulo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada |
| `config.py` | Colores, constantes |
| `consultas.py` | Puente pyswip (Prolog → Python) |
| `data/jugadores.py` | Datos de jugadores (desde Prolog o mock) |
| `data/analisis.py` | pandas, numpy, map/filter/reduce |
| `ui/panel_base.py` | Clase base con utilidades compartidas |
| `ui/panel_dashboard.py` | KPIs, barras de distribución, resumen financiero |
| `ui/panel_todos.py` | Tabla + detalle expandible con 30 campos |
| `ui/panel_vip.py` | Invitaciones VIP |
| `ui/panel_retener.py` | Bonos de retorno |
| `ui/panel_cuidar.py` | Alertas y supervisión |
| `ui/panel_rapido.py` | Atención prioritaria |
| `ui/panel_estadisticas.py` | Análisis descriptivo, groupby, correlaciones |
| `tests/test_clasificaciones.py` | 16 pruebas unitarias |

### Datos por Jugador (30 campos)

Organizados en 6 grupos funcionales:

1. **Identificación**: id, nombre, edad, ocupacion
2. **Económico**: presupuesto_hoy, fichas_actuales, gasto_hoy, gasto_promedio_ronda, gasto_maximo_historico, perdidas_acumuladas, ganancias_acumuladas
3. **Comportamiento**: prefiere_azar_o_estrategia, prefiere_rapido_o_lento, cambia_al_perder, cambia_al_ganar, juega_solo, reinvierte_ganancias, acepta_recomendaciones
4. **Sesión Actual**: juego_actual, monto_apuesta, resultado_ultima_ronda, rondas_jugadas_hoy, tiempo_en_casino_hoy, hora_actual
5. **Historial de Visitas**: frecuencia_semanal, tiempo_promedio_visita, horario_habitual, dias_visita, total_visitas, dias_desde_primera_visita, dias_desde_ultima_visita
6. **Preferencias**: juego_favorito, variedad_juegos_probados

### Clasificaciones

| Tipo | Descripción | Acción |
|---|---|---|
| VIP | Alto valor, viene seguido, gasta bien | Invitar a eventos exclusivos |
| Retener | Dejó de venir o riesgo de pérdida | Ofrecer bono de retorno |
| Cuidar | Edad joven, tiempo excesivo, pérdidas altas | Sugerir descanso, monitorear |
| Servicio Rápido | Ritmo rápido, visitas cortas, presupuesto alto | Atender con prioridad |

---

## 💻 Implementación

### Fragmento clave — Regla VIP en Prolog

```prolog
% Un jugador es VIP si visita >= 3 veces por semana
vip(Id) :- visitas(Id, Freq, _, _, _, _, _, _), Freq >= 3.

% O si su gasto máximo histórico es >= 100
vip(Id) :- economia(Id, _, _, _, _, GastoMax, _, _), GastoMax >= 100.
```

### Fragmento clave — Consulta pyswip desde Python

```python
from pyswip import Prolog
prolog = Prolog()
prolog.consult("../prolog/casino.pl")
vips = list(prolog.query("lista_vip(Lista)"))
```

### Fragmento clave — Análisis con pandas

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(datos_jugadores)
gasto_por_clasificacion = df.groupby("clasificacion")["gasto_hoy"].mean()
limite_perdidas = np.percentile(df["perdidas"], 75)
```

### Fragmento clave — Python funcional

```python
from functools import reduce

vips = list(filter(lambda j: j["clasificacion"] == "VIP", jugadores))
nombres_vip = list(map(lambda j: j["nombre"], vips))
total = reduce(lambda acc, j: acc + j["gasto_hoy"], jugadores, 0)
```

---

## 🧪 Pruebas

El sistema incluye 16 pruebas unitarias en `python/tests/test_clasificaciones.py`:

| Grupo | Pruebas | Verifica |
|---|---|---|
| TestJugadores | 6 | Datos completos, clasificaciones válidas, existencia |
| TestAnalisis | 6 | DataFrame, groupby, filter, map, reduce, resumen |
| TestFuncional | 4 | Demostración de filter, map, reduce, comprehensions |

Ejecutar con:
```bash
cd python
python -m pytest tests/ -v
```

---

## 📊 Resultados

### Dashboard
- 8 jugadores registrados con datos completos
- Clasificaciones: VIP, Retener, Cuidar, Servicio Rápido
- KPIs en tiempo real: totales, financieros, distribución
- Barras de progreso visuales para presupuesto y riesgo

### Paneles Funcionales
1. **Dashboard**: Vista general con KPIs y resumen financiero
2. **Todos los Usuarios**: Tabla con detalle expandible (30 campos)
3. **Invitar a VIP**: Tarjetas con datos clave + botón de invitación
4. **Personas a Retener**: Tarjetas con indicador de riesgo + bono
5. **Personas a Cuidar**: Alertas automáticas con código de colores
6. **Servicio Rápido**: Prioridades + atención ágil
7. **Estadísticas**: Análisis descriptivo, groupby, correlaciones, funcional

### Análisis de Datos
- Gasto promedio por clasificación (pandas groupby)
- Matriz de correlación entre variables numéricas (numpy)
- Top jugadores en percentil de pérdidas
- Python funcional: map, filter, reduce aplicados a datos reales

---

## ✅ Conclusiones

1. **Integración multiparadigma exitosa**: Se logró combinar Prolog (lógico), Python funcional (map/filter/reduce) y Python POO (clases) en un solo sistema cohesivo.

2. **Motor de inferencia funcional**: Las 22+ reglas de Prolog clasifican correctamente a los jugadores según su perfil, y el cambio de una regla modifica el comportamiento del sistema sin tocar Python.

3. **Dashboard profesional**: La interfaz oscura con acentos dorados ofrece una experiencia visual premium, con 7 paneles funcionales y navegación fluida.

4. **Análisis de datos**: pandas y numpy permiten extraer patrones de comportamiento (correlación frecuencia-pérdidas, gasto promedio por clasificación) que serían difíciles de detectar manualmente.

5. **Pruebas automatizadas**: 16 pruebas unitarias validan la integridad de los datos, las clasificaciones y las funciones de análisis.

### Limitaciones
- Los datos son estáticos (mock) cuando no hay conexión a Prolog.
- No hay persistencia en base de datos.
- Las visualizaciones gráficas (matplotlib) están planificadas para una versión futura.

### Trabajo Futuro
- Conexión a base de datos real para datos dinámicos.
- Visualizaciones gráficas con matplotlib embebido en tkinter.
- Módulo de recomendaciones en vivo basado en sesión actual.
- Interfaz web con Flask o Django.

---

## 📚 Referencias

- SWI-Prolog. (2024). *SWI-Prolog documentation*. https://www.swi-prolog.org
- Yüce, B. (2024). *pyswip: Python-SWI-Prolog bridge*. https://github.com/yuce/pyswip
- The pandas development team. (2024). *pandas documentation*. https://pandas.pydata.org
- NumPy contributors. (2024). *NumPy documentation*. https://numpy.org
- Python Software Foundation. (2024). *tkinter documentation*. https://docs.python.org/3/library/tkinter.html
- Krekel, H. et al. (2024). *pytest documentation*. https://docs.pytest.org
- Clocksin, W.F. & Mellish, C.S. (2003). *Programming in Prolog*. Springer.
