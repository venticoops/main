suma = 0
sueño = []
counter = 0
while True:
    try:
        for _ in range(7):
            hora = float(input(f"Pone hora de dia {_+1}: "))
            if hora >= 0:
                sueño.append(hora)
                suma = suma + hora
                if hora < 6:
                    counter += 1
            else:
                print("malo")
                hora = float(input(f"Pone hora de dia {_+1}: "))

        break
    except ValueError:
        print("malo")

pedidos={}

print(sueño)
print(suma)
print(suma/len(sueño))
print(counter)

if suma/len(sueño) <= 4:
    print("malo")
elif suma/len(sueño) <=6 :
    print("regular")
elif suma/len(sueño) > 6 :
    print("epa")