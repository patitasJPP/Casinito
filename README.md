# 🎰 CASINO SAPIENS

> Sistema Experto de Perfilado y Recomendación para Casino
> Proyecto Universitario — Prolog + Python

---

## 📋 CONTEXTO COMPLETO DEL PROYECTO

### 1. Visión General

Casino virtual inteligente donde **Prolog** funciona como motor de inferencia (gerente inteligente) que clasifica jugadores y recomienda acciones, mientras **Python** muestra los resultados en un dashboard para empleados.

**Filosofía:** Toda la lógica e inteligencia está en Prolog. Python solo es la interfaz visual.

### 2. Decisión de Arquitectura

Originalmente se planteó un casino con juegos interactivos (tragamonedas, ruleta, blackjack) donde Python mostraba menús y Prolog recomendaba en vivo. Se decidió simplificar a:

- **Prolog:** Contiene datos fijos de jugadores (30 campos c/u) + 25+ reglas de inferencia
- **Python:** Solo consulta a Prolog via pyswip y muestra resultados bonitos para empleados
- **Sin login, sin formularios, sin datos en tiempo real** — todo es estático por ahora

### 3. Datos por Jugador (30 campos)

Organizados en 6 grupos:

**Identificación:** id, nombre, edad, ocupacion
**Sesión Actual:** juego_actual, monto_apuesta, resultado_ultima_ronda, rondas_jugadas_hoy, tiempo_en_casino_hoy, hora_actual
**Económico:** presupuesto_hoy, fichas_actuales, gasto_hoy, gasto_promedio_ronda, gasto_maximo_historico, perdidas_acumuladas, ganancias_acumuladas
**Comportamiento:** prefiere_azar_o_estrategia, prefiere_rapido_o_lento, cambia_al_perder, cambia_al_ganar, juega_solo, reinvierte_ganancias, acepta_recomendaciones
**Historial de Visitas:** frecuencia_semanal, tiempo_promedio_visita, horario_habitual, dias_visita, total_visitas, dias_desde_primera_visita, dias_desde_ultima_visita
**Preferencias:** juego_favorito, variedad_juegos_probados

### 4. Clasificaciones de Jugadores (5 tipos)

| Clasificación | Significado | Acción |
|---|---|---|
| VIP | Alto valor, viene seguido, gasta bien | Invitar a eventos exclusivos |
| Retener | Dejó de venir, riesgo de pérdida | Ofrecer bono de retorno |
| Cuidar | Gasta mucho, muy joven, muchas horas | Sugerir descanso, monitorear |
| Servicio_Rápido | Prefiere ritmo rápido, poco tiempo | Atender con prioridad |
| *(normal)* | Sin clasificación especial | Seguimiento normal |

### 5. Reglas Pendientes en Prolog (25+)

Faltan implementar en los archivos `.pl`:

**VIP (5+ reglas):** frecuencia ≥ 3x/sem, gasto max historico ≥ 100, ganancias acumuladas altas, antigüedad > 1 año, trajo referidos
**Retener (5+ reglas):** días desde última visita > 30, frecuencia disminuyó, pérdidas acumuladas altas, antes venía seguido
**Cuidar (5+ reglas):** edad < 25, tiempo en casino ≥ 4hrs, gasto_hoy ≥ 80% presupuesto, pérdidas >> ganancias
**Recomendar (10+ reglas):** azar→tragamonedas/ruleta, estrategia→blackjack, rápido→tragamonedas, lento→ruleta/blackjack, etc.

---

## 🗂️ ESTRUCTURA ACTUAL DE ARCHIVOS

```
C:\Users\yalli\OneDrive\Desktop\casino_sapiens/
│
├── README.md                      ← Este archivo (contexto completo)
│
├── python/                        ← TODO FUNCIONAL
│   ├── ventana_usuarios.py        ← Dashboard completo con 5 paneles
│   ├── main.py                    ← (vacío - pendiente)
│   ├── consultas.py               ← (vacío - pendiente de conectar pyswip)
│   ├── ventana_vip.py             ← (vacío - pendiente)
│   ├── ventana_retener.py         ← (vacío - pendiente)
│   ├── ventana_detener.py         ← (vacío - pendiente)
│   └── ventana_recomendar.py      ← (vacío - pendiente)
│
└── prolog/                        ← TODO VACÍO (pendiente de escribir)
    ├── casino.pl                  ← Archivo principal (consulta módulos)
    ├── hechos.pl                  ← 30 datos x 6+ jugadores de prueba
    ├── reglas_vip.pl              ← Reglas: clientes VIP
    ├── reglas_retener.pl          ← Reglas: clientes en riesgo
    ├── reglas_detener.pl          ← Reglas: jugadores a detener/cuidar
    └── reglas_recomendar.pl       ← Reglas: qué juego recomendar
```

---

## ✅ LO QUE ESTÁ HECHO

### Software Instalado
| Herramienta | Versión | Ruta |
|---|---|---|
| Python 3 | 3.13.3 | `C:\Users\yalli\AppData\Local\Programs\Python\Python313\python.exe` |
| pip | 25.0.1 | Viene con Python |
| pyswip | 0.3.3 | `pip install pyswip` |
| SWI-Prolog | 9.2.9 | `C:\Users\yalli\AppData\Local\Programs\SWI-Prolog\bin\swipl.exe` |
| Git | 2.54.0 | Ya venía instalado |

### Fix aplicado
Se reordenó el PATH de usuario para que Python real esté antes que `WindowsApps` (los stubs de Microsoft Store). Si `python --version` no funciona, ejecutar:
```powershell
$env:Path = [Environment]::GetEnvironmentVariable("Path", "User") + ";" + [Environment]::GetEnvironmentVariable("Path", "Machine")
```

### Interfaz Python (ventana_usuarios.py)
- Ventana maximizada con sidebar de navegación (5 opciones)
- Panel **Todos los Usuarios**: tabla + detalle expandible con 30 campos
- Panel **Invitar a VIP**: tarjetas con botón de invitación
- Panel **Personas a Retener**: tarjetas con bono de retorno
- Panel **Personas a Cuidar**: alertas automáticas + botones de acción
- Panel **Servicio Rápido**: prioridades + atención rápida
- Colores rojos análogos minimalistas (fondo gris claro, sidebar rojo oscuro, acentos rojos)
- 6 jugadores mock con datos completos
- Sin conexión a Prolog aún (datos hardcodeados)

---

## ❌ LO QUE FALTA HACER

### 1. Rellenar archivos Prolog (hechos + reglas)

**hechos.pl:** Convertir los 6 jugadores mock de Python a hechos Prolog usando los 6 predicados definidos:
```prolog
jugador(+Id, +Nombre, +Edad, +Ocupacion).
economia(+Id, +PresupuestoHoy, +FichasActuales, +GastoHoy,
         +GastoPromedioRonda, +GastoMaximoHistorico,
         +PerdidasAcumuladas, +GananciasAcumuladas).
comportamiento(+Id, +TipoPreferido, +RitmoPreferido,
               +CambiaAlPerder, +CambiaAlGanar,
               +ReinvierteGanancias, +JuegaSolo,
               +AceptaRecomendaciones).
sesion(+Id, +JuegoActual, +MontoApuesta, +ResultadoUltimaRonda,
        +RondasJugadasHoy, +HorasEnCasinoHoy, +HoraActual).
visitas(+Id, +FrecuenciaSemanal, +TiempoPromedio, +HorarioHabitual,
         +DiasFavoritos, +TotalVisitas, +DiasDesdePrimeraVisita,
         +DiasDesdeUltimaVisita).
preferencias(+Id, +JuegoFavorito, +VariedadProbada).
```

**reglas_vip.pl:** 
```prolog
vip(Id) :- visitas(Id, Freq, _, _, _, _, _, _), Freq >= 3.
vip(Id) :- economia(Id, _, _, _, _, GastoMax, _, _), GastoMax >= 100.
% + más reglas
```

**reglas_retener.pl:**
```prolog
en_riesgo_irse(Id) :- visitas(Id, _, _, _, _, _, _, DiasUltima), DiasUltima > 30.
```

**reglas_cuidar.pl** (o en reglas_detener.pl):
```prolog
detener_juego(Id) :- sesion(Id, _, _, _, _, Horas, _), Horas >= 4.
```

**reglas_recomendar.pl:**
```prolog
recomendar_juego(Id, tragamonedas) :- comportamiento(Id, azar, rapido, _, _, _, _, _).
```

### 2. Conectar Python con Prolog

En `consultas.py` o directamente en `ventana_usuarios.py`, reemplazar los datos mock con consultas via pyswip:
```python
from pyswip import Prolog
prolog = Prolog()
prolog.consult("../prolog/casino.pl")
resultado = list(prolog.query("lista_vip(Lista)"))
```

### 3. Refinamientos

- Agregar más jugadores de prueba (8-10)
- Agregar más reglas hasta completar 25+
- Probar que al cambiar una regla en Prolog, el comportamiento de Python cambie
- Preparar 3 casos de prueba para la presentación

---

## 🚀 CÓMO EJECUTAR (estado actual)

```powershell
# 1. Activar PATH correcto
$env:Path = [Environment]::GetEnvironmentVariable("Path", "User") + ";"
$env:Path += [Environment]::GetEnvironmentVariable("Path", "Machine")

# 2. Ir a la carpeta
cd C:\Users\yalli\OneDrive\Desktop\casino_sapiens\python

# 3. Ejecutar
python ventana_usuarios.py
```

Para verificar que pyswip funciona:
```powershell
python -c "from pyswip import Prolog; p = Prolog(); print('pyswip OK')"
```

Para verificar SWI-Prolog:
```powershell
& "$env:LOCALAPPDATA\Programs\SWI-Prolog\bin\swipl.exe" --version
```

---

## 🧠 TEMAS DEL SÍLABO CUBIERTOS

| Tema | Dónde se aplicará |
|---|---|
| Átomos, constantes | `tragamonedas`, `VIP`, `j1` en hechos Prolog |
| Predicados | `jugador/4`, `vip/1`, `recomendar_juego/2` |
| Reglas | Todo en `reglas_*.pl` con `:-` |
| Unificación | Prolog matchea consultas como `recomendar_juego(j1, X)` |
| Control de ejecución | Orden de reglas, uso de `!` (cut) si necesario |
| Listas | `findall` para listar VIPs, lista de días de visita |
| Indeterminismo | Múltiples reglas que pueden aplicar al mismo jugador |
| Python: clases | `AplicacionCasino`, paneles como clases |
| Python: tkinter | Interfaz gráfica completa |

---

## 📝 NOTAS PARA CONTINUAR

1. **No se usa Chocolatey** — no tiene permisos de admin. Todo se instaló manual.
2. **El archivo principal de Python** es `ventana_usuarios.py` (no `main.py`).
3. **Los archivos separados** (`ventana_vip.py`, `ventana_retener.py`, etc.) están vacíos — todo está dentro de `ventana_usuarios.py`.
4. **Después de escribir Prolog**, migrar las consultas de datos mock a consultas pyswip.
5. **La clasificación "Detener"** se renombró a "Cuidar" en la interfaz (enfoque más ético).
6. **Para la presentación:** preparar 3 casos de prueba (principiante, VIP, riesgo) mostrando cómo cambiar una regla Prolog cambia el resultado.

---

*Última actualización: 05/06/2026*
