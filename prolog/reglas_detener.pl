% reglas_detener.pl - Jugadores que requieren supervision/intervencion
% Un jugador necesita intervencion si cumple AL MENOS UNA:

% 1. Edad < 25 (menor de edad o muy joven)
detener_juego(Id) :- jugador(Id, _, Edad, _), Edad < 25.

% 2. Horas en casino hoy >= 4 (tiempo excesivo)
detener_juego(Id) :- sesion(Id, _, _, _, _, Horas, _), Horas >= 4.

% 3. Gasto hoy >= 80% del presupuesto del dia
detener_juego(Id) :- economia(Id, Presup, _, Gasto, _, _, _, _),
                      Presup > 0, Gasto >= Presup * 0.8.

% 4. Perdidas acumuladas > 2x ganancias acumuladas
detener_juego(Id) :- economia(Id, _, _, _, _, _, Perdidas, Ganancias),
                      Ganancias > 0, Perdidas > Ganancias * 2.

% 5. Juega solo y perdidas acumuladas > 200 (perfil de riesgo)
detener_juego(Id) :- comportamiento(Id, _, _, _, _, _, JuegaSolo, _),
                      JuegaSolo = si,
                      economia(Id, _, _, _, _, _, Perdidas, _), Perdidas > 200.
