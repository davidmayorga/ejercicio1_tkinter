from tkinter import *
from tkinter import messagebox

def sumar():
    # messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    c = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + a.get() + " + " + b.get() + " casi siempre es " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    a.set("")
    b.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("David Mayorga")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="black")

# -------------------
# variables globales
# -------------------
a = StringVar()
b = StringVar()
c = IntVar()

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="gold", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para titulo de app
titulo= Label(frame_entrada, text="Colegio San José de Guanentá ")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=240,y=10)

#Etiqueta para subtitulo de app
subtitulo= Label(frame_entrada, text="Ejercicio_1")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=240,y=40)

#Etiqueta para subtitulo 2 de app
subtitulo2= Label(frame_entrada, text="Calcular valor del IVA")
subtitulo2.config(bg="yellow", fg="blue", font=("Arial", 15))
subtitulo2.place(x=240,y=70)


frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="ivory2", width=780, height=120)
frame_operaciones.place(x=10,y=260)

# boton para sumar los números - texto
bt_sum = PhotoImage(file="sumar.png")
# bt_sumar = Button(frame_operaciones, text= "Sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

# boton para borrar entradas y resultado
bt_bor = PhotoImage(file="borrar.png")
# bt_borrar = Button(frame_operaciones, text="Borrar", width=10)
bt_borrar = Button(frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

# boton para salir - cerrar la app
bt_sal = PhotoImage(file="salir.png")
# bt_salir = Button(frame_operaciones, text="Salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place(x=558, y=7)

#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="red", width=780, height=100)
frame_resultados.place(x=10,y=390)

#area de texto para resultados 
t_resultados = Text(frame_resultados, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Arial", 20),)
t_resultados.pack()


#Se ejecuta el metodo mainloop de la clase Tk a traves de la instancia ventana_principal.Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.Cada acción del usuario se conoce como un evento.El método mainloop es un bucle infinito

ventana_principal.mainloop()
