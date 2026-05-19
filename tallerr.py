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

    
def GUI():
    print("ingrese ejercicio")
    print("""1      2
          3      4
          5      6
          7      8
          9      10
          11      12
""")

option = int()