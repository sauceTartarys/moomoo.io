import sys
import pygame
from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor


class Player(QGraphicsRectItem):
    def __init__(self, x, y, w, h, speed, texture, parent=None, ):
        super().__init__(parent)
        self.speed = speed
        self.texture = pygame.image.load(texture)
        self.setRect(50, 50, w, h)
        self.setPos(x, y)
        self.setBrush(QColor("blue"))
        self.direction = {"up": False, "down": False, "left": False, "right": False}
        self.speed = 5

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


class Game(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Game")
        self.setSceneRect(0, 0, 800, 600)

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.player = Player(0, 0, 30, 30)
        self.scene.addItem(self.player)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 // 60)

    def update(self):
        self.player.move()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = Game()
    game.show()
    sys.exit(app.exec_())