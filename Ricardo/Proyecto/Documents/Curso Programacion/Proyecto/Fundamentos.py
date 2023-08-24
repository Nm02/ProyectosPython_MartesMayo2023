# file=open(r"C://Users//RICARDO RODRIGUEZ//Documents//Curso Programacion//Proyecto//Fundamento.txt","r") 
# file.closed       
from tkinter import *
from tkinter import ttk

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Proyecto")
if __name__ == "__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop()
    
