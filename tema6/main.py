from tkinter import N
from xml.etree.ElementTree import QName


class Dino:
    _encendido = False # No tocar las propiedades que tienen la barra baja "_" delante

    def enciende(self):
        self._encendido = True

    def isEncendido(self):
        return self._encendido


d = Dino()
d.enciende()
print(d.isEncendido())

class Estatica:
    numero =1 

    def incrementa():
        Estatica.numero+=1

class Probaturas(Dino):
    color = None
    nombre = None 

    def __init__(self,nombre):
        self.color="Verde"
        self.nombre=nombre

    def __del__(self):
        print("Estoy en el destructor de la clase", self.__class__)
    

p = Probaturas("Pepe")
print(p.color)
print(p.nombre)
