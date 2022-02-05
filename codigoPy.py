def resta(num1, num2):
    res = num1 - num2
    print("Su resta es: ", res)


def division(num1, num2):
    div = num1 * num2
    print("Su division es: ", div)


def multiplicacion(num1, num2):
    mul = num1 * num2
    print("Su multiplicacion es: ",  mul)


def suma(num1, num2):
    suma = num1 + num2
    print("Su suma es: ", suma)


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
        """
        eleccion = int(input(mensaje))
        if eleccion == 1:
            suma(num1, num2)
        elif eleccion == 2:
            resta(num1, num2)
        elif eleccion == 3:
            division(num1, num2)
        elif eleccion == 4:
            multiplicacion(num1, num2)
        else:
            print("numero incorrecto")
        respuesta = input("Desea continuar? ")
    