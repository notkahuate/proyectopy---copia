from regis_equipo import equipos


encuentros = {}

def programar_encuentro(equipo1, equipo2, dia, mes, año):
    if equipo1 in equipos and equipo2 in equipos:

        encuentro = {
            'equipo1': equipo1,
            'equipo2': equipo2,
            'fecha': f"{dia}/{mes}/{año}",
            'resultado': None
        }

        encuentros[f"{equipo1} vs {equipo2}"] = encuentro
        print(f"Encuentro entre {equipo1} y {equipo2} programado para {dia}/{mes}/{año}.")

    
    else:
        print("Uno o ambos equipos no existen, verifique los nombres.")


def resultados_Encuentros(equipo1, equipo2, goles1, goles2):
    try:
        encuentro_equipos = f"{equipo1} vs {equipo2}"
        
        if encuentro_equipos in encuentros:
            # Actualizar el resultado del encuentro
            encuentros[encuentro_equipos]['resultado'] = f"{goles1} - {goles2}"

            # Actualizar estadísticas de los equipos
            equipos[equipo1]['pj'] += 1
            equipos[equipo2]['pj'] += 1
            equipos[equipo1]['gf'] += goles1
            equipos[equipo1]['gc'] += goles2
            equipos[equipo2]['gf'] += goles2
            equipos[equipo2]['gc'] += goles1

            # Determinar el equipo ganador
            if goles1 > goles2:
                equipos[equipo1]['pg'] += 1
                equipos[equipo1]['puntos'] += 3
                equipos[equipo2]['pp'] += 1
            elif goles2 > goles1:
                equipos[equipo2]['pg'] += 1
                equipos[equipo2]['puntos'] += 3
                equipos[equipo1]['pp'] += 1
            else:
                equipos[equipo1]['pe'] += 1
                equipos[equipo2]['pe'] += 1
                equipos[equipo1]['puntos'] += 1
                equipos[equipo2]['puntos'] += 1

            print(f"Resultado registrado: {equipo1} {goles1} - {goles2} {equipo2}")

          
            print(f"\nIngresa los nombres de los jugadores que marcaron  goles para {equipo1}:")
            for i in range(goles1):
                jugador = input(f"Nombre del jugador {i+1} que marcó en {equipo1}: ")
                if jugador in equipos[equipo1]['jugadores']:
                    equipos[equipo1]['jugadores'][jugador]['Goles'] += 1
                    print(f"Actualizado: {jugador} ahora tiene {equipos[equipo1]['jugadores'][jugador]['Goles']} gol(es).")
                else:
                    print(f"El jugador {jugador} no está registrado en {equipo1}.")
            
           
            print(f"\nIngresa el nombre del jugador que marcó  para {equipo2}:")
            for i in range(goles2):
                jugador = input(f"Nombre del jugador {i+1} que marcó en {equipo2}: ")
                if jugador in equipos[equipo2]['jugadores']:
                    equipos[equipo2]['jugadores'][jugador]['Goles'] += 1
                    print(f"Actualizado: {jugador} ahora tiene {equipos[equipo2]['jugadores'][jugador]['Goles']} gol(es).")
                else:
                    print(f"El jugador {jugador} no está registrado en {equipo2}.")

            
            print("\nAhora, ingresa las tarjetas del partido:")
            total_tarjetas = int(input("¿Cuántas tarjetas hubo en total? "))
            if total_tarjetas > 0:
                amarillas = int(input("¿Cuántas fueron amarillas? "))
                rojas = int(input("¿Cuántas fueron rojas? "))

                for i in range(amarillas):
                    jugador = input(f"Nombre del jugador que recibió tarjeta amarilla ({i+1} de {amarillas}): ")
                    equipo = input(f"¿De qué equipo es {jugador}? ({equipo1}/{equipo2}): ")
                    if jugador in equipos[equipo]['jugadores']:
                        equipos[equipo]['jugadores'][jugador]['tarjetas_amarillas'] += 1
                        print(f"{jugador} ahora tiene {equipos[equipo]['jugadores'][jugador]['tarjetas_amarillas']} tarjeta(s) amarilla(s).")
                    else:
                        print(f"El jugador {jugador} no está registrado en {equipo}.")
                
                for i in range(rojas):
                    jugador = input(f"Nombre del jugador que recibió tarjeta roja ({i+1} de {rojas}): ")
                    equipo = input(f"¿De qué equipo es {jugador}? ({equipo1}/{equipo2}): ")
                    if jugador in equipos[equipo]['jugadores']:
                        equipos[equipo]['jugadores'][jugador]['tarjetas_rojas'] += 1
                        print(f"{jugador} ahora tiene {equipos[equipo]['jugadores'][jugador]['tarjetas_rojas']} tarjeta(s) roja(s).")
                    else:
                        print(f"El jugador {jugador} no está registrado en {equipo}.")
        else:
            print("El encuentro no está programado.")
    
    except Exception as e:
        print(f"Error al registrar el resultado o estadísticas: {e}")


def mostrar_tabla():
    print("\nTabla de posiciones:")
    print("Equipo | PJ | PG | PP | PE | GF | GC | Pts")
    for equipo in equipos:
     print(f"{equipo}: PJ: {equipos[equipo]['pj']}, PG: {equipos[equipo]['pg']}, PP: {equipos[equipo]['pp']}, PE: {equipos[equipo]['pe']}, GF: {equipos[equipo]['gf']}, GC: {equipos[equipo]['gc']}, Puntos: {equipos[equipo]['puntos']}")

   