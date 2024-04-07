import pygame
import PyQt5.QtWidgets

class stive:
    def __init__(self, x, y, w, h, speed, texture):
        self.speed = speed
        self.texture = pygame.image.load(texture)


        self.texture = pygame.transform.scale(self.texture, (w, h))
        self.hit_box = self.texture.get_rect()
        self.hit_box.x = x
        self.hit_box.y = y
        self.sound_step = pygame.mixer.Sound("zvuk_-_shagov.mp3")
        self.sound_step.play(-1)
        self.sound_step.set_volume(0)


    def render(self, window):

        window.blit(self.texture, (self.hit_box.x, self.hit_box.y))


    def muve(self):
        keys = pygame.key.get_pressed()
        is_step = False
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
            is_step = True
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
            is_step = True
        if keys[pygame.K_w]:
            self.hit_box.y -= self.speed
            is_step = True
        if keys[pygame.K_s]:
            self.hit_box.y += self.speed
            is_step = True

        if is_step == True:
            self.sound_step.set_volume(0.5)
        else:
            self.sound_step.set_volume(0)
