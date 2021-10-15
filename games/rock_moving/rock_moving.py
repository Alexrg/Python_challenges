"""
You have a chessboard with only the Rock on it. The rock can move up, down, left
or rigth from your prespective. Write a function (or a class) that takes a
series of movements and at the end of the sequence movements prints two numbers:

a) The distance traveled by the rock.
b) How far away the rock is from it's starting point.

Assume that the chessboard has no edges (the rock can travel any distance in
any direction)

For example, if the Rock is moved in the following sequence (up 1, left 3, down
2), then the rock has traveled a distance of 6 spaces, and is 4 spaces away from
it's starting point.
"""
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

def main():
    pygame.init()
    pygame.font.init() 
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    # creamos la ventana y le indicamos un titulo:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Rock game")

    # cargamos el fondo y una imagen (se crea objetos "Surface")
    fondo = pygame.image.load("texture.jpeg").convert()
    rock = pygame.image.load("descarga.png").convert_alpha()
    rock = pygame.transform.scale(rock, (150, 100))

    rock_pos_x = 550
    rock_pos_y = 200

    # Indicamos la posicion de las "Surface" sobre la ventana
    screen.blit(rock, (rock_pos_x, rock_pos_y))
    screen.blit(fondo, (0, 0))
    # se muestran lo cambios en pantalla
    pygame.display.flip()

    # el bucle principal del juego
    while True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
        	rock_pos_y -= 1
        if keys[pygame.K_DOWN]:
        	rock_pos_y += 1
        if keys[pygame.K_LEFT]:
        	rock_pos_x -= 1
        if keys[pygame.K_RIGHT]:
        	rock_pos_x += 1

        # Redibujamos todos los elementos de la pantalla
        screen.blit(fondo, (0, 0))
        screen.blit(rock, (rock_pos_x, rock_pos_y))
        # se muestran lo cambios en pantalla
        pygame.display.flip()

        # Posibles entradas del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        textsurface = myfont.render('Some Text', False, (0, 0, 0))
        screen.blit(textsurface,(0,0))

if __name__ == "__main__":
    main()