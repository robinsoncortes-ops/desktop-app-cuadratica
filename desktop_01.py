from tkinter import *
from tkinter import messagebox

# funciones de app
def calcular():
    A = entry_A.get()
    B = entry_B.get()
    C = entry_C.get()

    if A == "" or B == "" or C == "":
        messagebox.showerror("Error", "Por favor ingrese todos los valores")
        return

    try:
        A = float(A)
        B = float(B)
        C = float(C)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
        return

    discriminante = B**2 - 4*A*C

    if discriminante < 0:
        t_resultodos.delete("1.0", END)
        t_resultodos.insert(END, "No hay soluciones reales")
        t_resultodos_2.delete("1.0", END)
        t_resultodos_2.insert(END, "")
    else:
        x1 = (-B + discriminante**0.5) / (2*A)
        x2 = (-B - discriminante**0.5) / (2*A)
        t_resultodos.delete("1.0", END)
        t_resultodos.insert(END, f"x1 = {x1}")
        t_resultodos_2.delete("1.0", END)
        t_resultodos_2.insert(END, f"x2 = {x2}")


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
# label para titulo de la app
#------------------------------------------------
lb_A = Label(frame_entrada, text="A = ")                        
lb_A.config(bg="yellow", fg="blue",font=("TIME NEW ROMAN",16))
lb_A.place(x=10, y=20)


#------------------------------------------------
lb_B = Label(frame_entrada, text="B = ")                        
lb_B.config(bg="yellow", fg="blue",font=("TIME NEW ROMAN",16))
lb_B.place(x=10, y=60)


#------------------------------------------------
lb_C = Label(frame_entrada, text="C = ")                        
lb_C.config(bg="yellow", fg="blue",font=("TIME NEW ROMAN",16))
lb_C.place(x=10, y=100)

#------------------------------------------------
# Entrada para el valor de A
#------------------------------------------------
entry_A = Entry(frame_entrada, textvariable="A")
entry_A.config(bg="white", fg="black", font=("Times New Roman",16))
entry_A.focus_set()
entry_A.place(x=100, y=20, width=150, height=30)

#------------------------------------------------
entry_B = Entry(frame_entrada, textvariable="B")
entry_B.config(bg="white", fg="black", font=("Times New Roman",16))
entry_B.focus_set()
entry_B.place(x=100, y=60, width=150, height=30)

#------------------------------------------------
entry_C = Entry(frame_entrada, textvariable="C")
entry_C.config(bg="white", fg="black", font=("Times New Roman",16))
entry_C.focus_set()
entry_C.place(x=100, y=100, width=150, height=30)



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
t_resultodos.config(bg= "yellow", fg="black", font=("Arial", 28))
t_resultodos.place(x=10, y=10, width= 200, height=50)

# freme resultados 2
frame_resultados_2 = Frame(frame_1)
frame_resultados_2.config(bg="#BA0C2F" , width=480, height=120)
frame_resultados_2.place(x=10,y=220)

# AREA de texto para resultdos 2
t_resultodos_2 = Text(frame_resultados_2)
t_resultodos_2.config(bg= "yellow", fg="black", font=("Arial", 28))
t_resultodos_2.place(x=10, y=10, width= 200, height=50)


# bucle principal
ventana_principal.mainloop()