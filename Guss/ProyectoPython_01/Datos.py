import pandas as pd #libreria para la manipulacion de datos
import Graficos as gf

def SeleccionarDatos(elemento,media,des1U,des1D,des2U,des2D,des3U,des3D):
    datos=pd.read_excel("Datos.xlsx",sheet_name="Datos", header=0)
    # se toman los valores del elemento seleccionado
    valoresE=datos[elemento]
    # se toman los numeros de muestras correspondientes al elemento seleccionado
    Nmuestras=datos["N°Samples"]
    # se toman los valores de la media
    media=datos[media]
    # 1° Desvio por arriba de la media
    desv1U=datos[des1U]
    # 1° Desvio por debajo de la media y asi con los siguientes desvios
    desv1D=datos[des1D]
    # 2° Desvio
    desv2U=datos[des2U]
    desv2D=datos[des2D]
    # 3° Desvio
    desv3U=datos[des3U]
    desv3D=datos[des3D]
    #se toman los id de las muestras las cuales serviran como label para identificar a las muestras
    etiquetas=datos["Sample"]
    # se llama 
    gf.fnHacerGraficos(valoresE,elemento,Nmuestras, media,desv1U,desv1D,desv2U,desv2D,desv3U,desv3D,etiquetas)