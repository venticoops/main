grados = (6,7,8,9,10,11)
equipos = []

class Partido:
    def __init__(self, equipoUno, equipoDos, golesEU, golesED):
        self.equipoUno = equipoUno
        self.equipoDos = equipoDos
        self.golesEU = golesEU
        self.golesED = golesED

    def resultado(self):
        if self.golesED > self.golesEU:
            resultadoED = 3
        elif self.golesED == self.golesEU:
            resultado = 1
        else:
            resultado = 0
        return resultado


class Equipo: 
    def __init__(self, grado, nombre, capitan, puntos=0, integrantes = []):
        self.nombre = nombre
        self.grado = grado
        self.capitan = capitan
        self.integrantes = list()
        self.puntos = puntos
        self.integrantes = integrantes
        equipos.append(nombre)

    def registrarIntegrantes(self, *integrantes): #Funcion que define promedio
        self.integrantes = integrantes
      

def GUI():
        print("\nPROGRAMA DE INTERCLASES!")
        print("\nelegir una opción:")
        print("""1. registrar equipo
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
            9: salir,
        
        } 

        while True:
            try:
                option = int(input("> "))
                
                if option in funciones:
                    funciones[option]()   # ejecuta la función
                    break
                else:
                    print("Ingresa un número válido.")

            except ValueError:
                print("Ingresa un número válido.")



def registrarIntegrantes():
    while True:
        while True:
            equipo = input("\nIngrese el nombre del equipo: ").strip()
            if equipo and equipo.isalpha() and equipo in equipos:
                equipo = registrarIntegrantes(equipo)
                break
            else:
                print("Ingrese un nombre válido (solo letras)")

        i = 0
        print(" ")

        while i<5:
            while True:
                try:
                    nota_est = float(input("Dame una nota: "))
                    if nota_est < 1 or nota_est > 5:
                        print("Ingresa un número mayor a 1 y menor a 5\n")
                        continue
                    estudiante.est_notas.append(nota_est)
                    break
                except ValueError:
                    print("ingresa un numero, no  una letra\n")
            i += 1

        estudiantes.append(estudiante)
        print("\nQuieres registrar otro estudiante? (s/n): ")
        respuesta = input("> " ).strip().lower()
        while respuesta not in ["s", "n"]:
            print("Respuesta no válida, por favor ingresa 's' o 'n'")
            respuesta = input("> ").strip().lower()

        if respuesta == "n":
            print("\nGracias por usar el sistema!!")
            estudiantes.sort(key=lambda e: e.promedioDesempeño(e.est_notas)[1], reverse=True) #funcion lambda para ordenar por promedio de desempeño, reverse true para ordenar de mayor a menor, se usa e porque es cada estudiante en la lista estudiantes, e.promedioDesempeño(e.est_notas)[1] porque el promedio es el segundo valor que devuelve la funcion promedioDesempeño
            print("\nESTUDIANTES ORDENADOS POR DESEMPEÑO ACADÉMICO:\n")
            for est in estudiantes:
                desempeño, promedio, desglosado = est.promedioDesempeño(est.est_notas)
                print(f"NOMBRE: {est.nombre}\nNOTAS: {desglosado}\nPROMEDIO: {promedio}\nDESEMPEÑO: {desempeño}")
            break
        else:
            continue

    