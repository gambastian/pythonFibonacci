user_input = input("Ingrese el limite para la serie de fibonacci:")
try:
    limit = int(user_input)
    print "Calculando serie de fibonacci inferior a " + str(limit) + ""
    serie = []
    index = 0
    current = 0
    message = ""
    while current <= limit:
        if index == 0:
            current = 0
        elif index == 1:
            current = 1
        else:
            current = serie[index - 1] + serie[index - 2]

        serie.append(current)
        if index > 1 and current <= limit:
            if len(message) == 0:
                message += str(current)
            else:
                message += "," + str(current)
        index += 1

    print "Serie resultante: " + message

except ValueError:
    print("El limite debe ser un numero entero")
