import pygame, sys, time
from nivel_grafico import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height)) #ventana de visualización en la que se representará el juego.
clock = pygame.time.Clock() #configura un reloj que se utiliza para medir el tiempo transcurrido entre fotogramas y controlar la velocidad de actualización del juego.
pygame.display.set_caption("Contador de Tiempo")

level = Level(level_map, screen)
start_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    current_time = time.time() - start_time
    
    if current_time >= 60:
        pygame.quit()
        sys.exit()

    screen.fill("black")

#imprime tiempo en pantalla
    font = pygame.font.Font(None, 35) #None para nombre de archivo por defecto, 36 tamaño fuente
    time_text = font.render(f"Tiempo: {int(current_time)} segundos", True, ("white"))
    screen.blit(time_text, (10, 10))

    level.run()

    pygame.display.update()
    clock.tick(60) #fps
