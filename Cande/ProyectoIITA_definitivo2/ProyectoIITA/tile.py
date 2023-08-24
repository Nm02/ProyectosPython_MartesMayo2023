import pygame

# esta clase Tile crea un sprite rectangular blanco. 
class Tile (pygame.sprite.Sprite): #Sprite es una biblioteca base de pygame. Sirve para metodos y atributos de sprites
    def __init__ (self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill("white")
        self.rect = self.image.get_rect (topleft=pos) 
  
    def update(self, k_shift): #esto va a hacer que la pantalla se mueva
        self.rect.x += k_shift # Ajusta la posición horizontal del tile según el desplazamiento k_shift