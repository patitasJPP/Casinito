% casino.pl - Archivo principal del sistema experto
% Consulta todos los modulos y define meta-predicados para Python

:- consult('hechos.pl').
:- consult('reglas_vip.pl').
:- consult('reglas_retener.pl').
:- consult('reglas_detener.pl').
:- consult('reglas_recomendar.pl').

% Meta-predicados: listas completas para consultas desde Python

lista_vip(Lista)     :- findall(Id, vip(Id), Lista).
lista_retener(Lista) :- findall(Id, en_riesgo_irse(Id), Lista).
lista_cuidar(Lista)  :- findall(Id, detener_juego(Id), Lista).

% Clasificacion combinada: devuelve Id y su clasificacion
clasificacion(Id, vip)    :- vip(Id).
clasificacion(Id, retener) :- en_riesgo_irse(Id).
clasificacion(Id, cuidar)  :- detener_juego(Id).

% Datos completos de un jugador (para que Python construya el dashboard)
datos_jugador(Id, Nombre, Edad, Ocupacion, Presupuesto, Fichas, GastoHoy,
              GastoProm, GastoMax, Perdidas, Ganancias, JuegoActual,
              MontoApuesta, Resultado, RondasHoy, TiempoCasino, HoraActual,
              Frecuencia, TiempoProm, Horario, TotalVisitas, DiasPrimera,
              DiasUltima, JuegoFav, Variedad, PrefJuego, Ritmo,
              CambiaPierde, CambiaGana, JuegaSolo, Reinvierte, AceptaRec) :-
    jugador(Id, Nombre, Edad, Ocupacion),
    economia(Id, Presupuesto, Fichas, GastoHoy, GastoProm, GastoMax, Perdidas, Ganancias),
    sesion(Id, JuegoActual, MontoApuesta, Resultado, RondasHoy, TiempoCasino, HoraActual),
    visitas(Id, Frecuencia, TiempoProm, Horario, _, TotalVisitas, DiasPrimera, DiasUltima),
    preferencias(Id, JuegoFav, Variedad),
    comportamiento(Id, PrefJuego, Ritmo, CambiaPierde, CambiaGana, Reinvierte, JuegaSolo, AceptaRec).
