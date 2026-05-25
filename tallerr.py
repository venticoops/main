print("Taller teórico")
print("Preguntas del 1 al 10")
print("""
1. ¿Por qué una lista puede ser más útil que crear muchas variables como nota1, nota2,  nota3?
    - Porque las listas almacenan varias variables con una misma categoría.
      
2. Explique qué significa que las listas en Python empiezan en la posición 0
    - Porque en la memoria de la computadora representa una distancia, la posición significa desplazamiento (offset), y toda distancia debe iniciar desde 0.
      
3. ¿Qué función cumple append() dentro de una lista?
    - Añade un solo elemento a una lista.
      
4. ¿Para qué sirve len() cuando se trabaja con listas? 
    - Sirve para decirnos cuántos elementos tiene una lista.
      
5. Explique la diferencia entre mostrar una lista completa y mostrar un elemento por posición. 
    - Mostrar una lista completa significa mostrar cada uno de sus elementos, mientras que mostrar un elemento por posición solo nos muestra un solo elemento de una lista.
      
6. ¿Qué error puede ocurrir si se intenta consultar una posición que no existe en la lista? 
    - IndexError: list index out of range, significa que el elemento al que queremos acceder todavía no existe en esa posición.
      
7. ¿Por qué es útil recorrer una lista con for? 
    - Porque revisa todos los elementos de la lista sin importar el tamaño.

8. Explique cómo se puede calcular un promedio usando una lista, un acumulador y len(). 
    - Usando una lista vacía, agregando notas con while y un contador, validando con if y except, y calculando el promedio usando el acumulador y for para sumar.

9. ¿Qué ventaja tiene validar un dato antes de guardarlo en una lista? 
    - Evita que se guarden datos erróneos, como letras en vez de números, o números fuera de un rango establecido.      

10. Mencione tres situaciones escolares reales donde conviene usar listas.
    - Tomar asistencia
    - Consultar información de estudiantes
    - Registrar las notas del periodo de un estudiante
""")


# Taller practico




def listado():
    i = 0
    listado = []
    print(" ")

    while i < 5:
        while True:
            try:
            
                name= input("Ingresa un nombre: ")
                if not name.isalpha(): #verifica que el nombre solo tenga letras
                    print("Ingrese un nombre válido\n")
                else: 
                    listado.append(name)
                    break
            except TypeError:
                print("intenta de nuevo\n")

        i += 1

    print("\nLista de estudiantes: ", *listado)
    print("\nEnumerados:")

    i = 1

    for nombre in listado:
        
        print(f"{listado.index(nombre)+1}. {nombre}")
        i += 1
    
def promedio():
    print(" ")
    i = 0
    suma = 0
    notas = []
    while i<5:
        while True:
            try:
                nota_est = float(input("Dame una nota: "))
                if nota_est < 1 or nota_est > 5:
                    print("Ingresa un número mayor a 1 y menor a 5\n")
                    continue
                notas.append(nota_est)
                break
            except ValueError:
                print("ingresa un numero, no  una letra\n")
        i += 1

    for nota in notas:
        suma = suma + nota

    promedio = suma / len(notas)

    print(f"\n Promedio: {round(promedio, 2)}")

    if promedio < 3:
        print("Desempeño bajo")
    elif promedio < 3.9:
        print("Desempeño básico")
    elif promedio < 4.5:
        print("Desempeño alto")
    elif promedio <= 5:
        print("Desempeño superior")

def temp():
    print(" ")
    i = 0
    suma = 0
    temperaturas = []
    while i<7:
        while True:
            try:
                temp = float(input("Dame la temperatura: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("ingresa un numero, no  una letra\n")
        i += 1

    desglosado = ', '.join(map(str, temperaturas)) # map vuelve los valores en temperaturas cadenas para poder concatenar con ", "
    print("\nTemperaturas: ", desglosado)

    temperaturas.sort(reverse=True)
    print("\nTemperatura mayor: ", temperaturas[0])
    temperaturas.sort(reverse=False)
    print("\nTemperaturas menor: ", temperaturas[0])
    
    for temp in temperaturas:
        suma = suma + temp
                    

    promedio = suma / len(temperaturas)

    print("\nEl promedio de temperaturas es: ",round(promedio, 2))

            
def tareas():
    i = 0
    tareas = []
        
    while True:
        try:
            i = int(input("\n¿Cuantas tareas quieres registrar?: "))
            if i <= 0:
                print("Ingresa un número positivo.")
            else:
                break
        except ValueError:
            print("ingresa un numero")

    for _ in range(i):
        while True:
            
            tarea = input("Ingresa la tarea: ")
            if tarea is not None and tarea.strip() != "" and tarea.isalpha(): #evita q la tarea este vacía
                tareas.append(tarea)
                break
            else:
                print("La tarea no puede estar vacía o contener números. Intenta nuevamente.\n")


    print("\nLista de tareas:")
    for tarea in tareas:
        print(f"{tareas.index(tarea) + 1}. {tarea}")

    while True:
        marcar = input("\n¿Deseas marcar una tarea como terminada? (si/no): ")
        if marcar.lower() == 'si':
            while True:
                try:
                    num_tarea = int(input("\nIngresa el número de la tarea que deseas marcar como terminada: "))
                    if 1 <= num_tarea <= len(tareas) :
                        tareas.pop(num_tarea - 1)
                        print("\nTarea marcada como terminada.")
                        print("\nLista actualizada: ")
                        if len(tareas) == 0:
                            print("No hay tareas pendientes.")
                            break
                        else:
                            for tarea in tareas:
                                print(f"{tareas.index(tarea) + 1}. {tarea}")
                            break
                    else:
                        print("Número de tarea inválido. Intenta nuevamente.")
                except ValueError:
                    print("Ingresa un número válido.")
            if len(tareas) == 0:
                break
            

        elif marcar.lower() == 'no':
            print("\nNo se marcará ninguna tarea como terminada.")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

def productos():
    i = 0
    productos = []
        
    print(" ")

    while i < 4:
        while True:
            
            producto = input("Ingresa el producto: ")
            if producto is not None and producto.strip() != "" and producto.isalpha(): #evita q el producto este vacía
                productos.append(producto)
                break
            else:
                print("El producto no puede estar vacío o contener números. Intenta nuevamente.\n")
        i += 1


    print("\nLista de productos:")
    for producto in productos:
        print(f"{productos.index(producto) + 1}. {producto}")

    while True:
        marcar = input("\n¿Deseas consultar un producto? (si/no): ")
        if marcar.lower() == 'si':
            while True:
                try:
                    num_producto = int(input("\nIngresa el número del producto que deseas consultar: "))
                    if 1 <= num_producto <= len(productos):
                        chosen = productos[num_producto - 1]
                        print("\nConsultaste el producto:", chosen)
                        break
                    else:
                        print("Número de producto inválido. Intenta nuevamente.")
                except ValueError:
                    print("Ingresa un número válido.")

        elif marcar.lower() == 'no':
            print("\nNo se marcará ningun producto como consultado.")
            break

        elif marcar.lower() != 'si' and marcar.lower() != 'no':
            print("Opción no válida. No se marcará ningun producto como consultado.")

def precios():
    print(" ")
    i=0
    precios = []
    while i < 5:
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio <= 0:
                    print("Ingresa un número positivo.\n")
                else:
                    precios.append(precio)
                    break
            except ValueError:
                print("ingresa un numero.\n")
        i += 1
    
    suma = 0

    for precio in precios:
        suma = suma + precio

    discount = "como es una suma de mas de 50000, tienes descuento" if suma > 50000 else "como es una suma de menos de 50000, no tienes descuento"

    print(f"\nEl total es {suma}, {discount}")
    
def edadlista():
    print(" ")

    edades = []
    menores = []
    
    i=0
    while i < 6:
        while True:
            try:
                edad = int(input("Ingrese una edad: "))
                if edad < 1:
                    print("Ingrese una edad válida\n")
                else:
                    edades.append(edad)
                    break
            except ValueError:
                print("Ingrese un valor válido\n")
        i += 1

    desglosado = ', '.join(map(str, edades)) 

    print(f"\nlista de edades: {desglosado}")

    for edad in edades:
        if edad < 18:
            menores.append(edad)

    mayores = len([edad for edad in edades if edad >= 18])

    print(f"\nmayores de edad: {mayores}")
    print(f"menores de edad: {len(menores)}")

def encuesta():
    print(" ")
    respuestas = []

    for i in range(6):
        while True:
            respuesta = input("¿Prefieres Python, Java, Excel o Scratch?: ").lower()

            if respuesta in ["python", "java", "scratch", "excel"]:
                respuestas.append(respuesta)
                break
            else:
                print("Ingrese una opción válida\n")

    print("\nResultados:")
    print("\nPython:", respuestas.count("python"))
    print("Java:", respuestas.count("java"))
    print("Excel:", respuestas.count("excel"))
    print("Scratch:", respuestas.count("scratch"))
    
def buscar():
    estudiantes = ["Laura", "Isabella", "Ariana", "Valerie", "Ángela", "Samuel", "Juan Manuel", "Emanuel", "Danny", "Christian", "Sergio"]
    estudiantes_lower = [nombre.lower() for nombre in estudiantes]
    print("\nPuede consultar los nombres de algunos de los estudiantes de grado Once")

    while True:
        try:
            revisar = input("\nIngrese un nombre para buscar: ").strip().lower()
            if revisar != "" or revisar.isalpha():
                break
            else:
                print("Ingrese un nombre válido")
        except (TypeError, ValueError):
            print("Ingrese un nombre válido")

    if revisar in estudiantes_lower:
        print("\nEstudiante registrado")
    else:
        print("\nEstudiante no registrado")

def clasificar():
    numeros = []
    print(" ")


    i = 0
    while i < 8:
        while True:
            try:
                numero = int(input("Ingrese un número entero del -900 al 900: "))
                if -900 <= numero <= 900:
                    numeros.append(numero)
                    break
                else:
                    print("Ingrese un número dentro del rango permitido.\n")
            except (ValueError, TypeError):
                print("Ingrese un número válido.\n")
        i += 1

    pares = sum(1 for numero in numeros if numero != 0 and numero % 2 == 0) #saca los pares si el residuo de su division es 0
    impares = sum(1 for numero in numeros if numero % 2 != 0) # lo contrario
    ceros = numeros.count(0)

    print(f"\nNúmeros pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Ceros: {ceros}")

def analisis():
    print(" ")

    palabras = []
    i=0
    while i<5:
        while True:
            try:
                palabra = input("Ingrese una palabra: ").lower()
                if palabra is not None and palabra.strip() != "" and palabra.isalpha():
                    palabras.append(palabra)
                    break
                else:
                    print("Ingrese una palabra válida.\n")
            except TypeError or ValueError:
                print("Ingrese letras.\n")
        i+=1
    
    print(" ")

    for palabra in palabras:
        print(f"{palabra}: caracteres: {len(palabra)}")

def control():
    while True:
        try:
            nombre = input("\nIngrese el nombre del estudiante: ").lower()
            if nombre is not None and nombre.strip() != "" or nombre.isalpha():
                break
            else:
                print("Ingrese un nombre válido")
        except TypeError or ValueError:
            print("Ingrese letras")

    i = 0
    suma = 0
    notas = []
    print(" ")

    while i<5:
        while True:
            try:
                nota_est = float(input("Dame una nota: "))
                if nota_est < 1 or nota_est > 5:
                    print("Ingresa un número mayor a 1 y menor a 5\n")
                    continue
                notas.append(nota_est)
                break
            except ValueError:
                print("ingresa un numero, no  una letra\n")
        i += 1

    for nota in notas:
        suma = suma + nota

    promedio = round(suma / len(notas),2)


    if promedio < 3:
        desempeño = "BAJO"
    elif promedio < 3.9:
        desempeño = "BÁSICO"
    elif promedio < 4.5:
        desempeño = "ALTO"
    elif promedio <= 5:
        desempeño = "SUPERIOR"

    

    desglosado= ", ".join(map(str, notas))

    print(f"\nDESEMPEÑO ACADÉMICO\nNOMBRE: {nombre}\nNOTAS: {desglosado}\nPROMEDIO: {promedio}\nDESEMPEÑO: {desempeño}")

def final():
    estudiantes = []

    class Estudiante: #Clase estudiante para registrar múltiples estudiantes
        def __init__(self, nombre):
            self.nombre = nombre
            self.est_notas = []

        def promedioDesempeño(self, est_notas): #Funcion que define promedio
            suma = 0
            for nota in est_notas:
                suma = suma + nota

            promedio = round(suma / len(est_notas),2)

            if promedio < 3:
                desempeño = "BAJO"
            elif promedio < 3.9:
                desempeño = "BÁSICO"
            elif promedio < 4.5:
                desempeño = "ALTO"
            elif promedio <= 5:
                desempeño = "SUPERIOR"

            desglosado= ", ".join(map(str,est_notas))


            return desempeño, promedio, desglosado
    
    print("\nBIENVENIDO!! Deseas registrar estudiantes? (s/n): ")
    respuesta = input("> " ).strip().lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta no válida, por favor ingresa 's' o 'n'")
        respuesta = input("> ").strip().lower()

    if respuesta == "n":
        print("\nGracias por usar el sistema!!")
    else:
        while True:
            while True:
                nombre = input("\nIngrese el nombre del estudiante: ").strip()
                if nombre and nombre.isalpha():
                    estudiante = Estudiante(nombre)
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

def GUI():
    print("\ningrese ejercicio del 1 al 13")
    

    funciones = {
        1: listado,
        2: promedio,
        3: temp,
        4: tareas,
        5: productos,
        6: precios,
        7: edadlista,
        8: encuesta,
        9: buscar,
        10: clasificar,
        11: analisis,
        12: control,
        13: final
    } #diccionario key-value para llamar funciones

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

    i = 0
    while i<12:
        GUI() #repite el GUI 12 veces mas para probar todos los ejercicios

GUI()
