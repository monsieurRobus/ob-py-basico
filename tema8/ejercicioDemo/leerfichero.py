f = open('texto.txt','r')
datos = f.readline()

f.close()

fi = open('pokemon-favorito','w')
fi.write(f'{datos}\n')
fi.write("Y este es mi fichero uwu")
fi.close()

