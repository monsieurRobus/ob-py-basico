#GUI / Graphical User Interface

import tkinter

# WIdget/componentes - botones, radiobutrtons...
#componentes: ventanas y demás

window = tkinter.Tk()


label3 = tkinter.Label(window, text="tres", bg="purple", fg="orange")
label3.pack(ipadx=50,ipady=15, side='top', fill="x")


label4 = tkinter.Label(window, text="cuatro", bg="blue", fg="white")
label4.pack(ipadx=50,ipady=15, side='bottom', fill="x")

label1 = tkinter.Label(window, text="uno", bg="yellow", fg="blue")
label1.pack(ipadx=50,ipady=15, side='left')


label2 = tkinter.Label(window, text="dos", bg="red", fg="white")
label2.pack(ipadx=50,ipady=15, side='right')



label5 = tkinter.Label(window, text="cinco", bg="orange", fg="purple")
label5.pack(ipadx=50,ipady=15, side='left')


label6 = tkinter.Label(window, text="cinco", bg="white", fg="black")
label6.pack(ipadx=50,ipady=15, side='right')





window.mainloop()

#geometria pack, grid y place


