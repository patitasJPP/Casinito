# INFORME COMPLETO — CASINO SAPIENS

---
VVV
## 1. DATOS GENERALES

| Campo | Valor |
|---|---|
| Nombre del sistema | Casino Sapiens |
| Tipo | Sistema Experto Multiparadigma de Perfilado para Casino |
| Universidad | [Nombre de la universidad] |
| Curso | [Nombre del curso] |
| Integrantes | [Nombres de los integrantes] |
| Versión | 1.0 |
| Fecha | Julio 2026 |

---

## 2. PROPÓSITO DEL SISTEMA

Casino Sapiens es un sistema experto que automatiza la clasificación de jugadores de casino en cuatro categorías (VIP, Retener, Cuidar, Servicio Rápido) utilizando un motor de inferencia lógica en Prolog y una interfaz gráfica interactiva en Python/tkinter.

**Objetivo principal:** Demostrar la integración de los paradigmas de programación lógico (Prolog), funcional (map/filter/reduce) y orientado a objetos (Python) en un solo sistema cohesivo con aplicación en el mundo real.

**¿Para qué sirve?**
- Clasificar jugadores automáticamente según su perfil y comportamiento
- Visualizar KPIs financieros y métricas clave del casino
- Identificar jugadores VIP para atención exclusiva
- Detectar jugadores en riesgo de abandono para aplicar retención
- Supervisar jugadores con comportamiento de riesgo (juego responsable)
- Priorizar atención rápida a jugadores de ritmo ágil
- Generar reportes detallados por jugador
- Analizar estadísticas descriptivas, correlaciones y tendencias

---

## 3. TECNOLOGÍAS UTILIZADAS

| Tecnología | Versión | Propósito |
|---|---|---|
| **SWI-Prolog** | 9.x | Motor de inferencia lógica — base de hechos y reglas de clasificación |
| **Python** | 3.13+ | Lenguaje principal — dashboard, análisis de datos, lógica funcional y POO |
| **pyswip** | 0.3+ | Puente de comunicación Python ↔ Prolog (consultas en tiempo real) |
| **tkinter** | — (stdlib) | Interfaz gráfica de usuario (GUI nativa) |
| **pandas** | 2.x | Análisis y transformación de datos (DataFrame, groupby) |
| **numpy** | 1.x | Cálculos estadísticos, percentiles, arrays numéricos |
| **matplotlib** | 3.x | Visualización de datos embebida (gráficos de pastel y barras) |
| **pytest** | 8.x | Pruebas unitarias automatizadas |

---

## 4. ESTRUCTURA DE CARPETAS

```
casino_sapiens/
├── README.md                          # Documentación general del proyecto
├── plan.md                            # Plan de desarrollo
├── informe.md                         # Este documento
├── .gitignore
│
├── data/
│   └── jugadores.csv                  # Datos de jugadores en formato CSV
│
├── prolog/                            # Motor de inferencia lógica
│   ├── casino.pl                      # Meta-predicados, findall, consultas globales
│   ├── hechos.pl                      # Base de hechos (8 jugadores × 6 predicados)
│   ├── reglas_vip.pl                  # Reglas para clasificación VIP
│   ├── reglas_retener.pl              # Reglas para clasificación Retener
│   ├── reglas_detener.pl              # Reglas para clasificación Cuidar
│   └── reglas_recomendar.pl           # Reglas para recomendación Servicio Rápido
│
└── python/                            # Interfaz Python
    ├── main.py                        # Punto de entrada de la aplicación
    ├── ventana_principal.py           # Ventana principal con sidebar de navegación
    ├── config.py                      # Paleta de colores y constantes globales
    ├── consultas.py                   # Puente pyswip (consultas a Prolog)
    ├── requirements.txt               # Dependencias Python
    ├── generar_jugadores.py           # Generador de datos mock (100+ jugadores)
    ├── check_data.py                  # Script de validación de datos
    ├── check_ids.py                   # Script de verificación de IDs
    ├── salida.txt                     # Salida de depuración
    │
    ├── assets/                        # Recursos estáticos (imágenes, fuentes)
    │
    ├── data/                          # Capa de datos
    │   ├── __init__.py
    │   ├── jugadores.py               # Datos mock (200 jugadores), cache, funciones de acceso
    │   ├── analisis.py                # pandas, numpy, map/filter/reduce, resumen estadístico
    │   └── reporte_generado.csv       # Reporte exportado
    │
    ├── ui/                            # Capa de interfaz de usuario
    │   ├── __init__.py
    │   ├── panel_base.py              # Clase base: headers, cards, scroll, tags, detalle
    │   ├── panel_dashboard.py         # Dashboard ejecutivo: KPIs, barras, top 10, heatmap, alertas
    │   ├── panel_todos.py             # Todos los usuarios: tabla, filtros, detalle expandible
    │   ├── panel_vip.py               # Invitaciones VIP: grid de 3 columnas
    │   ├── panel_retener.py           # Retención: grid de 4 columnas, barras de riesgo
    │   ├── panel_cuidar.py            # Supervisión: grid de 3 columnas, alertas dinámicas
    │   ├── panel_rapido.py            # Servicio rápido: grid de 4 columnas, prioridades
    │   └── panel_estadisticas.py      # Estadísticas: resumen, comparativa, top 10, gráficos
    │
    ├── modules/                       # Módulos auxiliares
    │   ├── __init__.py
    │   ├── jugador.py                 # Clase Jugador (POO) con métodos de análisis
    │   ├── casino.py                  # Clase Casino (POO) con operaciones agregadas
    │   ├── operaciones.py             # Funciones matemáticas (sumar, restar, promedio)
    │   ├── cargar_datos.py            # Lectura de CSV, conversión a diccionarios
    │   ├── reportes.py               # Generación de reportes (texto, CSV)
    │   └── ventana_reporte.py         # Ventana tkinter para reporte detallado por jugador
    │
    └── tests/                         # Pruebas unitarias
        ├── __init__.py
        └── test_clasificaciones.py    # 16 pruebas: jugadores, análisis, funcional
```

---

## 5. FUNCIONALIDADES DEL SISTEMA

### 5.1 Panel Dashboard (Vista Ejecutiva)
- **KPIs** (6 tarjetas en grid de 3 columnas): Ingresos del Día, Jugadores Activos, LTV Promedio, Tasa Retención, Riesgo Churn, Margen Bruto
- **Distribución de Clasificaciones**: Barras proporcionales por tipo de jugador
- **Comparativa Financiera**: Gasto y neto por clasificación (VIP, Retener, Cuidar, Rápido)
- **Top 10 Jugadores**: Tabla ordenada por gasto hoy con indicador de riesgo churn
- **Estado Financiero Detallado**: Ingresos (apuestas + comisiones + VIP), costos variables (premios, dealers, fichas), costos fijos (12 items), margen bruto/neto/ROI, impuestos
- **Mapa de Calor por Zona**: Tragamonedas, Ruleta, Blackjack, etc. con color coding (verde/naranja/rojo)
- **Alertas**: VIP en riesgo, tráfico bajo, churn risk, meta diaria %, balance negativo

### 5.2 Panel Todos los Usuarios
- **Tabla** con 8 columnas (Nombre, Edad, Clasificación, Presupuesto, Gasto Hoy, Juego Favorito, Frecuencia, Pérdidas Acum.)
- **Filtros combinados**: búsqueda por nombre, clasificación, rango de gasto (mín/máx), rango de edad (mín/máx)
- **Ordenamiento**: click en cualquier encabezado de columna (ascendente/descendente)
- **Contador**: "X de Y resultados"
- **Detalle expandible**: al seleccionar una fila se muestra el perfil completo del jugador (30 campos organizados en 6 categorías)
- **Botón "Abrir Reporte Detallado"** para cada jugador
- **Botón "Limpiar Filtros"** para restaurar la vista completa

### 5.3 Panel Invitar a VIP
- Grid de **3 columnas** con tarjetas de jugadores clasificados como VIP
- Cada tarjeta muestra: nombre, edad, ocupación, presupuesto, frecuencia, gasto máximo histórico, visitas totales, juego favorito, ganancias acumuladas
- Botón "Enviar Invitación VIP" por tarjeta
- Indicador visual con borde dorado y estrella

### 5.4 Panel Personas a Retener
- Grid de **4 columnas** con tarjetas de jugadores en riesgo de abandono
- Cada tarjeta muestra: días sin venir, visitas totales, frecuencia, último juego, gasto promedio, pérdidas acumuladas
- **Barra de riesgo** visual (verde/naranja/rojo según días de inactividad)
- Botón "Ofrecer Bono de Retorno" por tarjeta

### 5.5 Panel Personas a Cuidar
- Grid de **3 columnas** con tarjetas de jugadores que requieren supervisión
- Alertas dinámicas calculadas en vivo:
  - Edad <= 22: "Monitorear tiempo de juego"
  - Tiempo en casino >= 4 hrs: "Sugerir descanso"
  - Gasto >= 80% presupuesto: "Monitorear"
  - Pérdidas > ganancias × 2: "Pérdidas altas"
- Botones: "Sugerir Descanso" y "Registrar Intervención"

### 5.6 Panel Servicio Rápido
- Grid de **4 columnas** con tarjetas de jugadores de ritmo ágil
- Prioridades calculadas dinámicamente (prefiere rápido, cambia al perder, visitas cortas, presupuesto alto)
- Botón "Atender Prioritariamente" por tarjeta

### 5.7 Panel Estadísticas
- **Resumen General**: KPIs (total jugadores, gasto total, promedios, balance) + conteo por clasificación con colores
- **Comparativa por Clasificación**: Tabla con filas coloreadas mostrando cantidad, gasto prom., pérdida prom., ganancia prom. por grupo
- **Top 10 Gastadores**: Ranking del día con nombre, clasificación, gasto, juego, frecuencia
- **Gráficos matplotlib**: Pastel de distribución + barras horizontales de top 10 gastadores

### 5.8 Reportes por Jugador
- Ventana emergente con perfil completo del jugador
- 30 campos organizados en 6 categorías funcionales
- Exportación a CSV

---

## 6. DATOS DE LOS JUGADORES

### 6.1 Volumen de Datos

| Tipo | Cantidad |
|---|---|
| Jugadores en base de hechos Prolog | 8 |
| Jugadores generados (mock) | 100 |
| Jugadores con datos duplicados fusionados | 100 |
| **Total jugadores disponibles** | **200** (IDs únicos j1–j200) |

### 6.2 Estructura de Datos por Jugador (30 campos)

Cada jugador se representa como un diccionario Python con los siguientes campos:

| Grupo | Campo | Tipo | Descripción | Ejemplo |
|---|---|---|---|---|
| **Identificación** | `id` | string | Identificador único | `"j1"` |
| | `nombre` | string | Nombre del jugador | `"Carlos"` |
| | `edad` | int | Edad en años | `45` |
| | `ocupacion` | string | Profesión | `"Ingeniero"` |
| **Económico** | `presupuesto_hoy` | int | Presupuesto disponible hoy (S/) | `500` |
| | `fichas_actuales` | int | Fichas que tiene en este momento | `200` |
| | `gasto_hoy` | int | Gasto acumulado hoy (S/) | `300` |
| | `gasto_promedio_ronda` | int | Gasto promedio por ronda (S/) | `50` |
| | `gasto_maximo_historico` | int | Mayor gasto registrado (S/) | `200` |
| | `perdidas_acumuladas` | int | Pérdidas totales históricas (S/) | `5000` |
| | `ganancias_acumuladas` | int | Ganancias totales históricas (S/) | `3000` |
| **Comportamiento** | `prefiere_azar_o_estrategia` | string | Preferencia de juego | `"Azar"` |
| | `prefiere_rapido_o_lento` | string | Ritmo preferido | `"Rápido"` |
| | `cambia_al_perder` | string | Cambia de juego al perder | `"Sí"` |
| | `cambia_al_ganar` | string | Cambia de juego al ganar | `"No"` |
| | `juega_solo` | string | Prefiere jugar solo | `"No"` |
| | `reinvierte_ganancias` | string | Reinvierte lo ganado | `"Sí"` |
| | `acepta_recomendaciones` | string | Acepta sugerencias del sistema | `"Sí"` |
| **Sesión Actual** | `juego_actual` | string | Juego que está jugando ahora | `"Tragamonedas"` |
| | `monto_apuesta` | int | Monto de la última apuesta (S/) | `50` |
| | `resultado_ultima_ronda` | string | Resultado de la última ronda | `"Ganó"` |
| | `rondas_jugadas_hoy` | int | Total de rondas hoy | `15` |
| | `tiempo_en_casino_hoy` | float | Horas en casino hoy | `2.5` |
| | `hora_actual` | string | Hora del registro | `"22:00"` |
| **Historial Visitas** | `frecuencia_semanal` | int | Veces que viene por semana | `3` |
| | `tiempo_promedio_visita` | int | Duración promedio por visita (min) | `180` |
| | `horario_habitual` | string | Momento del día que prefiere | `"Nocturno"` |
| | `dias_visita` | string | Días de la semana que visita | `"Vie,Sáb"` |
| | `total_visitas` | int | Total de visitas registradas | `45` |
| | `dias_desde_primera_visita` | int | Días desde su primera visita | `90` |
| | `dias_desde_ultima_visita` | int | Días desde su última visita | `2` |
| **Preferencias** | `juego_favorito` | string | Juego que más juega | `"Tragamonedas"` |
| | `variedad_juegos_probados` | int | Cantidad de juegos distintos probados | `3` |
| **Calculado** | `clasificacion` | string | Categoría asignada por el sistema | `"VIP"` |

### 6.3 Organización de los Datos

Los datos están organizados en **tres capas**:

1. **Capa Prolog** (`prolog/hechos.pl`): 8 jugadores como hechos lógicos en 6 predicados:
   - `jugador(Id, Nombre, Edad, Ocupacion)`
   - `economia(Id, Presupuesto, Fichas, GastoHoy, GastoProm, GastoMax, Perdidas, Ganancias)`
   - `comportamiento(Id, AzarEstrategia, RapidoLento, CambiaPerder, CambiaGanar, Solo, Reinvierte, AceptaRec)`
   - `sesion(Id, Juego, Apuesta, Resultado, Rondas, Tiempo, Hora)`
   - `visitas(Id, FrecSem, TiempoProm, Horario, Dias, Total, DiasPrimera, DiasUltima)`
   - `preferencias(Id, JuegoFav, Variedad)`

2. **Capa Mock** (`python/data/jugadores.py`): 200 jugadores como lista de diccionarios `JUGADORES_MOCK`. Cuando Prolog no está disponible, se usa esta lista directamente.

3. **Cache** (`python/data/jugadores.py`): `_cache_jugadores` almacena el resultado de `obtener_todos()` para evitar consultas repetitivas a Prolog. Se invalida con `invalidar_cache_jugadores()`.

---

## 7. SISTEMA DE CLASIFICACIÓN

### 7.1 Categorías

| Clasificación | Criterios Prolog | Color | Acción |
|---|---|---|---|
| **VIP** | Frecuencia >= 3x/sem O gasto máx >= 100 O ganancias >= 2000 O antigüedad >= 365 días O edad >= 60 | Dorado `#f0c040` | Invitar a eventos exclusivos |
| **Retener** | Días sin visita >= 7 O caída de frecuencia O pérdidas >= 3000 O perfil en riesgo | Naranja `#ffa726` | Ofrecer bono de retorno |
| **Cuidar** | Edad <= 22 O tiempo >= 4 hrs O gasto >= 80% presupuesto O pérdidas > ganancias×2 | Rojo `#ef5350` | Sugerir descanso, monitorear |
| **Servicio Rápido** | Prefiere rápido O cambia al perder O visitas <= 150 min O presupuesto >= 200 | Verde `#66bb6a` | Atender con prioridad |

### 7.2 Flujo de Clasificación

```
                    ┌──────────────┐
                    │  Jugador     │
                    │  (30 campos) │
                    └──────┬───────┘
                           │
                           ▼
              ┌────────────────────────┐
              │  Motor Prolog          │
              │  (22+ reglas lógicas)  │
              └────────┬───────────────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
    ┌─────────┐  ┌─────────┐  ┌─────────┐
    │   VIP   │  │ Retener │  │  Cuidar │
    └─────────┘  └─────────┘  └─────────┘
          ┌─────────┐
          │ Rápido  │
          └─────────┘
```

---

## 8. FILTROS DISPONIBLES

### 8.1 Panel Todos los Usuarios

| Filtro | Tipo | Comportamiento |
|---|---|---|
| **Búsqueda por nombre** | Texto (KeyRelease) | Filtro parcial (case-insensitive) mientras se escribe |
| **Clasificación** | Combobox (Todas/VIP/Retener/Cuidar/Servicio Rápido) | Filtro exacto, se aplica al seleccionar |
| **Rango de gasto mín/máx** | Entry numérico (KeyRelease) | Filtro por intervalo en tiempo real |
| **Rango de edad mín/máx** | Entry numérico (KeyRelease) | Filtro por intervalo en tiempo real |
| **Ordenamiento** | Click en encabezado de columna | Alterna ascendente/descendente |
| **Limpiar Filtros** | Botón | Restaura todos los filtros a valores por defecto |

### 8.2 Panel Dashboard (KPIs y Tablas)

| Elemento | Tipo | Detalle |
|---|---|---|
| **KPIs** | 6 tarjetas fijas | Datos calculados de `resumen_estadistico()` |
| **Top 10** | Tabla estática | Ordenada por `gasto_hoy` descendente |
| **Barras de distribución** | Barras Canvas | 4 grupos, ancho proporcional |
| **Mapa de Calor** | Tarjetas coloreadas | 4 zonas con intensidad de tráfico |

---

## 9. PALETA DE COLORES (UI)

| Elemento | Código | Descripción |
|---|---|---|
| Fondo general | `#0a0e17` | Azul noche profundo |
| Sidebar | `#0f1420` | Azul oscuro |
| Sidebar hover | `#1a2340` | Azul medio |
| Sidebar seleccionado | `#f0c040` | Dorado brillante |
| Card background | `#141a2b` | Azul card |
| Card alt | `#1a2340` | Azul card alternativo |
| Dorado (acento) | `#f0c040` | Dorado brillante |
| Rojo (alerta) | `#ef5350` | Rojo vibrante |
| Verde (positivo) | `#66bb6a` | Verde vivo |
| Naranja (advertencia) | `#ffa726` | Naranja brillante |
| Texto principal | `#e8eaf6` | Blanco azulado |
| Texto secundario | `#9ea7c3` | Gris azulado |
| Texto tenue | `#5c6a8a` | Gris oscuro |
| Bordes | `#2a3355` | Azul borde |
| Input background | `#1a2340` | Azul input |

---

## 10. ARQUITECTURA DE COMUNICACIÓN

```
         ┌─────────────────────────────────────────┐
         │              USUARIO                     │
         │    (interactúa con la GUI tkinter)       │
         └────────────────┬────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│                   PYTHON (Frontend)                  │
│                                                      │
│  ventana_principal.py                                │
│    ├── Sidebar de navegación (7 paneles)            │
│    ├── Cache de paneles (navegación instantánea)    │
│    └── Atajos de teclado (Ctrl+1..7)               │
│                                                      │
│  ui/ (paneles tkinter)                               │
│    ├── panel_base.py ─── utilidades compartidas     │
│    ├── panel_dashboard.py ─── KPIs + gráficos       │
│    ├── panel_todos.py ─── tabla + filtros           │
│    ├── panel_vip.py / retener / cuidar / rapido    │
│    └── panel_estadisticas.py ─── análisis           │
│                                                      │
│  data/ (capa de datos)                               │
│    ├── jugadores.py ─── cache, acceso a datos       │
│    └── analisis.py ─── pandas, numpy, funcional     │
│                                                      │
│  consultas.py ─── puente pyswip                     │
└────────────┬──────────────────────────┬─────────────┘
             │                          │
             ▼                          ▼
┌────────────────────┐    ┌──────────────────────────┐
│   JUGADORES_MOCK   │    │      PROLOG (Backend)    │
│   (200 jugadores)  │    │                          │
│   ┌──────────────┐ │    │  hechos.pl (8 jug.)      │
│   │ obtener_todos│ │◄───┤  reglas_vip.pl           │
│   │ ()           │ │    │  reglas_retener.pl       │
│   │ cache        │ │    │  reglas_detener.pl       │
│   └──────────────┘ │    │  reglas_recomendar.pl    │
└────────────────────┘    │  casino.pl               │
                          └──────────────────────────┘
```

---

## 11. MECANISMOS DE OPTIMIZACIÓN

1. **Cache de datos** (`jugadores.py`): `_cache_jugadores` evita consultas repetitivas a Prolog. `obtener_todos()` solo ejecuta las ~400 consultas (2 por jugador) **una vez** por sesión.

2. **Cache de paneles** (`ventana_principal.py`): `_cache_paneles` almacena las instancias de los 7 paneles después de su primera carga. La navegación posterior es instantánea (sin recrear widgets).

3. **Datos pre-filtrados** (`jugadores.py`): Las variables `VIP`, `RETENER`, `CUIDAR`, `SERVICIO_RAPIDO` se calculan al importar el módulo, evitando filtros redundantes en cada panel.

4. **Invalidación manual**: `recargar_datos()` y `recargar_panel_actual()` permiten forzar la recarga cuando sea necesario.

---

## 12. PRUEBAS UNITARIAS

El sistema incluye **16 pruebas** en `python/tests/test_clasificaciones.py`:

| Grupo | Pruebas | Verifica |
|---|---|---|
| TestJugadores | 6 | Datos completos (30 campos), clasificaciones válidas, existencia |
| TestAnalisis | 6 | DataFrame, groupby, filter, map, reduce, resumen estadístico |
| TestFuncional | 4 | filter, map, reduce, list comprehensions |

Ejecutar con:
```bash
cd python
python -m pytest tests/ -v
```

---

## 13. DEPENDENCIAS (requirements.txt)

```
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
pyswip>=0.3.0
pytest>=8.0.0
```

Instalación:
```bash
cd python
pip install -r requirements.txt
```

---

## 14. EJECUCIÓN DEL SISTEMA

```bash
cd python
python main.py                    # Inicia la interfaz gráfica
python main.py --demo             # Modo demo en consola
python -m pytest tests/ -v        # Ejecutar pruebas
python generar_jugadores.py       # Regenerar datos mock
```

---

## 15. CONCLUSIONES

1. **Integración multiparadigma exitosa**: Prolog (lógico), map/filter/reduce (funcional) y clases Python (POO) conviven en un sistema cohesivo.

2. **Motor de inferencia funcional**: Las 22+ reglas de Prolog clasifican correctamente a los jugadores. Cambiar una regla modifica el comportamiento sin tocar Python.

3. **Dashboard profesional**: Interfaz oscura con acentos dorados, 7 paneles funcionales con navegación por sidebar y atajos de teclado.

4. **Análisis de datos**: pandas y numpy permiten extraer patrones (gasto promedio por clasificación, correlaciones) que serían difíciles de detectar manualmente.

5. **Datos a escala**: 200 jugadores con 30 campos cada uno, pre-cargados y optimizados con cache para rendimiento en tiempo real.
