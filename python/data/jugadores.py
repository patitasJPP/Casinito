from consultas import prolog_disponible,obtener_datos_jugador,clasificar_jugador

JUGADORES_MOCK=[
{
"id":"j1","nombre":"Carlos","edad":45,"ocupacion":"Ingeniero",
"presupuesto_hoy":500,"fichas_actuales":200,"juego_actual":"Tragamonedas",
"monto_apuesta":50,"resultado_ultima_ronda":"Ganó","tiempo_en_casino_hoy":2.5,
"hora_actual":"22:00","rondas_jugadas_hoy":15,"gasto_hoy":300,
"frecuencia_semanal":3,"tiempo_promedio_visita":180,"horario_habitual":"Nocturno",
"prefiere_azar_o_estrategia":"Azar","prefiere_rapido_o_lento":"Rápido",
"cambia_al_perder":"Sí","cambia_al_ganar":"No","gasto_promedio_ronda":50,
"gasto_maximo_historico":200,"perdidas_acumuladas":5000,
"ganancias_acumuladas":3000,"variedad_juegos_probados":3,
"juego_favorito":"Tragamonedas","dias_visita":"Vie,Sáb",
"juega_solo":"No","reinvierte_ganancias":"Sí","acepta_recomendaciones":"Sí",
"total_visitas":120,"dias_desde_primera_visita":365,"dias_desde_ultima_visita":2,
"clasificacion":"VIP"
},
{
"id":"j2","nombre":"María","edad":28,"ocupacion":"Docente",
"presupuesto_hoy":200,"fichas_actuales":50,"juego_actual":"Ruleta",
"monto_apuesta":20,"resultado_ultima_ronda":"Perdió","tiempo_en_casino_hoy":1.0,
"hora_actual":"20:00","rondas_jugadas_hoy":8,"gasto_hoy":150,
"frecuencia_semanal":1,"tiempo_promedio_visita":90,"horario_habitual":"Tarde",
"prefiere_azar_o_estrategia":"Azar","prefiere_rapido_o_lento":"Lento",
"cambia_al_perder":"Sí","cambia_al_ganar":"Sí","gasto_promedio_ronda":20,
"gasto_maximo_historico":80,"perdidas_acumuladas":800,
"ganancias_acumuladas":200,"variedad_juegos_probados":2,
"juego_favorito":"Ruleta","dias_visita":"Sáb",
"juega_solo":"Sí","reinvierte_ganancias":"No","acepta_recomendaciones":"Sí",
"total_visitas":15,"dias_desde_primera_visita":60,"dias_desde_ultima_visita":35,
"clasificacion":"Retener"
},
{
"id":"j3","nombre":"Jorge","edad":52,"ocupacion":"Empresario",
"presupuesto_hoy":1000,"fichas_actuales":800,"juego_actual":"Blackjack",
"monto_apuesta":100,"resultado_ultima_ronda":"Ganó","tiempo_en_casino_hoy":3.0,
"hora_actual":"21:30","rondas_jugadas_hoy":20,"gasto_hoy":200,
"frecuencia_semanal":5,"tiempo_promedio_visita":240,"horario_habitual":"Nocturno",
"prefiere_azar_o_estrategia":"Estrategia","prefiere_rapido_o_lento":"Lento",
"cambia_al_perder":"No","cambia_al_ganar":"No","gasto_promedio_ronda":100,
"gasto_maximo_historico":500,"perdidas_acumuladas":2000,
"ganancias_acumuladas":8000,"variedad_juegos_probados":4,
"juego_favorito":"Blackjack","dias_visita":"LunaVie",
"juega_solo":"No","reinvierte_ganancias":"Sí","acepta_recomendaciones":"No",
"total_visitas":300,"dias_desde_primera_visita":800,"dias_desde_ultima_visita":1,
"clasificacion":"VIP"
},
{
"id":"j4","nombre":"Lucía","edad":22,"ocupacion":"Estudiante",
"presupuesto_hoy":50,"fichas_actuales":5,"juego_actual":"Tragamonedas",
"monto_apuesta":5,"resultado_ultima_ronda":"Perdió","tiempo_en_casino_hoy":4.5,
"hora_actual":"23:00","rondas_jugadas_hoy":30,"gasto_hoy":45,
"frecuencia_semanal":2,"tiempo_promedio_visita":120,"horario_habitual":"Noche",
"prefiere_azar_o_estrategia":"Azar","prefiere_rapido_o_lento":"Rápido",
"cambia_al_perder":"Sí","cambia_al_ganar":"Sí","gasto_promedio_ronda":5,
"gasto_maximo_historico":20,"perdidas_acumuladas":300,
"ganancias_acumuladas":50,"variedad_juegos_probados":1,
"juego_favorito":"Tragamonedas","dias_visita":"Sáb,Dom",
"juega_solo":"Sí","reinvierte_ganancias":"No","acepta_recomendaciones":"Sí",
"total_visitas":20,"dias_desde_primera_visita":45,"dias_desde_ultima_visita":1,
"clasificacion":"Cuidar"
},
{
"id":"j5","nombre":"Pedro","edad":38,"ocupacion":"Abogado",
"presupuesto_hoy":300,"fichas_actuales":100,"juego_actual":"Ruleta",
"monto_apuesta":30,"resultado_ultima_ronda":"Ganó","tiempo_en_casino_hoy":1.5,
"hora_actual":"19:00","rondas_jugadas_hoy":10,"gasto_hoy":200,
"frecuencia_semanal":2,"tiempo_promedio_visita":150,"horario_habitual":"Tarde",
"prefiere_azar_o_estrategia":"Azar","prefiere_rapido_o_lento":"Rápido",
"cambia_al_perder":"Sí","cambia_al_ganar":"No","gasto_promedio_ronda":30,
"gasto_maximo_historico":100,"perdidas_acumuladas":1500,
"ganancias_acumuladas":2000,"variedad_juegos_probados":3,
"juego_favorito":"Ruleta","dias_visita":"Jue,Vie",
"juega_solo":"Sí","reinvierte_ganancias":"No","acepta_recomendaciones":"Sí",
"total_visitas":60,"dias_desde_primera_visita":180,"dias_desde_ultima_visita":5,
"clasificacion":"Servicio_Rapido"
},
{
"id":"j6","nombre":"Ana","edad":48,"ocupacion":"Médico",
"presupuesto_hoy":800,"fichas_actuales":600,"juego_actual":"Blackjack",
"monto_apuesta":80,"resultado_ultima_ronda":"Ganó","tiempo_en_casino_hoy":0.5,
"hora_actual":"18:00","rondas_jugadas_hoy":3,"gasto_hoy":200,
"frecuencia_semanal":4,"tiempo_promedio_visita":120,"horario_habitual":"Tarde",
"prefiere_azar_o_estrategia":"Estrategia","prefiere_rapido_o_lento":"Lento",
"cambia_al_perder":"No","cambia_al_ganar":"No","gasto_promedio_ronda":80,
"gasto_maximo_historico":300,"perdidas_acumuladas":500,
"ganancias_acumuladas":4000,"variedad_juegos_probados":2,
"juego_favorito":"Blackjack","dias_visita":"Mar,Jue,Sáb",
"juega_solo":"No","reinvierte_ganancias":"Sí","acepta_recomendaciones":"Sí",
"total_visitas":200,"dias_desde_primera_visita":500,"dias_desde_ultima_visita":1,
"clasificacion":"VIP"
},
{
"id":"j7","nombre":"Rosa","edad":55,"ocupacion":"Diseñadora",
"presupuesto_hoy":400,"fichas_actuales":250,"juego_actual":"Ruleta",
"monto_apuesta":60,"resultado_ultima_ronda":"Perdió","tiempo_en_casino_hoy":2.0,
"hora_actual":"20:30","rondas_jugadas_hoy":12,"gasto_hoy":350,
"frecuencia_semanal":3,"tiempo_promedio_visita":200,"horario_habitual":"Noche",
"prefiere_azar_o_estrategia":"Estrategia","prefiere_rapido_o_lento":"Rápido",
"cambia_al_perder":"Sí","cambia_al_ganar":"No","gasto_promedio_ronda":60,
"gasto_maximo_historico":150,"perdidas_acumuladas":3000,
"ganancias_acumuladas":1000,"variedad_juegos_probados":5,
"juego_favorito":"Ruleta","dias_visita":"Mié,Vie,Sáb",
"juega_solo":"Sí","reinvierte_ganancias":"Sí","acepta_recomendaciones":"Sí",
"total_visitas":90,"dias_desde_primera_visita":300,"dias_desde_ultima_visita":15,
"clasificacion":"Retener"
},
{
"id":"j8","nombre":"Luis","edad":19,"ocupacion":"Estudiante",
"presupuesto_hoy":30,"fichas_actuales":2,"juego_actual":"Tragamonedas",
"monto_apuesta":2,"resultado_ultima_ronda":"Perdió","tiempo_en_casino_hoy":5.0,
"hora_actual":"01:00","rondas_jugadas_hoy":25,"gasto_hoy":25,
"frecuencia_semanal":1,"tiempo_promedio_visita":180,"horario_habitual":"Madrugada",
"prefiere_azar_o_estrategia":"Azar","prefiere_rapido_o_lento":"Rápido",
"cambia_al_perder":"Sí","cambia_al_ganar":"Sí","gasto_promedio_ronda":3,
"gasto_maximo_historico":10,"perdidas_acumuladas":100,
"ganancias_acumuladas":10,"variedad_juegos_probados":1,
"juego_favorito":"Tragamonedas","dias_visita":"Dom",
"juega_solo":"Sí","reinvierte_ganancias":"No","acepta_recomendaciones":"Sí",
"total_visitas":8,"dias_desde_primera_visita":30,"dias_desde_ultima_visita":1,
"clasificacion":"Cuidar"
},


{

"id":"j101",

"nombre":"MiguelAlvarez",

"edad":62,

"ocupacion":"Chofer",

"presupuesto_hoy":1835,

"fichas_actuales":1224,

"juego_actual":"Ruleta",

"monto_apuesta":152,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"17:57",

"rondas_jugadas_hoy":32,

"gasto_hoy":608,

"frecuencia_semanal":7,

"tiempo_promedio_visita":234,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":424,

"perdidas_acumuladas":7506,

"ganancias_acumuladas":18135,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Vie,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":96,

"dias_desde_primera_visita":1128,

"dias_desde_ultima_visita":35,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j102",

"nombre":"MarioLopez",

"edad":28,

"ocupacion":"Disenador",

"presupuesto_hoy":1753,

"fichas_actuales":179,

"juego_actual":"Cartas",

"monto_apuesta":175,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"20:06",

"rondas_jugadas_hoy":22,

"gasto_hoy":1566,

"frecuencia_semanal":7,

"tiempo_promedio_visita":212,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":71,

"gasto_maximo_historico":86,

"perdidas_acumuladas":6260,

"ganancias_acumuladas":14927,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Sab,Vie,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":406,

"dias_desde_primera_visita":1259,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j103",

"nombre":"EduardoCruz",

"edad":70,

"ocupacion":"Arquitecto",

"presupuesto_hoy":730,

"fichas_actuales":591,

"juego_actual":"Blackjack",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.7,

"hora_actual":"16:54",

"rondas_jugadas_hoy":12,

"gasto_hoy":117,

"frecuencia_semanal":0,

"tiempo_promedio_visita":224,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":978,

"perdidas_acumuladas":6665,

"ganancias_acumuladas":18161,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Lun,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":248,

"dias_desde_primera_visita":503,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j104",

"nombre":"SergioTorres",

"edad":21,

"ocupacion":"Abogado",

"presupuesto_hoy":915,

"fichas_actuales":872,

"juego_actual":"Ruleta",

"monto_apuesta":128,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"13:56",

"rondas_jugadas_hoy":34,

"gasto_hoy":32,

"frecuencia_semanal":0,

"tiempo_promedio_visita":241,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":149,

"perdidas_acumuladas":1538,

"ganancias_acumuladas":18629,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Jue,Mie,Vie,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":474,

"dias_desde_primera_visita":694,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j105",

"nombre":"AngelVargas",

"edad":38,

"ocupacion":"Enfermero",

"presupuesto_hoy":1786,

"fichas_actuales":1133,

"juego_actual":"Blackjack",

"monto_apuesta":182,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.0,

"hora_actual":"15:24",

"rondas_jugadas_hoy":28,

"gasto_hoy":630,

"frecuencia_semanal":0,

"tiempo_promedio_visita":283,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":22,

"gasto_maximo_historico":687,

"perdidas_acumuladas":4128,

"ganancias_acumuladas":8749,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie,Dom,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":2,

"dias_desde_primera_visita":1126,

"dias_desde_ultima_visita":46,

"clasificacion":"Retener",

},

{

"id":"j106",

"nombre":"FelipeCruz",

"edad":20,

"ocupacion":"Cocinero",

"presupuesto_hoy":679,

"fichas_actuales":139,

"juego_actual":"Poker",

"monto_apuesta":157,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.8,

"hora_actual":"21:58",

"rondas_jugadas_hoy":34,

"gasto_hoy":524,

"frecuencia_semanal":7,

"tiempo_promedio_visita":224,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":984,

"perdidas_acumuladas":8860,

"ganancias_acumuladas":11214,

"variedad_juegos_probados":6,

"juego_favorito":"Poker",

"dias_visita":"Vie,Dom,Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":447,

"dias_desde_primera_visita":617,

"dias_desde_ultima_visita":9,

"clasificacion":"Cuidar",

},

{

"id":"j107",

"nombre":"NataliaMendoza",

"edad":34,

"ocupacion":"Docente",

"presupuesto_hoy":1480,

"fichas_actuales":204,

"juego_actual":"Ruleta",

"monto_apuesta":144,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"15:02",

"rondas_jugadas_hoy":29,

"gasto_hoy":1261,

"frecuencia_semanal":4,

"tiempo_promedio_visita":282,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":656,

"perdidas_acumuladas":144,

"ganancias_acumuladas":8889,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Jue,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":296,

"dias_desde_primera_visita":150,

"dias_desde_ultima_visita":6,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j108",

"nombre":"ManuelCastillo",

"edad":57,

"ocupacion":"Enfermero",

"presupuesto_hoy":333,

"fichas_actuales":82,

"juego_actual":"Blackjack",

"monto_apuesta":59,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"16:38",

"rondas_jugadas_hoy":13,

"gasto_hoy":236,

"frecuencia_semanal":5,

"tiempo_promedio_visita":286,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":18,

"gasto_maximo_historico":621,

"perdidas_acumuladas":12224,

"ganancias_acumuladas":12162,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Jue,Mar,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":303,

"dias_desde_primera_visita":1287,

"dias_desde_ultima_visita":21,

"clasificacion":"Cuidar",

},

{

"id":"j109",

"nombre":"MartinFlores",

"edad":56,

"ocupacion":"Desempleado",

"presupuesto_hoy":1324,

"fichas_actuales":773,

"juego_actual":"Poker",

"monto_apuesta":103,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.2,

"hora_actual":"11:50",

"rondas_jugadas_hoy":19,

"gasto_hoy":548,

"frecuencia_semanal":5,

"tiempo_promedio_visita":103,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":28,

"gasto_maximo_historico":91,

"perdidas_acumuladas":4351,

"ganancias_acumuladas":14715,

"variedad_juegos_probados":2,

"juego_favorito":"Poker",

"dias_visita":"Sab,Lun,Mar,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":327,

"dias_desde_primera_visita":257,

"dias_desde_ultima_visita":16,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j110",

"nombre":"LuciaVazquez",

"edad":49,

"ocupacion":"Cocinero",

"presupuesto_hoy":1405,

"fichas_actuales":160,

"juego_actual":"Cartas",

"monto_apuesta":189,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.6,

"hora_actual":"16:38",

"rondas_jugadas_hoy":31,

"gasto_hoy":1229,

"frecuencia_semanal":0,

"tiempo_promedio_visita":298,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":39,

"gasto_maximo_historico":886,

"perdidas_acumuladas":8373,

"ganancias_acumuladas":1366,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":1,

"dias_desde_primera_visita":530,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j111",

"nombre":"JuliaMartinez",

"edad":51,

"ocupacion":"Pintor",

"presupuesto_hoy":1279,

"fichas_actuales":261,

"juego_actual":"Tragamonedas",

"monto_apuesta":45,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.3,

"hora_actual":"17:19",

"rondas_jugadas_hoy":23,

"gasto_hoy":1006,

"frecuencia_semanal":6,

"tiempo_promedio_visita":233,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":294,

"perdidas_acumuladas":9488,

"ganancias_acumuladas":4580,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mie,Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":187,

"dias_desde_primera_visita":1012,

"dias_desde_ultima_visita":14,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j112",

"nombre":"VictoriaTorres",

"edad":37,

"ocupacion":"Desempleado",

"presupuesto_hoy":256,

"fichas_actuales":138,

"juego_actual":"Cartas",

"monto_apuesta":10,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"21:05",

"rondas_jugadas_hoy":6,

"gasto_hoy":104,

"frecuencia_semanal":6,

"tiempo_promedio_visita":314,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":17,

"gasto_maximo_historico":899,

"perdidas_acumuladas":9374,

"ganancias_acumuladas":5971,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":497,

"dias_desde_primera_visita":1439,

"dias_desde_ultima_visita":40,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j113",

"nombre":"LuisFlores",

"edad":40,

"ocupacion":"Desempleado",

"presupuesto_hoy":699,

"fichas_actuales":369,

"juego_actual":"Dados",

"monto_apuesta":81,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.3,

"hora_actual":"18:38",

"rondas_jugadas_hoy":10,

"gasto_hoy":310,

"frecuencia_semanal":7,

"tiempo_promedio_visita":360,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":326,

"perdidas_acumuladas":13438,

"ganancias_acumuladas":14128,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Mie,Sab,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":212,

"dias_desde_primera_visita":1439,

"dias_desde_ultima_visita":17,

"clasificacion":"Cuidar",

},

{

"id":"j114",

"nombre":"CarlaFlores",

"edad":60,

"ocupacion":"Medico",

"presupuesto_hoy":657,

"fichas_actuales":162,

"juego_actual":"Tragamonedas",

"monto_apuesta":4,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"20:34",

"rondas_jugadas_hoy":18,

"gasto_hoy":491,

"frecuencia_semanal":2,

"tiempo_promedio_visita":151,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":27,

"gasto_maximo_historico":349,

"perdidas_acumuladas":8331,

"ganancias_acumuladas":12595,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Dom,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":314,

"dias_desde_primera_visita":1305,

"dias_desde_ultima_visita":41,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j115",

"nombre":"AlejandraRivera",

"edad":19,

"ocupacion":"Contador",

"presupuesto_hoy":1972,

"fichas_actuales":952,

"juego_actual":"Tragamonedas",

"monto_apuesta":137,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"21:44",

"rondas_jugadas_hoy":7,

"gasto_hoy":1017,

"frecuencia_semanal":1,

"tiempo_promedio_visita":77,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":145,

"gasto_maximo_historico":238,

"perdidas_acumuladas":10629,

"ganancias_acumuladas":8253,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":340,

"dias_desde_primera_visita":1283,

"dias_desde_ultima_visita":31,

"clasificacion":"Cuidar",

},

{

"id":"j116",

"nombre":"SergioAlvarez",

"edad":18,

"ocupacion":"Disenador",

"presupuesto_hoy":1937,

"fichas_actuales":404,

"juego_actual":"Tragamonedas",

"monto_apuesta":161,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"20:24",

"rondas_jugadas_hoy":33,

"gasto_hoy":1508,

"frecuencia_semanal":5,

"tiempo_promedio_visita":156,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":45,

"gasto_maximo_historico":533,

"perdidas_acumuladas":11942,

"ganancias_acumuladas":11143,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Lun,Mar,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":183,

"dias_desde_primera_visita":865,

"dias_desde_ultima_visita":26,

"clasificacion":"Cuidar",

},

{

"id":"j117",

"nombre":"EduardoReyes",

"edad":22,

"ocupacion":"Docente",

"presupuesto_hoy":721,

"fichas_actuales":588,

"juego_actual":"Poker",

"monto_apuesta":50,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"12:03",

"rondas_jugadas_hoy":9,

"gasto_hoy":115,

"frecuencia_semanal":3,

"tiempo_promedio_visita":297,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":12,

"gasto_maximo_historico":876,

"perdidas_acumuladas":8930,

"ganancias_acumuladas":8785,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Jue,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":393,

"dias_desde_primera_visita":550,

"dias_desde_ultima_visita":57,

"clasificacion":"Cuidar",

},

{

"id":"j118",

"nombre":"AdrianaTorres",

"edad":30,

"ocupacion":"Electricista",

"presupuesto_hoy":1987,

"fichas_actuales":936,

"juego_actual":"Dados",

"monto_apuesta":184,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.2,

"hora_actual":"11:07",

"rondas_jugadas_hoy":24,

"gasto_hoy":1032,

"frecuencia_semanal":7,

"tiempo_promedio_visita":93,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":80,

"perdidas_acumuladas":5334,

"ganancias_acumuladas":5013,

"variedad_juegos_probados":5,

"juego_favorito":"Dados",

"dias_visita":"Dom,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":446,

"dias_desde_primera_visita":1006,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j119",

"nombre":"EduardoReyes",

"edad":39,

"ocupacion":"Vendedor",

"presupuesto_hoy":239,

"fichas_actuales":233,

"juego_actual":"Tragamonedas",

"monto_apuesta":155,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.9,

"hora_actual":"17:36",

"rondas_jugadas_hoy":2,

"gasto_hoy":0,

"frecuencia_semanal":6,

"tiempo_promedio_visita":342,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":427,

"perdidas_acumuladas":10169,

"ganancias_acumuladas":13239,

"variedad_juegos_probados":3,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Sab,Lun,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":448,

"dias_desde_primera_visita":1331,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j120",

"nombre":"SofiaGarcia",

"edad":47,

"ocupacion":"Pintor",

"presupuesto_hoy":815,

"fichas_actuales":265,

"juego_actual":"Poker",

"monto_apuesta":35,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.0,

"hora_actual":"19:16",

"rondas_jugadas_hoy":25,

"gasto_hoy":543,

"frecuencia_semanal":3,

"tiempo_promedio_visita":269,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":286,

"perdidas_acumuladas":14333,

"ganancias_acumuladas":16968,

"variedad_juegos_probados":2,

"juego_favorito":"Poker",

"dias_visita":"Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":444,

"dias_desde_primera_visita":81,

"dias_desde_ultima_visita":8,

"clasificacion":"Cuidar",

},

{

"id":"j121",

"nombre":"AndresRodriguez",

"edad":54,

"ocupacion":"Enfermero",

"presupuesto_hoy":1696,

"fichas_actuales":1237,

"juego_actual":"Ruleta",

"monto_apuesta":37,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"16:43",

"rondas_jugadas_hoy":7,

"gasto_hoy":451,

"frecuencia_semanal":7,

"tiempo_promedio_visita":319,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":64,

"gasto_maximo_historico":911,

"perdidas_acumuladas":11660,

"ganancias_acumuladas":2631,

"variedad_juegos_probados":1,

"juego_favorito":"Ruleta",

"dias_visita":"Sab,Mar,Jue,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":340,

"dias_desde_primera_visita":54,

"dias_desde_ultima_visita":53,

"clasificacion":"Cuidar",

},

{

"id":"j122",

"nombre":"MateoMedina",

"edad":64,

"ocupacion":"Contador",

"presupuesto_hoy":1504,

"fichas_actuales":363,

"juego_actual":"Keno",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.1,

"hora_actual":"10:42",

"rondas_jugadas_hoy":34,

"gasto_hoy":1123,

"frecuencia_semanal":5,

"tiempo_promedio_visita":261,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":33,

"gasto_maximo_historico":383,

"perdidas_acumuladas":11000,

"ganancias_acumuladas":14753,

"variedad_juegos_probados":1,

"juego_favorito":"Keno",

"dias_visita":"Sab,Dom,Mar,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":401,

"dias_desde_primera_visita":656,

"dias_desde_ultima_visita":60,

"clasificacion":"Cuidar",

},

{

"id":"j123",

"nombre":"SergioRomero",

"edad":36,

"ocupacion":"Mecanico",

"presupuesto_hoy":1028,

"fichas_actuales":528,

"juego_actual":"Dados",

"monto_apuesta":146,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"22:21",

"rondas_jugadas_hoy":40,

"gasto_hoy":470,

"frecuencia_semanal":7,

"tiempo_promedio_visita":188,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":11,

"gasto_maximo_historico":812,

"perdidas_acumuladas":7929,

"ganancias_acumuladas":3930,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Vie,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":310,

"dias_desde_primera_visita":709,

"dias_desde_ultima_visita":32,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j124",

"nombre":"AlejandroGonzalez",

"edad":20,

"ocupacion":"Disenador",

"presupuesto_hoy":1458,

"fichas_actuales":1280,

"juego_actual":"Blackjack",

"monto_apuesta":112,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"21:34",

"rondas_jugadas_hoy":39,

"gasto_hoy":177,

"frecuencia_semanal":1,

"tiempo_promedio_visita":111,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":175,

"perdidas_acumuladas":9396,

"ganancias_acumuladas":9977,

"variedad_juegos_probados":6,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Mie,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":374,

"dias_desde_primera_visita":820,

"dias_desde_ultima_visita":28,

"clasificacion":"Cuidar",

},

{

"id":"j125",

"nombre":"DanielaVargas",

"edad":65,

"ocupacion":"Mecanico",

"presupuesto_hoy":385,

"fichas_actuales":322,

"juego_actual":"Baccarat",

"monto_apuesta":116,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"12:43",

"rondas_jugadas_hoy":1,

"gasto_hoy":35,

"frecuencia_semanal":1,

"tiempo_promedio_visita":272,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":35,

"gasto_maximo_historico":656,

"perdidas_acumuladas":1953,

"ganancias_acumuladas":15139,

"variedad_juegos_probados":3,

"juego_favorito":"Baccarat",

"dias_visita":"Vie,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":156,

"dias_desde_primera_visita":1119,

"dias_desde_ultima_visita":21,

"clasificacion":"Retener",

},

{

"id":"j126",

"nombre":"MariaRivera",

"edad":51,

"ocupacion":"Cocinero",

"presupuesto_hoy":1568,

"fichas_actuales":1159,

"juego_actual":"Dados",

"monto_apuesta":66,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"23:17",

"rondas_jugadas_hoy":33,

"gasto_hoy":383,

"frecuencia_semanal":1,

"tiempo_promedio_visita":306,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":11,

"gasto_maximo_historico":833,

"perdidas_acumuladas":9181,

"ganancias_acumuladas":12233,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Vie,Jue,Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":365,

"dias_desde_primera_visita":1109,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j127",

"nombre":"MariaRivera",

"edad":53,

"ocupacion":"Abogado",

"presupuesto_hoy":397,

"fichas_actuales":65,

"juego_actual":"Baccarat",

"monto_apuesta":101,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.9,

"hora_actual":"13:50",

"rondas_jugadas_hoy":23,

"gasto_hoy":303,

"frecuencia_semanal":7,

"tiempo_promedio_visita":45,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":201,

"perdidas_acumuladas":479,

"ganancias_acumuladas":8000,

"variedad_juegos_probados":5,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Dom,Lun,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":492,

"dias_desde_primera_visita":1286,

"dias_desde_ultima_visita":52,

"clasificacion":"VIP",

},

{

"id":"j128",

"nombre":"DanielaRuiz",

"edad":43,

"ocupacion":"Vendedor",

"presupuesto_hoy":752,

"fichas_actuales":258,

"juego_actual":"Ruleta",

"monto_apuesta":70,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"17:51",

"rondas_jugadas_hoy":21,

"gasto_hoy":470,

"frecuencia_semanal":3,

"tiempo_promedio_visita":278,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":22,

"gasto_maximo_historico":764,

"perdidas_acumuladas":9152,

"ganancias_acumuladas":11289,

"variedad_juegos_probados":5,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Lun,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":7,

"dias_desde_primera_visita":91,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j129",

"nombre":"PedroAlvarez",

"edad":67,

"ocupacion":"Vendedor",

"presupuesto_hoy":650,

"fichas_actuales":454,

"juego_actual":"Tragamonedas",

"monto_apuesta":51,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"16:41",

"rondas_jugadas_hoy":14,

"gasto_hoy":195,

"frecuencia_semanal":4,

"tiempo_promedio_visita":152,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":384,

"perdidas_acumuladas":7794,

"ganancias_acumuladas":3516,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":362,

"dias_desde_primera_visita":672,

"dias_desde_ultima_visita":57,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j130",

"nombre":"ElenaRuiz",

"edad":54,

"ocupacion":"Electricista",

"presupuesto_hoy":1153,

"fichas_actuales":200,

"juego_actual":"Keno",

"monto_apuesta":179,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"15:38",

"rondas_jugadas_hoy":30,

"gasto_hoy":944,

"frecuencia_semanal":2,

"tiempo_promedio_visita":37,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":475,

"perdidas_acumuladas":12729,

"ganancias_acumuladas":15772,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Sab,Mar,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":389,

"dias_desde_primera_visita":1079,

"dias_desde_ultima_visita":41,

"clasificacion":"Cuidar",

},

{

"id":"j131",

"nombre":"ValeriaRuiz",

"edad":19,

"ocupacion":"Docente",

"presupuesto_hoy":1602,

"fichas_actuales":958,

"juego_actual":"Tragamonedas",

"monto_apuesta":116,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.9,

"hora_actual":"20:36",

"rondas_jugadas_hoy":21,

"gasto_hoy":621,

"frecuencia_semanal":3,

"tiempo_promedio_visita":293,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":29,

"gasto_maximo_historico":774,

"perdidas_acumuladas":3972,

"ganancias_acumuladas":1140,

"variedad_juegos_probados":6,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mie,Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":368,

"dias_desde_primera_visita":903,

"dias_desde_ultima_visita":49,

"clasificacion":"Cuidar",

},

{

"id":"j132",

"nombre":"NataliaMartinez",

"edad":22,

"ocupacion":"Empresario",

"presupuesto_hoy":1704,

"fichas_actuales":544,

"juego_actual":"Baccarat",

"monto_apuesta":8,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"15:46",

"rondas_jugadas_hoy":26,

"gasto_hoy":1143,

"frecuencia_semanal":5,

"tiempo_promedio_visita":222,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":876,

"perdidas_acumuladas":248,

"ganancias_acumuladas":8039,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Vie,Mie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":473,

"dias_desde_primera_visita":450,

"dias_desde_ultima_visita":43,

"clasificacion":"Cuidar",

},

{

"id":"j133",

"nombre":"TomasVazquez",

"edad":70,

"ocupacion":"Pintor",

"presupuesto_hoy":24,

"fichas_actuales":9,

"juego_actual":"Blackjack",

"monto_apuesta":189,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"17:05",

"rondas_jugadas_hoy":2,

"gasto_hoy":8,

"frecuencia_semanal":5,

"tiempo_promedio_visita":205,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":868,

"perdidas_acumuladas":11507,

"ganancias_acumuladas":3520,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":51,

"dias_desde_primera_visita":977,

"dias_desde_ultima_visita":40,

"clasificacion":"Cuidar",

},

{

"id":"j134",

"nombre":"BeatrizPerez",

"edad":47,

"ocupacion":"Programador",

"presupuesto_hoy":619,

"fichas_actuales":77,

"juego_actual":"Cartas",

"monto_apuesta":181,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.6,

"hora_actual":"11:15",

"rondas_jugadas_hoy":1,

"gasto_hoy":533,

"frecuencia_semanal":7,

"tiempo_promedio_visita":66,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":533,

"gasto_maximo_historico":79,

"perdidas_acumuladas":10332,

"ganancias_acumuladas":16439,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Mie,Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":327,

"dias_desde_primera_visita":142,

"dias_desde_ultima_visita":55,

"clasificacion":"Cuidar",

},

{

"id":"j135",

"nombre":"MarianaRuiz",

"edad":57,

"ocupacion":"Ingeniero",

"presupuesto_hoy":156,

"fichas_actuales":99,

"juego_actual":"Blackjack",

"monto_apuesta":126,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"15:06",

"rondas_jugadas_hoy":21,

"gasto_hoy":42,

"frecuencia_semanal":3,

"tiempo_promedio_visita":357,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":2,

"gasto_maximo_historico":135,

"perdidas_acumuladas":7680,

"ganancias_acumuladas":1476,

"variedad_juegos_probados":1,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":338,

"dias_desde_primera_visita":69,

"dias_desde_ultima_visita":36,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j136",

"nombre":"MariaMendoza",

"edad":44,

"ocupacion":"Cocinero",

"presupuesto_hoy":635,

"fichas_actuales":113,

"juego_actual":"Baccarat",

"monto_apuesta":66,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"21:36",

"rondas_jugadas_hoy":16,

"gasto_hoy":514,

"frecuencia_semanal":0,

"tiempo_promedio_visita":188,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":32,

"gasto_maximo_historico":797,

"perdidas_acumuladas":11527,

"ganancias_acumuladas":7126,

"variedad_juegos_probados":1,

"juego_favorito":"Baccarat",

"dias_visita":"Sab,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":272,

"dias_desde_primera_visita":174,

"dias_desde_ultima_visita":17,

"clasificacion":"Cuidar",

},

{

"id":"j137",

"nombre":"JavierRamirez",

"edad":60,

"ocupacion":"Mecanico",

"presupuesto_hoy":1002,

"fichas_actuales":478,

"juego_actual":"Keno",

"monto_apuesta":194,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"23:10",

"rondas_jugadas_hoy":7,

"gasto_hoy":506,

"frecuencia_semanal":5,

"tiempo_promedio_visita":348,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":72,

"gasto_maximo_historico":482,

"perdidas_acumuladas":14591,

"ganancias_acumuladas":18671,

"variedad_juegos_probados":1,

"juego_favorito":"Keno",

"dias_visita":"Vie,Jue,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":455,

"dias_desde_primera_visita":1185,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j138",

"nombre":"JoseOrtiz",

"edad":62,

"ocupacion":"Medico",

"presupuesto_hoy":1466,

"fichas_actuales":931,

"juego_actual":"Tragamonedas",

"monto_apuesta":130,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"21:14",

"rondas_jugadas_hoy":4,

"gasto_hoy":518,

"frecuencia_semanal":1,

"tiempo_promedio_visita":32,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":129,

"gasto_maximo_historico":307,

"perdidas_acumuladas":12045,

"ganancias_acumuladas":7798,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":159,

"dias_desde_primera_visita":1247,

"dias_desde_ultima_visita":33,

"clasificacion":"Cuidar",

},

{

"id":"j139",

"nombre":"GabrielaReyes",

"edad":59,

"ocupacion":"Enfermero",

"presupuesto_hoy":747,

"fichas_actuales":406,

"juego_actual":"Blackjack",

"monto_apuesta":110,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.6,

"hora_actual":"23:19",

"rondas_jugadas_hoy":20,

"gasto_hoy":318,

"frecuencia_semanal":4,

"tiempo_promedio_visita":48,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":694,

"perdidas_acumuladas":2145,

"ganancias_acumuladas":17039,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Jue,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":262,

"dias_desde_primera_visita":1466,

"dias_desde_ultima_visita":15,

"clasificacion":"VIP",

},

{

"id":"j140",

"nombre":"FernandoRuiz",

"edad":39,

"ocupacion":"Mecanico",

"presupuesto_hoy":1916,

"fichas_actuales":1440,

"juego_actual":"Ruleta",

"monto_apuesta":63,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.4,

"hora_actual":"14:44",

"rondas_jugadas_hoy":3,

"gasto_hoy":474,

"frecuencia_semanal":2,

"tiempo_promedio_visita":278,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":158,

"gasto_maximo_historico":744,

"perdidas_acumuladas":13057,

"ganancias_acumuladas":426,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Mie,Lun,Mar,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":168,

"dias_desde_primera_visita":898,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j141",

"nombre":"VeronicaVazquez",

"edad":26,

"ocupacion":"Pintor",

"presupuesto_hoy":1547,

"fichas_actuales":1397,

"juego_actual":"Cartas",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"21:38",

"rondas_jugadas_hoy":8,

"gasto_hoy":136,

"frecuencia_semanal":4,

"tiempo_promedio_visita":334,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":17,

"gasto_maximo_historico":421,

"perdidas_acumuladas":9833,

"ganancias_acumuladas":18559,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":490,

"dias_desde_primera_visita":1403,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j142",

"nombre":"CarlaVazquez",

"edad":61,

"ocupacion":"Mecanico",

"presupuesto_hoy":1086,

"fichas_actuales":592,

"juego_actual":"Keno",

"monto_apuesta":109,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.3,

"hora_actual":"21:14",

"rondas_jugadas_hoy":35,

"gasto_hoy":494,

"frecuencia_semanal":1,

"tiempo_promedio_visita":302,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":14,

"gasto_maximo_historico":822,

"perdidas_acumuladas":4659,

"ganancias_acumuladas":18811,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Vie,Dom,Jue,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":171,

"dias_desde_primera_visita":23,

"dias_desde_ultima_visita":6,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j143",

"nombre":"AdrianRivera",

"edad":22,

"ocupacion":"Desempleado",

"presupuesto_hoy":336,

"fichas_actuales":157,

"juego_actual":"Tragamonedas",

"monto_apuesta":115,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"22:39",

"rondas_jugadas_hoy":21,

"gasto_hoy":152,

"frecuencia_semanal":6,

"tiempo_promedio_visita":311,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":7,

"gasto_maximo_historico":60,

"perdidas_acumuladas":8751,

"ganancias_acumuladas":17842,

"variedad_juegos_probados":5,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Mie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":339,

"dias_desde_primera_visita":100,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j144",

"nombre":"AngelMendoza",

"edad":62,

"ocupacion":"Estudiante",

"presupuesto_hoy":1591,

"fichas_actuales":258,

"juego_actual":"Dados",

"monto_apuesta":9,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"21:30",

"rondas_jugadas_hoy":10,

"gasto_hoy":1328,

"frecuencia_semanal":4,

"tiempo_promedio_visita":289,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":132,

"gasto_maximo_historico":361,

"perdidas_acumuladas":14427,

"ganancias_acumuladas":16547,

"variedad_juegos_probados":4,

"juego_favorito":"Dados",

"dias_visita":"Mar,Dom,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":145,

"dias_desde_primera_visita":22,

"dias_desde_ultima_visita":58,

"clasificacion":"Cuidar",

},

{

"id":"j145",

"nombre":"AliciaLopez",

"edad":45,

"ocupacion":"Electricista",

"presupuesto_hoy":521,

"fichas_actuales":497,

"juego_actual":"Poker",

"monto_apuesta":198,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"20:55",

"rondas_jugadas_hoy":7,

"gasto_hoy":16,

"frecuencia_semanal":6,

"tiempo_promedio_visita":232,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":2,

"gasto_maximo_historico":687,

"perdidas_acumuladas":4687,

"ganancias_acumuladas":14693,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":378,

"dias_desde_primera_visita":157,

"dias_desde_ultima_visita":27,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j146",

"nombre":"LilianaPerez",

"edad":19,

"ocupacion":"Chofer",

"presupuesto_hoy":1828,

"fichas_actuales":108,

"juego_actual":"Tragamonedas",

"monto_apuesta":3,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.8,

"hora_actual":"17:04",

"rondas_jugadas_hoy":8,

"gasto_hoy":1700,

"frecuencia_semanal":4,

"tiempo_promedio_visita":319,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":212,

"gasto_maximo_historico":436,

"perdidas_acumuladas":8346,

"ganancias_acumuladas":14857,

"variedad_juegos_probados":5,

"juego_favorito":"Tragamonedas",

"dias_visita":"Dom,Lun,Sab,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":332,

"dias_desde_primera_visita":1074,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j147",

"nombre":"PatriciaAguilar",

"edad":50,

"ocupacion":"Cocinero",

"presupuesto_hoy":1509,

"fichas_actuales":525,

"juego_actual":"Poker",

"monto_apuesta":173,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.9,

"hora_actual":"21:16",

"rondas_jugadas_hoy":6,

"gasto_hoy":972,

"frecuencia_semanal":4,

"tiempo_promedio_visita":159,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":162,

"gasto_maximo_historico":85,

"perdidas_acumuladas":2674,

"ganancias_acumuladas":6229,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Sab,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":240,

"dias_desde_primera_visita":462,

"dias_desde_ultima_visita":12,

"clasificacion":"VIP",

},

{

"id":"j148",

"nombre":"JulioGomez",

"edad":57,

"ocupacion":"Chofer",

"presupuesto_hoy":1291,

"fichas_actuales":499,

"juego_actual":"Ruleta",

"monto_apuesta":138,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.5,

"hora_actual":"11:07",

"rondas_jugadas_hoy":2,

"gasto_hoy":779,

"frecuencia_semanal":6,

"tiempo_promedio_visita":356,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":389,

"gasto_maximo_historico":652,

"perdidas_acumuladas":9793,

"ganancias_acumuladas":2302,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Dom,Jue,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":349,

"dias_desde_primera_visita":1235,

"dias_desde_ultima_visita":16,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j149",

"nombre":"IvanVazquez",

"edad":61,

"ocupacion":"Disenador",

"presupuesto_hoy":424,

"fichas_actuales":374,

"juego_actual":"Ruleta",

"monto_apuesta":136,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.6,

"hora_actual":"23:46",

"rondas_jugadas_hoy":37,

"gasto_hoy":34,

"frecuencia_semanal":3,

"tiempo_promedio_visita":329,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":474,

"perdidas_acumuladas":13578,

"ganancias_acumuladas":396,

"variedad_juegos_probados":6,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":198,

"dias_desde_primera_visita":466,

"dias_desde_ultima_visita":14,

"clasificacion":"Cuidar",

},

{

"id":"j150",

"nombre":"SantiagoTorres",

"edad":45,

"ocupacion":"Ingeniero",

"presupuesto_hoy":519,

"fichas_actuales":98,

"juego_actual":"Blackjack",

"monto_apuesta":14,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":6.0,

"hora_actual":"11:43",

"rondas_jugadas_hoy":10,

"gasto_hoy":397,

"frecuencia_semanal":6,

"tiempo_promedio_visita":306,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":39,

"gasto_maximo_historico":502,

"perdidas_acumuladas":6998,

"ganancias_acumuladas":1515,

"variedad_juegos_probados":1,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":375,

"dias_desde_primera_visita":962,

"dias_desde_ultima_visita":28,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j151",

"nombre":"PaulaRomero",

"edad":23,

"ocupacion":"Carpintero",

"presupuesto_hoy":1818,

"fichas_actuales":594,

"juego_actual":"Baccarat",

"monto_apuesta":48,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"23:45",

"rondas_jugadas_hoy":6,

"gasto_hoy":1197,

"frecuencia_semanal":1,

"tiempo_promedio_visita":127,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":199,

"gasto_maximo_historico":835,

"perdidas_acumuladas":6192,

"ganancias_acumuladas":7990,

"variedad_juegos_probados":5,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Mar,Lun,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":208,

"dias_desde_primera_visita":1045,

"dias_desde_ultima_visita":34,

"clasificacion":"Cuidar",

},

{

"id":"j152",

"nombre":"JuanReyes",

"edad":61,

"ocupacion":"Disenador",

"presupuesto_hoy":1344,

"fichas_actuales":1321,

"juego_actual":"Cartas",

"monto_apuesta":52,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.7,

"hora_actual":"12:31",

"rondas_jugadas_hoy":38,

"gasto_hoy":0,

"frecuencia_semanal":4,

"tiempo_promedio_visita":239,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":393,

"perdidas_acumuladas":1360,

"ganancias_acumuladas":9201,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":300,

"dias_desde_primera_visita":958,

"dias_desde_ultima_visita":51,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j153",

"nombre":"ElenaTorres",

"edad":54,

"ocupacion":"Estudiante",

"presupuesto_hoy":1008,

"fichas_actuales":631,

"juego_actual":"Ruleta",

"monto_apuesta":145,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.9,

"hora_actual":"14:13",

"rondas_jugadas_hoy":16,

"gasto_hoy":351,

"frecuencia_semanal":7,

"tiempo_promedio_visita":125,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":810,

"perdidas_acumuladas":14340,

"ganancias_acumuladas":5995,

"variedad_juegos_probados":1,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":255,

"dias_desde_primera_visita":224,

"dias_desde_ultima_visita":24,

"clasificacion":"Cuidar",

},

{

"id":"j154",

"nombre":"HugoAlvarez",

"edad":70,

"ocupacion":"Estudiante",

"presupuesto_hoy":443,

"fichas_actuales":218,

"juego_actual":"Cartas",

"monto_apuesta":133,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.4,

"hora_actual":"16:07",

"rondas_jugadas_hoy":23,

"gasto_hoy":207,

"frecuencia_semanal":5,

"tiempo_promedio_visita":183,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":853,

"perdidas_acumuladas":7656,

"ganancias_acumuladas":16750,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Dom,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":132,

"dias_desde_primera_visita":206,

"dias_desde_ultima_visita":14,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j155",

"nombre":"DanielaGonzalez",

"edad":39,

"ocupacion":"Empresario",

"presupuesto_hoy":935,

"fichas_actuales":400,

"juego_actual":"Baccarat",

"monto_apuesta":49,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.3,

"hora_actual":"19:37",

"rondas_jugadas_hoy":16,

"gasto_hoy":505,

"frecuencia_semanal":0,

"tiempo_promedio_visita":292,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":894,

"perdidas_acumuladas":13324,

"ganancias_acumuladas":10838,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":86,

"dias_desde_primera_visita":476,

"dias_desde_ultima_visita":50,

"clasificacion":"Cuidar",

},

{

"id":"j156",

"nombre":"DanielOrtiz",

"edad":54,

"ocupacion":"Disenador",

"presupuesto_hoy":820,

"fichas_actuales":158,

"juego_actual":"Ruleta",

"monto_apuesta":154,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.8,

"hora_actual":"11:19",

"rondas_jugadas_hoy":14,

"gasto_hoy":639,

"frecuencia_semanal":0,

"tiempo_promedio_visita":105,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":45,

"gasto_maximo_historico":381,

"perdidas_acumuladas":3908,

"ganancias_acumuladas":2100,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Jue,Mie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":423,

"dias_desde_primera_visita":1040,

"dias_desde_ultima_visita":39,

"clasificacion":"Retener",

},

{

"id":"j157",

"nombre":"FernandoVazquez",

"edad":59,

"ocupacion":"Empresario",

"presupuesto_hoy":527,

"fichas_actuales":226,

"juego_actual":"Ruleta",

"monto_apuesta":70,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"23:34",

"rondas_jugadas_hoy":12,

"gasto_hoy":290,

"frecuencia_semanal":1,

"tiempo_promedio_visita":270,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":24,

"gasto_maximo_historico":452,

"perdidas_acumuladas":5147,

"ganancias_acumuladas":712,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Dom,Vie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":238,

"dias_desde_primera_visita":625,

"dias_desde_ultima_visita":60,

"clasificacion":"Retener",

},

{

"id":"j158",

"nombre":"VictoriaMartinez",

"edad":50,

"ocupacion":"Mecanico",

"presupuesto_hoy":355,

"fichas_actuales":131,

"juego_actual":"Keno",

"monto_apuesta":173,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.5,

"hora_actual":"22:49",

"rondas_jugadas_hoy":32,

"gasto_hoy":211,

"frecuencia_semanal":1,

"tiempo_promedio_visita":322,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":6,

"gasto_maximo_historico":566,

"perdidas_acumuladas":1061,

"ganancias_acumuladas":18233,

"variedad_juegos_probados":5,

"juego_favorito":"Keno",

"dias_visita":"Lun,Dom,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":422,

"dias_desde_primera_visita":1354,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j159",

"nombre":"JoseMendoza",

"edad":55,

"ocupacion":"Desempleado",

"presupuesto_hoy":1785,

"fichas_actuales":650,

"juego_actual":"Cartas",

"monto_apuesta":65,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"22:58",

"rondas_jugadas_hoy":25,

"gasto_hoy":1115,

"frecuencia_semanal":2,

"tiempo_promedio_visita":358,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":44,

"gasto_maximo_historico":980,

"perdidas_acumuladas":442,

"ganancias_acumuladas":6148,

"variedad_juegos_probados":2,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Lun,Sab,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":35,

"dias_desde_primera_visita":936,

"dias_desde_ultima_visita":44,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j160",

"nombre":"SilviaVazquez",

"edad":55,

"ocupacion":"Pintor",

"presupuesto_hoy":167,

"fichas_actuales":109,

"juego_actual":"Keno",

"monto_apuesta":86,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"14:12",

"rondas_jugadas_hoy":13,

"gasto_hoy":47,

"frecuencia_semanal":5,

"tiempo_promedio_visita":118,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":575,

"perdidas_acumuladas":10483,

"ganancias_acumuladas":2960,

"variedad_juegos_probados":4,

"juego_favorito":"Keno",

"dias_visita":"Dom,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":106,

"dias_desde_primera_visita":445,

"dias_desde_ultima_visita":51,

"clasificacion":"Cuidar",

},

{

"id":"j161",

"nombre":"NataliaReyes",

"edad":57,

"ocupacion":"Cocinero",

"presupuesto_hoy":1579,

"fichas_actuales":546,

"juego_actual":"Ruleta",

"monto_apuesta":101,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"21:59",

"rondas_jugadas_hoy":32,

"gasto_hoy":1011,

"frecuencia_semanal":1,

"tiempo_promedio_visita":282,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":65,

"perdidas_acumuladas":4873,

"ganancias_acumuladas":5891,

"variedad_juegos_probados":5,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":270,

"dias_desde_primera_visita":316,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j162",

"nombre":"NataliaTorres",

"edad":53,

"ocupacion":"Estudiante",

"presupuesto_hoy":1734,

"fichas_actuales":15,

"juego_actual":"Tragamonedas",

"monto_apuesta":38,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.0,

"hora_actual":"23:08",

"rondas_jugadas_hoy":31,

"gasto_hoy":1690,

"frecuencia_semanal":3,

"tiempo_promedio_visita":52,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":54,

"gasto_maximo_historico":146,

"perdidas_acumuladas":14320,

"ganancias_acumuladas":9341,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":485,

"dias_desde_primera_visita":535,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j163",

"nombre":"IsabelMendoza",

"edad":30,

"ocupacion":"Programador",

"presupuesto_hoy":1559,

"fichas_actuales":887,

"juego_actual":"Cartas",

"monto_apuesta":176,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.4,

"hora_actual":"16:56",

"rondas_jugadas_hoy":18,

"gasto_hoy":665,

"frecuencia_semanal":3,

"tiempo_promedio_visita":271,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":36,

"gasto_maximo_historico":504,

"perdidas_acumuladas":4101,

"ganancias_acumuladas":3197,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Lun,Dom,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":461,

"dias_desde_primera_visita":1473,

"dias_desde_ultima_visita":54,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j164",

"nombre":"ManuelRodriguez",

"edad":47,

"ocupacion":"Ingeniero",

"presupuesto_hoy":1712,

"fichas_actuales":619,

"juego_actual":"Tragamonedas",

"monto_apuesta":183,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.5,

"hora_actual":"19:19",

"rondas_jugadas_hoy":23,

"gasto_hoy":1085,

"frecuencia_semanal":1,

"tiempo_promedio_visita":97,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":47,

"gasto_maximo_historico":82,

"perdidas_acumuladas":11157,

"ganancias_acumuladas":2085,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":405,

"dias_desde_primera_visita":623,

"dias_desde_ultima_visita":52,

"clasificacion":"Cuidar",

},

{

"id":"j165",

"nombre":"PedroVazquez",

"edad":31,

"ocupacion":"Empresario",

"presupuesto_hoy":880,

"fichas_actuales":351,

"juego_actual":"Blackjack",

"monto_apuesta":44,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"17:13",

"rondas_jugadas_hoy":34,

"gasto_hoy":515,

"frecuencia_semanal":4,

"tiempo_promedio_visita":296,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":665,

"perdidas_acumuladas":1034,

"ganancias_acumuladas":1982,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Mie,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":83,

"dias_desde_primera_visita":756,

"dias_desde_ultima_visita":55,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j166",

"nombre":"XimenaVazquez",

"edad":49,

"ocupacion":"Empresario",

"presupuesto_hoy":1965,

"fichas_actuales":1375,

"juego_actual":"Tragamonedas",

"monto_apuesta":183,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"20:32",

"rondas_jugadas_hoy":5,

"gasto_hoy":587,

"frecuencia_semanal":4,

"tiempo_promedio_visita":48,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":117,

"gasto_maximo_historico":473,

"perdidas_acumuladas":10279,

"ganancias_acumuladas":16895,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Mie,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":25,

"dias_desde_primera_visita":1233,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j167",

"nombre":"RosaRodriguez",

"edad":23,

"ocupacion":"Disenador",

"presupuesto_hoy":1599,

"fichas_actuales":1570,

"juego_actual":"Cartas",

"monto_apuesta":80,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.6,

"hora_actual":"16:43",

"rondas_jugadas_hoy":39,

"gasto_hoy":17,

"frecuencia_semanal":3,

"tiempo_promedio_visita":307,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":92,

"perdidas_acumuladas":11729,

"ganancias_acumuladas":14713,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Lun,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":50,

"dias_desde_primera_visita":143,

"dias_desde_ultima_visita":50,

"clasificacion":"Cuidar",

},

{

"id":"j168",

"nombre":"NataliaOrtiz",

"edad":46,

"ocupacion":"Mecanico",

"presupuesto_hoy":650,

"fichas_actuales":275,

"juego_actual":"Keno",

"monto_apuesta":68,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.9,

"hora_actual":"15:40",

"rondas_jugadas_hoy":39,

"gasto_hoy":346,

"frecuencia_semanal":0,

"tiempo_promedio_visita":168,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":8,

"gasto_maximo_historico":684,

"perdidas_acumuladas":7443,

"ganancias_acumuladas":10378,

"variedad_juegos_probados":5,

"juego_favorito":"Keno",

"dias_visita":"Mar,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":465,

"dias_desde_primera_visita":854,

"dias_desde_ultima_visita":51,

"clasificacion":"Retener",

},

{

"id":"j169",

"nombre":"CarlosGarcia",

"edad":50,

"ocupacion":"Enfermero",

"presupuesto_hoy":1863,

"fichas_actuales":358,

"juego_actual":"Tragamonedas",

"monto_apuesta":28,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.6,

"hora_actual":"16:43",

"rondas_jugadas_hoy":6,

"gasto_hoy":1475,

"frecuencia_semanal":0,

"tiempo_promedio_visita":107,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":245,

"gasto_maximo_historico":910,

"perdidas_acumuladas":2527,

"ganancias_acumuladas":18707,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":36,

"dias_desde_primera_visita":1305,

"dias_desde_ultima_visita":27,

"clasificacion":"Retener",

},

{

"id":"j170",

"nombre":"OscarTorres",

"edad":39,

"ocupacion":"Programador",

"presupuesto_hoy":75,

"fichas_actuales":28,

"juego_actual":"Baccarat",

"monto_apuesta":200,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"20:29",

"rondas_jugadas_hoy":11,

"gasto_hoy":43,

"frecuencia_semanal":1,

"tiempo_promedio_visita":338,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":575,

"perdidas_acumuladas":12751,

"ganancias_acumuladas":12517,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Jue,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":3,

"dias_desde_primera_visita":1071,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j171",

"nombre":"RosaRomero",

"edad":41,

"ocupacion":"Vendedor",

"presupuesto_hoy":897,

"fichas_actuales":165,

"juego_actual":"Baccarat",

"monto_apuesta":70,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"10:50",

"rondas_jugadas_hoy":3,

"gasto_hoy":728,

"frecuencia_semanal":7,

"tiempo_promedio_visita":169,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":242,

"gasto_maximo_historico":323,

"perdidas_acumuladas":2297,

"ganancias_acumuladas":7108,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Sab,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":264,

"dias_desde_primera_visita":358,

"dias_desde_ultima_visita":3,

"clasificacion":"VIP",

},

{

"id":"j172",

"nombre":"GabrielaOrtiz",

"edad":24,

"ocupacion":"Disenador",

"presupuesto_hoy":1364,

"fichas_actuales":710,

"juego_actual":"Baccarat",

"monto_apuesta":65,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"21:56",

"rondas_jugadas_hoy":40,

"gasto_hoy":638,

"frecuencia_semanal":2,

"tiempo_promedio_visita":139,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":552,

"perdidas_acumuladas":9039,

"ganancias_acumuladas":12456,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mar,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":136,

"dias_desde_primera_visita":913,

"dias_desde_ultima_visita":18,

"clasificacion":"Cuidar",

},

{

"id":"j173",

"nombre":"SergioOrtiz",

"edad":26,

"ocupacion":"Enfermero",

"presupuesto_hoy":517,

"fichas_actuales":144,

"juego_actual":"Keno",

"monto_apuesta":49,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.1,

"hora_actual":"20:12",

"rondas_jugadas_hoy":26,

"gasto_hoy":343,

"frecuencia_semanal":4,

"tiempo_promedio_visita":277,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":493,

"perdidas_acumuladas":7820,

"ganancias_acumuladas":11979,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Dom,Lun,Sab,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":155,

"dias_desde_primera_visita":743,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j174",

"nombre":"FernandaRivera",

"edad":21,

"ocupacion":"Cocinero",

"presupuesto_hoy":1020,

"fichas_actuales":28,

"juego_actual":"Tragamonedas",

"monto_apuesta":62,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.6,

"hora_actual":"12:22",

"rondas_jugadas_hoy":26,

"gasto_hoy":973,

"frecuencia_semanal":2,

"tiempo_promedio_visita":78,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":37,

"gasto_maximo_historico":690,

"perdidas_acumuladas":14085,

"ganancias_acumuladas":7146,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":145,

"dias_desde_primera_visita":812,

"dias_desde_ultima_visita":37,

"clasificacion":"Cuidar",

},

{

"id":"j175",

"nombre":"SilviaRomero",

"edad":70,

"ocupacion":"Programador",

"presupuesto_hoy":163,

"fichas_actuales":87,

"juego_actual":"Blackjack",

"monto_apuesta":136,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"17:58",

"rondas_jugadas_hoy":6,

"gasto_hoy":55,

"frecuencia_semanal":6,

"tiempo_promedio_visita":273,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":940,

"perdidas_acumuladas":11909,

"ganancias_acumuladas":6574,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":27,

"dias_desde_primera_visita":1009,

"dias_desde_ultima_visita":37,

"clasificacion":"Cuidar",

},

{

"id":"j176",

"nombre":"MonicaVargas",

"edad":66,

"ocupacion":"Abogado",

"presupuesto_hoy":859,

"fichas_actuales":98,

"juego_actual":"Keno",

"monto_apuesta":128,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.5,

"hora_actual":"23:36",

"rondas_jugadas_hoy":35,

"gasto_hoy":750,

"frecuencia_semanal":4,

"tiempo_promedio_visita":133,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":88,

"perdidas_acumuladas":12291,

"ganancias_acumuladas":11823,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Vie,Mar,Dom,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":109,

"dias_desde_primera_visita":1059,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j177",

"nombre":"NadiaGonzalez",

"edad":21,

"ocupacion":"Programador",

"presupuesto_hoy":374,

"fichas_actuales":212,

"juego_actual":"Keno",

"monto_apuesta":54,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.2,

"hora_actual":"19:02",

"rondas_jugadas_hoy":19,

"gasto_hoy":133,

"frecuencia_semanal":3,

"tiempo_promedio_visita":62,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":7,

"gasto_maximo_historico":58,

"perdidas_acumuladas":13183,

"ganancias_acumuladas":887,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Sab,Mar,Vie,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":496,

"dias_desde_primera_visita":569,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j178",

"nombre":"CamilaDiaz",

"edad":56,

"ocupacion":"Mecanico",

"presupuesto_hoy":1296,

"fichas_actuales":615,

"juego_actual":"Ruleta",

"monto_apuesta":115,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"19:35",

"rondas_jugadas_hoy":34,

"gasto_hoy":653,

"frecuencia_semanal":3,

"tiempo_promedio_visita":104,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":298,

"perdidas_acumuladas":5526,

"ganancias_acumuladas":16262,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":493,

"dias_desde_primera_visita":1233,

"dias_desde_ultima_visita":24,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j179",

"nombre":"JavierRodriguez",

"edad":20,

"ocupacion":"Enfermero",

"presupuesto_hoy":731,

"fichas_actuales":388,

"juego_actual":"Blackjack",

"monto_apuesta":45,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.9,

"hora_actual":"15:50",

"rondas_jugadas_hoy":11,

"gasto_hoy":330,

"frecuencia_semanal":6,

"tiempo_promedio_visita":197,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":30,

"gasto_maximo_historico":972,

"perdidas_acumuladas":11003,

"ganancias_acumuladas":13611,

"variedad_juegos_probados":3,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":139,

"dias_desde_primera_visita":376,

"dias_desde_ultima_visita":0,

"clasificacion":"Cuidar",

},

{

"id":"j180",

"nombre":"SilviaRivera",

"edad":69,

"ocupacion":"Chofer",

"presupuesto_hoy":80,

"fichas_actuales":57,

"juego_actual":"Dados",

"monto_apuesta":193,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"17:43",

"rondas_jugadas_hoy":10,

"gasto_hoy":0,

"frecuencia_semanal":5,

"tiempo_promedio_visita":356,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":750,

"perdidas_acumuladas":4570,

"ganancias_acumuladas":16012,

"variedad_juegos_probados":2,

"juego_favorito":"Dados",

"dias_visita":"Jue,Mar,Vie,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":350,

"dias_desde_primera_visita":668,

"dias_desde_ultima_visita":29,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j181",

"nombre":"BeatrizOrtiz",

"edad":48,

"ocupacion":"Electricista",

"presupuesto_hoy":1930,

"fichas_actuales":1466,

"juego_actual":"Cartas",

"monto_apuesta":66,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"23:55",

"rondas_jugadas_hoy":9,

"gasto_hoy":443,

"frecuencia_semanal":0,

"tiempo_promedio_visita":75,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":49,

"gasto_maximo_historico":441,

"perdidas_acumuladas":8739,

"ganancias_acumuladas":10588,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Sab,Dom,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":11,

"dias_desde_primera_visita":736,

"dias_desde_ultima_visita":11,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j182",

"nombre":"FelipeGomez",

"edad":42,

"ocupacion":"Abogado",

"presupuesto_hoy":1026,

"fichas_actuales":738,

"juego_actual":"Blackjack",

"monto_apuesta":164,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"12:12",

"rondas_jugadas_hoy":10,

"gasto_hoy":262,

"frecuencia_semanal":7,

"tiempo_promedio_visita":150,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":26,

"gasto_maximo_historico":417,

"perdidas_acumuladas":11553,

"ganancias_acumuladas":16207,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Lun,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":130,

"dias_desde_primera_visita":1064,

"dias_desde_ultima_visita":3,

"clasificacion":"Cuidar",

},

{

"id":"j183",

"nombre":"FernandoMendoza",

"edad":50,

"ocupacion":"Disenador",

"presupuesto_hoy":204,

"fichas_actuales":178,

"juego_actual":"Ruleta",

"monto_apuesta":146,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.8,

"hora_actual":"20:01",

"rondas_jugadas_hoy":16,

"gasto_hoy":4,

"frecuencia_semanal":6,

"tiempo_promedio_visita":297,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":862,

"perdidas_acumuladas":3234,

"ganancias_acumuladas":17071,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":400,

"dias_desde_primera_visita":569,

"dias_desde_ultima_visita":55,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j184",

"nombre":"PatriciaRomero",

"edad":68,

"ocupacion":"Mecanico",

"presupuesto_hoy":1844,

"fichas_actuales":924,

"juego_actual":"Blackjack",

"monto_apuesta":46,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.5,

"hora_actual":"20:25",

"rondas_jugadas_hoy":7,

"gasto_hoy":915,

"frecuencia_semanal":0,

"tiempo_promedio_visita":240,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":130,

"gasto_maximo_historico":463,

"perdidas_acumuladas":1994,

"ganancias_acumuladas":5026,

"variedad_juegos_probados":4,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Jue,Mar,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":78,

"dias_desde_primera_visita":1271,

"dias_desde_ultima_visita":31,

"clasificacion":"Retener",

},

{

"id":"j185",

"nombre":"ElenaSanchez",

"edad":38,

"ocupacion":"Electricista",

"presupuesto_hoy":929,

"fichas_actuales":225,

"juego_actual":"Tragamonedas",

"monto_apuesta":196,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"21:05",

"rondas_jugadas_hoy":16,

"gasto_hoy":694,

"frecuencia_semanal":7,

"tiempo_promedio_visita":316,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":908,

"perdidas_acumuladas":8477,

"ganancias_acumuladas":7053,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":203,

"dias_desde_primera_visita":1275,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j186",

"nombre":"AlejandraLopez",

"edad":25,

"ocupacion":"Jubilado",

"presupuesto_hoy":138,

"fichas_actuales":79,

"juego_actual":"Blackjack",

"monto_apuesta":104,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.0,

"hora_actual":"22:21",

"rondas_jugadas_hoy":3,

"gasto_hoy":54,

"frecuencia_semanal":2,

"tiempo_promedio_visita":303,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":18,

"gasto_maximo_historico":322,

"perdidas_acumuladas":4585,

"ganancias_acumuladas":825,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Jue,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":138,

"dias_desde_primera_visita":859,

"dias_desde_ultima_visita":39,

"clasificacion":"Cuidar",

},

{

"id":"j187",

"nombre":"JuliaDiaz",

"edad":55,

"ocupacion":"Abogado",

"presupuesto_hoy":411,

"fichas_actuales":338,

"juego_actual":"Baccarat",

"monto_apuesta":192,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.1,

"hora_actual":"12:37",

"rondas_jugadas_hoy":15,

"gasto_hoy":51,

"frecuencia_semanal":0,

"tiempo_promedio_visita":111,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":640,

"perdidas_acumuladas":11090,

"ganancias_acumuladas":7092,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mar,Jue,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":449,

"dias_desde_primera_visita":253,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j188",

"nombre":"NataliaVazquez",

"edad":38,

"ocupacion":"Pintor",

"presupuesto_hoy":1626,

"fichas_actuales":736,

"juego_actual":"Tragamonedas",

"monto_apuesta":6,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"16:37",

"rondas_jugadas_hoy":25,

"gasto_hoy":863,

"frecuencia_semanal":7,

"tiempo_promedio_visita":111,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":34,

"gasto_maximo_historico":975,

"perdidas_acumuladas":11750,

"ganancias_acumuladas":17356,

"variedad_juegos_probados":3,

"juego_favorito":"Tragamonedas",

"dias_visita":"Lun,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":155,

"dias_desde_primera_visita":1213,

"dias_desde_ultima_visita":47,

"clasificacion":"Cuidar",

},

{

"id":"j189",

"nombre":"PedroGomez",

"edad":46,

"ocupacion":"Empresario",

"presupuesto_hoy":226,

"fichas_actuales":81,

"juego_actual":"Keno",

"monto_apuesta":21,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"12:50",

"rondas_jugadas_hoy":24,

"gasto_hoy":115,

"frecuencia_semanal":6,

"tiempo_promedio_visita":270,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":749,

"perdidas_acumuladas":1482,

"ganancias_acumuladas":18636,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Mar,Sab,Jue,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":282,

"dias_desde_primera_visita":743,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j190",

"nombre":"JuanAguilar",

"edad":59,

"ocupacion":"Programador",

"presupuesto_hoy":1414,

"fichas_actuales":1212,

"juego_actual":"Blackjack",

"monto_apuesta":137,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.0,

"hora_actual":"16:43",

"rondas_jugadas_hoy":28,

"gasto_hoy":179,

"frecuencia_semanal":1,

"tiempo_promedio_visita":248,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":6,

"gasto_maximo_historico":952,

"perdidas_acumuladas":8307,

"ganancias_acumuladas":11955,

"variedad_juegos_probados":6,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Jue,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":447,

"dias_desde_primera_visita":720,

"dias_desde_ultima_visita":26,

"clasificacion":"Retener",

},

{

"id":"j191",

"nombre":"AlejandraOrtiz",

"edad":50,

"ocupacion":"Ingeniero",

"presupuesto_hoy":652,

"fichas_actuales":190,

"juego_actual":"Keno",

"monto_apuesta":130,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"22:50",

"rondas_jugadas_hoy":12,

"gasto_hoy":461,

"frecuencia_semanal":1,

"tiempo_promedio_visita":311,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":38,

"gasto_maximo_historico":399,

"perdidas_acumuladas":7878,

"ganancias_acumuladas":8846,

"variedad_juegos_probados":4,

"juego_favorito":"Keno",

"dias_visita":"Mie,Vie,Mar,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":250,

"dias_desde_primera_visita":1158,

"dias_desde_ultima_visita":49,

"clasificacion":"Retener",

},

{

"id":"j192",

"nombre":"JavierRivera",

"edad":30,

"ocupacion":"Abogado",

"presupuesto_hoy":1851,

"fichas_actuales":179,

"juego_actual":"Ruleta",

"monto_apuesta":145,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"18:08",

"rondas_jugadas_hoy":23,

"gasto_hoy":1654,

"frecuencia_semanal":0,

"tiempo_promedio_visita":241,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":71,

"gasto_maximo_historico":726,

"perdidas_acumuladas":983,

"ganancias_acumuladas":14765,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":45,

"dias_desde_primera_visita":811,

"dias_desde_ultima_visita":28,

"clasificacion":"Retener",

},

{

"id":"j193",

"nombre":"LucasDiaz",

"edad":60,

"ocupacion":"Desempleado",

"presupuesto_hoy":776,

"fichas_actuales":761,

"juego_actual":"Cartas",

"monto_apuesta":68,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.3,

"hora_actual":"16:27",

"rondas_jugadas_hoy":35,

"gasto_hoy":0,

"frecuencia_semanal":3,

"tiempo_promedio_visita":113,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":429,

"perdidas_acumuladas":10678,

"ganancias_acumuladas":11727,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Dom,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":350,

"dias_desde_primera_visita":1092,

"dias_desde_ultima_visita":14,

"clasificacion":"Cuidar",

},

{

"id":"j194",

"nombre":"RafaelRivera",

"edad":49,

"ocupacion":"Jubilado",

"presupuesto_hoy":514,

"fichas_actuales":432,

"juego_actual":"Baccarat",

"monto_apuesta":157,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"13:37",

"rondas_jugadas_hoy":20,

"gasto_hoy":71,

"frecuencia_semanal":5,

"tiempo_promedio_visita":325,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":528,

"perdidas_acumuladas":14110,

"ganancias_acumuladas":15264,

"variedad_juegos_probados":6,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Mie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":448,

"dias_desde_primera_visita":246,

"dias_desde_ultima_visita":40,

"clasificacion":"Cuidar",

},

{

"id":"j195",

"nombre":"PaolaMartinez",

"edad":22,

"ocupacion":"Electricista",

"presupuesto_hoy":51,

"fichas_actuales":49,

"juego_actual":"Blackjack",

"monto_apuesta":123,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.6,

"hora_actual":"10:26",

"rondas_jugadas_hoy":1,

"gasto_hoy":0,

"frecuencia_semanal":1,

"tiempo_promedio_visita":139,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":245,

"perdidas_acumuladas":8225,

"ganancias_acumuladas":1455,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Mie,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":91,

"dias_desde_primera_visita":1387,

"dias_desde_ultima_visita":46,

"clasificacion":"Cuidar",

},

{

"id":"j196",

"nombre":"SofiaGarcia",

"edad":33,

"ocupacion":"Abogado",

"presupuesto_hoy":306,

"fichas_actuales":73,

"juego_actual":"Ruleta",

"monto_apuesta":121,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.4,

"hora_actual":"13:10",

"rondas_jugadas_hoy":3,

"gasto_hoy":226,

"frecuencia_semanal":0,

"tiempo_promedio_visita":68,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":75,

"gasto_maximo_historico":50,

"perdidas_acumuladas":5437,

"ganancias_acumuladas":11638,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Mie,Vie,Jue,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":70,

"dias_desde_primera_visita":501,

"dias_desde_ultima_visita":21,

"clasificacion":"Retener",

},

{

"id":"j197",

"nombre":"IsabelTorres",

"edad":63,

"ocupacion":"Desempleado",

"presupuesto_hoy":1529,

"fichas_actuales":692,

"juego_actual":"Keno",

"monto_apuesta":27,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"20:21",

"rondas_jugadas_hoy":18,

"gasto_hoy":807,

"frecuencia_semanal":1,

"tiempo_promedio_visita":106,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":44,

"gasto_maximo_historico":728,

"perdidas_acumuladas":1517,

"ganancias_acumuladas":4762,

"variedad_juegos_probados":3,

"juego_favorito":"Keno",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":37,

"dias_desde_primera_visita":1496,

"dias_desde_ultima_visita":4,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j198",

"nombre":"DanielGonzalez",

"edad":30,

"ocupacion":"Medico",

"presupuesto_hoy":1399,

"fichas_actuales":963,

"juego_actual":"Baccarat",

"monto_apuesta":121,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.6,

"hora_actual":"23:21",

"rondas_jugadas_hoy":32,

"gasto_hoy":422,

"frecuencia_semanal":1,

"tiempo_promedio_visita":302,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":298,

"perdidas_acumuladas":7190,

"ganancias_acumuladas":11834,

"variedad_juegos_probados":3,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Jue,Dom,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":122,

"dias_desde_primera_visita":34,

"dias_desde_ultima_visita":58,

"clasificacion":"Retener",

},

{

"id":"j199",

"nombre":"AngelRodriguez",

"edad":51,

"ocupacion":"Disenador",

"presupuesto_hoy":54,

"fichas_actuales":24,

"juego_actual":"Dados",

"monto_apuesta":144,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"21:28",

"rondas_jugadas_hoy":13,

"gasto_hoy":0,

"frecuencia_semanal":2,

"tiempo_promedio_visita":38,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":309,

"perdidas_acumuladas":6610,

"ganancias_acumuladas":16971,

"variedad_juegos_probados":6,

"juego_favorito":"Dados",

"dias_visita":"Lun,Vie,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":230,

"dias_desde_primera_visita":811,

"dias_desde_ultima_visita":34,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j200",

"nombre":"EnriqueRamirez",

"edad":65,

"ocupacion":"Cocinero",

"presupuesto_hoy":1637,

"fichas_actuales":1290,

"juego_actual":"Baccarat",

"monto_apuesta":136,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.1,

"hora_actual":"14:50",

"rondas_jugadas_hoy":17,

"gasto_hoy":337,

"frecuencia_semanal":0,

"tiempo_promedio_visita":45,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":567,

"perdidas_acumuladas":5397,

"ganancias_acumuladas":16074,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Mie,Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":140,

"dias_desde_primera_visita":67,

"dias_desde_ultima_visita":55,

"clasificacion":"Retener",

},







{

"id":"j101",

"nombre":"MiguelAlvarez",

"edad":62,

"ocupacion":"Chofer",

"presupuesto_hoy":1835,

"fichas_actuales":1224,

"juego_actual":"Ruleta",

"monto_apuesta":152,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"17:57",

"rondas_jugadas_hoy":32,

"gasto_hoy":608,

"frecuencia_semanal":7,

"tiempo_promedio_visita":234,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":424,

"perdidas_acumuladas":7506,

"ganancias_acumuladas":18135,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Vie,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":96,

"dias_desde_primera_visita":1128,

"dias_desde_ultima_visita":35,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j102",

"nombre":"MarioLopez",

"edad":28,

"ocupacion":"Disenador",

"presupuesto_hoy":1753,

"fichas_actuales":179,

"juego_actual":"Cartas",

"monto_apuesta":175,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"20:06",

"rondas_jugadas_hoy":22,

"gasto_hoy":1566,

"frecuencia_semanal":7,

"tiempo_promedio_visita":212,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":71,

"gasto_maximo_historico":86,

"perdidas_acumuladas":6260,

"ganancias_acumuladas":14927,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Sab,Vie,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":406,

"dias_desde_primera_visita":1259,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j103",

"nombre":"EduardoCruz",

"edad":70,

"ocupacion":"Arquitecto",

"presupuesto_hoy":730,

"fichas_actuales":591,

"juego_actual":"Blackjack",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.7,

"hora_actual":"16:54",

"rondas_jugadas_hoy":12,

"gasto_hoy":117,

"frecuencia_semanal":0,

"tiempo_promedio_visita":224,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":978,

"perdidas_acumuladas":6665,

"ganancias_acumuladas":18161,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Lun,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":248,

"dias_desde_primera_visita":503,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j104",

"nombre":"SergioTorres",

"edad":21,

"ocupacion":"Abogado",

"presupuesto_hoy":915,

"fichas_actuales":872,

"juego_actual":"Ruleta",

"monto_apuesta":128,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"13:56",

"rondas_jugadas_hoy":34,

"gasto_hoy":32,

"frecuencia_semanal":0,

"tiempo_promedio_visita":241,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":149,

"perdidas_acumuladas":1538,

"ganancias_acumuladas":18629,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Jue,Mie,Vie,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":474,

"dias_desde_primera_visita":694,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j105",

"nombre":"AngelVargas",

"edad":38,

"ocupacion":"Enfermero",

"presupuesto_hoy":1786,

"fichas_actuales":1133,

"juego_actual":"Blackjack",

"monto_apuesta":182,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.0,

"hora_actual":"15:24",

"rondas_jugadas_hoy":28,

"gasto_hoy":630,

"frecuencia_semanal":0,

"tiempo_promedio_visita":283,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":22,

"gasto_maximo_historico":687,

"perdidas_acumuladas":4128,

"ganancias_acumuladas":8749,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie,Dom,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":2,

"dias_desde_primera_visita":1126,

"dias_desde_ultima_visita":46,

"clasificacion":"Retener",

},

{

"id":"j106",

"nombre":"FelipeCruz",

"edad":20,

"ocupacion":"Cocinero",

"presupuesto_hoy":679,

"fichas_actuales":139,

"juego_actual":"Poker",

"monto_apuesta":157,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.8,

"hora_actual":"21:58",

"rondas_jugadas_hoy":34,

"gasto_hoy":524,

"frecuencia_semanal":7,

"tiempo_promedio_visita":224,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":984,

"perdidas_acumuladas":8860,

"ganancias_acumuladas":11214,

"variedad_juegos_probados":6,

"juego_favorito":"Poker",

"dias_visita":"Vie,Dom,Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":447,

"dias_desde_primera_visita":617,

"dias_desde_ultima_visita":9,

"clasificacion":"Cuidar",

},

{

"id":"j107",

"nombre":"NataliaMendoza",

"edad":34,

"ocupacion":"Docente",

"presupuesto_hoy":1480,

"fichas_actuales":204,

"juego_actual":"Ruleta",

"monto_apuesta":144,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"15:02",

"rondas_jugadas_hoy":29,

"gasto_hoy":1261,

"frecuencia_semanal":4,

"tiempo_promedio_visita":282,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":656,

"perdidas_acumuladas":144,

"ganancias_acumuladas":8889,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Jue,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":296,

"dias_desde_primera_visita":150,

"dias_desde_ultima_visita":6,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j108",

"nombre":"ManuelCastillo",

"edad":57,

"ocupacion":"Enfermero",

"presupuesto_hoy":333,

"fichas_actuales":82,

"juego_actual":"Blackjack",

"monto_apuesta":59,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"16:38",

"rondas_jugadas_hoy":13,

"gasto_hoy":236,

"frecuencia_semanal":5,

"tiempo_promedio_visita":286,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":18,

"gasto_maximo_historico":621,

"perdidas_acumuladas":12224,

"ganancias_acumuladas":12162,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Jue,Mar,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":303,

"dias_desde_primera_visita":1287,

"dias_desde_ultima_visita":21,

"clasificacion":"Cuidar",

},

{

"id":"j109",

"nombre":"MartinFlores",

"edad":56,

"ocupacion":"Desempleado",

"presupuesto_hoy":1324,

"fichas_actuales":773,

"juego_actual":"Poker",

"monto_apuesta":103,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.2,

"hora_actual":"11:50",

"rondas_jugadas_hoy":19,

"gasto_hoy":548,

"frecuencia_semanal":5,

"tiempo_promedio_visita":103,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":28,

"gasto_maximo_historico":91,

"perdidas_acumuladas":4351,

"ganancias_acumuladas":14715,

"variedad_juegos_probados":2,

"juego_favorito":"Poker",

"dias_visita":"Sab,Lun,Mar,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":327,

"dias_desde_primera_visita":257,

"dias_desde_ultima_visita":16,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j110",

"nombre":"LuciaVazquez",

"edad":49,

"ocupacion":"Cocinero",

"presupuesto_hoy":1405,

"fichas_actuales":160,

"juego_actual":"Cartas",

"monto_apuesta":189,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.6,

"hora_actual":"16:38",

"rondas_jugadas_hoy":31,

"gasto_hoy":1229,

"frecuencia_semanal":0,

"tiempo_promedio_visita":298,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":39,

"gasto_maximo_historico":886,

"perdidas_acumuladas":8373,

"ganancias_acumuladas":1366,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":1,

"dias_desde_primera_visita":530,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j111",

"nombre":"JuliaMartinez",

"edad":51,

"ocupacion":"Pintor",

"presupuesto_hoy":1279,

"fichas_actuales":261,

"juego_actual":"Tragamonedas",

"monto_apuesta":45,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.3,

"hora_actual":"17:19",

"rondas_jugadas_hoy":23,

"gasto_hoy":1006,

"frecuencia_semanal":6,

"tiempo_promedio_visita":233,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":294,

"perdidas_acumuladas":9488,

"ganancias_acumuladas":4580,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mie,Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":187,

"dias_desde_primera_visita":1012,

"dias_desde_ultima_visita":14,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j112",

"nombre":"VictoriaTorres",

"edad":37,

"ocupacion":"Desempleado",

"presupuesto_hoy":256,

"fichas_actuales":138,

"juego_actual":"Cartas",

"monto_apuesta":10,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"21:05",

"rondas_jugadas_hoy":6,

"gasto_hoy":104,

"frecuencia_semanal":6,

"tiempo_promedio_visita":314,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":17,

"gasto_maximo_historico":899,

"perdidas_acumuladas":9374,

"ganancias_acumuladas":5971,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":497,

"dias_desde_primera_visita":1439,

"dias_desde_ultima_visita":40,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j113",

"nombre":"LuisFlores",

"edad":40,

"ocupacion":"Desempleado",

"presupuesto_hoy":699,

"fichas_actuales":369,

"juego_actual":"Dados",

"monto_apuesta":81,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.3,

"hora_actual":"18:38",

"rondas_jugadas_hoy":10,

"gasto_hoy":310,

"frecuencia_semanal":7,

"tiempo_promedio_visita":360,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":326,

"perdidas_acumuladas":13438,

"ganancias_acumuladas":14128,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Mie,Sab,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":212,

"dias_desde_primera_visita":1439,

"dias_desde_ultima_visita":17,

"clasificacion":"Cuidar",

},

{

"id":"j114",

"nombre":"CarlaFlores",

"edad":60,

"ocupacion":"Medico",

"presupuesto_hoy":657,

"fichas_actuales":162,

"juego_actual":"Tragamonedas",

"monto_apuesta":4,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"20:34",

"rondas_jugadas_hoy":18,

"gasto_hoy":491,

"frecuencia_semanal":2,

"tiempo_promedio_visita":151,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":27,

"gasto_maximo_historico":349,

"perdidas_acumuladas":8331,

"ganancias_acumuladas":12595,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Dom,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":314,

"dias_desde_primera_visita":1305,

"dias_desde_ultima_visita":41,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j115",

"nombre":"AlejandraRivera",

"edad":19,

"ocupacion":"Contador",

"presupuesto_hoy":1972,

"fichas_actuales":952,

"juego_actual":"Tragamonedas",

"monto_apuesta":137,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"21:44",

"rondas_jugadas_hoy":7,

"gasto_hoy":1017,

"frecuencia_semanal":1,

"tiempo_promedio_visita":77,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":145,

"gasto_maximo_historico":238,

"perdidas_acumuladas":10629,

"ganancias_acumuladas":8253,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":340,

"dias_desde_primera_visita":1283,

"dias_desde_ultima_visita":31,

"clasificacion":"Cuidar",

},

{

"id":"j116",

"nombre":"SergioAlvarez",

"edad":18,

"ocupacion":"Disenador",

"presupuesto_hoy":1937,

"fichas_actuales":404,

"juego_actual":"Tragamonedas",

"monto_apuesta":161,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"20:24",

"rondas_jugadas_hoy":33,

"gasto_hoy":1508,

"frecuencia_semanal":5,

"tiempo_promedio_visita":156,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":45,

"gasto_maximo_historico":533,

"perdidas_acumuladas":11942,

"ganancias_acumuladas":11143,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Lun,Mar,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":183,

"dias_desde_primera_visita":865,

"dias_desde_ultima_visita":26,

"clasificacion":"Cuidar",

},

{

"id":"j117",

"nombre":"EduardoReyes",

"edad":22,

"ocupacion":"Docente",

"presupuesto_hoy":721,

"fichas_actuales":588,

"juego_actual":"Poker",

"monto_apuesta":50,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"12:03",

"rondas_jugadas_hoy":9,

"gasto_hoy":115,

"frecuencia_semanal":3,

"tiempo_promedio_visita":297,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":12,

"gasto_maximo_historico":876,

"perdidas_acumuladas":8930,

"ganancias_acumuladas":8785,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Jue,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":393,

"dias_desde_primera_visita":550,

"dias_desde_ultima_visita":57,

"clasificacion":"Cuidar",

},

{

"id":"j118",

"nombre":"AdrianaTorres",

"edad":30,

"ocupacion":"Electricista",

"presupuesto_hoy":1987,

"fichas_actuales":936,

"juego_actual":"Dados",

"monto_apuesta":184,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.2,

"hora_actual":"11:07",

"rondas_jugadas_hoy":24,

"gasto_hoy":1032,

"frecuencia_semanal":7,

"tiempo_promedio_visita":93,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":80,

"perdidas_acumuladas":5334,

"ganancias_acumuladas":5013,

"variedad_juegos_probados":5,

"juego_favorito":"Dados",

"dias_visita":"Dom,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":446,

"dias_desde_primera_visita":1006,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j119",

"nombre":"EduardoReyes",

"edad":39,

"ocupacion":"Vendedor",

"presupuesto_hoy":239,

"fichas_actuales":233,

"juego_actual":"Tragamonedas",

"monto_apuesta":155,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.9,

"hora_actual":"17:36",

"rondas_jugadas_hoy":2,

"gasto_hoy":0,

"frecuencia_semanal":6,

"tiempo_promedio_visita":342,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":427,

"perdidas_acumuladas":10169,

"ganancias_acumuladas":13239,

"variedad_juegos_probados":3,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Sab,Lun,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":448,

"dias_desde_primera_visita":1331,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j120",

"nombre":"SofiaGarcia",

"edad":47,

"ocupacion":"Pintor",

"presupuesto_hoy":815,

"fichas_actuales":265,

"juego_actual":"Poker",

"monto_apuesta":35,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.0,

"hora_actual":"19:16",

"rondas_jugadas_hoy":25,

"gasto_hoy":543,

"frecuencia_semanal":3,

"tiempo_promedio_visita":269,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":286,

"perdidas_acumuladas":14333,

"ganancias_acumuladas":16968,

"variedad_juegos_probados":2,

"juego_favorito":"Poker",

"dias_visita":"Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":444,

"dias_desde_primera_visita":81,

"dias_desde_ultima_visita":8,

"clasificacion":"Cuidar",

},

{

"id":"j121",

"nombre":"AndresRodriguez",

"edad":54,

"ocupacion":"Enfermero",

"presupuesto_hoy":1696,

"fichas_actuales":1237,

"juego_actual":"Ruleta",

"monto_apuesta":37,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"16:43",

"rondas_jugadas_hoy":7,

"gasto_hoy":451,

"frecuencia_semanal":7,

"tiempo_promedio_visita":319,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":64,

"gasto_maximo_historico":911,

"perdidas_acumuladas":11660,

"ganancias_acumuladas":2631,

"variedad_juegos_probados":1,

"juego_favorito":"Ruleta",

"dias_visita":"Sab,Mar,Jue,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":340,

"dias_desde_primera_visita":54,

"dias_desde_ultima_visita":53,

"clasificacion":"Cuidar",

},

{

"id":"j122",

"nombre":"MateoMedina",

"edad":64,

"ocupacion":"Contador",

"presupuesto_hoy":1504,

"fichas_actuales":363,

"juego_actual":"Keno",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.1,

"hora_actual":"10:42",

"rondas_jugadas_hoy":34,

"gasto_hoy":1123,

"frecuencia_semanal":5,

"tiempo_promedio_visita":261,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":33,

"gasto_maximo_historico":383,

"perdidas_acumuladas":11000,

"ganancias_acumuladas":14753,

"variedad_juegos_probados":1,

"juego_favorito":"Keno",

"dias_visita":"Sab,Dom,Mar,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":401,

"dias_desde_primera_visita":656,

"dias_desde_ultima_visita":60,

"clasificacion":"Cuidar",

},

{

"id":"j123",

"nombre":"SergioRomero",

"edad":36,

"ocupacion":"Mecanico",

"presupuesto_hoy":1028,

"fichas_actuales":528,

"juego_actual":"Dados",

"monto_apuesta":146,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"22:21",

"rondas_jugadas_hoy":40,

"gasto_hoy":470,

"frecuencia_semanal":7,

"tiempo_promedio_visita":188,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":11,

"gasto_maximo_historico":812,

"perdidas_acumuladas":7929,

"ganancias_acumuladas":3930,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Vie,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":310,

"dias_desde_primera_visita":709,

"dias_desde_ultima_visita":32,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j124",

"nombre":"AlejandroGonzalez",

"edad":20,

"ocupacion":"Disenador",

"presupuesto_hoy":1458,

"fichas_actuales":1280,

"juego_actual":"Blackjack",

"monto_apuesta":112,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"21:34",

"rondas_jugadas_hoy":39,

"gasto_hoy":177,

"frecuencia_semanal":1,

"tiempo_promedio_visita":111,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":175,

"perdidas_acumuladas":9396,

"ganancias_acumuladas":9977,

"variedad_juegos_probados":6,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Mie,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":374,

"dias_desde_primera_visita":820,

"dias_desde_ultima_visita":28,

"clasificacion":"Cuidar",

},

{

"id":"j125",

"nombre":"DanielaVargas",

"edad":65,

"ocupacion":"Mecanico",

"presupuesto_hoy":385,

"fichas_actuales":322,

"juego_actual":"Baccarat",

"monto_apuesta":116,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"12:43",

"rondas_jugadas_hoy":1,

"gasto_hoy":35,

"frecuencia_semanal":1,

"tiempo_promedio_visita":272,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":35,

"gasto_maximo_historico":656,

"perdidas_acumuladas":1953,

"ganancias_acumuladas":15139,

"variedad_juegos_probados":3,

"juego_favorito":"Baccarat",

"dias_visita":"Vie,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":156,

"dias_desde_primera_visita":1119,

"dias_desde_ultima_visita":21,

"clasificacion":"Retener",

},

{

"id":"j126",

"nombre":"MariaRivera",

"edad":51,

"ocupacion":"Cocinero",

"presupuesto_hoy":1568,

"fichas_actuales":1159,

"juego_actual":"Dados",

"monto_apuesta":66,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"23:17",

"rondas_jugadas_hoy":33,

"gasto_hoy":383,

"frecuencia_semanal":1,

"tiempo_promedio_visita":306,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":11,

"gasto_maximo_historico":833,

"perdidas_acumuladas":9181,

"ganancias_acumuladas":12233,

"variedad_juegos_probados":3,

"juego_favorito":"Dados",

"dias_visita":"Vie,Jue,Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":365,

"dias_desde_primera_visita":1109,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j127",

"nombre":"MariaRivera",

"edad":53,

"ocupacion":"Abogado",

"presupuesto_hoy":397,

"fichas_actuales":65,

"juego_actual":"Baccarat",

"monto_apuesta":101,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.9,

"hora_actual":"13:50",

"rondas_jugadas_hoy":23,

"gasto_hoy":303,

"frecuencia_semanal":7,

"tiempo_promedio_visita":45,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":201,

"perdidas_acumuladas":479,

"ganancias_acumuladas":8000,

"variedad_juegos_probados":5,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Dom,Lun,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":492,

"dias_desde_primera_visita":1286,

"dias_desde_ultima_visita":52,

"clasificacion":"VIP",

},

{

"id":"j128",

"nombre":"DanielaRuiz",

"edad":43,

"ocupacion":"Vendedor",

"presupuesto_hoy":752,

"fichas_actuales":258,

"juego_actual":"Ruleta",

"monto_apuesta":70,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"17:51",

"rondas_jugadas_hoy":21,

"gasto_hoy":470,

"frecuencia_semanal":3,

"tiempo_promedio_visita":278,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":22,

"gasto_maximo_historico":764,

"perdidas_acumuladas":9152,

"ganancias_acumuladas":11289,

"variedad_juegos_probados":5,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Lun,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":7,

"dias_desde_primera_visita":91,

"dias_desde_ultima_visita":7,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j129",

"nombre":"PedroAlvarez",

"edad":67,

"ocupacion":"Vendedor",

"presupuesto_hoy":650,

"fichas_actuales":454,

"juego_actual":"Tragamonedas",

"monto_apuesta":51,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"16:41",

"rondas_jugadas_hoy":14,

"gasto_hoy":195,

"frecuencia_semanal":4,

"tiempo_promedio_visita":152,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":384,

"perdidas_acumuladas":7794,

"ganancias_acumuladas":3516,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":362,

"dias_desde_primera_visita":672,

"dias_desde_ultima_visita":57,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j130",

"nombre":"ElenaRuiz",

"edad":54,

"ocupacion":"Electricista",

"presupuesto_hoy":1153,

"fichas_actuales":200,

"juego_actual":"Keno",

"monto_apuesta":179,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"15:38",

"rondas_jugadas_hoy":30,

"gasto_hoy":944,

"frecuencia_semanal":2,

"tiempo_promedio_visita":37,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":475,

"perdidas_acumuladas":12729,

"ganancias_acumuladas":15772,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Sab,Mar,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":389,

"dias_desde_primera_visita":1079,

"dias_desde_ultima_visita":41,

"clasificacion":"Cuidar",

},

{

"id":"j131",

"nombre":"ValeriaRuiz",

"edad":19,

"ocupacion":"Docente",

"presupuesto_hoy":1602,

"fichas_actuales":958,

"juego_actual":"Tragamonedas",

"monto_apuesta":116,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.9,

"hora_actual":"20:36",

"rondas_jugadas_hoy":21,

"gasto_hoy":621,

"frecuencia_semanal":3,

"tiempo_promedio_visita":293,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":29,

"gasto_maximo_historico":774,

"perdidas_acumuladas":3972,

"ganancias_acumuladas":1140,

"variedad_juegos_probados":6,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mie,Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":368,

"dias_desde_primera_visita":903,

"dias_desde_ultima_visita":49,

"clasificacion":"Cuidar",

},

{

"id":"j132",

"nombre":"NataliaMartinez",

"edad":22,

"ocupacion":"Empresario",

"presupuesto_hoy":1704,

"fichas_actuales":544,

"juego_actual":"Baccarat",

"monto_apuesta":8,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"15:46",

"rondas_jugadas_hoy":26,

"gasto_hoy":1143,

"frecuencia_semanal":5,

"tiempo_promedio_visita":222,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":876,

"perdidas_acumuladas":248,

"ganancias_acumuladas":8039,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Vie,Mie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":473,

"dias_desde_primera_visita":450,

"dias_desde_ultima_visita":43,

"clasificacion":"Cuidar",

},

{

"id":"j133",

"nombre":"TomasVazquez",

"edad":70,

"ocupacion":"Pintor",

"presupuesto_hoy":24,

"fichas_actuales":9,

"juego_actual":"Blackjack",

"monto_apuesta":189,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"17:05",

"rondas_jugadas_hoy":2,

"gasto_hoy":8,

"frecuencia_semanal":5,

"tiempo_promedio_visita":205,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":868,

"perdidas_acumuladas":11507,

"ganancias_acumuladas":3520,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":51,

"dias_desde_primera_visita":977,

"dias_desde_ultima_visita":40,

"clasificacion":"Cuidar",

},

{

"id":"j134",

"nombre":"BeatrizPerez",

"edad":47,

"ocupacion":"Programador",

"presupuesto_hoy":619,

"fichas_actuales":77,

"juego_actual":"Cartas",

"monto_apuesta":181,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.6,

"hora_actual":"11:15",

"rondas_jugadas_hoy":1,

"gasto_hoy":533,

"frecuencia_semanal":7,

"tiempo_promedio_visita":66,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":533,

"gasto_maximo_historico":79,

"perdidas_acumuladas":10332,

"ganancias_acumuladas":16439,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Mie,Lun,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":327,

"dias_desde_primera_visita":142,

"dias_desde_ultima_visita":55,

"clasificacion":"Cuidar",

},

{

"id":"j135",

"nombre":"MarianaRuiz",

"edad":57,

"ocupacion":"Ingeniero",

"presupuesto_hoy":156,

"fichas_actuales":99,

"juego_actual":"Blackjack",

"monto_apuesta":126,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"15:06",

"rondas_jugadas_hoy":21,

"gasto_hoy":42,

"frecuencia_semanal":3,

"tiempo_promedio_visita":357,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":2,

"gasto_maximo_historico":135,

"perdidas_acumuladas":7680,

"ganancias_acumuladas":1476,

"variedad_juegos_probados":1,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":338,

"dias_desde_primera_visita":69,

"dias_desde_ultima_visita":36,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j136",

"nombre":"MariaMendoza",

"edad":44,

"ocupacion":"Cocinero",

"presupuesto_hoy":635,

"fichas_actuales":113,

"juego_actual":"Baccarat",

"monto_apuesta":66,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"21:36",

"rondas_jugadas_hoy":16,

"gasto_hoy":514,

"frecuencia_semanal":0,

"tiempo_promedio_visita":188,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":32,

"gasto_maximo_historico":797,

"perdidas_acumuladas":11527,

"ganancias_acumuladas":7126,

"variedad_juegos_probados":1,

"juego_favorito":"Baccarat",

"dias_visita":"Sab,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":272,

"dias_desde_primera_visita":174,

"dias_desde_ultima_visita":17,

"clasificacion":"Cuidar",

},

{

"id":"j137",

"nombre":"JavierRamirez",

"edad":60,

"ocupacion":"Mecanico",

"presupuesto_hoy":1002,

"fichas_actuales":478,

"juego_actual":"Keno",

"monto_apuesta":194,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"23:10",

"rondas_jugadas_hoy":7,

"gasto_hoy":506,

"frecuencia_semanal":5,

"tiempo_promedio_visita":348,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":72,

"gasto_maximo_historico":482,

"perdidas_acumuladas":14591,

"ganancias_acumuladas":18671,

"variedad_juegos_probados":1,

"juego_favorito":"Keno",

"dias_visita":"Vie,Jue,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":455,

"dias_desde_primera_visita":1185,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j138",

"nombre":"JoseOrtiz",

"edad":62,

"ocupacion":"Medico",

"presupuesto_hoy":1466,

"fichas_actuales":931,

"juego_actual":"Tragamonedas",

"monto_apuesta":130,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"21:14",

"rondas_jugadas_hoy":4,

"gasto_hoy":518,

"frecuencia_semanal":1,

"tiempo_promedio_visita":32,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":129,

"gasto_maximo_historico":307,

"perdidas_acumuladas":12045,

"ganancias_acumuladas":7798,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":159,

"dias_desde_primera_visita":1247,

"dias_desde_ultima_visita":33,

"clasificacion":"Cuidar",

},

{

"id":"j139",

"nombre":"GabrielaReyes",

"edad":59,

"ocupacion":"Enfermero",

"presupuesto_hoy":747,

"fichas_actuales":406,

"juego_actual":"Blackjack",

"monto_apuesta":110,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.6,

"hora_actual":"23:19",

"rondas_jugadas_hoy":20,

"gasto_hoy":318,

"frecuencia_semanal":4,

"tiempo_promedio_visita":48,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":694,

"perdidas_acumuladas":2145,

"ganancias_acumuladas":17039,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Jue,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":262,

"dias_desde_primera_visita":1466,

"dias_desde_ultima_visita":15,

"clasificacion":"VIP",

},

{

"id":"j140",

"nombre":"FernandoRuiz",

"edad":39,

"ocupacion":"Mecanico",

"presupuesto_hoy":1916,

"fichas_actuales":1440,

"juego_actual":"Ruleta",

"monto_apuesta":63,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.4,

"hora_actual":"14:44",

"rondas_jugadas_hoy":3,

"gasto_hoy":474,

"frecuencia_semanal":2,

"tiempo_promedio_visita":278,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":158,

"gasto_maximo_historico":744,

"perdidas_acumuladas":13057,

"ganancias_acumuladas":426,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Mie,Lun,Mar,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":168,

"dias_desde_primera_visita":898,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j141",

"nombre":"VeronicaVazquez",

"edad":26,

"ocupacion":"Pintor",

"presupuesto_hoy":1547,

"fichas_actuales":1397,

"juego_actual":"Cartas",

"monto_apuesta":105,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"21:38",

"rondas_jugadas_hoy":8,

"gasto_hoy":136,

"frecuencia_semanal":4,

"tiempo_promedio_visita":334,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":17,

"gasto_maximo_historico":421,

"perdidas_acumuladas":9833,

"ganancias_acumuladas":18559,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":490,

"dias_desde_primera_visita":1403,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j142",

"nombre":"CarlaVazquez",

"edad":61,

"ocupacion":"Mecanico",

"presupuesto_hoy":1086,

"fichas_actuales":592,

"juego_actual":"Keno",

"monto_apuesta":109,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.3,

"hora_actual":"21:14",

"rondas_jugadas_hoy":35,

"gasto_hoy":494,

"frecuencia_semanal":1,

"tiempo_promedio_visita":302,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":14,

"gasto_maximo_historico":822,

"perdidas_acumuladas":4659,

"ganancias_acumuladas":18811,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Vie,Dom,Jue,Sab",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":171,

"dias_desde_primera_visita":23,

"dias_desde_ultima_visita":6,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j143",

"nombre":"AdrianRivera",

"edad":22,

"ocupacion":"Desempleado",

"presupuesto_hoy":336,

"fichas_actuales":157,

"juego_actual":"Tragamonedas",

"monto_apuesta":115,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"22:39",

"rondas_jugadas_hoy":21,

"gasto_hoy":152,

"frecuencia_semanal":6,

"tiempo_promedio_visita":311,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":7,

"gasto_maximo_historico":60,

"perdidas_acumuladas":8751,

"ganancias_acumuladas":17842,

"variedad_juegos_probados":5,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Mie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":339,

"dias_desde_primera_visita":100,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j144",

"nombre":"AngelMendoza",

"edad":62,

"ocupacion":"Estudiante",

"presupuesto_hoy":1591,

"fichas_actuales":258,

"juego_actual":"Dados",

"monto_apuesta":9,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"21:30",

"rondas_jugadas_hoy":10,

"gasto_hoy":1328,

"frecuencia_semanal":4,

"tiempo_promedio_visita":289,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":132,

"gasto_maximo_historico":361,

"perdidas_acumuladas":14427,

"ganancias_acumuladas":16547,

"variedad_juegos_probados":4,

"juego_favorito":"Dados",

"dias_visita":"Mar,Dom,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":145,

"dias_desde_primera_visita":22,

"dias_desde_ultima_visita":58,

"clasificacion":"Cuidar",

},

{

"id":"j145",

"nombre":"AliciaLopez",

"edad":45,

"ocupacion":"Electricista",

"presupuesto_hoy":521,

"fichas_actuales":497,

"juego_actual":"Poker",

"monto_apuesta":198,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"20:55",

"rondas_jugadas_hoy":7,

"gasto_hoy":16,

"frecuencia_semanal":6,

"tiempo_promedio_visita":232,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":2,

"gasto_maximo_historico":687,

"perdidas_acumuladas":4687,

"ganancias_acumuladas":14693,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":378,

"dias_desde_primera_visita":157,

"dias_desde_ultima_visita":27,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j146",

"nombre":"LilianaPerez",

"edad":19,

"ocupacion":"Chofer",

"presupuesto_hoy":1828,

"fichas_actuales":108,

"juego_actual":"Tragamonedas",

"monto_apuesta":3,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.8,

"hora_actual":"17:04",

"rondas_jugadas_hoy":8,

"gasto_hoy":1700,

"frecuencia_semanal":4,

"tiempo_promedio_visita":319,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":212,

"gasto_maximo_historico":436,

"perdidas_acumuladas":8346,

"ganancias_acumuladas":14857,

"variedad_juegos_probados":5,

"juego_favorito":"Tragamonedas",

"dias_visita":"Dom,Lun,Sab,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":332,

"dias_desde_primera_visita":1074,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j147",

"nombre":"PatriciaAguilar",

"edad":50,

"ocupacion":"Cocinero",

"presupuesto_hoy":1509,

"fichas_actuales":525,

"juego_actual":"Poker",

"monto_apuesta":173,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.9,

"hora_actual":"21:16",

"rondas_jugadas_hoy":6,

"gasto_hoy":972,

"frecuencia_semanal":4,

"tiempo_promedio_visita":159,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":162,

"gasto_maximo_historico":85,

"perdidas_acumuladas":2674,

"ganancias_acumuladas":6229,

"variedad_juegos_probados":5,

"juego_favorito":"Poker",

"dias_visita":"Sab,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":240,

"dias_desde_primera_visita":462,

"dias_desde_ultima_visita":12,

"clasificacion":"VIP",

},

{

"id":"j148",

"nombre":"JulioGomez",

"edad":57,

"ocupacion":"Chofer",

"presupuesto_hoy":1291,

"fichas_actuales":499,

"juego_actual":"Ruleta",

"monto_apuesta":138,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.5,

"hora_actual":"11:07",

"rondas_jugadas_hoy":2,

"gasto_hoy":779,

"frecuencia_semanal":6,

"tiempo_promedio_visita":356,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":389,

"gasto_maximo_historico":652,

"perdidas_acumuladas":9793,

"ganancias_acumuladas":2302,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Dom,Jue,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":349,

"dias_desde_primera_visita":1235,

"dias_desde_ultima_visita":16,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j149",

"nombre":"IvanVazquez",

"edad":61,

"ocupacion":"Disenador",

"presupuesto_hoy":424,

"fichas_actuales":374,

"juego_actual":"Ruleta",

"monto_apuesta":136,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.6,

"hora_actual":"23:46",

"rondas_jugadas_hoy":37,

"gasto_hoy":34,

"frecuencia_semanal":3,

"tiempo_promedio_visita":329,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":474,

"perdidas_acumuladas":13578,

"ganancias_acumuladas":396,

"variedad_juegos_probados":6,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":198,

"dias_desde_primera_visita":466,

"dias_desde_ultima_visita":14,

"clasificacion":"Cuidar",

},

{

"id":"j150",

"nombre":"SantiagoTorres",

"edad":45,

"ocupacion":"Ingeniero",

"presupuesto_hoy":519,

"fichas_actuales":98,

"juego_actual":"Blackjack",

"monto_apuesta":14,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":6.0,

"hora_actual":"11:43",

"rondas_jugadas_hoy":10,

"gasto_hoy":397,

"frecuencia_semanal":6,

"tiempo_promedio_visita":306,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":39,

"gasto_maximo_historico":502,

"perdidas_acumuladas":6998,

"ganancias_acumuladas":1515,

"variedad_juegos_probados":1,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":375,

"dias_desde_primera_visita":962,

"dias_desde_ultima_visita":28,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j151",

"nombre":"PaulaRomero",

"edad":23,

"ocupacion":"Carpintero",

"presupuesto_hoy":1818,

"fichas_actuales":594,

"juego_actual":"Baccarat",

"monto_apuesta":48,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"23:45",

"rondas_jugadas_hoy":6,

"gasto_hoy":1197,

"frecuencia_semanal":1,

"tiempo_promedio_visita":127,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":199,

"gasto_maximo_historico":835,

"perdidas_acumuladas":6192,

"ganancias_acumuladas":7990,

"variedad_juegos_probados":5,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Mar,Lun,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":208,

"dias_desde_primera_visita":1045,

"dias_desde_ultima_visita":34,

"clasificacion":"Cuidar",

},

{

"id":"j152",

"nombre":"JuanReyes",

"edad":61,

"ocupacion":"Disenador",

"presupuesto_hoy":1344,

"fichas_actuales":1321,

"juego_actual":"Cartas",

"monto_apuesta":52,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.7,

"hora_actual":"12:31",

"rondas_jugadas_hoy":38,

"gasto_hoy":0,

"frecuencia_semanal":4,

"tiempo_promedio_visita":239,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":393,

"perdidas_acumuladas":1360,

"ganancias_acumuladas":9201,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":300,

"dias_desde_primera_visita":958,

"dias_desde_ultima_visita":51,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j153",

"nombre":"ElenaTorres",

"edad":54,

"ocupacion":"Estudiante",

"presupuesto_hoy":1008,

"fichas_actuales":631,

"juego_actual":"Ruleta",

"monto_apuesta":145,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.9,

"hora_actual":"14:13",

"rondas_jugadas_hoy":16,

"gasto_hoy":351,

"frecuencia_semanal":7,

"tiempo_promedio_visita":125,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":810,

"perdidas_acumuladas":14340,

"ganancias_acumuladas":5995,

"variedad_juegos_probados":1,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":255,

"dias_desde_primera_visita":224,

"dias_desde_ultima_visita":24,

"clasificacion":"Cuidar",

},

{

"id":"j154",

"nombre":"HugoAlvarez",

"edad":70,

"ocupacion":"Estudiante",

"presupuesto_hoy":443,

"fichas_actuales":218,

"juego_actual":"Cartas",

"monto_apuesta":133,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.4,

"hora_actual":"16:07",

"rondas_jugadas_hoy":23,

"gasto_hoy":207,

"frecuencia_semanal":5,

"tiempo_promedio_visita":183,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":853,

"perdidas_acumuladas":7656,

"ganancias_acumuladas":16750,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Dom,Lun,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":132,

"dias_desde_primera_visita":206,

"dias_desde_ultima_visita":14,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j155",

"nombre":"DanielaGonzalez",

"edad":39,

"ocupacion":"Empresario",

"presupuesto_hoy":935,

"fichas_actuales":400,

"juego_actual":"Baccarat",

"monto_apuesta":49,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.3,

"hora_actual":"19:37",

"rondas_jugadas_hoy":16,

"gasto_hoy":505,

"frecuencia_semanal":0,

"tiempo_promedio_visita":292,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":894,

"perdidas_acumuladas":13324,

"ganancias_acumuladas":10838,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":86,

"dias_desde_primera_visita":476,

"dias_desde_ultima_visita":50,

"clasificacion":"Cuidar",

},

{

"id":"j156",

"nombre":"DanielOrtiz",

"edad":54,

"ocupacion":"Disenador",

"presupuesto_hoy":820,

"fichas_actuales":158,

"juego_actual":"Ruleta",

"monto_apuesta":154,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.8,

"hora_actual":"11:19",

"rondas_jugadas_hoy":14,

"gasto_hoy":639,

"frecuencia_semanal":0,

"tiempo_promedio_visita":105,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":45,

"gasto_maximo_historico":381,

"perdidas_acumuladas":3908,

"ganancias_acumuladas":2100,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Jue,Mie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":423,

"dias_desde_primera_visita":1040,

"dias_desde_ultima_visita":39,

"clasificacion":"Retener",

},

{

"id":"j157",

"nombre":"FernandoVazquez",

"edad":59,

"ocupacion":"Empresario",

"presupuesto_hoy":527,

"fichas_actuales":226,

"juego_actual":"Ruleta",

"monto_apuesta":70,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.1,

"hora_actual":"23:34",

"rondas_jugadas_hoy":12,

"gasto_hoy":290,

"frecuencia_semanal":1,

"tiempo_promedio_visita":270,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":24,

"gasto_maximo_historico":452,

"perdidas_acumuladas":5147,

"ganancias_acumuladas":712,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Dom,Vie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":238,

"dias_desde_primera_visita":625,

"dias_desde_ultima_visita":60,

"clasificacion":"Retener",

},

{

"id":"j158",

"nombre":"VictoriaMartinez",

"edad":50,

"ocupacion":"Mecanico",

"presupuesto_hoy":355,

"fichas_actuales":131,

"juego_actual":"Keno",

"monto_apuesta":173,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.5,

"hora_actual":"22:49",

"rondas_jugadas_hoy":32,

"gasto_hoy":211,

"frecuencia_semanal":1,

"tiempo_promedio_visita":322,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":6,

"gasto_maximo_historico":566,

"perdidas_acumuladas":1061,

"ganancias_acumuladas":18233,

"variedad_juegos_probados":5,

"juego_favorito":"Keno",

"dias_visita":"Lun,Dom,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":422,

"dias_desde_primera_visita":1354,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j159",

"nombre":"JoseMendoza",

"edad":55,

"ocupacion":"Desempleado",

"presupuesto_hoy":1785,

"fichas_actuales":650,

"juego_actual":"Cartas",

"monto_apuesta":65,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"22:58",

"rondas_jugadas_hoy":25,

"gasto_hoy":1115,

"frecuencia_semanal":2,

"tiempo_promedio_visita":358,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":44,

"gasto_maximo_historico":980,

"perdidas_acumuladas":442,

"ganancias_acumuladas":6148,

"variedad_juegos_probados":2,

"juego_favorito":"Cartas",

"dias_visita":"Mar,Lun,Sab,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":35,

"dias_desde_primera_visita":936,

"dias_desde_ultima_visita":44,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j160",

"nombre":"SilviaVazquez",

"edad":55,

"ocupacion":"Pintor",

"presupuesto_hoy":167,

"fichas_actuales":109,

"juego_actual":"Keno",

"monto_apuesta":86,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"14:12",

"rondas_jugadas_hoy":13,

"gasto_hoy":47,

"frecuencia_semanal":5,

"tiempo_promedio_visita":118,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":575,

"perdidas_acumuladas":10483,

"ganancias_acumuladas":2960,

"variedad_juegos_probados":4,

"juego_favorito":"Keno",

"dias_visita":"Dom,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":106,

"dias_desde_primera_visita":445,

"dias_desde_ultima_visita":51,

"clasificacion":"Cuidar",

},

{

"id":"j161",

"nombre":"NataliaReyes",

"edad":57,

"ocupacion":"Cocinero",

"presupuesto_hoy":1579,

"fichas_actuales":546,

"juego_actual":"Ruleta",

"monto_apuesta":101,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"21:59",

"rondas_jugadas_hoy":32,

"gasto_hoy":1011,

"frecuencia_semanal":1,

"tiempo_promedio_visita":282,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":31,

"gasto_maximo_historico":65,

"perdidas_acumuladas":4873,

"ganancias_acumuladas":5891,

"variedad_juegos_probados":5,

"juego_favorito":"Ruleta",

"dias_visita":"Vie,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":270,

"dias_desde_primera_visita":316,

"dias_desde_ultima_visita":20,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j162",

"nombre":"NataliaTorres",

"edad":53,

"ocupacion":"Estudiante",

"presupuesto_hoy":1734,

"fichas_actuales":15,

"juego_actual":"Tragamonedas",

"monto_apuesta":38,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.0,

"hora_actual":"23:08",

"rondas_jugadas_hoy":31,

"gasto_hoy":1690,

"frecuencia_semanal":3,

"tiempo_promedio_visita":52,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":54,

"gasto_maximo_historico":146,

"perdidas_acumuladas":14320,

"ganancias_acumuladas":9341,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":485,

"dias_desde_primera_visita":535,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j163",

"nombre":"IsabelMendoza",

"edad":30,

"ocupacion":"Programador",

"presupuesto_hoy":1559,

"fichas_actuales":887,

"juego_actual":"Cartas",

"monto_apuesta":176,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.4,

"hora_actual":"16:56",

"rondas_jugadas_hoy":18,

"gasto_hoy":665,

"frecuencia_semanal":3,

"tiempo_promedio_visita":271,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":36,

"gasto_maximo_historico":504,

"perdidas_acumuladas":4101,

"ganancias_acumuladas":3197,

"variedad_juegos_probados":6,

"juego_favorito":"Cartas",

"dias_visita":"Lun,Dom,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":461,

"dias_desde_primera_visita":1473,

"dias_desde_ultima_visita":54,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j164",

"nombre":"ManuelRodriguez",

"edad":47,

"ocupacion":"Ingeniero",

"presupuesto_hoy":1712,

"fichas_actuales":619,

"juego_actual":"Tragamonedas",

"monto_apuesta":183,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.5,

"hora_actual":"19:19",

"rondas_jugadas_hoy":23,

"gasto_hoy":1085,

"frecuencia_semanal":1,

"tiempo_promedio_visita":97,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":47,

"gasto_maximo_historico":82,

"perdidas_acumuladas":11157,

"ganancias_acumuladas":2085,

"variedad_juegos_probados":1,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":405,

"dias_desde_primera_visita":623,

"dias_desde_ultima_visita":52,

"clasificacion":"Cuidar",

},

{

"id":"j165",

"nombre":"PedroVazquez",

"edad":31,

"ocupacion":"Empresario",

"presupuesto_hoy":880,

"fichas_actuales":351,

"juego_actual":"Blackjack",

"monto_apuesta":44,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":0.6,

"hora_actual":"17:13",

"rondas_jugadas_hoy":34,

"gasto_hoy":515,

"frecuencia_semanal":4,

"tiempo_promedio_visita":296,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":665,

"perdidas_acumuladas":1034,

"ganancias_acumuladas":1982,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Mie,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":83,

"dias_desde_primera_visita":756,

"dias_desde_ultima_visita":55,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j166",

"nombre":"XimenaVazquez",

"edad":49,

"ocupacion":"Empresario",

"presupuesto_hoy":1965,

"fichas_actuales":1375,

"juego_actual":"Tragamonedas",

"monto_apuesta":183,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"20:32",

"rondas_jugadas_hoy":5,

"gasto_hoy":587,

"frecuencia_semanal":4,

"tiempo_promedio_visita":48,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":117,

"gasto_maximo_historico":473,

"perdidas_acumuladas":10279,

"ganancias_acumuladas":16895,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Mie,Lun",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":25,

"dias_desde_primera_visita":1233,

"dias_desde_ultima_visita":7,

"clasificacion":"Cuidar",

},

{

"id":"j167",

"nombre":"RosaRodriguez",

"edad":23,

"ocupacion":"Disenador",

"presupuesto_hoy":1599,

"fichas_actuales":1570,

"juego_actual":"Cartas",

"monto_apuesta":80,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.6,

"hora_actual":"16:43",

"rondas_jugadas_hoy":39,

"gasto_hoy":17,

"frecuencia_semanal":3,

"tiempo_promedio_visita":307,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":92,

"perdidas_acumuladas":11729,

"ganancias_acumuladas":14713,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Lun,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":50,

"dias_desde_primera_visita":143,

"dias_desde_ultima_visita":50,

"clasificacion":"Cuidar",

},

{

"id":"j168",

"nombre":"NataliaOrtiz",

"edad":46,

"ocupacion":"Mecanico",

"presupuesto_hoy":650,

"fichas_actuales":275,

"juego_actual":"Keno",

"monto_apuesta":68,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.9,

"hora_actual":"15:40",

"rondas_jugadas_hoy":39,

"gasto_hoy":346,

"frecuencia_semanal":0,

"tiempo_promedio_visita":168,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":8,

"gasto_maximo_historico":684,

"perdidas_acumuladas":7443,

"ganancias_acumuladas":10378,

"variedad_juegos_probados":5,

"juego_favorito":"Keno",

"dias_visita":"Mar,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":465,

"dias_desde_primera_visita":854,

"dias_desde_ultima_visita":51,

"clasificacion":"Retener",

},

{

"id":"j169",

"nombre":"CarlosGarcia",

"edad":50,

"ocupacion":"Enfermero",

"presupuesto_hoy":1863,

"fichas_actuales":358,

"juego_actual":"Tragamonedas",

"monto_apuesta":28,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.6,

"hora_actual":"16:43",

"rondas_jugadas_hoy":6,

"gasto_hoy":1475,

"frecuencia_semanal":0,

"tiempo_promedio_visita":107,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":245,

"gasto_maximo_historico":910,

"perdidas_acumuladas":2527,

"ganancias_acumuladas":18707,

"variedad_juegos_probados":2,

"juego_favorito":"Tragamonedas",

"dias_visita":"Mar,Dom,Vie,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":36,

"dias_desde_primera_visita":1305,

"dias_desde_ultima_visita":27,

"clasificacion":"Retener",

},

{

"id":"j170",

"nombre":"OscarTorres",

"edad":39,

"ocupacion":"Programador",

"presupuesto_hoy":75,

"fichas_actuales":28,

"juego_actual":"Baccarat",

"monto_apuesta":200,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.7,

"hora_actual":"20:29",

"rondas_jugadas_hoy":11,

"gasto_hoy":43,

"frecuencia_semanal":1,

"tiempo_promedio_visita":338,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":575,

"perdidas_acumuladas":12751,

"ganancias_acumuladas":12517,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Jue,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":3,

"dias_desde_primera_visita":1071,

"dias_desde_ultima_visita":20,

"clasificacion":"Cuidar",

},

{

"id":"j171",

"nombre":"RosaRomero",

"edad":41,

"ocupacion":"Vendedor",

"presupuesto_hoy":897,

"fichas_actuales":165,

"juego_actual":"Baccarat",

"monto_apuesta":70,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"10:50",

"rondas_jugadas_hoy":3,

"gasto_hoy":728,

"frecuencia_semanal":7,

"tiempo_promedio_visita":169,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":242,

"gasto_maximo_historico":323,

"perdidas_acumuladas":2297,

"ganancias_acumuladas":7108,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Sab,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":264,

"dias_desde_primera_visita":358,

"dias_desde_ultima_visita":3,

"clasificacion":"VIP",

},

{

"id":"j172",

"nombre":"GabrielaOrtiz",

"edad":24,

"ocupacion":"Disenador",

"presupuesto_hoy":1364,

"fichas_actuales":710,

"juego_actual":"Baccarat",

"monto_apuesta":65,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"21:56",

"rondas_jugadas_hoy":40,

"gasto_hoy":638,

"frecuencia_semanal":2,

"tiempo_promedio_visita":139,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":15,

"gasto_maximo_historico":552,

"perdidas_acumuladas":9039,

"ganancias_acumuladas":12456,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mar,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":136,

"dias_desde_primera_visita":913,

"dias_desde_ultima_visita":18,

"clasificacion":"Cuidar",

},

{

"id":"j173",

"nombre":"SergioOrtiz",

"edad":26,

"ocupacion":"Enfermero",

"presupuesto_hoy":517,

"fichas_actuales":144,

"juego_actual":"Keno",

"monto_apuesta":49,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.1,

"hora_actual":"20:12",

"rondas_jugadas_hoy":26,

"gasto_hoy":343,

"frecuencia_semanal":4,

"tiempo_promedio_visita":277,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":493,

"perdidas_acumuladas":7820,

"ganancias_acumuladas":11979,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Dom,Lun,Sab,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":155,

"dias_desde_primera_visita":743,

"dias_desde_ultima_visita":12,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j174",

"nombre":"FernandaRivera",

"edad":21,

"ocupacion":"Cocinero",

"presupuesto_hoy":1020,

"fichas_actuales":28,

"juego_actual":"Tragamonedas",

"monto_apuesta":62,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.6,

"hora_actual":"12:22",

"rondas_jugadas_hoy":26,

"gasto_hoy":973,

"frecuencia_semanal":2,

"tiempo_promedio_visita":78,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":37,

"gasto_maximo_historico":690,

"perdidas_acumuladas":14085,

"ganancias_acumuladas":7146,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Jue,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":145,

"dias_desde_primera_visita":812,

"dias_desde_ultima_visita":37,

"clasificacion":"Cuidar",

},

{

"id":"j175",

"nombre":"SilviaRomero",

"edad":70,

"ocupacion":"Programador",

"presupuesto_hoy":163,

"fichas_actuales":87,

"juego_actual":"Blackjack",

"monto_apuesta":136,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"17:58",

"rondas_jugadas_hoy":6,

"gasto_hoy":55,

"frecuencia_semanal":6,

"tiempo_promedio_visita":273,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":9,

"gasto_maximo_historico":940,

"perdidas_acumuladas":11909,

"ganancias_acumuladas":6574,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":27,

"dias_desde_primera_visita":1009,

"dias_desde_ultima_visita":37,

"clasificacion":"Cuidar",

},

{

"id":"j176",

"nombre":"MonicaVargas",

"edad":66,

"ocupacion":"Abogado",

"presupuesto_hoy":859,

"fichas_actuales":98,

"juego_actual":"Keno",

"monto_apuesta":128,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.5,

"hora_actual":"23:36",

"rondas_jugadas_hoy":35,

"gasto_hoy":750,

"frecuencia_semanal":4,

"tiempo_promedio_visita":133,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":21,

"gasto_maximo_historico":88,

"perdidas_acumuladas":12291,

"ganancias_acumuladas":11823,

"variedad_juegos_probados":6,

"juego_favorito":"Keno",

"dias_visita":"Vie,Mar,Dom,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":109,

"dias_desde_primera_visita":1059,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j177",

"nombre":"NadiaGonzalez",

"edad":21,

"ocupacion":"Programador",

"presupuesto_hoy":374,

"fichas_actuales":212,

"juego_actual":"Keno",

"monto_apuesta":54,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.2,

"hora_actual":"19:02",

"rondas_jugadas_hoy":19,

"gasto_hoy":133,

"frecuencia_semanal":3,

"tiempo_promedio_visita":62,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":7,

"gasto_maximo_historico":58,

"perdidas_acumuladas":13183,

"ganancias_acumuladas":887,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Sab,Mar,Vie,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":496,

"dias_desde_primera_visita":569,

"dias_desde_ultima_visita":2,

"clasificacion":"Cuidar",

},

{

"id":"j178",

"nombre":"CamilaDiaz",

"edad":56,

"ocupacion":"Mecanico",

"presupuesto_hoy":1296,

"fichas_actuales":615,

"juego_actual":"Ruleta",

"monto_apuesta":115,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.5,

"hora_actual":"19:35",

"rondas_jugadas_hoy":34,

"gasto_hoy":653,

"frecuencia_semanal":3,

"tiempo_promedio_visita":104,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":298,

"perdidas_acumuladas":5526,

"ganancias_acumuladas":16262,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":493,

"dias_desde_primera_visita":1233,

"dias_desde_ultima_visita":24,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j179",

"nombre":"JavierRodriguez",

"edad":20,

"ocupacion":"Enfermero",

"presupuesto_hoy":731,

"fichas_actuales":388,

"juego_actual":"Blackjack",

"monto_apuesta":45,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.9,

"hora_actual":"15:50",

"rondas_jugadas_hoy":11,

"gasto_hoy":330,

"frecuencia_semanal":6,

"tiempo_promedio_visita":197,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":30,

"gasto_maximo_historico":972,

"perdidas_acumuladas":11003,

"ganancias_acumuladas":13611,

"variedad_juegos_probados":3,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":139,

"dias_desde_primera_visita":376,

"dias_desde_ultima_visita":0,

"clasificacion":"Cuidar",

},

{

"id":"j180",

"nombre":"SilviaRivera",

"edad":69,

"ocupacion":"Chofer",

"presupuesto_hoy":80,

"fichas_actuales":57,

"juego_actual":"Dados",

"monto_apuesta":193,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":0.9,

"hora_actual":"17:43",

"rondas_jugadas_hoy":10,

"gasto_hoy":0,

"frecuencia_semanal":5,

"tiempo_promedio_visita":356,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":750,

"perdidas_acumuladas":4570,

"ganancias_acumuladas":16012,

"variedad_juegos_probados":2,

"juego_favorito":"Dados",

"dias_visita":"Jue,Mar,Vie,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":350,

"dias_desde_primera_visita":668,

"dias_desde_ultima_visita":29,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j181",

"nombre":"BeatrizOrtiz",

"edad":48,

"ocupacion":"Electricista",

"presupuesto_hoy":1930,

"fichas_actuales":1466,

"juego_actual":"Cartas",

"monto_apuesta":66,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"23:55",

"rondas_jugadas_hoy":9,

"gasto_hoy":443,

"frecuencia_semanal":0,

"tiempo_promedio_visita":75,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":49,

"gasto_maximo_historico":441,

"perdidas_acumuladas":8739,

"ganancias_acumuladas":10588,

"variedad_juegos_probados":4,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Sab,Dom,Mie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":11,

"dias_desde_primera_visita":736,

"dias_desde_ultima_visita":11,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j182",

"nombre":"FelipeGomez",

"edad":42,

"ocupacion":"Abogado",

"presupuesto_hoy":1026,

"fichas_actuales":738,

"juego_actual":"Blackjack",

"monto_apuesta":164,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.8,

"hora_actual":"12:12",

"rondas_jugadas_hoy":10,

"gasto_hoy":262,

"frecuencia_semanal":7,

"tiempo_promedio_visita":150,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":26,

"gasto_maximo_historico":417,

"perdidas_acumuladas":11553,

"ganancias_acumuladas":16207,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Lun,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":130,

"dias_desde_primera_visita":1064,

"dias_desde_ultima_visita":3,

"clasificacion":"Cuidar",

},

{

"id":"j183",

"nombre":"FernandoMendoza",

"edad":50,

"ocupacion":"Disenador",

"presupuesto_hoy":204,

"fichas_actuales":178,

"juego_actual":"Ruleta",

"monto_apuesta":146,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.8,

"hora_actual":"20:01",

"rondas_jugadas_hoy":16,

"gasto_hoy":4,

"frecuencia_semanal":6,

"tiempo_promedio_visita":297,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":862,

"perdidas_acumuladas":3234,

"ganancias_acumuladas":17071,

"variedad_juegos_probados":3,

"juego_favorito":"Ruleta",

"dias_visita":"Dom,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":400,

"dias_desde_primera_visita":569,

"dias_desde_ultima_visita":55,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j184",

"nombre":"PatriciaRomero",

"edad":68,

"ocupacion":"Mecanico",

"presupuesto_hoy":1844,

"fichas_actuales":924,

"juego_actual":"Blackjack",

"monto_apuesta":46,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.5,

"hora_actual":"20:25",

"rondas_jugadas_hoy":7,

"gasto_hoy":915,

"frecuencia_semanal":0,

"tiempo_promedio_visita":240,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":130,

"gasto_maximo_historico":463,

"perdidas_acumuladas":1994,

"ganancias_acumuladas":5026,

"variedad_juegos_probados":4,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Jue,Mar,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":78,

"dias_desde_primera_visita":1271,

"dias_desde_ultima_visita":31,

"clasificacion":"Retener",

},

{

"id":"j185",

"nombre":"ElenaSanchez",

"edad":38,

"ocupacion":"Electricista",

"presupuesto_hoy":929,

"fichas_actuales":225,

"juego_actual":"Tragamonedas",

"monto_apuesta":196,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":1.1,

"hora_actual":"21:05",

"rondas_jugadas_hoy":16,

"gasto_hoy":694,

"frecuencia_semanal":7,

"tiempo_promedio_visita":316,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":43,

"gasto_maximo_historico":908,

"perdidas_acumuladas":8477,

"ganancias_acumuladas":7053,

"variedad_juegos_probados":4,

"juego_favorito":"Tragamonedas",

"dias_visita":"Vie,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":203,

"dias_desde_primera_visita":1275,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j186",

"nombre":"AlejandraLopez",

"edad":25,

"ocupacion":"Jubilado",

"presupuesto_hoy":138,

"fichas_actuales":79,

"juego_actual":"Blackjack",

"monto_apuesta":104,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.0,

"hora_actual":"22:21",

"rondas_jugadas_hoy":3,

"gasto_hoy":54,

"frecuencia_semanal":2,

"tiempo_promedio_visita":303,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":18,

"gasto_maximo_historico":322,

"perdidas_acumuladas":4585,

"ganancias_acumuladas":825,

"variedad_juegos_probados":5,

"juego_favorito":"Blackjack",

"dias_visita":"Dom,Jue,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":138,

"dias_desde_primera_visita":859,

"dias_desde_ultima_visita":39,

"clasificacion":"Cuidar",

},

{

"id":"j187",

"nombre":"JuliaDiaz",

"edad":55,

"ocupacion":"Abogado",

"presupuesto_hoy":411,

"fichas_actuales":338,

"juego_actual":"Baccarat",

"monto_apuesta":192,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":4.1,

"hora_actual":"12:37",

"rondas_jugadas_hoy":15,

"gasto_hoy":51,

"frecuencia_semanal":0,

"tiempo_promedio_visita":111,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":640,

"perdidas_acumuladas":11090,

"ganancias_acumuladas":7092,

"variedad_juegos_probados":4,

"juego_favorito":"Baccarat",

"dias_visita":"Mar,Jue,Dom",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":449,

"dias_desde_primera_visita":253,

"dias_desde_ultima_visita":1,

"clasificacion":"Cuidar",

},

{

"id":"j188",

"nombre":"NataliaVazquez",

"edad":38,

"ocupacion":"Pintor",

"presupuesto_hoy":1626,

"fichas_actuales":736,

"juego_actual":"Tragamonedas",

"monto_apuesta":6,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.7,

"hora_actual":"16:37",

"rondas_jugadas_hoy":25,

"gasto_hoy":863,

"frecuencia_semanal":7,

"tiempo_promedio_visita":111,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":34,

"gasto_maximo_historico":975,

"perdidas_acumuladas":11750,

"ganancias_acumuladas":17356,

"variedad_juegos_probados":3,

"juego_favorito":"Tragamonedas",

"dias_visita":"Lun,Mar",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":155,

"dias_desde_primera_visita":1213,

"dias_desde_ultima_visita":47,

"clasificacion":"Cuidar",

},

{

"id":"j189",

"nombre":"PedroGomez",

"edad":46,

"ocupacion":"Empresario",

"presupuesto_hoy":226,

"fichas_actuales":81,

"juego_actual":"Keno",

"monto_apuesta":21,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":2.2,

"hora_actual":"12:50",

"rondas_jugadas_hoy":24,

"gasto_hoy":115,

"frecuencia_semanal":6,

"tiempo_promedio_visita":270,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":4,

"gasto_maximo_historico":749,

"perdidas_acumuladas":1482,

"ganancias_acumuladas":18636,

"variedad_juegos_probados":2,

"juego_favorito":"Keno",

"dias_visita":"Mar,Sab,Jue,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":282,

"dias_desde_primera_visita":743,

"dias_desde_ultima_visita":60,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j190",

"nombre":"JuanAguilar",

"edad":59,

"ocupacion":"Programador",

"presupuesto_hoy":1414,

"fichas_actuales":1212,

"juego_actual":"Blackjack",

"monto_apuesta":137,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.0,

"hora_actual":"16:43",

"rondas_jugadas_hoy":28,

"gasto_hoy":179,

"frecuencia_semanal":1,

"tiempo_promedio_visita":248,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":6,

"gasto_maximo_historico":952,

"perdidas_acumuladas":8307,

"ganancias_acumuladas":11955,

"variedad_juegos_probados":6,

"juego_favorito":"Blackjack",

"dias_visita":"Vie,Jue,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":447,

"dias_desde_primera_visita":720,

"dias_desde_ultima_visita":26,

"clasificacion":"Retener",

},

{

"id":"j191",

"nombre":"AlejandraOrtiz",

"edad":50,

"ocupacion":"Ingeniero",

"presupuesto_hoy":652,

"fichas_actuales":190,

"juego_actual":"Keno",

"monto_apuesta":130,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"22:50",

"rondas_jugadas_hoy":12,

"gasto_hoy":461,

"frecuencia_semanal":1,

"tiempo_promedio_visita":311,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":38,

"gasto_maximo_historico":399,

"perdidas_acumuladas":7878,

"ganancias_acumuladas":8846,

"variedad_juegos_probados":4,

"juego_favorito":"Keno",

"dias_visita":"Mie,Vie,Mar,Lun",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":250,

"dias_desde_primera_visita":1158,

"dias_desde_ultima_visita":49,

"clasificacion":"Retener",

},

{

"id":"j192",

"nombre":"JavierRivera",

"edad":30,

"ocupacion":"Abogado",

"presupuesto_hoy":1851,

"fichas_actuales":179,

"juego_actual":"Ruleta",

"monto_apuesta":145,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":3.8,

"hora_actual":"18:08",

"rondas_jugadas_hoy":23,

"gasto_hoy":1654,

"frecuencia_semanal":0,

"tiempo_promedio_visita":241,

"horario_habitual":"Madrugada",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":71,

"gasto_maximo_historico":726,

"perdidas_acumuladas":983,

"ganancias_acumuladas":14765,

"variedad_juegos_probados":2,

"juego_favorito":"Ruleta",

"dias_visita":"Mar,Mie",

"juega_solo":"Si",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"Si",

"total_visitas":45,

"dias_desde_primera_visita":811,

"dias_desde_ultima_visita":28,

"clasificacion":"Retener",

},

{

"id":"j193",

"nombre":"LucasDiaz",

"edad":60,

"ocupacion":"Desempleado",

"presupuesto_hoy":776,

"fichas_actuales":761,

"juego_actual":"Cartas",

"monto_apuesta":68,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.3,

"hora_actual":"16:27",

"rondas_jugadas_hoy":35,

"gasto_hoy":0,

"frecuencia_semanal":3,

"tiempo_promedio_visita":113,

"horario_habitual":"Nocturno",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":429,

"perdidas_acumuladas":10678,

"ganancias_acumuladas":11727,

"variedad_juegos_probados":3,

"juego_favorito":"Cartas",

"dias_visita":"Jue,Dom,Vie",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":350,

"dias_desde_primera_visita":1092,

"dias_desde_ultima_visita":14,

"clasificacion":"Cuidar",

},

{

"id":"j194",

"nombre":"RafaelRivera",

"edad":49,

"ocupacion":"Jubilado",

"presupuesto_hoy":514,

"fichas_actuales":432,

"juego_actual":"Baccarat",

"monto_apuesta":157,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.1,

"hora_actual":"13:37",

"rondas_jugadas_hoy":20,

"gasto_hoy":71,

"frecuencia_semanal":5,

"tiempo_promedio_visita":325,

"horario_habitual":"Manana",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":3,

"gasto_maximo_historico":528,

"perdidas_acumuladas":14110,

"ganancias_acumuladas":15264,

"variedad_juegos_probados":6,

"juego_favorito":"Baccarat",

"dias_visita":"Jue,Mie,Sab",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":448,

"dias_desde_primera_visita":246,

"dias_desde_ultima_visita":40,

"clasificacion":"Cuidar",

},

{

"id":"j195",

"nombre":"PaolaMartinez",

"edad":22,

"ocupacion":"Electricista",

"presupuesto_hoy":51,

"fichas_actuales":49,

"juego_actual":"Blackjack",

"monto_apuesta":123,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.6,

"hora_actual":"10:26",

"rondas_jugadas_hoy":1,

"gasto_hoy":0,

"frecuencia_semanal":1,

"tiempo_promedio_visita":139,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":245,

"perdidas_acumuladas":8225,

"ganancias_acumuladas":1455,

"variedad_juegos_probados":2,

"juego_favorito":"Blackjack",

"dias_visita":"Sab,Mie,Dom",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":91,

"dias_desde_primera_visita":1387,

"dias_desde_ultima_visita":46,

"clasificacion":"Cuidar",

},

{

"id":"j196",

"nombre":"SofiaGarcia",

"edad":33,

"ocupacion":"Abogado",

"presupuesto_hoy":306,

"fichas_actuales":73,

"juego_actual":"Ruleta",

"monto_apuesta":121,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":2.4,

"hora_actual":"13:10",

"rondas_jugadas_hoy":3,

"gasto_hoy":226,

"frecuencia_semanal":0,

"tiempo_promedio_visita":68,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":75,

"gasto_maximo_historico":50,

"perdidas_acumuladas":5437,

"ganancias_acumuladas":11638,

"variedad_juegos_probados":4,

"juego_favorito":"Ruleta",

"dias_visita":"Mie,Vie,Jue,Mar",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"No",

"total_visitas":70,

"dias_desde_primera_visita":501,

"dias_desde_ultima_visita":21,

"clasificacion":"Retener",

},

{

"id":"j197",

"nombre":"IsabelTorres",

"edad":63,

"ocupacion":"Desempleado",

"presupuesto_hoy":1529,

"fichas_actuales":692,

"juego_actual":"Keno",

"monto_apuesta":27,

"resultado_ultima_ronda":"Gano",

"tiempo_en_casino_hoy":5.0,

"hora_actual":"20:21",

"rondas_jugadas_hoy":18,

"gasto_hoy":807,

"frecuencia_semanal":1,

"tiempo_promedio_visita":106,

"horario_habitual":"Noche",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":44,

"gasto_maximo_historico":728,

"perdidas_acumuladas":1517,

"ganancias_acumuladas":4762,

"variedad_juegos_probados":3,

"juego_favorito":"Keno",

"dias_visita":"Lun,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":37,

"dias_desde_primera_visita":1496,

"dias_desde_ultima_visita":4,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j198",

"nombre":"DanielGonzalez",

"edad":30,

"ocupacion":"Medico",

"presupuesto_hoy":1399,

"fichas_actuales":963,

"juego_actual":"Baccarat",

"monto_apuesta":121,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":3.6,

"hora_actual":"23:21",

"rondas_jugadas_hoy":32,

"gasto_hoy":422,

"frecuencia_semanal":1,

"tiempo_promedio_visita":302,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"No",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":13,

"gasto_maximo_historico":298,

"perdidas_acumuladas":7190,

"ganancias_acumuladas":11834,

"variedad_juegos_probados":3,

"juego_favorito":"Baccarat",

"dias_visita":"Mie,Jue,Dom,Vie",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":122,

"dias_desde_primera_visita":34,

"dias_desde_ultima_visita":58,

"clasificacion":"Retener",

},

{

"id":"j199",

"nombre":"AngelRodriguez",

"edad":51,

"ocupacion":"Disenador",

"presupuesto_hoy":54,

"fichas_actuales":24,

"juego_actual":"Dados",

"monto_apuesta":144,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":1.4,

"hora_actual":"21:28",

"rondas_jugadas_hoy":13,

"gasto_hoy":0,

"frecuencia_semanal":2,

"tiempo_promedio_visita":38,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Estrategia",

"prefiere_rapido_o_lento":"Rapido",

"cambia_al_perder":"Si",

"cambia_al_ganar":"No",

"gasto_promedio_ronda":1,

"gasto_maximo_historico":309,

"perdidas_acumuladas":6610,

"ganancias_acumuladas":16971,

"variedad_juegos_probados":6,

"juego_favorito":"Dados",

"dias_visita":"Lun,Vie,Jue",

"juega_solo":"Si",

"reinvierte_ganancias":"No",

"acepta_recomendaciones":"Si",

"total_visitas":230,

"dias_desde_primera_visita":811,

"dias_desde_ultima_visita":34,

"clasificacion":"Servicio_Rapido",

},

{

"id":"j200",

"nombre":"EnriqueRamirez",

"edad":65,

"ocupacion":"Cocinero",

"presupuesto_hoy":1637,

"fichas_actuales":1290,

"juego_actual":"Baccarat",

"monto_apuesta":136,

"resultado_ultima_ronda":"Perdio",

"tiempo_en_casino_hoy":4.1,

"hora_actual":"14:50",

"rondas_jugadas_hoy":17,

"gasto_hoy":337,

"frecuencia_semanal":0,

"tiempo_promedio_visita":45,

"horario_habitual":"Tarde",

"prefiere_azar_o_estrategia":"Azar",

"prefiere_rapido_o_lento":"Lento",

"cambia_al_perder":"Si",

"cambia_al_ganar":"Si",

"gasto_promedio_ronda":19,

"gasto_maximo_historico":567,

"perdidas_acumuladas":5397,

"ganancias_acumuladas":16074,

"variedad_juegos_probados":2,

"juego_favorito":"Baccarat",

"dias_visita":"Dom,Mie,Sab,Jue",

"juega_solo":"No",

"reinvierte_ganancias":"Si",

"acepta_recomendaciones":"No",

"total_visitas":140,

"dias_desde_primera_visita":67,

"dias_desde_ultima_visita":55,

"clasificacion":"Retener",

},

]



def obtener_todos():
    if prolog_disponible():
        jugadores = []
        ids = [jugador["id"] for jugador in JUGADORES_MOCK]
        
        for jid in ids:
            datos = obtener_datos_jugador(jid)
            if datos:
                datos["clasificacion"] = clasificar_jugador(jid)
                jugadores.append(datos)
        
        if jugadores:
            return jugadores
    
    return JUGADORES_MOCK


def obtener_por_clasificacion(jugadores, clasif):
    return [j for j in jugadores if j["clasificacion"] == clasif]
#aqui vamos a precargar los datos asi que preparence malditos 

VIP=obtener_por_clasificacion(obtener_todos(), "VIP")
CUIDAR=obtener_por_clasificacion(obtener_todos(), "Cuidar")
RETENER=obtener_por_clasificacion(obtener_todos(), "Retener")
SERVICIO_RAPIDO=obtener_por_clasificacion(obtener_todos(), "Servicio_Rapido")