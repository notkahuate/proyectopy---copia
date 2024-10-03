

from core import ReadFile, NewFile

def crear_equipo(nombre):
    """Crea un equipo y lo añade a la base de datos (JSON)."""
    
    # Leer los datos actuales del archivo JSON
    data = ReadFile()
    
    # Verificar si el equipo ya existe
    if nombre in data.get('equipos', {}):
        print(f"El equipo {nombre} ya está registrado.")
        return None
    
    # Definir las estadísticas y estructura del equipo
    equipo = {
        'nombre': nombre,
        'cuerpo_tecnico': {},
        'jugadores': {},
        'pj': 0,  
        'pg': 0,  
        'pp': 0, 
        'pe': 0,  
        'gf': 0,  
        'gc': 0,  
        'puntos': 0
    }
    
    # Agregar el equipo a los datos existentes
    data.setdefault('equipos', {})[nombre] = equipo
    
    # Guardar los datos actualizados en el archivo JSON
    NewFile(data)
    
    # Confirmar la creación del equipo
    print(f"Equipo {nombre} registrado exitosamente.")
    return equipo



def mostrar_equipos():
    if equipos:
        print("Equipos registrados:")
        for nombre, equipo in equipos.items():
            print(f"- {nombre}")
    else:
        print("No hay equipos registrados.")




