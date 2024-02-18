from PyQt5.QtWidgets import *
import random


app = QApplication([])
window = QWidget()
window.resize(400, 300)



mainline = QVBoxLayout()

menubut = QPushButton('меню')
restbtn = QPushButton('настройки')
timlb = QLabel('ведіть нік')
redaguvaty = QPushButton('соцмережі розраба')

firstline = QHBoxLayout()
firstline.addWidget(menubut)
firstline.addWidget(restbtn)
firstline.addWidget(timlb)
mainline.addLayout(firstline)




result = QLabel('Результат :')

result.hide()

ansbut = QPushButton('скіни')
nextque = QPushButton('наступне питання')
mainline.addWidget(ansbut)
mainline.addWidget(nextque)
nextque.hide()
mainline.addWidget(redaguvaty)


window.setLayout(mainline)
window.show()
app.exec()