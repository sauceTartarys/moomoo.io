
from PyQt5.QtWidgets import *
import random

from main import game

app = QApplication([])
window = QWidget()

window.resize(700, 500)
window.resize(500, 400)




window.resize(400, 300)


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


ansbut = QPushButton('скіни')
mainline.addWidget(ansbut)


mainline.addWidget(redaguvaty)

menubut.clicked.connect(game)
window.setLayout(mainline)
window.show()
app.exec()