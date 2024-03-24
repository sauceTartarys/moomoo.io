import pygame
import player
import struktur
import struktur2


def game():
    pygame.init()

    font = pygame.font.Font(None, 36)
    window = pygame.display.set_mode((800,500))
    fps = pygame.time.Clock()


    fone = pygame.image.load("moomoo-io-1280x720.jpg")

    fone = pygame.transform.scale(fone,(800,500))
    score = 0
    heroplayer = player.stive(350,50, 100,100, 1, "yUrxd7Uv_400x400.jpg")
    asp = struktur.stoneblock(350,350,150,150, "488-4884792_moomoo-io-wiki-moomoo-io-wiki-sapling-hd.png")
    asp2 = struktur2.stoneblock2(50,150,150,150, "560-5606073_moomoo-io-wiki-wood-hd-png-download.png")
    game = True


    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()

        heroplayer.muve()

        text = font.render("рахунок:" + str(score), True, (155,155,155))



        window.fill((123,123,123))

        window.blit(fone,(0,0))
        heroplayer.render(window)
        window.blit(text, (10, 10))
        asp.render(window)
        asp2.render(window)
        pygame.display.flip()
        fps.tick()