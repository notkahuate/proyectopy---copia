from regis_equipo import crear_equipo, mostrar_equipos
from jugadores_regis import crear_jugador, mostrar_jugadores
from cuerpo_tecnico import crear_tecnico,mostrar_tc
from encuentros import programar_encuentro,resultados_Encuentros

def menu_user():
    while True:
        print(" Liga BetPlay ")
        print("1. Registrar equipo")
        print("2. Registrar jugador")
        print("3. Registrar cuerpo técnico")
        print("4. Programar encuentro")
        print("5. Registrar resultado de partido")
        print("6. mostrar estadisticas torneo")
        print("7. Salir")
        opcion = input("Seleccionela opcion a donde desea ir : ")

        if opcion == '1':
            print("1. Registrar equipo")
            print("2. ver equipos")

            opcion_equipo = int(input('ingrese la opcion deseada:  '))

            if opcion_equipo == 1 :
                nombre = input("ingrese el nombre del equipo:  ")
                crear_equipo(nombre)
                
            elif opcion_equipo ==2:
                mostrar_equipos()
            else:
                print("ingrese una opcion valida ")


        elif opcion == '2':

            print("1. Registrar jugador")
            print("2. mostrar jugadores")

            opcion_jugador = int(input(" "))

            if opcion_jugador == 1 :
              equipo_jgd = input("ingrese el equipo del jugador : ")
              nombre_jgd = input("ingrese el nombre del jugador : ")
              dorsal = input("ingrese la dorsal del jugador : ")
              pósicion = input("ingrese la posicion del jugador : ")
              crear_jugador(nombre_jgd,dorsal,pósicion ,equipo_jgd)
            elif opcion_jugador == 2 :
                equipo_jgd = input("ingrese el equipo de los jugador : ")
                mostrar_jugadores(equipo_jgd)
            else :
                print("ingrese una opcion valida")

        elif opcion == '3':
             
            print("1. Registrar tecnicos")
            print("2. mostrar tecnicos")

            opcion_tc = int(input(" "))

            if opcion_tc == 1 :
              nombre_Tc = input("ingrese nombre : ")
              equipo_Tc = input("ingrese el equipo : ")
              crear_tecnico(nombre_Tc,equipo_Tc)
            elif opcion_tc == 2 :
                equipo_Tc = input("ingrese el equipo del cuerpo tecnico que desea : ")
                mostrar_tc(equipo_Tc)
            else :
                print("ingrese una opcion valida")


        elif opcion == '4':
            print("4. Programar encuentro")
            equipo1 = input("ingrese el primer equipo a disputas: ")
            equipo2= input("ingrese el segundo equipo a disputas : ")
            dia = input("ingrese el dia del encuentro : ")
            mes = input("ingrese el mes del encuentro : ")
            ano = input("ingrese el año del encuentro : ")

            programar_encuentro(equipo1,equipo2,dia,mes,ano)




        elif opcion == '5':
            print("5. Registrar resultado de partido")
            equipo1 = input("ingrese el primer equipo a disputas: ")
            equipo2= input("ingrese el segundo equipo a disputas : ")
            goles1 = int(input(f"Goles de {equipo1}: "))
            goles2 = int(input(f"Goles de {equipo2}: "))
            resultados_Encuentros(equipo1,equipo2,goles1,goles2)
            





        elif opcion == '6':
            print("Estadisticas")
            equipo_contra()
            equipo_mas_puntos()
            equipo_mas_goles()

            
        
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")