import pandas as pd 
import Datos as dt
import tkinter as tk
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import ImageTk,Image


def obtener_valor_seleccionado():
    elemento = variable.get()
    parametros=desvio[elemento]
    dt.SeleccionarDatos(elemento,parametros[0],parametros[1],parametros[2],parametros[3],parametros[4],parametros[5],parametros[6])

def buscarArchivo():
    global archivo, desvio
    archivo = filedialog.askopenfilename() # Guarda el contenido del cuadro de texto en la variable
    try:
# se lee el arvhivo excel
        desvio=pd.read_excel(archivo,sheet_name="Desvios", header=0)
#cabeza contiene los elementos a graficar
        cabeza=desvio.columns
        etiqueta=Label(ventana,text="Seleccione un elemento:")
        etiqueta.config(width=40,height=1)
        etiqueta.place(x=20,y=133)

# se crea el combobox o lista desplegable
        cbElementos = OptionMenu(ventana, variable, *cabeza)
        cbElementos.config(width=12,height=1)
        cbElementos.place(x=330,y=130)

# se crea el boton graficar
        btnGraficar = tk.Button(ventana, text="GRAFICAR", command=obtener_valor_seleccionado)
        btnGraficar.config(width=15,height=1)
        btnGraficar.place(x=480,y=133)
    except pd.errors.ParserError:
        messagebox.showerror("Error", "Archivo no es un Excel válido")


# se crea la ventana
ventana=Tk()
ventana.title('Control de calidad')
ventana.geometry("800x600")
ventana.resizable(width=False, height=False)
fondo=ImageTk.PhotoImage(Image.open('Altar_01.jpg'))
etiqueta=Label(image=fondo)
etiqueta.pack()
ventana.iconbitmap('Grafico.ico')
#se crea una variable para almacenar el valor seleccionado
variable = tk.StringVar(ventana)

etiquita=Label(ventana,text="Presione buscar para seleccionar el archivo de datos: ")
etiquita.place(x=20,y=38)
btnBuscar = tk.Button(ventana, text="BUSCAR", command=buscarArchivo)
btnBuscar.config(width=15,height=1)
btnBuscar.place(x=330,y=38)

ventana.mainloop()