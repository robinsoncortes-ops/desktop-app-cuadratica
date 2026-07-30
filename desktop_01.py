import cmath
from tkinter import *
from tkinter import messagebox
import tkinter

# funciones de app


def A():
    messagebox.showinfo("Información", "Este es el valor de A")
    frame_entrada.destroy()
def B():
    messagebox.showinfo("Información", "Este es el valor de B")
    frame_entrada.destroy()

def C():
    messagebox.showinfo("Información", "Este es el valor de C")
    frame_entrada.destroy()


def limpiar():
    messagebox.showinfo("Información", "Se limpiaran los datos")
    A.set("")
    B.set("")
    C.set("")
    t_resultodos.delete("1.0", END)

def calcular():
    try:
        va = float(A.get())
        vb = float(B.get())
        vc = float(C.get())
    except ValueError:
        messagebox.showinfo(
            "Cuadratica 1.0", "Por favor ingresa números válidos en A, B y C"
        )
        return

    if va == 0:
        messagebox.showinfo(
            "Cuadratica 1.0",
            "El valor de A no puede ser 0 (no sería una ecuación cuadrática)",
        )
        return

    discriminante = (vb**2) - (4 * va * vc)

    t_resultodos.insert(
        tkinter.END, f"Ecuación: {va}x² + {vb}x + {vc} = 0\n"
    )
    t_resultodos.insert(tkinter.END, f"Discriminante = {discriminante}\n")

    if discriminante > 0:
        raiz1 = (-vb + discriminante**0.5) / (2 * va)
        raiz2 = (-vb - discriminante**0.5) / (2 * va)
        t_resultodos.insert(tkinter.END, "Dos raíces reales distintas:\n")
        t_resultodos.insert(tkinter.END, f"x1 = {raiz1}\n")
        t_resultodos.insert(tkinter.END, f"x2 = {raiz2}\n\n")

    elif discriminante == 0:
        raiz = -vb / (2 * va)
        t_resultodos.insert(tkinter.END, "Una raíz real (doble):\n")
        t_resultodos.insert(tkinter.END, f"x = {raiz}\n\n")

    else:
        raiz1 = (-vb + cmath.sqrt(discriminante)) / (2 * va)
        raiz2 = (-vb - cmath.sqrt(discriminante)) / (2 * va)
        t_resultodos.insert(tkinter.END, "Dos raíces complejas:\n")
        t_resultodos.insert(tkinter.END, f"x1 = {raiz1}\n")
        t_resultodos.insert(tkinter.END, f"x2 = {raiz2}\n\n")





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

# variables globales
A = StringVar()
B = StringVar()
C = StringVar()


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
# label para titulo de la app
#------------------------------------------------
lb_A = Label(frame_entrada, text="A = ")                        
lb_A.config(bg="#050304" , fg="blue",font=("TIME NEW ROMAN",16))
lb_A.place(x=10, y=20)


#------------------------------------------------
lb_B = Label(frame_entrada, text="B = ")                        
lb_B.config(bg="#050304" , fg="blue",font=("TIME NEW ROMAN",16))
lb_B.place(x=10, y=60)


#------------------------------------------------
lb_C = Label(frame_entrada, text="C = ")                        
lb_C.config(bg="#050304" , fg="blue",font=("TIME NEW ROMAN",16))
lb_C.place(x=10, y=100)

#------------------------------------------------
# Entrada para el valor de A
#------------------------------------------------
entry_A = Entry(frame_entrada, textvariable=A)
entry_A.config(bg="white", fg="black", font=("Times New Roman",16))
entry_A.focus_set()
entry_A.place(x=100, y=20, width=150, height=30)

#------------------------------------------------
entry_B = Entry(frame_entrada, textvariable=B)
entry_B.config(bg="white", fg="black", font=("Times New Roman",16))
entry_B.focus_set()
entry_B.place(x=100, y=60, width=150, height=30)

#------------------------------------------------
entry_C = Entry(frame_entrada, textvariable=C)
entry_C.config(bg="white", fg="black", font=("Times New Roman",16))
entry_C.focus_set()
entry_C.place(x=100, y=100, width=150, height=30)



#------------------------------------------------
# boton para calcular
#------------------------------------------------
bt_calcular = Button(ventana_principal, text="calcular", command=calcular)
bt_calcular.place(x=50,y =400, width=150, height=30)

#------------------------------------------------
# boton para limpiar
#------------------------------------------------
bt_limpiar = Button(ventana_principal, text="limpiar", command=limpiar)
bt_limpiar.place(x=220,y =400, width=150, height=30)

# titulo de la app
titulo = Label(ventana_principal, text="solucion de ecuaciones de segundo grado")
titulo.config(bg="#FFFFFF", fg="blue",font=("arial",16))
titulo.place(x=190, y=10)
#------------------------------------------------
titulo_2 = Label(frame_1, text="resultado")
titulo_2.config(bg="#FFFFFF", fg="blue",font=("arial",16))
titulo_2.place(x=100, y=10)

#-------------------------------------------------
#frame resultados
#------------------------------------------------
frame_resultados = Frame(frame_1)
frame_resultados.config(bg="#BA0C2F" , width=480, height=120)
frame_resultados.place(x=10,y=90)

# AREA de texto para resultdos
t_resultodos = Text(frame_resultados)
t_resultodos.config(bg= "black", fg="white", font=("Arial", 10))
t_resultodos.place(x=10, y=10, width= 250, height=200)



# bucle principal
ventana_principal.mainloop()