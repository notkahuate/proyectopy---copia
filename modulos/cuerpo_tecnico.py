
from core import ReadFile,NewFile

def crear_tecnico(nombre,equipo_tc):

    try:
        data = ReadFile()
        equipos = data.get('equipos',{})
        if equipo_tc in equipos:

            tecnico = {
                'nombre': nombre
            }
            equipos[equipo_tc]['cuerpo_tecnico'][nombre] = tecnico
            NewFile(data)
            print(f"Cuerpo técnico {nombre} registrado en el equipo {equipo_tc}.")
        else:
            print(f"El equipo {equipo_tc} no existe.")
    except Exception as e:
        print(f"Error al registrar cuerpo técnico: {e}")


def mostrar_tc(equipo_tc):
    try:
        if equipo_tc in equipos:
            tecnicos = equipos[equipo_tc]['cuerpo_tecnico']
            if tecnicos:
                print(f"Cuerpo técnico del equipo {equipo_tc}:")
                for nombre, tecnico in tecnicos.items():
                    print(f"- Nombre: {nombre}")
            else:
                print(f"No hay cuerpo técnico registrado en el equipo {equipo_tc}.")
        else:
            print(f"El equipo {equipo_tc} no existe.")
    except Exception as e:
        print(f"Error al mostrar cuerpo técnico: {e}")


