def resta(num1, num2):
    sum = num1 - num2
    return sum


def division(num1, num2):
    sum = num1 * num2
    return sum


def multiplicacion(num1, num2):
    mul = num1 * num2
    print("Su multiplicacion es: ",  mul)


def suma(num1, num2):
    sum = num1 + num2
    print("Su suma es: ", )


if __name__ == '__main__':
    num1 = int(input("Ingrese un numero 1: "))
    num2 = int(input("Ingrese un numero 2: "))
    multiplicacion(num1, num2)
    suma(num1, num2)
    resta(num1, num2)
    division(num1, num2)
    
    