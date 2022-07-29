# Crea un script que le pida al usuario una lista de países (separados por comas).
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set).
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

def main():
    paises = input("Introduce los paises: ")
    paises = paises.replace(" ","")
    paises = paises.title()
    paises = paises.split(",")     
    paises = set(paises)
    paises = sorted(paises) #Al ordenar los paises, nos convierte el SET en una lista
    print(paises)


if __name__ == "__main__":
    main()