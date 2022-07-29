import tkinter
from tkinter import ttk

window = tkinter.Tk()

#Definimos tamaño del grid (algo parecido a grid en css)

#00             10          20
#USERNAME      ENTRY        
#01             11          21
#PASSNWORD     ENTRY

window.columnconfigure(0,weight=1)
window.columnconfigure(0,weight=3)

#USER
username_label = ttk.Label(window, text="Username:")
username_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5) # Hemos usado STICKY para que se quede pegado en un sitio y no se mueva

username_entry = ttk.Entry(window)
username_entry.grid(column=1,row=0, sticky=tkinter.E, padx=5, pady=5)

#PASSWORD
password_label = ttk.Label(window, text="Password:")
password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5) # Hemos usado STICKY para que se quede pegado en un sitio y no se mueva

password_entry = ttk.Entry(window, show='x')
password_entry.grid(column=1,row=1, sticky=tkinter.E, padx=5, pady=5)

#BOTON
login_button = ttk.Button(window, text="Enviar")
login_button.grid(column=1,row=2,sticky=tkinter.E, padx=5, pady=5)


window.mainloop()