def repeticiones (num1, num2, eleccion):
    contador = int(input("Seleccione cuantas veces desea repetir la operacion: "))
    operacion = 0
    if eleccion == 1:
        eleccion = "Suma"
        for valor in range(contador):
            operacion += suma(num1, num2)
    elif eleccion == 2:
        eleccion = "Resta"
        for valor in range(contador):
            operacion += resta(num1, num2)
    elif eleccion == 3:
        eleccion = "Division"
        for valor in range(contador):
            operacion += division(num1, num2)
    elif eleccion == 4:
        eleccion = "Multiplicacion"
        for valor in range(contador):
            operacion += multiplicacion(num1, num2)
    elif eleccion == 5:
            eleccion = "Suma y division"
            for valor in range(contador):
                operacion += sumDiv(num1, num2)
        elif eleccion == 6:
            eleccion = "Resta y multiplicacion"
            for valor in range(contador):
                operacion += resMul(num1, num2)
    else:
            print("numero incorrecto")
    print ("Este es el resultado de la suma de la cantidad de veces que se repitio la", eleccion)
    print (operacion)


def resMul(num1, num2):
    resMul = (num1-num2) * num1
    print("Su resta es: ", resMul)


def sumDiv(num1, num2):
    sumDiv = (num1 + num2) / num1
    print("Su resta es: ", sumDiv)


def resta(num1, num2):
    res = num1 - num2
    return res


def division(num1, num2):
    div = num1 / num2
    return div


def multiplicacion(num1, num2):
    mul = num1 * num2
    return mul


def suma(num1, num2):
    suma = num1 + num2
    return suma


if __name__ == '__main__':
    num1 = int(input("Ingrese un numero 1: "))
    num2 = int(input("Ingrese un numero 2: "))
    respuesta = "Si"
    while(respuesta == "Si" or respuesta == "si"):
        mensaje =""" BIENVENIDOS A LA NUEVA VERSION CON SSH
            Escoja la opcion de la operacion que desea realizar:
            1. Suma
            2. Resta
            3. Division
            4. Multiplicacion
            5. Summar y dividir el resultado
            6. Restar y multiplicar el resultado
        """
        eleccion = int(input(mensaje))
        repeticiones(num1, num2, eleccion)

        respuesta = input("Desea continuar? ")
    