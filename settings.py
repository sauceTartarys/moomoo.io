import PyQt5.QtWidgets
import pygame


def nastrigs():
    pygame.init()

    window = pygame.display.set_mode((800, 500))
    fps = pygame.time.Clock()
    game = True



    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()



    window.fill((123,123,123))
    pygame.display.flip()
    fps.tick()