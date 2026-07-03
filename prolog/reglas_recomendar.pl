% reglas_recomendar.pl - Recomendacion de juegos segun perfil
% recomendar(Id, Juego) significa que ese juego es adecuado para el jugador

% Azar + Rapido -> Tragamonedas (accion inmediata, sin estrategia)
recomendar(Id, tragamonedas) :- comportamiento(Id, azar, rapido, _, _, _, _, _).

% Estrategia -> Blackjack (requiere habilidad y decision)
recomendar(Id, blackjack) :- comportamiento(Id, estrategia, _, _, _, _, _, _).

% Azar + Lento -> Ruleta (ritmo pausado, suerte)
recomendar(Id, ruleta) :- comportamiento(Id, azar, lento, _, _, _, _, _).

% Si juega favorito tragamonedas y es azar -> tragamonedas
recomendar(Id, tragamonedas) :- comportamiento(Id, azar, _, _, _, _, _, _),
                                 preferencias(Id, tragamonedas, _).

% Reinvierte ganancias -> Blackjack (puede sostener juego de estrategia)
recomendar(Id, blackjack) :- comportamiento(Id, _, _, _, _, si, _, _).

% Ritmo lento (sin importar azar/estrategia) -> Ruleta o Blackjack
recomendar(Id, ruleta)    :- comportamiento(Id, _, lento, _, _, _, _, _).
recomendar(Id, blackjack) :- comportamiento(Id, _, lento, _, _, _, _, _).

% Cambia al perder + Cambia al ganar -> Tragamonedas (busca emocion rapida)
recomendar(Id, tragamonedas) :- comportamiento(Id, _, _, si, si, _, _, _).

% Juega solo + Azar -> Tragamonedas (no necesita interaccion social)
recomendar(Id, tragamonedas) :- comportamiento(Id, azar, _, _, _, _, JuegaSolo, _),
                                 JuegaSolo = si.
