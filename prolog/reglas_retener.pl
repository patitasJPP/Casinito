% reglas_retener.pl - Clientes en riesgo de irse
% Un jugador necesita retencion si cumple AL MENOS UNA:

% 1. Mas de 30 dias sin visitar
en_riesgo_irse(Id) :- visitas(Id, _, _, _, _, _, _, DiasUlt), DiasUlt > 30.

% 2. Frecuencia baja (< 2) a pesar de tener historial (total visitas > 10)
en_riesgo_irse(Id) :- visitas(Id, Freq, _, _, _, TotalVis, _, _),
                       Freq < 2, TotalVis > 10.

% 3. Perdidas acumuladas >= 3000 (frustracion economica)
en_riesgo_irse(Id) :- economia(Id, _, _, _, _, _, Perdidas, _), Perdidas >= 3000.

% 4. Edad > 50 y mas de 14 dias sin venir (perfil mayor se desanima rapido)
en_riesgo_irse(Id) :- jugador(Id, _, Edad, _), Edad > 50,
                       visitas(Id, _, _, _, _, _, _, DiasUlt), DiasUlt > 14.

% 5. Gasto promedio bajo (< 10) comparado con su presupuesto historico
en_riesgo_irse(Id) :- economia(Id, _, _, _, GastoProm, _, _, _),
                       GastoProm < 10,
                       visitas(Id, _, _, _, _, TotalVis, _, _), TotalVis < 30.
