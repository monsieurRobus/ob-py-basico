from functools import reduce
from getpass import getpass

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
letras = ["a","b","c","d","e","f","g","h","i","j",3]

def funcionFiltro(x): # Si la función filtro devuelve TRUE, devuelve el numero, si devuelve FALSE, no
    if x%2==0:
        return True
    return False

numPar = filter(lambda x: not x%2 ,numeros) ## si es igual a 0 equivale a FALSO, por eso hay que negarlo delantes

print(list(numPar))

numCuad = map(lambda x: x**2 , numeros)

print(list(numCuad))

#Reduce realiza una operación entre todos los valores hasta que solo queda uno

numSum = reduce(lambda a,b: a+b, numeros)
print(numSum)

#ZIP asocia elementos de dos ITERABLES en una sola tupla
zipeado = zip(numeros,letras)
print(list(zipeado))

##any y and

sioque = all(map(lambda x: type(x)==int ,   numeros))
sioque2 = any(map(lambda x: type(x)==int,   letras))
print(sioque2)


## GETPASS

usr = input("Usuario: ")
psw = getpass("Password: ",'*')