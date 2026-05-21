"""
Taller teórico
1. ¿Por qué una lista puede ser más útil que crear muchas variables como nota1, nota2, nota3?
    -   Porque la lista almacena esas variables dentro de una misma categoria, permitiendo que se extraigan de forma más eficaz


"""

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
    class Estudiante:
        def __init__(self, nombre, *notas:int):
            nombre = nombre
            est_notas = []
            est_notas.extend(notas)
    
    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ").lower()
            if nombre is not None and nombre.strip() != "":

                Estudiante.nombre = nombre
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
                Estudiante.notas = nota_est
                break
            except ValueError:
                print("ingresa un numero, no  una letra")
        i += 1

    def promedioDesempeño(Estudiante):
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

        return desempeño, promedio

    desglosado= ", ".join(notas)

    print(f"DESEMPEÑO ACADÉMICO\nNOMBRE: {nombre}\nNOTAS: {desglosado}\nPROMEDIO: {promedio}\nDESEMPEÑO: {desempeño}")


    


def GUI():
    print("ingrese ejercicio del 1 al 12")
    

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
        12: control
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

    GUI()

GUI()