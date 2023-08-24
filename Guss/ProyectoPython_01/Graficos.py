
import matplotlib.pyplot as plt
def fnHacerGraficos (elemento, elemento2,Nmuestras, media,desv1U,desv1D,desv2U,desv2D,desv3U,desv3D,etiquetas):
   
    plt.figure(figsize=(20,8))
# Grafica de las lineas de control
    plt.plot(Nmuestras, media, color='g')
# primer desvio
    plt.plot(Nmuestras, desv1U, color='b')
    plt.plot(Nmuestras, desv1D , color='b')
#segundo desvio
    plt.plot(Nmuestras, desv2U, color='m')
    plt.plot(Nmuestras, desv2D , color='m')
# tercer desvio
    plt.plot(Nmuestras, desv3U, color='r')
    plt.plot(Nmuestras, desv3D , color='r')
# grafico del elemento
    plt.plot(Nmuestras, elemento , color='k',marker='.')
# etiquetas

    for i, label in enumerate(etiquetas):
        plt.annotate(label, (Nmuestras[i] + 0.1, elemento[i]),rotation=90)
    
    if "ppm" in elemento2:
        titulo="(expresado en partes por millones)"
    else:
        titulo="(expresado en porcentaje)"
    plt.suptitle(elemento2,fontsize=20, fontweight="bold")
    plt.title(titulo)
    plt.xlabel("N° de muestras")
    # se coloca una grilla en el grafico con lineas cortadas y transparencia
    plt.grid(ls = "dashed",alpha = 0.25)
    #tamaño del grafico
    
    plt.show()





