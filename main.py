import pygame
import player
import struktur


def game():
    pygame.init()


    window = pygame.display.set_mode((800,500))
    fps = pygame.time.Clock()

    fone = pygame.image.load("moomoo-io-1280x720.jpg")

    fone = pygame.transform.scale(fone,(800,500))

    heroplayer = player.stive(50,50, 50,50, 0.5, ("yUrxd7Uv_400x400.jpg"))
    amps = struktur.stoneblock(100,100,50,50,())

    game = True


    while game:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        heroplayer.muve()


        window.fill((123,123,123))
        window.blit(fone,(0,0))
        heroplayer.render(window)
        pygame.display.flip()
        fps.tick()