import tkinter as tk
from tkinter.font import BOLD
from archivos.forms.login import App
import archivos.util.generic as utl


class MasterPanel:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio')

         # Establecer el icono de la ventana
        icon_path = "./archivos/imagenes/icono.ico"  
        self.ventana.iconbitmap(icon_path)

        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        
        logo = utl.leer_imagen("./archivos/imagenes/logo.png", (200, 200))  # Ajustar tamaño a la ventana
        label = tk.Label(self.ventana, image=logo, bg='#3a7ff6')
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        # Crear el botón de Iniciar
        boton_iniciar = tk.Button(self.ventana, text="Iniciar", font=(None, 12, BOLD), command=self.iniciar_click)
        boton_iniciar.place(relx=0.5, rely=0.7, anchor='center')

        self.ventana.mainloop()

    def iniciar_click(self):
        
        # Crear una instancia de la clase App
        self.ventana.destroy()
        App()


        
if __name__ == "__main__":
    ventana = MasterPanel()