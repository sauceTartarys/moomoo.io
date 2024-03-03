import sys
import player
import pygame
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt



cyb = player.Player(100,100, 50,50, 1, "yUrxd7Uv_400x400.jpg", "brown")


def move(self):
    if self.direction["up"]:
        self.moveBy(0, -self.speed)
    if self.direction["down"]:
        self.moveBy(0, self.speed)
    if self.direction["left"]:
        self.moveBy(-self.speed, 0)
    if self.direction["right"]:
            self.moveBy(self.speed, 0)

def keyPressEvent(self, event):
    if event.key() == Qt.K_W:
        self.direction["up"] = True
    elif event.key() == Qt.K_S:
        self.direction["down"] = True
    elif event.key() == Qt.K_A:
        self.direction["left"] = True
    elif event.key() == Qt.K_D:
        self.direction["right"] = True

def keyReleaseEvent(self, event):
    if event.key() == Qt.K_W:
        self.direction["up"] = False
    elif event.key() == Qt.K_S:
        self.direction["down"] = False
    elif event.key() == Qt.K_A:
        self.direction["left"] = False
    elif event.key() == Qt.K_D:
        self.direction["right"] = False



    def update(self):
        self.player.move()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec_())