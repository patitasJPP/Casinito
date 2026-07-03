% reglas_vip.pl - Clasificacion VIP
% Un jugador es VIP si cumple AL MENOS UNA de estas condiciones:

% 1. Frecuencia semanal >= 3 visitas
vip(Id) :- visitas(Id, Freq, _, _, _, _, _, _), Freq >= 3.

% 2. Gasto maximo historico >= 100
vip(Id) :- economia(Id, _, _, _, _, GastoMax, _, _), GastoMax >= 100.

% 3. Ganancias acumuladas >= 3000
vip(Id) :- economia(Id, _, _, _, _, _, _, Ganancias), Ganancias >= 3000.

% 4. Antiguedad > 1 anio (365 dias) y visitas totales > 100
vip(Id) :- visitas(Id, _, _, _, _, TotalVis, DiasPrimera, _),
           DiasPrimera > 365, TotalVis > 100.

% 5. Edad >= 40 y perdidas acumuladas >= 2000 (jugador veterano que gasta)
vip(Id) :- jugador(Id, _, Edad, _), Edad >= 40,
           economia(Id, _, _, _, _, _, Perdidas, _), Perdidas >= 2000.
