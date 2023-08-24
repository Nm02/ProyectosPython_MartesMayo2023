from tkinter import *
from tkinter import ttk
#import tkinter as Tk

from tkinter import Image


class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Entrenamiento Femenino")
if __name__ == "__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)

#ventana.iconbitmap(" ")

# ventana.resizable(0,0)#permiso para editar el tamaño de ventana desde el programa (X,Y)
ventana.geometry("650x550")
ventana.config(bg="pink")


#frame1=Frame
#frame1.pack(fill="both",expand=True)
#frame1.config(bg="red")#cambiar color del frame
#frame1.config(width=400,height=400)#cambiar tamaño (X,Y)
#frame1.config(relief="groove")#cambiar color del borde
#frame1.config(bd=4)#establece el tamaño del borde
#frame1.config(cursor="pirate")#cambia el cuerosr en el frame
#frame1.config(fill=)
#frame1.pack_propagate(False)
#frame1.grid_propagate(False)

#def __init__(self,frame1):
   # self.frame1=frame1
  #  self.frame1.title("Ingresar")

File=open("Fundamento.txt","r")
label1 = Label(ventana,text=File.read(),bg="skyblue")
label1.pack()

label1.config(height=100,width=500)
label1.grid(column=1,row=10)
label1.pack(side="top")
# label1.place(x=0,y=0)
File.close()

#ventana=BitmapImage(file="c:\Users\RICARDO RODRIGUEZ\Documents\Curso Programacion\Proyecto\OIP.png")



#fondo=label1(ventana,imagefondo=imagenfondo).place(x=0,y=0)





#from tkinter import *
 #ventana ventana = Tk () #el frame debe posicionarse en...si lo colocas vació es tenerlo en memoria pero no pasa a ser mostrado
 #  Myframe = Frame (ventana) Myframe.pack (fill="both",expand=True) Imagen=PhotoImage (file="logo.png") 
 # #la mayoria de las palabras reservadas por el lenguaje o una libreria deben ser respetadas tenias "Image=Imagen" 
#y lo correcto 
#"image=variable (en este caso Imagen)" 
#Imagen_2 =Label (Myframe, image=Imagen)
#Imagen_2.place (x=0, y=0)
#ventana.mainloop ()

def abrir_ventana1():
    ventana1=Toplevel()
    
    ventana1.title("Entrenamiento")
    ventana1.config(bg="green")
    ventana1.mainloop()

    boton_cerrar=ttk.Button(ventana1,text="cerrar",command=ventana1.destroy)

button=Button(ventana,text="INGRESAR",command=abrir_ventana1)
#button.grid(column=10,row=15)
button.config(bg="yellow")
button.pack(side=RIGHT, padx=50,pady=60)
button2=Button(ventana,text="SALIR",command=ventana.destroy)
button2.pack(side=LEFT,padx=50,pady=60)
button2.config(bg="yellow")
#button=ttk.Button(ventana,text="Ingresar",command=ingresar _ventana1)

#Ventana secundaria


#class ventana1():
 # def __init__(self,ventana1):
  # super().__init__(ventana1)
   #ventana1=Toplevel()
   #s#elf.ventana1=ventana1
   #se#lf.ventana1.title("Entrenamiento Femenino")

   #self.config(width=300,height=200)
   #self.boton_cerrar=ttk.Button(self,text="Cerrar",command=self.destroy)
   #self.boton_cerrar.place(x=75,y=75)
   #self.focus()
   #self.grab_st()

ventana.mainloop()
