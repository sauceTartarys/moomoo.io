from PyQt5.QtWidgets import *
import random

from main import game
from merega import profile
from settings import nastrigs

app = QApplication([])
window = QWidget()

window.resize(700, 500)



app.setStyleSheet("""
 QPushButton{
    background-image: none;
    color: crimson;
    background:qlineargradient(x1; 0, y1; 0, x2; 1, y2; 1, stop: 0,1 gold, stop: 0.4 lime,stop: 1 blue);
    font: bold 2.2em system-ui;
    border: 2px solid red;
    border-radius: 9.5px;
    } 
""")

mainline = QVBoxLayout()

menubut = QPushButton('Іграти')
restbtn = QPushButton('настройки')

redaguvaty = QPushButton('соцмережі розраба')
herfg = QLineEdit()
herfg.setPlaceholderText("ведіть нік")



firstline = QHBoxLayout()
haifline = QVBoxLayout()

mainline.addStretch(1)

mainline.addWidget(menubut)
mainline.addWidget(herfg)
mainline.addWidget(restbtn)


mainline.addStretch(1)

ansbut = QPushButton('скіни')
mainline.addWidget(ansbut)



mainline.addWidget(redaguvaty)

menubut.clicked.connect(game)
window.setLayout(mainline)
redaguvaty.clicked.connect(profile)
restbtn.clicked.connect(nastrigs)
window.show()
app.exec()