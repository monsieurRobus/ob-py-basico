import _thread
import time

def horaActual(nombre_thread, tiempo_de_espera):
    c = 0

    while c < 5:
        time.sleep(tiempo_de_espera)
        c+=1
        print(f'Hilo {nombre_thread} tiempo {time.ctime(time.time())}')

_thread.start_new_thread(horaActual,("hilo1",1))
_thread.start_new_thread(horaActual,("hilo2",4))

while True:
    pass



