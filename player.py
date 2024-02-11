import pygame
import PyQt5.QtWidgets

class Player():
    def __init__(self, x, y, w, h, speed, texture, color, parent=None, ):
        super().__init__(parent)
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.setRect(50, 50, w, h)
        self.setPos(x, y)
        self.setBrush(color("blue"))
        self.direction = {"up": False, "down": False, "left": False, "right": False}
        self.speed = 5