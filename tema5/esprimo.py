test = 100

def esprimo(numero):
    for divisor in range(2,numero-1):
        if (numero % divisor == 0):
            print("¡¡ALTO!! NO ES PRIMO! Es divisible por ",divisor)
            return False
    print("Es primo")
    return True

print (esprimo(test))
