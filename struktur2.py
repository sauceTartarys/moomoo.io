import PyQt5.QtWidgets
import pygame

class stoneblock2:
    def __init__(self, x, y, w, h, texture):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y


    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))
