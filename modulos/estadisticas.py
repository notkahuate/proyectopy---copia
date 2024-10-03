from regis_equipo import equipos

def equipo_mas_puntos():
    puntos = 0
    equipo_max = None

    
    for equipo in equipos:
        if equipos[equipo]['puntos'] >= puntos:
            puntos = equipos[equipo]['puntos']
            equipo_max = equipo
    print(f"El equipo con más puntos es: {equipo_max} con {puntos} puntos.")

def equipo_mas_goles():
    max_goles = 0
    equipo_max_goles = None
    for equipo in equipos:
        goles_a_favor = equipos[equipo]['gf']  
        if goles_a_favor > max_goles:
            max_goles = goles_a_favor
            equipo_max_goles = equipo
    print(f"El equipo que más goles marcó es: {equipo_max_goles} con {max_goles} goles a favor.")

def equipo_contra():
    min_goles = 0
    equipo_min_goles = None
    for equipo in equipos:
        goles_contra = equipos[equipo]['gc']  
        if goles_contra >= min_goles:
            min_goles = goles_contra
            equipo_min_goles = equipo
    print(f"El equipo que mas goles le marcaron: {equipo_min_goles} con {min_goles} goles en contra.")