def sumar (numero_1,numero_2):
    return(numero_1 + numero_2)
def resta (numero_1,numero_2):
    return(numero_1 - numero_2)
def multiplicacion (numero_1,numero_2):
    return(numero_1 * numero_2)
def division (numero_1,numero_2):
    if numero_2 == 0:
        print("No se puede dividir entre cero")
    elif numero_2 != 0:
        return(numero_1 / numero_2)
def residuo (numero_1,numero_2):
    if numero_2 == 0:
        print("No se puede dividir entre cero")
    elif numero_2 != 0:
        return(numero_1 % numero_2)

if __name__ == "__main__":
    while 1:

        numero_1= int(input("Escribe el primer numero: "))
        numero_2= int(input("Escribe el segundo numero: "))
        selector= int(input("Selecione su operacion:\n  1 para sumar \n  2 para restar \n  3 para multiplicar \n  4 para dividir \n  5 para residual \n"))
        

        if selector == 1:
            print("Su resultado es: ",sumar(numero_1,numero_2))
        elif selector == 2:
            print("Su resultado es: ",resta(numero_1,numero_2))
        elif selector == 3:
            print("Su resultado es: ",multiplicacion(numero_1,numero_2))
        elif selector == 4:
            if numero_2 == 0:
                print("No se puede dividir entre cero")
            else:
                print("Su resultado es: ",division(numero_1,numero_2))
        elif selector == 5:
            if numero_2 == 0:
                print("No se puede dividir entre cero")
            else:
                print("Su resultado es: ",residuo(numero_1,numero_2))
        else:
            print("El numero ingresado no es valido")