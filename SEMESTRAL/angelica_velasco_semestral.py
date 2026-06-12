def feria():
    proyectos = []
    categorias = ("robotica", "programacion", "diseñotresd", "videojuegos")
    print("\nREGISTRA 4 PROYECTOS:\n")
    for _ in range(4):
        while True:
            nombre_est = input("Dame el nombre del estudiante: ")
            if nombre_est.isalpha() and nombre_est:
                break
            else:
                print("Ingrese un nombre válido")
                
        while True:
            nombre_proy = input("Dame el nombre del proyecto: ")
            if nombre_proy.isalpha() and nombre_proy:
                break
            else:
                print("ingrese un nombre válido")
                

        while True:
            catg = input("Dame el nombre de la categoría (robotica, programacion, diseñotresd, videojuegos): ")
            if catg.isalpha() and catg and catg.lower() in categorias:
                break
            else:
                print("Ingrese una categoría válida")
                
        
        while True:
            try:
                puntaje = float(input("Dame el puntaje del jurado (0-5): "))
                if puntaje >= 0 and puntaje <= 5:
                    break
                else:
                    print("Ingrese una calificación válida entre 0 a 5")
            except ValueError:
                print("Ingrese números")
                
                
        while True:
            try:
                mins = float(input("Dame el tiempo de exposición en minutos: "))
                if mins > 0:
                    break
                else:
                    print("Ingrese un tiempo válido mayor que 0")
            except ValueError:
                print("Ingrese números")

        result = {"nombre": nombre_est,
                  "proyecto": nombre_proy,
                  "categoria": catg,
                  "puntaje": puntaje,
                  "tiempo": mins}
        
        proyectos.append(result)
        
        print("\n------------------\n")

    peornombre = ""
    peor = 5
    mejornombre = ""
    mejor = 0
    suma = 0
    peores = []
    print("Lista de proyectos: \n")
    print("-------------------\n")
    for proyecto in proyectos:
        print("nombre del estudiante:", proyecto["nombre"])
        print("nombre del proyecto:", proyecto["proyecto"])
        print("categoría:", proyecto["categoria"])
        print("puntaje:", proyecto["puntaje"])
        print("tiempo en mins:", proyecto["tiempo"])
        print("\n-------------------\n")
        suma += proyecto["puntaje"]
        if proyecto["puntaje"] > mejor:
            mejor = proyecto["puntaje"]
            mejornombre = proyecto["proyecto"]
        if proyecto["puntaje"] < peor:
            peor = proyecto["puntaje"]
            peornombre = proyecto["proyecto"]
        if proyecto["puntaje"] < 2.5:
            peores.append(proyecto["proyecto"])

    promedio = suma / len(proyectos)
    desempeño = ""
    if promedio < 2.5:
        desempeño = "BAJO"
    elif promedio < 3:
        desempeño = "BÁSICO"
    elif promedio < 4:
        desempeño = "ALTO"
    elif promedio <= 5:
        desempeño = "SUPERIOR"

    print(f"Promedio general de puntajes: {promedio}")
    print("")
    print("Mejor puntaje:\nNombre:", mejornombre,"\npuntaje:" , mejor)    
    print("")   
    print("Peor puntaje:\nNombre:", peornombre,"\npuntaje:" , peor)
    print("")
    print("cantidad de proyectos con menos de 2.5:", len(peores))
    print("")
    print("CLASIFICACIÓN FINAL:")
    print("EL PROMEDIO DE LA FERIA FUE DE:", promedio)
    print("CLASIFICACIÓN:", desempeño)
    print("\n-------------------\n")


    

feria()


