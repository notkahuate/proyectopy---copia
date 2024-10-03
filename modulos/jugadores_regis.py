from core import ReadFile,NewFile


def crear_jugador(nombre,dorsal,posicion,equipo_jgd):
   

    try:
        data = ReadFile()
        equipos = data.get('equipos', {})
        if equipo_jgd in equipos:
            jugador = {
                'nombre': nombre,
                'dorsal': dorsal,
                'posicion': posicion,
                'tarjetas rojas' : 0,
                'tarjetas AMARILLAS' : 0,
                'Goles' : 0

            }
            equipos[equipo_jgd]['jugadores'][nombre] = jugador
            NewFile(data)
            print(f"Jugador {nombre} registrado en el equipo {equipo_jgd}.")
        else:
            print(f"El equipo {equipo_jgd} no existe.")
    except Exception as e:
        print(f"Error al registrar jugador: {e}")


def mostrar_jugadores(equipo_jgd):
    try:
        data=ReadFile()
        equipos=data.get('equipos',{})
        if equipo_jgd in equipos:
            jugadores = equipos[equipo_jgd]['jugadores']
            if jugadores:
                print(f"Jugadores del equipo {equipo_jgd}:")
                for nombre, jugador in jugadores.items():
                    print(f"- Nombre: {nombre}, Dorsal: {jugador['dorsal']}, Posición: {jugador['posicion']}")
            else:
                print(f"No hay jugadores registrados en el equipo {equipo_jgd}.")
        else:
            print(f"El equipo {equipo_jgd} no existe.")
    except Exception as e:
        print(f"Error al mostrar jugadores: {e}")



 