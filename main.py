import pygame
from PyQt5.QtWidgets import *
import player
import struktur
import struktur2


def game():

    pygame.init()
    font = pygame.font.Font(None, 36)
    window = pygame.display.set_mode((800,500))
    fps = pygame.time.Clock()


    fone = pygame.image.load("depositphotos_206763476-stock-photo-green-grass-texture-background.webp")

    fone = pygame.transform.scale(fone,(800,500))
    score = 0
    stone_score=0
    heroplayer = player.stive(350,50, 100,100, 1, "1711834846381152.png")
    asp = struktur.stoneblock(350,350,150,150, "171183458479330.png")
    asp2 = struktur2.stoneblock2(50,150,150,150, "1711834438564893.png")
    game = True



    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if heroplayer.hit_box.colliderect(asp.hit_box):
                    stone_score+=1
                if heroplayer.hit_box.colliderect(asp2.hit_box):
                    score+=1


        heroplayer.muve()

        text = font.render("Камінь:" + str(stone_score), True, (155,155,155))
        text1 = font.render("Дерево:" + str(score), True, (155, 199, 155))




        window.fill((123,123,123))

        window.blit(fone,(0,0))
        heroplayer.render(window)
        window.blit(text, (10, 10))
        window.blit(text1, (10,40))
        asp.render(window)
        asp2.render(window)
        pygame.display.flip()
        fps.tick()