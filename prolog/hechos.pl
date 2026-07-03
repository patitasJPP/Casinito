% hechos.pl - Base de hechos: 8 jugadores con 30 campos c/u
% Organizados en 6 predicados: jugador, economia, comportamiento, sesion, visitas, preferencias

jugador(j1, 'Carlos', 45, ingeniero).
jugador(j2, 'Maria',  28, docente).
jugador(j3, 'Jorge',  52, empresario).
jugador(j4, 'Lucia',  22, estudiante).
jugador(j5, 'Pedro',  38, abogado).
jugador(j6, 'Ana',    48, medico).
jugador(j7, 'Rosa',   55, disenadora).
jugador(j8, 'Luis',   19, estudiante).

economia(j1, 500,  200, 300, 50,  200, 5000, 3000).
economia(j2, 200,  50,  150, 20,  80,  800,  200).
economia(j3, 1000, 800, 200, 100, 500, 2000, 8000).
economia(j4, 50,   5,   45,  5,   20,  300,  50).
economia(j5, 300,  100, 200, 30,  100, 1500, 2000).
economia(j6, 800,  600, 200, 80,  300, 500,  4000).
economia(j7, 400,  250, 350, 60,  150, 3000, 1000).
economia(j8, 30,   2,   25,  3,   10,  100,  10).

comportamiento(j1, azar,       rapido,  si, no, si, no, si).
comportamiento(j2, azar,       lento,   si, si, no, si, si).
comportamiento(j3, estrategia, lento,   no, no, si, no, no).
comportamiento(j4, azar,       rapido,  si, si, no, si, si).
comportamiento(j5, azar,       rapido,  si, no, si, no, si).
comportamiento(j6, estrategia, lento,   no, no, si, no, si).
comportamiento(j7, estrategia, rapido,  si, no, si, si, si).
comportamiento(j8, azar,       rapido,  si, si, no, si, si).

sesion(j1, tragamonedas, 50,   gano,  15, 2.5, '22:00').
sesion(j2, ruleta,       20,   perdio, 8, 1.0, '20:00').
sesion(j3, blackjack,    100,  gano,  20, 3.0, '21:30').
sesion(j4, tragamonedas, 5,    perdio, 30, 4.5, '23:00').
sesion(j5, ruleta,       30,   gano,  10, 1.5, '19:00').
sesion(j6, blackjack,    80,   gano,   3, 0.5, '18:00').
sesion(j7, ruleta,       70,   perdio, 12, 2.0, '20:30').
sesion(j8, tragamonedas, 2,    perdio, 25, 5.0, '01:00').

visitas(j1, 3, 180, nocturno, [viernes,sabado],           120, 365, 2).
visitas(j2, 1, 90,  tarde,    [sabado],                   15,  60,  35).
visitas(j3, 5, 240, nocturno, [lunes,martes,miercoles,jueves,viernes], 300, 800, 1).
visitas(j4, 2, 120, noche,    [sabado,domingo],           20,  45,  1).
visitas(j5, 2, 150, tarde,    [jueves,viernes],           60,  180, 5).
visitas(j6, 4, 120, tarde,    [martes,jueves,sabado],     200, 500, 1).
visitas(j7, 3, 200, noche,    [miercoles,viernes,sabado], 90,  300, 15).
visitas(j8, 1, 180, madrugada,[domingo],                  8,   30,  1).

preferencias(j1, tragamonedas, 3).
preferencias(j2, ruleta,       2).
preferencias(j3, blackjack,    4).
preferencias(j4, tragamonedas, 1).
preferencias(j5, ruleta,       3).
preferencias(j6, blackjack,    2).
preferencias(j7, ruleta,       5).
preferencias(j8, tragamonedas, 1).
