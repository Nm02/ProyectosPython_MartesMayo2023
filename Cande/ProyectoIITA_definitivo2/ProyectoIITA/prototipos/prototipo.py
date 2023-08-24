#import pygame
#import random
#import sys

# Inicialización de Pygame
#pygame.init()

# Configuración de la pantalla
#screen_width = 800
#screen_height = 600
#screen = pygame.display.set_mode((screen_width, screen_height))
#background = pygame.image.load("fondo2.png")
#background = pygame.transform.scale(background, (screen_width, screen_height))
#pygame.display.set_caption("Juego del Ladrón")

#background_x = 0 #posicion del fondo

# Colores
#white = (255, 255, 255)
#black = (0, 0, 0)

# Clase para el personaje principal
#class Ladron(pygame.sprite.Sprite):
#    def __init__(self):
#        super().__init__()
#        original_image = pygame.image.load("ladron.png")
#        self.image = pygame.transform.scale(original_image, (50, 50))  # Cambia el tamaño del sprite
#        self.rect = self.image.get_rect()
#        self.rect.center = (screen_width // 2, screen_height - 50)
#        self.speed = 5
#        self.lives = 3

#    def update(self):
#        keys = pygame.key.get_pressed()
#        if keys[pygame.K_a]:
#            self.rect.x -= self.speed
#        if keys[pygame.K_d]:
#            self.rect.x += self.speed

        # Evitar que el personaje salga de la pantalla
#        if self.rect.left < 0:
#            self.rect.left = 0
#        if self.rect.right > screen_width:
#            self.rect.right = screen_width

# Crear instancia del ladron
#ladron = Ladron()

# Grupos de sprites
#all_sprites = pygame.sprite.Group()
#all_sprites.add(ladron)

# Bucle principal del juego
#clock = pygame.time.Clock()
#running = True
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False

#    keys = pygame.key.get_pressed()
#    if keys[pygame.K_a]:
#        ladron.rect.x -= ladron.speed
#        background_x += ladron.speed  # Mueve el fondo junto con el personaje
#    if keys[pygame.K_d]:
#        ladron.rect.x += ladron.speed
#        background_x -= ladron.speed  # Mueve el fondo junto con el personaje

    # Asegúrate de que el fondo no se mueva más allá de los límites
#    if background_x > 0:
#        background_x = 0
#    if background_x < -background.get_width():
#        background_x = -background.get_width()

    # Actualizar sprites
#    all_sprites.update()

    # Dibujar fondo
#    screen.blit(background, (background_x, 0))

    # Dibujar sprites
#    all_sprites.draw(screen)

#    pygame.display.flip()

#    clock.tick(60)

#pygame.quit()
#sys.exit()


#A
