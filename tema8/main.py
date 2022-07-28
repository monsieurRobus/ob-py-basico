class Juguete:
    nombre=""
    precio=0

    # def __str__(self):  #Este método se ejecutará cada vez que haga un print sobre j1, pero se usa para representaciones informarles. 
#                     #Se puede desbordar pero para este fin ya existe __repr__
#     return f'Este juguete es un {self.nombre} y cuesta {self.precio} €'

#__repr__ SALIDAS TECNICAS
#__str__ SALIDAS INFORMALES / PRODUCCION

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    
    def __repr__(self):
        return f'Este juguete es un {self.nombre} y cuesta {self.precio} €'

j1 = Juguete("Madel Man",2000)

print(repr(j1))

