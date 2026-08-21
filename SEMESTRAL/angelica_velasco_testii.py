print("Bienvenido al programa de asistencia estudiantil")
print("¿Cuántos estudiantes desea registrar?")

estudiantes = []
presentes = []
ausentes = []

while True:
    try: 
        i = int(input("> "))
        if i > 0:
            break
        else:
            print("Ingrese un número positivo")
            continue
    except ValueError:
        print("Ingrese un número, no letras ni espacios")
        continue

for _ in range(i):
    while True:
        nombre = input("Nombre del estudiante: ")
        if nombre and nombre.isalpha():
            estudiantes.append(nombre)
            break
        else:
            print("Ingrese un nombre válido")        

    while True:
        try: 
            grado = int(input("grado: "))
            if grado < 6 or grado > 11:
                print("Ingrese un grado válido (6-11)")
                continue
            else:
                break
        except ValueError:
            print("Ingrese un número")
            continue

    while True: 
        asist = input("¿Asistió? (s/n): ")
        if asist.lower() not in ["s", "n"]:
            print("Ingrese una opción válida")
            continue
        elif asist.lower() == "s":
            presentes.append(nombre)
            break
        else:
            ausentes.append(nombre)
            break

porcentAsist = (len(presentes) / len(estudiantes))*100

print("")
print(f"ESTUDIANTES REGISTRADOS: {len(estudiantes)}")
print(f"Asistieron: {len(presentes)}")
print(f"Faltaron: {len(ausentes)}")
print(f"Porcentaje de asistencia: {porcentAsist}%")
print(f"Lista de estudiantes ausentes:")

i = 0
for ausente in ausentes:
    print(f"{i+1}. {ausente}")    
