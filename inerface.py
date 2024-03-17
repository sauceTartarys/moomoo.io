
from PyQt5.QtWidgets import *
import random

from main import game

app = QApplication([])
window = QWidget()
window.resize(700, 500)

mainline = QVBoxLayout()

menubut = QPushButton('Іграти')
restbtn = QPushButton('настройки')
timlb = QLabel('ведіть нік')
redaguvaty = QPushButton('соцмережі розраба')

firstline = QHBoxLayout()
haifline = QVBoxLayout()
firstline.addWidget(menubut)
haifline.addWidget(restbtn)

firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timlb)
mainline.addLayout(firstline)

class cordint():
    def herf(self):
        self.menubut.setGeometry((440, 80, 75, 23))



ansbut = QPushButton('скіни')
mainline.addWidget(ansbut)


mainline.addWidget(redaguvaty)

menubut.clicked.connect(game)
window.setLayout(mainline)
window.show()
app.exec()