print("Taller teórico")
print("Ejercicios del 1 al 13")
print("""
1. ¿Por qué una lista puede ser más útil que crear muchas variables como nota1, nota2,  nota3?
    - Porque las listas almacenan varias variables con una misma categoría
      
2. Explique qué significa que las listas en Python empiezan en la posición 0
    - Porque en la memoria de la computadora representa una distancia, la posición significa desplazamiento (offset), y toda distancia debe iniciar desde 0
      
3. ¿Qué función cumple append() dentro de una lista?
    - Añade un solo elemento a una lista
      
4. ¿Para qué sirve len() cuando se trabaja con listas? 
    - Sirve para decirnos cuántos elementos tiene una lista.
      
5. Explique la diferencia entre mostrar una lista completa y mostrar un elemento por posición. 
    - Mostrar una lista completa significa mostrar cada uno de sus elementos, mientras que mostrar un elemento por posición solo nos muestra un solo elemento de una lista.
      
6. ¿Qué error puede ocurrir si se intenta consultar una posición que no existe en la lista? 
    - IndexError: list index out of range, significa que el elemento al que queremos acceder todavía no existe en esa posición
      
7. ¿Por qué es útil recorrer una lista con for? 
    - Porque revisa todos los elementos de la lista sin importar el tamaño.

8. Explique cómo se puede calcular un promedio usando una lista, un acumulador y len(). 
    - Usando una lista vacía, agregando notas con while y un contador, validando con if y except, y calculando el promedio usando el acumulador y for para sumar

9. ¿Qué ventaja tiene validar un dato antes de guardarlo en una lista? 
      

10. Mencione tres situaciones escolares reales donde conviene usar listas.
    - Tomar asistencia
    - Consultar información de estudiantes
    - Registrar las notas del periodo de un estudiante

""")


# Taller practico

def listado():
    i = 0
    listado = []

    while i < 5:
        while True:
            try:
            
                name= input("Ingresa un nombre:")
                listado.append(name)
                if not name.isalpha():
                    print("Ingrese un nombre válido")
                else: 
                    break
            except TypeError:
                print("intenta de nuevo")

        i += 1

    print("Lista de estudiantes: ", *listado)
    print("Enumerados:")

    i = 1

    for nombre in listado:
        
        print(f"{listado.index(nombre)+1}. {nombre}")
        i += 1
    
def temp():
    while True:
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
                    print("ingresa un numero, no  una letra")
            i += 1

        desglosado = ', '.join(map(str, temperaturas))
        print("Temperaturas: ", desglosado)

        temperaturas.sort(reverse=True)
        print("Temperatura mayor: ", temperaturas[0])
        temperaturas.sort(reverse=False)
        print("Temperaturas menor: ", temperaturas[0])
        
        for temp in temperaturas:
            suma = suma + temp
                        

        promedio = suma / len(temperaturas)

        print("El promedio de temperaturas es: ",round(promedio, 2))

def promedio():

    while True:
        i = 0
        suma = 0
        notas = []
        while i<5:
            while True:
                try:
                    nota_est = float(input("Dame una nota: "))
                    if nota_est < 1 or nota_est > 5:
                        print("Ingresa un número mayor a 1 y menor a 5")
                        continue
                    notas.append(nota_est)
                    break
                except ValueError:
                    print("ingresa un numero, no  una letra")
            i += 1

        for nota in notas:
            suma = suma + nota

        promedio = suma / len(notas)

        print(round(promedio, 2))

        if promedio < 3:
            print("Desempeño bajo")
        elif promedio < 3.9:
            print("Desempeño básico")
        elif promedio < 4.5:
            print("Desempeño alto")
        elif promedio <= 5:
            print("Desempeño superior")
            
def tareas():
    i = 0
    tareas = []
        
    while True:
        try:
            i = int(input("¿Cuantas tareas quieres registrar?: "))
            if i <= 0:
                print("Ingresa un número positivo.")
            else:
                break
        except ValueError:
            print("ingresa un numero")

    for _ in range(i):
        while True:
            
            tarea = input("Ingresa la tarea: ")
            if tarea is not None and tarea.strip() != "":
                tareas.append(tarea)
                break
            else:
                print("La tarea no puede estar vacía. Intenta nuevamente.")


    print("Lista de tareas:")
    for tarea in tareas:
        print(f"{tareas.index(tarea) + 1}. {tarea}")

    marcar = input("¿Deseas marcar una tarea como terminada? (si/no): ")
    if marcar.lower() == 'si':
        while True:
            try:
                num_tarea = int(input("Ingresa el número de la tarea que deseas marcar como terminada: "))
                if 1 <= num_tarea <= len(tareas) :
                    tareas.pop(num_tarea - 1)
                    print("Tarea marcada como terminada.")
                    print("Lista actualizada: ")
                    if len(tareas) == 0:
                        print("No hay tareas pendientes.")
                    else:
                        for tarea in tareas:
                            print(f"{tareas.index(tarea) + 1}. {tarea}")
                        break
                else:
                    print("Número de tarea inválido. Intenta nuevamente.")
            except ValueError:
                print("Ingresa un número válido.")

    elif marcar.lower() == 'no':
        print("No se marcará ninguna tarea como terminada.")

    elif marcar.lower() != 'si' and marcar.lower() != 'no':
        print("Opción no válida. No se marcará ninguna tarea como terminada.")

def productos():
    i = 0
    productos = []
        

    while i < 4:
        while True:
            
            producto = input("Ingresa el producto: ")
            if producto is not None:
                productos.append(producto)
                break
            else:
                print("El producto no puede estar vacío. Intenta nuevamente.")
        i += 1


    print("Lista de productos:")
    for producto in productos:
        print(f"{productos.index(producto) + 1}. {producto}")

    marcar = input("¿Deseas consultar un producto? (si/no): ")
    if marcar.lower() == 'si':
        while True:
            try:
                num_producto = int(input("Ingresa el número del producto que deseas consultar: "))
                if 1 <= num_producto <= len(productos) :
                    chosen = productos.index(num_producto - 1)
                    print("Consultaste el producto: ", chosen)
                    break
                else:
                    print("Número de producto inválido. Intenta nuevamente.")
            except ValueError:
                print("Ingresa un número válido.")

    elif marcar.lower() == 'no':
        print("No se marcará ningun producto como consultado.")

    elif marcar.lower() != 'si' and marcar.lower() != 'no':
        print("Opción no válida. No se marcará ningun producto como consultado.")

def precios():
    i=0
    precios = []
    while i < 5:
        while True:
            try:
                precio = float(input("Ingresa el precio del producto: "))
                if precio <= 0:
                    print("Ingresa un número positivo.")
                else:
                    precios.append(precio)
                    break
            except ValueError:
                print("ingresa un numero, no  una letra")
        i += 1
    
    suma = 0

    for precio in precios:
        suma = suma + precio

    discount = "como es una suma de mas de 50000, tienes descuento" if suma > 50000 else "como es una suma de menos de 50000, no tienes descuento"

    print(f"El total es {suma}, {discount}")
    
def edadlista():
    
    edades = []
    menores = []
    
    i=0
    while i > 6:
        while True:
            try:
                edad = int(input("Ingrese una edad: "))
                if edad < 1:
                    print("Ingrese una edad válida")
                else:
                    edades.append(edad)
                    break
            except ValueError:
                print("Ingrese un valor válido")
            i += 1

    print(f"lista de edades: {edades}")

    for edad in edades:
        if edad < 18:
            menores.append(edad)
            edades.pop(edad)

    print(f"mayores de edad: {len(edades)}")
    print(f"menores de edad: {len(menores)}")

def encuesta():
    respuestas = []

    for i in range(6):
        while True:
            respuesta = input("¿Prefieres Python, Java, Excel o Scratch?: ").lower()

            if respuesta in ["python", "java", "scratch", "excel"]:
                respuestas.append(respuesta)
                break
            else:
                print("Ingrese una opción válida")

    print("\nResultados:")
    print("Python:", respuestas.count("python"))
    print("Java:", respuestas.count("java"))
    print("Excel:", respuestas.count("excel"))
    print("Scratch:", respuestas.count("scratch"))
    
def buscar():
    estudiantes = ["Laura", "Isabella", "Ariana", "Valerie", "Ángela", "Samuel", "Juan Manuel", "Emmanuel", "Danny", "Christian", "Sergio"]
    print("Puede consultar los nombres de algunos de los estudiantes de grado Once")

    while True:
        try:
            revisar = input("Ingrese un nombre para buscar: ").lower()
            if revisar is not None and revisar.strip() != "":
                break
            else:
                print("Ingrese un nombre vàlido")
        except TypeError or ValueError:
            print("Ingrese un nombre vàlido")

    if revisar in estudiantes:
        print("Estudiante registrado")
    else:
        print("estudiante no registrado")

def clasificar():
    numeros = []

    i=0
    while i<8:
        while True:
            try:
                numero = int(input("Ingrese un número entero del -900 al 900: "))
                if -900 <= numero <= 900:
                    numeros.append(numero)
                    break
                else:
                    print("Ingrese un número dentro del rango permitido.")
            except ValueError or TypeError:
                print("Ingrese un número válido.")
    i+=1

    pares = numeros.count(range(-901, 901, 2))
    impares = numeros.count(range(-900, 901, 1))
    ceros = numeros.count(0)


    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Ceros: {ceros}")

def analisis():
    palabras = []
    i=0
    while i<5:
        while True:
            try:
                palabra = input("Ingrese una palabra: ").lower()
                if palabra is not None and palabra.strip() != "":
                    palabras.append(palabra)
                    break
                else:
                    print("Ingrese una palabra válida")
            except TypeError or ValueError:
                print("Ingrese letras")
        i+=1
    
    for palabra in palabras:
        print(f"{palabra}: caracteres: {len(palabras[palabra])}")

def control():
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ").lower()
            if nombre is not None and nombre.strip() != "":
                break
            else:
                print("Ingrese un nombre válido")
        except TypeError or ValueError:
            print("Ingrese letras")

    i = 0
    suma = 0
    notas = []
    while i<5:
        while True:
            try:
                nota_est = float(input("Dame una nota: "))
                if nota_est < 1 or nota_est > 5:
                    print("Ingresa un número mayor a 1 y menor a 5")
                    continue
                notas.append(nota_est)
                break
            except ValueError:
                print("ingresa un numero, no  una letra")
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

    desglosado= ", ".join(notas)

    print(f"DESEMPEÑO ACADÉMICO\nNOMBRE: {nombre}\nNOTAS: {desglosado}\nPROMEDIO: {promedio}\nDESEMPEÑO: {desempeño}")

def final():
    estudiantes = []

    class Estudiante:
        def __init__(self, nombre):
            self.nombre = nombre
            self.est_notas = []

        def promedioDesempeño(self, est_notas):
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
    
    print("BIENVENIDO!! Deseas registrar estudiantes? (s/n): ")
    respuesta = input("> " ).strip().lower()
    while respuesta not in ["s", "n"]:
        print("Respuesta no válida, por favor ingresa 's' o 'n'")
        respuesta = input("> ").strip().lower()

    if respuesta == "n":
        print("Gracias por usar el sistema!!")
    else:
        while True:
            while True:
                nombre = input("Ingrese el nombre del estudiante: ").strip()
                if nombre and nombre.isalpha():
                    # valid name contains only letters
                    estudiante = Estudiante(nombre)
                    break
                else:
                    print("Ingrese un nombre válido (solo letras)")

            i = 0
        
            while i<5:
                while True:
                    try:
                        nota_est = float(input("Dame una nota: "))
                        if nota_est < 1 or nota_est > 5:
                            print("Ingresa un número mayor a 1 y menor a 5")
                            continue
                        estudiante.est_notas.append(nota_est)
                        break
                    except ValueError:
                        print("ingresa un numero, no  una letra")
                i += 1

            estudiantes.append(estudiante)
            print("Quieres registrar otro estudiante? (s/n): ")
            respuesta = input("> " ).strip().lower()
            while respuesta not in ["s", "n"]:
                print("Respuesta no válida, por favor ingresa 's' o 'n'")
                respuesta = input("> ").strip().lower()

            if respuesta == "n":
                print("Gracias por usar el sistema!!")
                estudiantes.sort(key=lambda e: e.promedioDesempeño(e.est_notas)[1], reverse=True)
                print("\nESTUDIANTES ORDENADOS POR DESEMPEÑO ACADÉMICO:")
                for est in estudiantes:
                    desempeño, promedio, desglosado = est.promedioDesempeño(est.est_notas)
                    print(f"NOMBRE: {est.nombre}\nNOTAS: {desglosado}\nPROMEDIO: {promedio}\nDESEMPEÑO: {desempeño}\n")
                break
            else:
                continue

def GUI():
    print("ingrese ejercicio del 1 al 13")
    

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

    i = 0
    while i<12:
        GUI()

GUI()