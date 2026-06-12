def feria():
    proyectos = []
    categorias = ("robotica", "programacion", "diseno3d", "videojuegos")

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
            catg = input("Dame el nombre de la categoría (robotica, programacion, diseno3d, videojuegos): ")
            if catg.isalpha() and catg and catg.lower() in categorias:
                break
            else:
                print("Ingrese una categoría válida")
                
        
        while True:
            try:
                puntaje = float(input("Dame el puntaje del jurado (0-5): "))
                if puntaje >= 0 and puntaje <= 5  and puntaje:
                    break
                else:
                    print("Ingrese una calificación válida entre 0 a 5")
            except ValueError:
                    print("Ingrese números")
                
        
        while True:
            try:
                mins = float(input("Dame el tiempo de exposición en minutos: "))
                if mins > 0 and mins:
                    break
                else:
                    print("Ingrese una calificación válida entre 0 a 5")
            except ValueError:
                print("Ingrese números")

        result = {"nombre": nombre_est,
                  "proyecto": nombre_proy,
                  "categoria": catg,
                  "puntaje": puntaje,
                  "tiempo": mins}
        
        proyectos.append(result)

    for key, value in proyectos:
        print(key, value)

feria()


