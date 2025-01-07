
def camb_porcentual(A,B):

        if A ==0:
                print("No se puede dividir por 0")
                return

        cambio_porcentual = ((B-A) / abs((A)) ) * 100

        return cambio_porcentual

def porcentaje(A,B):

        if A ==0:
                print("No se puede dividir por 0")
                return

        porcentaje = ((A*100) / abs((B)) )

        return porcentaje


##############################################################################

while True:
    print("1- Diferencia porcentual entre A y B")
    print("2- Que porcentaje es A de B")
    print("3- Salir")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        A = float(input("Ingrese el valor: "))
        B = float(input("Ingrese el valor: "))
        resultado = camb_porcentual(A, B)
        print(f"El cambio porcentual es: {resultado:.2f}%")
    elif opcion == "2":
        A = float(input("Ingrese el valor: "))
        B = float(input("Ingrese el valor: "))
        resultado = porcentaje (A, B)
        print(f"El  porcentual es: {resultado:.2f}%")
    elif opcion == "3":
        print("adiós")
        break
    else:
        print("Opción no válida")