
def main(): 
    f = open("testeo.txt",'w')
    f.write("Este texto es una prueba\nNo hay que buscarle sentido\nAl fin y al cabo es menos eficiente que un lorem ipsum\nLalala")
    f.close()

if __name__ == "__main__":
    main()