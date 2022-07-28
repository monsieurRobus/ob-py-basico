import pickle

class Juguete:
    _nombre=''
    _precio=0

    def __init__(self,nombre,precio):
        self._nombre = nombre
        self._precio = precio
    
    def getNombre(self):
        return self._nombre

j1 = Juguete("Potato",10)

print(j1.getNombre())

f = open('objeto.bin','wb')
pickle.dump(j1,f)
f.close()

a = open('objeto.bin','rb')
potato = pickle.load(a)
a.close()
print(potato.getNombre())