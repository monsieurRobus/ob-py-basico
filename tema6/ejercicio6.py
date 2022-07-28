class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

    def __init__(self,color,ruedas,puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas


class Coche(Vehiculo):
    velocidad=None
    cilindrada=0

    def __init__(self,velocidad,cilindrada,color,ruedas,puertas):
        super().__init__(color,ruedas,puertas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

cochazo = Coche(120,80,"Rojo",4,5)
print(cochazo)

print(cochazo.color," ",cochazo.ruedas," ", cochazo.puertas," ", cochazo.velocidad," ", cochazo.cilindrada," ")
