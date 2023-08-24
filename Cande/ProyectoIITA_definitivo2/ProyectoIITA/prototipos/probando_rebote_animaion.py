import pygame, sys #sys es parapoder cerrar la ventana despues.
pygame.init() #con init se inicializa pygame

BLACK= (  0,   0,   0)
WHITE= (255, 255, 255)

size = (800, 500) #variable del tamaño

screen=pygame.display.set_mode(size) #se crea una ventana con el tamao antes especificado. Lo de adentro del parentesis es una tupla.

#reloj: sirve para controlar los FPS (frames por segundo)
clock=pygame.time.Clock()
#coordenadas del cuadrado:
cord_x=400
cord_y=200
#velocidad a la que se moverá el cuadrado:
speed_x=3
speed_y=3

#un juego es un bucle gigante que se repite una y otra vez, entonces:
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #"si el tipo del evento es = a pygame.quit(quitar)"
            sys.exit() #todo esto es para poder cerrar la pestaña del juego.

###LOGICA
    if (cord_x > 720 or cord_x < 0): #esto sirve para que el cuadrado revote con las paredes de la ventana
        speed_x *= -1
    if(cord_y > 420 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x #animacion!
    cord_y += speed_y
    screen.fill(WHITE) #Se eleige color de fondo
###LOGICA

###ZONA DE DINUJO, siempre debajo de donde se pinta la pantalla
    pygame.draw.line(screen, BLACK, [0,100],[200,300], 7) #(donde se dibuja, color, coordenadas, grosor)
    pygame.draw.rect(screen, BLACK, (cord_x, cord_y, 80, 80))
#    pygame.draw.rect(screen, BLACK, (cord_x, 230, 50, 50)) #(x,y,tamañoxtamaño)
###FIN ZONA DIBUJO

    pygame.display.flip() #Se actualiza pantalla. Si no actualizo,no cambia de color
    clock.tick(60)
 

