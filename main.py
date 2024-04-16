import lecturaTabla as lec
import controlPrograma as con
import tkinter as tk
from tkinter import filedialog
from tabulate import tabulate

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)

tabla = lec.lecturaTabla(file_path)
tabla = tabla.leerTabla()
control = con.ControlPrograma()
table_data = []
headers = ['ip', 'clase', 'tipo', 'estructura', 'direccion', 'broadcast', 'mascara', 'host']

for i in tabla:
    control.setIp(i[0])
    table_data.append(control.to_array())

# Mostrar la tabla utilizando tabulate
table = tabulate(table_data, headers=headers, tablefmt='grid')
print(table)

#no cerrar la ventana de la consola
input("Presione enter para salir")

# Crear un archivo de texto con la tabla
file = open('tabla.txt', 'w')
file.write(table)
file.close()