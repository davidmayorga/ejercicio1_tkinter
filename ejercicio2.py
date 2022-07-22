import tkinter as tk


class bandera(tk.Frame):
   
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master 

        self.inicializar_gui()

    def inicializar_gui(self):
        frm_amarillo = tk.Frame(master=self.master, width=300, height=200, bg="#FCD116")
        frm_amarillo.pack(fill=tk.X, side=tk.TOP)   

        frm_azul = tk.Frame(master=self.master, width=450, height=150, bg="#003893")
        frm_azul.pack(fill=tk.X, side=tk.TOP) 

        frm_rojo = tk.Frame(master=self.master, width=450, height=200, bg="#CE1126")
        frm_rojo.pack(fill=tk.X, side=tk.TOP) 

def main():
    root = tk.Tk()
    root.title("bandera Colombiana")
    root.geometry("800x500")

    ventana = bandera(root)
    ventana.mainloop()

if __name__ == "__main__":
    main()

#etiqueta para el titulo de la app


        







        

        

        
        
        
        
        
