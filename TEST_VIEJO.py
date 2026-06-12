grados = (6,7,8,9,10,11)
equipos = []

class Equipo: 
    def __init__(self, grado, nombre, capitan):
        self.nombre = nombre
        self.grado = grado
        self.capitan = capitan
        self.puntos = 0
        self.integrantes = [capitan]
        self.goleadores = {}
        self.gf = 0
        self.gc = 0
        equipos.append(self)

    def registrarIntegrantes(self, *integrantes):
        for integrante in integrantes:
            self.integrantes.append(integrante)
      
def GUI():
    print("\nPROGRAMA DE INTERCLASES!")
    print("\nelegir una opción:")
    print("""    1. registrar equipo
    2. registrar integrantes de equipo
    3. registrar resultado de partido
    4. registrar goleadores
    5. tabla general
    6. campeon del torneo
    7. goleador del torneo
    8. malla menos vencida
    9. salir""")

    funciones = {
        1: registrarEquipo,
        2: registrarIntegrantes,
        3: registrarResultado,
        4: registrarGoleadores,
        5: tabla,
        6: campeon,
        7: goleadorTorneo,
        8: malla,
        9: exit
    }
  
    while True:
        try:
            option = int(input("opción: "))
            
            if option in funciones:
                funciones[option]()   # ejecuta la función
                
            elif option == 9:
                print("Saliendo...")
                break
            
            else:
                print("Ingresa un número válido.")

        except ValueError:
            print("Ingresa un número válido.")
        
def registrarEquipo():
    while True:
        try:
            grado = int(input("Ingrese el grado: "))
            grado_usado = False

            for equipo in equipos:
                if equipo.grado == grado:
                    grado_usado = True
                    break

            if grado_usado:
                print("Ya existe un equipo registrado para ese grado")
                continue

            if grado not in grados:
                print("Grado inválido (6-11)")
                continue
            else:
                break
        except ValueError:
            print("Inserte un número")
    
    while True:
        nombre = input("Nombre del equipo: ").strip().lower()

        if nombre == "" or not nombre.isalpha():
            print("El equipo debe tener nombre")
            continue

        repetido = False

        for e in equipos:
            if e.nombre == nombre:
                repetido = True
                break

        if repetido:
            print("Ya existe un equipo con ese nombre")
            continue

        break

    while True:
        capitan = input("Nombre del capitán: ").strip().lower()
        if capitan == "" or not capitan.isalpha():
            print("El capitán debe tener nombre")
            continue
        else:
            equipo = Equipo(grado, nombre, capitan)
            print("Equipo registrado.")
            print(f"""EQUIPO {equipo.nombre}
GRADO: {equipo.grado}
CAPITÁN: {equipo.capitan}
INTEGRANTES: {equipo.integrantes}""")
            break

def registrarIntegrantes():
    if not equipos:
        print("No hay equipos registrados. Por favor, registre un equipo primero.")
        return
        
    while True:
        nombreEquipo = input("Ingrese el nombre del equipo: ").strip().lower()
        if not (nombreEquipo and nombreEquipo.isalpha()):
            print("Ingrese un equipo válido y existente (solo letras)")
            continue

        equipo = None
        for e in equipos:
            if e.nombre == nombreEquipo:
                equipo = e
                break

        if equipo is None:
            print("Equipo no encontrado")
            continue

        break

    i = 0

    while True:
        try:
            i = int(input("\n¿Cuantos integrantes quieres registrar?: "))
            if i <= 0:
                print("Ingresa un número positivo")
            else:
                break
        except ValueError:
            print("ingresa un numero")

    for _ in range(i):
        while True:
            try:
                equipoAdd = input("Ingresa un integrante: ").strip().lower()
                if equipoAdd and equipoAdd.isalpha() and equipoAdd not in equipo.integrantes:
                    equipo.registrarIntegrantes(equipoAdd)
                    break
                else:
                    print("Ingrese un nombre válido (solo letras) o un integrante no registrado")
            except ValueError:
                print("ingresa el valor correspondiente")
        
    print("Integrantes registrados.")       

def registrarResultado():
    if len(equipos)<2:
        print("Registre 2 equipos primero.")
        return
   
    while True:
        nombre1 = input("\nIngrese el nombre del primer equipo: ").strip().lower()
        if nombre1 and nombre1.isalpha():
            equipoUno = None

            for e in equipos:
                if e.nombre == nombre1:
                    equipoUno = e
                    break

            if equipoUno is None:
                print("Equipo no encontrado")
                continue
            
            break
        else:
            print("Ingrese un equipo válido y existente (solo letras)")

    
    while True:
        nombre2 = input("\nIngrese el nombre del segundo equipo: ").strip().lower()
        if nombre2 and nombre2.isalpha() and nombre2 != nombre1:
            equipoDos = None

            for e in equipos:
                if e.nombre == nombre2:
                    equipoDos = e
                    break

            if equipoDos is None:
                print("Equipo no encontrado")
                continue
            break
        else:
            print("Ingrese un equipo válido, existente y diferente al primero (solo letras)")

    while True:
        try:
            golesEU = int(input(f"\nGoles de {equipoUno.nombre}: "))
            if golesEU < 0:
                print("Ingresa un número positivo")
            else:
                break
        except ValueError:
            print("Ingresa un número válido")

    while True:
        try:
            golesED = int(input(f"\nGoles de {equipoDos.nombre}: "))
            if golesED < 0:
                print("Ingresa un número positivo")
            else:
                break
        except ValueError:
            print("Ingresa un número válido")

    equipoUno.gf += golesEU
    equipoUno.gc += golesED

    equipoDos.gf += golesED
    equipoDos.gc += golesEU

    if golesEU > golesED:
        equipoUno.puntos += 3

    elif golesED > golesEU:
        equipoDos.puntos += 3

    else:
        equipoUno.puntos += 1
        equipoDos.puntos += 1

def registrarGoleadores():
    hayResultados = False

    for equipo in equipos:
        if equipo.gf > 0 or equipo.gc > 0 or equipo.puntos > 0:
            hayResultados = True
            break
    if not equipos or len(equipos) <2 or not hayResultados:
        print("No hay equipos o suficientes partidos para registrar goleadores. Por favor, registre un equipo primero.")
        return
    
    
    
    while True:
        nombreEquipo = input("Equipo: ").strip().lower()

        equipoEncontrado = None

        for equipo in equipos:
            if equipo.nombre.lower() == nombreEquipo.lower():
                equipoEncontrado = equipo

        if equipoEncontrado is None:
            print("Equipo no encontrado")
            continue
        else:
            break

    while True:
        jugador = input("Nombre del jugador: ").strip().lower()
        if jugador and jugador.isalpha() and jugador in equipoEncontrado.integrantes:
            break
        else:
            print("Ingrese un nombre válido (solo letras) o un jugador válido")

    while True:
        golesRegistrados = sum(equipoEncontrado.goleadores.values())

        disponibles = (equipoEncontrado.gf - golesRegistrados)

        print(f"Quedan {disponibles} goles por asignar")
        try:
            goles = int(input("Cantidad de goles: "))



            if goles <= 0:
                print("Ingresa un número positivo")
            elif goles > disponibles:
                print("No puedes registrar más goles de los que tiene el equipo")
                continue
            else:
                if jugador in equipoEncontrado.goleadores:
                    equipoEncontrado.goleadores[jugador] += goles
                    
                else:
                    equipoEncontrado.goleadores[jugador] = goles

            sobrantes = disponibles - goles
            print(f"Después de registrar esos goles quedarán {sobrantes}.")
            print("Goleador registrado.")
            break
        except ValueError:
            print("Ingresa un número válido")
        
def tabla():

    if not equipos:
        print("No hay equipos registrados")
        return

    for equipo in equipos:

        diferencia = equipo.gf - equipo.gc

        print("\n----------------")
        print("Equipo:", equipo.nombre)
        print("Grado:", equipo.grado)
        print("Puntos:", equipo.puntos)
        print("Integrantes:", equipo.integrantes)
        print("Capitán:", equipo.capitan)
        print("Goleadores:", equipo.goleadores)
        print("Goles a favor:", equipo.gf)
        print("Goles en contra:", equipo.gc)
        print("Diferencia de goles:", diferencia)

def campeon():
    hayResultados = False

    for equipo in equipos:
        if equipo.gf > 0 or equipo.gc > 0 or equipo.puntos > 0:
            hayResultados = True
            break



    if not equipos or len(equipos) < 2 or not hayResultados:
        print("No hay equipos o suficientes resultados para determinar un campeón.")
        return

    mejor = equipos[0]

    for equipo in equipos:

        dg_equipo = equipo.gf - equipo.gc
        dg_mejor = mejor.gf - mejor.gc

        if equipo.puntos > mejor.puntos:
            mejor = equipo

        elif (
            equipo.puntos == mejor.puntos
            and dg_equipo > dg_mejor
        ):
            mejor = equipo
        
    print("\n----------------")
    print(f"Campeón del torneo: {mejor.nombre}")
    print("\n----------------")

def goleadorTorneo():
    hayGoles = False

    for equipo in equipos:
        if len(equipo.goleadores) > 0:
            hayGoles = True
            break

    if not hayGoles:
        print("No se han registrado goleadores")
        return
    
    if not equipos or len(equipos) < 2 :
        print("No hay equipos ni suficientes equipos para determinar un goleador. Por favor registre más equipos.")
        return

    nombre = ""
    maxGoles = 0

    for equipo in equipos:

        for jugador, goles in equipo.goleadores.items():

            if goles > maxGoles:
                maxGoles = goles
                nombre = jugador

    if maxGoles == 0:
        print("No se han registrado goles")
    else:
        print(f"\n----------------"
            f"Goleador del torneo: "
            f"{nombre} ({maxGoles} goles)"
            f"\n----------------"
        )

def malla():
    hayResultados = False

    for equipo in equipos:
        if equipo.gf > 0 or equipo.gc > 0 or equipo.puntos > 0:
            hayResultados = True
            break

    if not equipos or hayResultados == False:
        print("No hay equipos o resultados, registre un equipo primero")
        return

    mejor = equipos[0]

    for equipo in equipos:

        if equipo.gc < mejor.gc:
            mejor = equipo

    print(
        f"\n----------------"
        f"Malla menos vencida: "
        f"{mejor.nombre} ({mejor.gc} goles)"
        f"\n----------------"
    )

GUI()
