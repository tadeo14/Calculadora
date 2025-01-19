import tkinter as tk
from tkinter import messagebox

# Funciones
def camb_porcentual(A, B):
    if A == 0:
        messagebox.showerror("Error", "No se puede dividir por 0")
        return None
    cambio_porcentual = ((B - A) / abs((A))) * 100
    return round(cambio_porcentual, 2)

def porcentaje(A, B):
    if A == 0:
        messagebox.showerror("Error", "No se puede dividir por 0")
        return None
    porcentaje = ((A * 100) / abs((B)))
    return round(porcentaje, 2)

def calcular_descuento_total(porcentajes_descuento):
    valor_inicial = 100  # Empieza con un valor base de 100 para simplificar el cálculo
    valor_final = valor_inicial
    
    # Aplica los descuentos escalonados
    for porcentaje in porcentajes_descuento:
        valor_final *= (1 - porcentaje / 100)
    
    # Calcular el descuento total en valor y el porcentaje final
    descuento_total = valor_inicial - valor_final
    porcentaje_total = (descuento_total / valor_inicial) * 100
    
    # Redondear el resultado a dos decimales
    return round(porcentaje_total, 2)

# Función para manejar la opción 1
def calcular_diferencia_porcentual():
    try:
        A = float(entry_A.get())
        B = float(entry_B.get())
        resultado = camb_porcentual(A, B)
        if resultado is not None:
            result_label.config(text=f"El cambio porcentual es: {resultado}%")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Función para manejar la opción 2
def calcular_porcentaje():
    try:
        A = float(entry_A.get())
        B = float(entry_B.get())
        resultado = porcentaje(A, B)
        if resultado is not None:
            result_label.config(text=f"El porcentaje es: {resultado}%")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Función para manejar la opción 3
def calcular_descuento():
    try:
        porcentajes_descuento = list(map(float, entry_descuentos.get().split(',')))
        resultado = calcular_descuento_total(porcentajes_descuento)
        if resultado is not None:
            result_label.config(text=f"Porcentaje total de descuento aplicado: {resultado}%")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese porcentajes válidos separados por coma.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora de Porcentajes y Descuentos")

# Crear los widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Etiquetas y campos de entrada
label_A = tk.Label(frame, text="Valor A:")
label_A.grid(row=0, column=0, padx=5, pady=5)
entry_A = tk.Entry(frame)
entry_A.grid(row=0, column=1, padx=5, pady=5)

label_B = tk.Label(frame, text="Valor B:")
label_B.grid(row=1, column=0, padx=5, pady=5)
entry_B = tk.Entry(frame)
entry_B.grid(row=1, column=1, padx=5, pady=5)

label_descuentos = tk.Label(frame, text="Porcentajes de descuento (separados por coma):")
label_descuentos.grid(row=2, column=0, padx=5, pady=5)
entry_descuentos = tk.Entry(frame)
entry_descuentos.grid(row=2, column=1, padx=5, pady=5)

# Botones para las opciones
button_diferencia = tk.Button(frame, text="Calcular Diferencia Porcentual", command=calcular_diferencia_porcentual)
button_diferencia.grid(row=3, column=0, columnspan=2, pady=5)

button_porcentaje = tk.Button(frame, text="Calcular Porcentaje", command=calcular_porcentaje)
button_porcentaje.grid(row=4, column=0, columnspan=2, pady=5)

button_descuento = tk.Button(frame, text="Calcular Descuento Escalonado", command=calcular_descuento)
button_descuento.grid(row=5, column=0, columnspan=2, pady=5)

# Etiqueta para mostrar el resultado
result_label = tk.Label(frame, text="Resultado aparecerá aquí", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()
