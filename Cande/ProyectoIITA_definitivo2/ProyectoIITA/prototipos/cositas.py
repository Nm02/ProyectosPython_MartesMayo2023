import arcade

#variables
screen_width = 1000
screen_height = 500
screen_title = "jueguito"

#variables para definir sprites
escala_personaje = 0.17
escala_piso = 0.20
objetos = 0.20

class Mygame(arcade.Window):
    def __init__(self):
        super().__init__(screen_width, screen_height, screen_title)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE) #le cambia el fondo

        #listas q va a contener los sprites
        self.coin_list = None()
        self.wall_list = None()
        self.player_list = None()

        self.player.sprite = None #VARIABLE DEL SPRITE DEL JUGADOR (el personaje)

    def setup(self): #para diseñar niveles
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        #SE CREA AL JUGADOR
        image_source = "verde_pixel.webp"
        self.player_sprite = arcade.Sprite(image_source, escala_personaje)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 93
        self.player_list.append (self.player_sprite)

    def on_draw(self):
        arcade.start_render()#aca se inicializa todo lo hecho en la funcion setup

def main():
    window = Mygame() #se crea la ventana
    window.setup() #se ejecuta la funcion setup
    arcade.run() #se corre el motor que es arcade

if __name__ == "__main__":
    main()


