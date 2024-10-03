

from core import NewFile,ReadFile

def programar_encuentro(equipo1, equipo2, dia, mes, año):
    data=ReadFile()

    if equipo1 in data.get('equipos',{}) and equipo2 in data.get('equipos',{}):

        encuentro = {
            'equipo1': equipo1,
            'equipo2': equipo2,
            'fecha': f"{dia}/{mes}/{año}",
            'resultado': None
        }

        encuentron= f"{equipo1} vs {equipo2}"
        data.setdefault('encuentros',{})[encuentron]=encuentro
        NewFile(data)
        print(f"Encuentro entre {equipo1} y {equipo2} programado para {dia}/{mes}/{año}.")

    
    else:
        print("Uno o ambos equipos no existen, verifique los nombres.")


def resultados_Encuentros(equipo1, equipo2, goles1, goles2):

    try:
        data=ReadFile()
        encuentro_equipos = f"{equipo1} vs {equipo2}"
        equipos=data.get('equipos',{})
        encuentros=data.get('encuentros',{})
        
        if encuentro_equipos in data.get('encuentros',{}):
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
            
            NewFile(data)

            print(f"Resultado registrado: {equipo1} {goles1} - {goles2} {equipo2}")
        else:
            print("El encuentro no está programado.")
    
    except Exception as e:
        print(f"Error al registrar el resultado o estadísticas: {e}")


def mostrar_tabla():
    print("\nTabla de posiciones:")
    print("Equipo | PJ | PG | PP | PE | GF | GC | Pts")
    for equipo in equipos:
     print(f"{equipo}: PJ: {equipos[equipo]['pj']}, PG: {equipos[equipo]['pg']}, PP: {equipos[equipo]['pp']}, PE: {equipos[equipo]['pe']}, GF: {equipos[equipo]['gf']}, GC: {equipos[equipo]['gc']}, Puntos: {equipos[equipo]['puntos']}")

   