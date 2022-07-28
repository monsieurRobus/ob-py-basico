class Alumno:
    _nota=0
    _nombre=None
    
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    def haAprobado(self):
        return (self._nota>=5)


a = Alumno("Perico Palote",3)

if(a.haAprobado()):
    print("Alright!!")
else:
    print("aaaw uwu")