# CASINO SAPIENS — REQUERIMIENTOS DEL PROYECTO

> **Proyecto:** Casino Sapiens — Sistema Experto de Perfilado para Casino
> **Paradigma:** Multiparadigma (Lógico + POO + Funcional + Estructurado)
> **Lenguajes:** Prolog (motor de inferencia) + Python (dashboard y análisis)
> **Profesor:** [Nombre del profesor]
> **Curso:** [Nombre del curso]
> **Fecha:** Julio 2026

---

## TABLA DE CONTENIDOS

1. [Estructura del Proyecto](#1-estructura-del-proyecto)
2. [Módulo 0 — Fundamentos y Configuración](#2-módulo-0--fundamentos-y-configuración-del-entorno)
3. [Módulo 1 — Gestión y Procesamiento de Datos](#3-módulo-1--gestión-y-procesamiento-de-datos)
4. [Módulo 2 — Funciones y Módulos](#4-módulo-2--funciones-y-módulos)
5. [Módulo 3 — Interfaz de Usuario con Tkinter](#5-módulo-3--interfaz-de-usuario-con-tkinter)
6. [Módulo 4 — Diálogos y Ventanas Avanzadas](#6-módulo-4--diálogos-y-ventanas-avanzadas)
7. [Módulo 5 — Aplicación Completa y Proyecto Final](#7-módulo-5--aplicación-completa-y-proyecto-final)
8. [Flujo de Interacción del Programa](#8-flujo-de-interacción-del-programa)
9. [Nuevos Archivos Creados](#9-nuevos-archivos-creados)
10. [Archivos Modificados](#10-archivos-modificados)

---

## 1. ESTRUCTURA DEL PROYECTO

```
Casinito/
│
├── .gitignore
├── README.md
├── plan.md                          ← Plan de exposición
├── data/
│   └── jugadores.csv                ← Datos de 8 jugadores en CSV
│
├── prolog/
│   ├── casino.pl                    ← Meta-predicados, consulta módulos
│   ├── hechos.pl                    ← 8 jugadores (hechos Prolog)
│   ├── reglas_vip.pl                ← Reglas VIP
│   ├── reglas_retener.pl            ← Reglas retener
│   ├── reglas_detener.pl            ← Reglas detener/cuidar
│   └── reglas_recomendar.pl         ← Reglas recomendar juegos
│
└── python/
    ├── main.py                      ← Punto de entrada dual: GUI o --demo
    ├── config.py                    ← Colores, fuentes, constantes
    ├── consultas.py                 ← Puente pyswip (Prolog → Python)
    ├── requirements.txt             ← Dependencias del proyecto
    ├── requerimentos.md             ← Este archivo
    ├── assets/
    │   └── icono.ico                ← Icono de la aplicación
    ├── docs/
    │   └── capturas/                ← Screenshots del proyecto
    │
    ├── data/
    │   ├── __init__.py
    │   ├── jugadores.py             ← Datos mock + funciones de consulta
    │   └── analisis.py              ← pandas + numpy + funcional + ejercicios
    │
    ├── modules/                     ← NUEVO — Módulos funcionales
    │   ├── __init__.py
    │   ├── jugador.py               ← Clase Jugador (POO)
    │   ├── casino.py                ← Clase Casino (POO)
    │   ├── cargar_datos.py          ← Lectura CSV con try-except
    │   ├── reportes.py              ← Reportes en consola y export CSV
    │   ├── operaciones.py           ← Funciones matemáticas básicas
    │   └── ventana_reporte.py       ← Toplevel con reporte detallado
    │
    ├── ui/
    │   ├── __init__.py
    │   ├── panel_base.py            ← Clase base con LabelFrame y utilidades
    │   ├── panel_dashboard.py       ← KPIs, barras, resumen financiero
    │   ├── panel_todos.py           ← Tabla + detalle + botón Toplevel
    │   ├── panel_vip.py             ← Invitaciones con askquestion
    │   ├── panel_retener.py         ← Bonos con askquestion
    │   ├── panel_cuidar.py          ← Alertas con showwarning
    │   ├── panel_rapido.py          ← Atención prioritaria
    │   └── panel_estadisticas.py    ← Radiobutton, Checkbutton, numpy, matplotlib
    │
    └── tests/
        ├── __init__.py
        └── test_clasificaciones.py  ← 16 pruebas unitarias
```

---

## 2. MÓDULO 0 — FUNDAMENTOS Y CONFIGURACIÓN DEL ENTORNO

| # | Requisito de la Rúbrica | Adaptación Casino | Estado | Archivo |
|---|---|---|---|---|
| 0.1 | Instalación de Python | `python --version` documentado, demo con `--demo` | ✅ | `main.py` |
| 0.2 | Entornos Virtuales | `requirements.txt` con numpy, pandas, matplotlib, pyswip, pytest | ✅ | `requirements.txt` |
| 0.3 | numpy, pandas, matplotlib, tkinter | Importados con try/except graceful fallback | ✅ | `data/analisis.py` |
| 0.4 | Editor de Código | Recomendación en README | ✅ | `README.md` |
| 0.5 | Carpeta `/data` | `data/jugadores.csv` con 8 jugadores | ✅ | `data/jugadores.csv` |
| 0.5 | Carpeta `/modules` | Módulos funcionales (jugador, casino, reportes, etc.) | ✅ | `modules/` |
| 0.5 | Carpeta `/ui` | 8 paneles + base | ✅ | `ui/` |
| 0.5 | Carpeta `/docs` | Capturas de pantalla + documentación | ✅ | `docs/capturas/` |
| 0.5 | `main.py` | Punto de entrada principal | ✅ | `main.py` |

---

## 3. MÓDULO 1 — GESTIÓN Y PROCESAMIENTO DE DATOS

### 3.1 Modelado de Datos con Diccionarios y Clases

| # | Requisito | Adaptación Casino | Archivo |
|---|---|---|---|
| 1.1 | Diccionario `{'nombre','codigo','notas'}` | Diccionario `{'nombre','id','gasto_hoy','perdidas','ganancias'}` | `data/jugadores.py` |
| 1.2 | **Clase Estudiante** | **Clase Jugador** con `__init__` | `modules/jugador.py` |
| 1.2 | `calcular_promedio()` | `calcular_gasto_promedio()` → gasto_hoy / rondas_jugadas_hoy | `modules/jugador.py` |
| 1.2 | `esta_aprobado()` (promedio >= 13) | `es_vip()` → gasto_max >= 100 o frecuencia >= 3 | `modules/jugador.py` |
| 1.3 | **Clase Curso** | **Clase Casino** con lista de Jugador | `modules/casino.py` |
| 1.3 | `agregar_estudiante()` | `agregar_jugador()` | `modules/casino.py` |
| 1.3 | `calcular_promedio_general()` | `calcular_gasto_promedio_general()` | `modules/casino.py` |
| 1.3 | `contar_aprobados()` | `contar_por_clasificacion(clasif)` | `modules/casino.py` |

### 3.2 Lectura y Escritura de Archivos (CSV)

| # | Requisito | Adaptación Casino | Archivo |
|---|---|---|---|
| 1.4 | `import csv` | `import csv` para leer `jugadores.csv` | `modules/cargar_datos.py` |
| 1.4 | Leer CSV → crear objetos | `leer_csv()` → lista de objetos `Jugador` | `modules/cargar_datos.py` |
| 1.4 | `try-except` para archivos | `try-except` para FileNotFound, PermissionError, ValueError | `modules/cargar_datos.py` |

### 3.3 Análisis con NumPy y Pandas

| # | Requisito | Adaptación Casino | Archivo |
|---|---|---|---|
| 1.5 | Array de notas como ndarray | Array de `gasto_hoy` como ndarray | `data/analisis.py` |
| 1.5 | `np.mean()`, `np.std()`, `np.max()`, `np.min()` | `calcular_estadisticas_generales()` con np.mean, np.std, np.max, np.min | `data/analisis.py` |
| 1.5 | Ejercicio 1: filtrar notas > 15 | `ejercicio_array_notas()` → filtrar gasto_hoy > 200 | `data/analisis.py` |
| 1.5 | Ejercicio 5: ventas (total, día+, día-) | `ejercicio_ventas()` → total, mayor/menor gastador | `data/analisis.py` |
| 1.6 | `df.head()`, `df.info()`, `df.describe()` | _crear_exploracion_inicial() muestra estos 3 | `ui/panel_estadisticas.py` |
| 1.6 | `df[df['promedio'] > 15]` | `df[df['gasto_hoy'] > 200]` | `data/analisis.py` |
| 1.6 | Agrupar por 'Aprobado'/'Desaprobado' | `groupby('clasificacion').agg(...)` | `data/analisis.py` |

---

## 4. MÓDULO 2 — FUNCIONES Y MÓDULOS

| # | Requisito | Adaptación Casino | Archivo |
|---|---|---|---|
| 2.1 | `analisis.py` → `calcular_promedio_estudiante(notas)` | `calcular_promedio_gasto(jugadores)` | `data/analisis.py` |
| 2.1 | `analisis.py` → `calcular_estadisticas_generales()` | ✅ Con np.mean, np.std, np.max, np.min | `data/analisis.py` |
| 2.2 | `reportes.py` → `generar_reporte_simple()` | ✅ Imprime en consola: nombre, gasto, estado | `modules/reportes.py` |
| 2.2 | `reportes.py` → `generar_reporte_csv()` | ✅ Exporta a `data/reporte_generado.csv` | `modules/reportes.py` |
| 2.3 | Práctica 1: promedio de lista | `promedio(lista)` en operaciones.py | `modules/operaciones.py` |
| 2.4 | Práctica 4: `operaciones.py` | `sumar`, `restar`, `multiplicar`, `dividir` | `modules/operaciones.py` |
| 2.5 | `main.py` importa módulos | ✅ `main.py` importa y usa todos los módulos en modo `--demo` | `main.py` |

---

## 5. MÓDULO 3 — INTERFAZ DE USUARIO CON TKINTER

| # | Requisito | Estado | Archivo |
|---|---|---|---|
| 3.1 | `Tk()` con título | ✅ | `ventana_principal.py:16-17` |
| 3.1 | Tamaño y `resizable(False, False)` | ✅ Agregado | `ventana_principal.py:19-20` |
| 3.1 | `iconbitmap` | ✅ `assets/icono.ico` | `ventana_principal.py:21-24` |
| 3.2 | `Label`, `Entry`, `Button` | ✅ Usados extensivamente | Varios |
| 3.2 | `pack()` y `grid()` | ✅ Ambos métodos | Varios |
| 3.2 | **`LabelFrame`** | ✅ `_crear_card_contenedor` ahora usa LabelFrame | `ui/panel_base.py` |
| 3.3 | **`Radiobutton` + `IntVar`** | ✅ Individual / Grupal en Estadísticas | `ui/panel_estadisticas.py` |
| 3.3 | **`Checkbutton`** | ✅ Gasto / Pérdidas / Ganancias en Estadísticas | `ui/panel_estadisticas.py` |
| 3.4 | `lambda` para eventos | ✅ En todos los botones | Varios |
| 3.4 | Botones conectados a módulos | ✅ Llaman a funciones de analisis.py, reportes.py, etc. | Varios |

---

## 6. MÓDULO 4 — DIÁLOGOS Y VENTANAS AVANZADAS

| # | Requisito | Estado | Archivo |
|---|---|---|---|
| 4.1 | `showinfo()` | ✅ En VIP, Retener, Cuidar | `ui/panel_vip.py`, etc. |
| 4.1 | `showwarning()` | ✅ Al sugerir descanso a jugador en Cuidar | `ui/panel_cuidar.py:100` |
| 4.1 | `showerror()` | ✅ Error al leer CSV en `cargar_datos.py` | `modules/cargar_datos.py` |
| 4.1 | **`askquestion()`** | ✅ Antes de enviar invitación VIP y bono Retener | `ui/panel_vip.py:73`, `ui/panel_retener.py:84` |
| 4.2 | **`Toplevel` (ventana secundaria)** | ✅ `VentanaReporte` con scroll, LabelFrames, botón cerrar | `modules/ventana_reporte.py` |
| 4.2 | Comunicación entre ventanas | ✅ Pasa diccionario del jugador de ventana principal a Toplevel | `ui/panel_todos.py:154` |
| 4.3 | `.destroy()` | ✅ Cerrar ventanas y widgets | `ventana_principal.py:106`, `modules/ventana_reporte.py` |

---

## 7. MÓDULO 5 — APLICACIÓN COMPLETA Y PROYECTO FINAL

| # | Requisito | Estado | Archivo |
|---|---|---|---|
| 5.1 | Integración en `main.py` | ✅ Orquesta carga → procesamiento → visualización | `main.py` |
| 5.2 | Paradigma Estructurado | ✅ for, while, funciones, condicionales | Varios |
| 5.2 | Paradigma POO | ✅ Clases Jugador, Casino, PanelBase, AplicacionCasino | Varios |
| 5.2 | Paradigma Funcional | ✅ map, filter, reduce, lambda, list comprehensions | `data/analisis.py`, `ui/panel_estadisticas.py` |
| 5.2 | Paradigma Lógico | ✅ 22+ reglas Prolog + pyswip | `prolog/`, `consultas.py` |
| 5.3 | Pruebas unitarias | ✅ 16 tests en 3 clases | `tests/test_clasificaciones.py` |
| 5.4 | `try-except` global | ✅ En imports, lectura CSV, groupby, correlaciones | Varios |
| 5.5 | Resultados en consola | ✅ Modo `--demo` + `generar_reporte_simple()` | `main.py`, `modules/reportes.py` |
| 5.5 | Resultados en GUI | ✅ Labels, Treeview, gráficos matplotlib | Varios |
| 5.5 | Gráficos matplotlib | ✅ Torta + barras horizontales | `ui/panel_estadisticas.py` |
| 5.6 | Archivos CSV de prueba | ✅ `data/jugadores.csv` con 8 jugadores | `data/jugadores.csv` |
| 5.6 | Documentación | ✅ `README.md` completo + `plan.md` + este archivo | Varios |
| 5.6 | Capturas de pantalla | ✅ Carpeta `docs/capturas/` lista | `docs/capturas/` |

---

## 8. FLUJO DE INTERACCIÓN DEL PROGRAMA

### 8.1 Flujo Principal (GUI)

```
INICIO
  │
  ├── main.py
  │     │
  │     ├── [sin args] → AplicacionCasino().ejecutar()
  │     │
  │     │    1. Configurar estilos (config.py)
  │     │    2. Crear ventana Tk (resizable=False, icono)
  │     │    3. Crear layout: barra superior + sidebar + frame paneles + barra estado
  │     │    4. Cargar panel Dashboard por defecto
  │     │    5. Iniciar mainloop
  │     │
  │     └── [--demo] → demo_modulos()
  │
  └── NAVEGACIÓN (sidebar, 7 paneles)
        │
        ├── Dashboard ───────── KPIs, barras distribución, resumen financiero
        ├── Todos Usuarios ──── Tabla con búsqueda + detalle + botón "Abrir Reporte"
        │                            └── Toplevel con datos completos del jugador
        ├── Invitar VIP ─────── Tarjetas + askquestion → showinfo
        ├── Retener ─────────── Tarjetas + barra riesgo + askquestion → showinfo
        ├── Cuidar ──────────── Tarjetas + alertas + showwarning
        ├── Rápido ──────────── Tarjetas con prioridades
        └── Estadísticas ────── Radiobutton/Checkbutton + head()/info()/describe()
                                + groupby + correlaciones + ejercicios numpy
                                + map/filter/reduce + gráficos matplotlib
```

### 8.2 Flujo de Datos

```
PROLOG (hechos + reglas)
    │ pyswip
    ▼
consultas.py ────────> data/analisis.py (pandas + numpy)
    │                       │
    │                       ├── crear_dataframe()
    │                       ├── analisis_por_clasificacion() ← groupby
    │                       ├── correlaciones() ← numpy
    │                       ├── calcular_estadisticas_generales() ← np.mean/std/max/min
    │                       ├── ejercicio_array_notas() ← Ej 1
    │                       ├── ejercicio_ventas() ← Ej 5
    │                       └── map/filter/reduce
    │
    ▼
data/jugadores.py ──> Módulos Python
    │                       │
    │                       ├── Jugador (clase POO)
    │                       ├── Casino (clase POO)
    │                       ├── cargar_datos.py (CSV → objetos)
    │                       ├── reportes.py (consola + CSV)
    │                       └── operaciones.py (suma/resta/etc.)
    │
    ▼
ui/paneles (tkinter) ──> Usuario final
```

### 8.3 Cobertura de Paradigmas por Sección

| Sección | Paradigma(s) | Archivo(s) |
|---|---|---|
| Clasificación de jugadores | **Lógico** (Prolog) | `prolog/` |
| Clases Jugador y Casino | **POO** | `modules/jugador.py`, `modules/casino.py` |
| map/filter/reduce | **Funcional** | `data/analisis.py` |
| PanelBase y herencia | **POO** | `ui/panel_base.py` |
| AplicacionCasino (orquestación) | **Estructurado + POO** | `ventana_principal.py` |
| Lectura CSV con try-except | **Estructurado** | `modules/cargar_datos.py` |
| Radiobutton/Checkbutton eventos | **Orientado a Eventos** | `ui/panel_estadisticas.py` |
| 22+ reglas de inferencia | **Lógico** | `prolog/reglas_*.pl` |

---

## 9. NUEVOS ARCHIVOS CREADOS

| Archivo | Propósito | Líneas aprox. |
|---|---|---|
| `python/modules/__init__.py` | Package init | 0 |
| `python/modules/jugador.py` | **Clase Jugador** con `__init__`, `calcular_gasto_promedio()`, `es_vip()`, `es_rentable()`, `en_riesgo()`, `calcular_balance()` | 34 |
| `python/modules/casino.py` | **Clase Casino** con `agregar_jugador()`, `calcular_gasto_promedio_general()`, `contar_por_clasificacion()`, `obtener_vips()`, `top_gastadores()` | 30 |
| `python/modules/cargar_datos.py` | `leer_csv()` con `import csv` + try-except (FileNotFound, PermissionError, ValueError) + `csv_a_diccionarios()` | 52 |
| `python/modules/reportes.py` | `generar_reporte_simple()` (consola) + `generar_reporte_csv()` (exporta a CSV) | 52 |
| `python/modules/operaciones.py` | `sumar()`, `restar()`, `multiplicar()`, `dividir()`, `promedio()` | 22 |
| `python/modules/ventana_reporte.py` | `VentanaReporte` (Toplevel) con scroll, LabelFrames agrupados, datos del jugador, botón cerrar | 81 |
| `data/jugadores.csv` | 8 jugadores con 34 campos cada uno, separado por comas | 9 |
| `python/requirements.txt` | numpy, pandas, matplotlib, pyswip, pytest | 5 |
| `python/assets/icono.ico` | Icono dorado de la aplicación | 1 |
| `python/requerimentos.md` | Este archivo de documentación | ~350 |

---

## 10. ARCHIVOS MODIFICADOS

| Archivo | Cambios realizados |
|---|---|
| `python/main.py` | Agregado modo `--demo` que prueba todos los módulos + imports de modules/ |
| `python/data/analisis.py` | Agregadas: `calcular_promedio_gasto()`, `calcular_estadisticas_generales()`(con np.mean/std/max/min), `ejercicio_array_notas()`(Ej 1), `ejercicio_ventas()`(Ej 5) |
| `python/ui/panel_estadisticas.py` | Agregados: `_crear_selector_analisis()`(Radiobutton+Checkbutton), `_crear_exploracion_inicial()`(head/info/describe), `_crear_ejercicios_numpy()` |
| `python/ui/panel_base.py` | `_crear_card_contenedor` cambiado de `tk.Frame` a `tk.LabelFrame` con título integrado |
| `python/ui/panel_todos.py` | Importado `VentanaReporte`, agregado método `_abrir_reporte()` y botón "Abrir Reporte Detallado" que abre Toplevel |
| `python/ui/panel_vip.py` | `messagebox.askquestion()` antes de enviar invitación VIP |
| `python/ui/panel_retener.py` | `messagebox.askquestion()` antes de ofrecer bono de retorno |
| `python/ui/panel_cuidar.py` | `showwarning()` en lugar de `showinfo()` al sugerir descanso |
| `python/ventana_principal.py` | Agregado `resizable(False, False)`, `iconbitmap()` con try-except |

---

## 11. RESUMEN DE COBERTURA DE RÚBRICA

| Módulo | Puntos totales | Cubiertos | % |
|---|---|---|---|
| M0 — Fundamentos | 8 | 8 | **100%** |
| M1 — Datos (POO + CSV + NumPy/Pandas) | 15 | 14 | **93%** |
| M2 — Funciones y Módulos | 6 | 6 | **100%** |
| M3 — Tkinter GUI | 9 | 9 | **100%** |
| M4 — Diálogos y Ventanas | 6 | 6 | **100%** |
| M5 — Aplicación Completa | 10 | 10 | **100%** |
| **TOTAL** | **54** | **53** | **~98%** |

> **Nota:** El único punto no cubierto al 100% es `{'nombre','codigo','notas'}` → se adaptó a `{'nombre','id','gasto_hoy','perdidas','ganancias'}` porque el dominio es casino, no estudiantes. El concepto (diccionario representando una entidad) es idéntico.
