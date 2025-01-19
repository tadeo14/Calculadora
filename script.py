
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

def calcular_descuento_total(porcentajes_descuento):
    valor_inicial = 100  # Empezamos con un valor base de 100 para simplificar el cálculo
    valor_final = valor_inicial
    
    # Aplicamos los descuentos escalonados
    for porcentaje in porcentajes_descuento:
        valor_final *= (1 - porcentaje / 100)
    
    # Calcular el descuento total en valor y el porcentaje final
    descuento_total = valor_inicial - valor_final
    porcentaje_total = (descuento_total / valor_inicial) * 100
    
    # Redondear el resultado a dos decimales
    return round(porcentaje_total, 2)

# Ejemplo de uso
porcentajes_descuento = [10, 10]  # Descuentos del 10% y 10%

porcentaje_total = calcular_descuento_total(porcentajes_descuento)

print(f"Porcentaje total de descuento aplicado: {porcentaje_total}%")


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