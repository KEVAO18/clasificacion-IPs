import lecturaTabla as lec
import controlPrograma as con
import tkinter as tk
from tkinter import Entry
from tkinter import filedialog
from tabulate import tabulate

def popup(mensaje: str = "default", titulo = "Mensaje"):
    tk.messagebox.showinfo(titulo, mensaje)
    return


# ejecutar de forma individual para una sola ip a la vez
# mostrar informacion con el metodo popup no guardar informacion
def exe_individual_sin_tabla():
    root = tk.Tk()
    root.title("Ingresar IP")
    root.config(bd=120)

    label = tk.Label(root, text="Ingrese una IP")
    label.pack()

    ip = tk.Entry(root)
    ip.pack()

    def mostrar_info():
        control = con.ControlPrograma()
        control.setIp(ip.get())
        popup(control)

    button = tk.Button(root, text="Mostrar info", command=mostrar_info)
    button.pack()

    # boton para cerrar
    button2 = tk.Button(root, text="Salir", command=root.destroy)
    button2.pack()

    root.mainloop()

# funcion encargada de ejecutar una instruccion individual usando un Entry para pedir las ip,
# guardar cada ip en un array y al final mostrar la tabla
def exe_individual():
    root = tk.Tk()
    root.title("Ingresar IP")
    root.config(bd=120)

    label = tk.Label(root, text="Ingrese una IP")
    label.pack()

    ip = tk.Entry(root)
    ip.pack()

    ips = []

    def guardar_ip():
        ips.append(ip.get())
        ip.delete(0, tk.END)

    def mostrar_tabla():
        table_data = []
        headers = ['ip', 'clase', 'tipo', 'estructura', 'direccion', 'broadcast', 'mascara', 'host']
        control = con.ControlPrograma()

        for i in ips:
            control.setIp(i)
            table_data.append(control.to_array())

        # Mostrar la tabla utilizando tabulate
        table = tabulate(table_data, headers=headers, tablefmt='grid')
        print(table)

        # Crear un archivo de texto con la tabla
        file = open('tabla.txt', 'w')
        file.write(table)
        file.close()

        popup("Tabla guardada en tabla.txt")

        root.destroy()

    button = tk.Button(root, text="Guardar IP", command=guardar_ip)
    button.pack()

    button2 = tk.Button(root, text="Mostrar tabla", command=mostrar_tabla)
    button2.pack()

    root.mainloop()

# funcion encargada de ejecutar una instruccion por lotes
def exe_lotes():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    popup("Archivo seleccionado: " + file_path)

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

    # Crear un archivo de texto con la tabla
    file = open('tabla.txt', 'w')
    file.write(table)
    file.close()

    popup("Tabla guardada en tabla.txt")

# funcion encargada de mostrar el menu principal usando tkinter
def menu():
    root = tk.Tk()
    root.title("Menu")
    root.config(bd=120)

    label = tk.Label(root, text="Seleccione una opcion")
    label.pack()

    button1 = tk.Button(root, text="Ejecutar instruccion individual", command=exe_individual)
    button1.pack()

    button2 = tk.Button(root, text="Ejecutar instruccion por lotes", command=exe_lotes)
    button2.pack()

    button3 = tk.Button(root, text="Ejecutar instruccion individual sin tabla", command=exe_individual_sin_tabla)
    button3.pack()

    # boton para cerrar el programa
    button3 = tk.Button(root, text="Salir", command=root.destroy)
    button3.pack()

    root.mainloop()

menu()
