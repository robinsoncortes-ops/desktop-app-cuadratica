from tkinter import *
from tkinter import messagebox


#------------------------------------------------
# ventana principal
#------------------------------------------------
ventana_principal = Tk()


#------------------------------------------------
# titulo
#------------------------------------------------
ventana_principal.title("sistemas guanenta")


#------------------------------------------------
# tamaño de la vantana
#------------------------------------------------
ventana_principal.geometry("700x500")


#------------------------------------------------
# color de fonde a la pantalla
#------------------------------------------------
ventana_principal.config(bg="black")


#------------------------------------------------
# deshabilitar el boton de maximizar
#------------------------------------------------
ventana_principal.resizable(0,0)

#------------------------------------------------
# frame entrada de datos
#------------------------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="#BA0C2F" , width=380, height=240)
frame_entrada.place(x=10,y=110)

frame_1 = Frame(ventana_principal)
frame_1.config(bg="#BA0C2F" , width=280, height=340)
frame_1.place(x=410,y=110)

#------------------------------------------------
# boton para calcular
#------------------------------------------------
bt_calcular = Button(ventana_principal, text="calcular", command="calcular")
bt_calcular.place(x=50,y =400, width=150, height=30)

#------------------------------------------------
# boton para limpiar
#------------------------------------------------
bt_limpiar = Button(ventana_principal, text="limpiar", command="limpiar")
bt_limpiar.place(x=220,y =400, width=150, height=30)

# titulo de la app
titulo = Label(ventana_principal, text="solucion de ecuaciones de segundo grado")
titulo.config(bg="#FFFFFF", fg="blue",font=("arial",16))
titulo.place(x=190, y=10)


# bucle principal
ventana_principal.mainloop()