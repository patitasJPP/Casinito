import random, json

nombres_m = ['Carlos','Jorge','Pedro','Luis','Miguel','Andres','Diego','David','Jose',
             'Juan','Pablo','Sergio','Ricardo','Javier','Fernando','Gustavo','Raul',
             'Alberto','Angel','Manuel','Eduardo','Rafael','Mario','Hector','Ivan',
             'Julio','Vicente','Enrique','Oscar','Hugo','Lucas','Mateo','Adrian',
             'Daniel','Alejandro','Gabriel','Martin','Santiago','Tomas','Felipe']

nombres_f = ['Maria','Lucia','Ana','Rosa','Sofia','Elena','Laura','Carla','Paula',
             'Valentina','Gabriela','Diana','Andrea','Fernanda','Claudia','Patricia',
             'Monica','Sara','Teresa','Carmen','Isabel','Silvia','Natalia','Beatriz',
             'Victoria','Lorena','Alicia','Julia','Liliana','Mariana','Ximena',
             'Camila','Daniela','Valeria','Renata','Alejandra','Paola','Veronica',
             'Adriana','Nadia']

apellidos = ['Garcia','Rodriguez','Martinez','Lopez','Gonzalez','Perez','Sanchez',
             'Ramirez','Torres','Flores','Rivera','Gomez','Diaz','Vazquez','Romero',
             'Moreno','Alvarez','Ortiz','Castillo','Mendoza','Ruiz','Medina','Aguilar',
             'Cruz','Reyes','Vargas']

ocupaciones = ['Ingeniero','Abogado','Medico','Docente','Empresario','Estudiante',
               'Disenador','Contador','Arquitecto','Mecanico','Vendedor','Jubilado',
               'Desempleado','Chofer','Cocinero','Electricista','Pintor','Carpintero',
               'Enfermero','Programador']

juegos = ['Tragamonedas','Ruleta','Blackjack','Poker','Baccarat','Dados','Cartas','Keno']

horarios = ['Tarde','Noche','Nocturno','Madrugada','Manana']

dias_opts = ['Lun','Mar','Mie','Jue','Vie','Sab','Dom']

resultados = ['Gano','Perdio']
si_no = ['Si','No']

def random_dias():
    n = random.randint(2, 4)
    return ', '.join(random.sample(dias_opts, n))

jugadores = []
for i in range(101, 201):
    sexo = random.choice(['m', 'f'])
    nombre = random.choice(nombres_m) if sexo == 'm' else random.choice(nombres_f)
    nombre += ' ' + random.choice(apellidos)

    edad = random.randint(18, 70)
    presupuesto = random.randint(20, 2000)
    gasto_hoy = max(0, random.randint(0, presupuesto) - random.randint(0, 50))
    fichas = max(0, presupuesto - gasto_hoy - random.randint(0, 30))
    monto_apuesta = random.randint(1, 200)
    rondas = random.randint(1, 40)
    tiempo = round(random.uniform(0.5, 6.0), 1)
    frecuencia = random.randint(0, 7)
    tiempo_prom = random.randint(30, 360)
    perdidas = random.randint(0, 15000)
    ganancias = random.randint(0, 20000)
    total_visitas = random.randint(1, 500)
    dias_primera = random.randint(1, 1500)
    dias_ultima = random.randint(0, 60)
    gasto_max_hist = random.randint(50, 1000)
    variedad = random.randint(1, 6)
    juego_fav = random.choice(juegos)
    gasto_prom_ronda = max(1, gasto_hoy // max(rondas, 1))
    horario = random.choice(horarios)
    resultado = random.choice(resultados)
    dias_visita = random_dias()
    ocupacion = random.choice(ocupaciones)

    if edad >= 35 and gasto_hoy >= 200 and frecuencia >= 3 and perdidas < 3000:
        clasif = 'VIP'
    elif edad <= 25 or perdidas > 10000 or (presupuesto > 0 and gasto_hoy > presupuesto * 0.9):
        clasif = 'Cuidar'
    elif frecuencia <= 1 and dias_ultima > 20:
        clasif = 'Retener'
    else:
        clasif = 'Servicio_Rapido'

    j = {}
    j['id'] = f'j{i}'
    j['nombre'] = nombre
    j['edad'] = edad
    j['ocupacion'] = ocupacion
    j['presupuesto_hoy'] = presupuesto
    j['fichas_actuales'] = fichas
    j['juego_actual'] = juego_fav
    j['monto_apuesta'] = monto_apuesta
    j['resultado_ultima_ronda'] = resultado
    j['tiempo_en_casino_hoy'] = tiempo
    j['hora_actual'] = f'{random.randint(10,23)}:{random.randint(0,59):02d}'
    j['rondas_jugadas_hoy'] = rondas
    j['gasto_hoy'] = gasto_hoy
    j['frecuencia_semanal'] = frecuencia
    j['tiempo_promedio_visita'] = tiempo_prom
    j['horario_habitual'] = horario
    j['prefiere_azar_o_estrategia'] = random.choice(['Azar', 'Estrategia'])
    j['prefiere_rapido_o_lento'] = random.choice(['Rapido', 'Lento'])
    j['cambia_al_perder'] = random.choice(si_no)
    j['cambia_al_ganar'] = random.choice(si_no)
    j['gasto_promedio_ronda'] = gasto_prom_ronda
    j['gasto_maximo_historico'] = gasto_max_hist
    j['perdidas_acumuladas'] = perdidas
    j['ganancias_acumuladas'] = ganancias
    j['variedad_juegos_probados'] = variedad
    j['juego_favorito'] = juego_fav
    j['dias_visita'] = dias_visita
    j['juega_solo'] = random.choice(si_no)
    j['reinvierte_ganancias'] = random.choice(si_no)
    j['acepta_recomendaciones'] = random.choice(si_no)
    j['total_visitas'] = total_visitas
    j['dias_desde_primera_visita'] = dias_primera
    j['dias_desde_ultima_visita'] = dias_ultima
    j['clasificacion'] = clasif
    jugadores.append(j)

# Output as python list literal
print("JUGADORES_100 = [")
for j in jugadores:
    print("    {")
    for k, v in j.items():
        if isinstance(v, str):
            print(f'        "{k}": "{v}",')
        else:
            print(f'        "{k}": {v},')
    print("    },")
print("]")
