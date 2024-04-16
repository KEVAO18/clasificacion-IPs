import csv

class lecturaTabla:

    def __init__(self, archivo):
        self.archivo = archivo

    #set file
    def setArchivo(self, archivo):
        self.archivo = archivo

    #get file
    def getArchivo(self):
        return self.archivo

    def leerTabla(self):
        with open(self.getArchivo(), newline='') as f:
            lector = csv.reader(f)
            tabla = [fila for fila in lector]
            return tuple(tabla)