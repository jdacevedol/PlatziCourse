from traceback import print_tb


def multiplicacion(num):
    sum = num * 5
    return sum

def suma(num):
    sum = num + 5
    return sum


if __name__ == '__main__':
    num = int(input("Ingrese un numero: "))
    print("Su multiplicacion es: ",  multiplicacion(num))
    print("Su suma es: ", suma(num))