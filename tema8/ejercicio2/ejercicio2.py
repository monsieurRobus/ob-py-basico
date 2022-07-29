import pickle

class Vehiculo():
    modelo = ""
    anyo = 0
    color = ""
    combustible = ""

    def __init__(self,modelo,anyo,color,combustible):
        self.modelo =   modelo
        self.anyo   =   anyo
        self.color  =   color
        self.combustible    =   combustible
        
    def __str__(self):
        return f'Este coche es un {self.modelo} del año {self.anyo} color {self.color}, y cuidao que usa {self.combustible}, ojo no la vayas a liar'

coche = Vehiculo("Opel Corsa", 2017, "rojo", "gasolina")

f = open("opelcorsa.bin","wb")
pickle.dump(coche,f)
f.close()

f = open("opelcorsa.bin","rb")
coche2 = pickle.load(f)
f.close()

print(coche2)