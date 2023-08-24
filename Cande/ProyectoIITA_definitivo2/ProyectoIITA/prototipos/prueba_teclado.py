import pygame, sys
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)

coord_x = 10
coord_y = 10
speed_x = 0
speed_y = 0

class Colisiones():
    def horizontal_movement_collision(self):
        player = self.rectangulo
        player.x += speed_x

        for sprite in self.tiles:
            if sprite.colliderect(player):
                if speed_x < 0:
                    player.left = sprite.right
                elif speed_x > 0:
                    player.right = sprite.left

    def check_collisions(self):
        self.horizontal_movement_collision()

choque = Colisiones()

# el rectángulo del jugador
rectangulo = pygame.Rect(coord_x, coord_y, 50, 50, )

# instancias de objetos Rect para los tiles y agregarlos a la lista
choque.tiles = [
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50),
    pygame.Rect(400, 400, 50, 50)
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                speed_x = -1
            if event.key == pygame.K_d:
                speed_x = 1
            if event.key == pygame.K_s:
                speed_y = 1
            if event.key == pygame.K_w:
                speed_y = -1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                speed_x = 0
            if event.key == pygame.K_d:
                speed_x = 0
            if event.key == pygame.K_s:
                speed_y = 0
            if event.key == pygame.K_w:
                speed_y = 0

    choque.rectangulo = rectangulo

    choque.check_collisions()

    #límites de la pantalla
    if rectangulo.left < 0:
        rectangulo.left = 0
    if rectangulo.right > size[0]:
        rectangulo.right = size[0]
    if rectangulo.top < 0:
        rectangulo.top = 0
    if rectangulo.bottom > size[1]:
        rectangulo.bottom = size[1]

    screen.fill(WHITE)

    rectangulo.x += speed_x
    rectangulo.y += speed_y

    pygame.draw.rect(screen, BLACK, rectangulo)
    for tile in choque.tiles:
        pygame.draw.rect(screen, BLACK, tile)
    pygame.display.flip()
