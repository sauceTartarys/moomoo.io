import pygame
import PyQt5.QtWidgets

class Player():
    def __init__(self, x, y, w, h, speed, texture, color, ):
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.direction = {"up": False, "down": False, "left": False, "right": False}
        self.speed = 5
    def render(self, window):
        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))

