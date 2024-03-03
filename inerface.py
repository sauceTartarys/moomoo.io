from PyQt5.QtWidgets import *
import random


app = QApplication([])
window = QWidget()
window.resize(500, 400)
background_image = ("moomoo-io-1280x720.jpg")
background_label = QLabel()
background_label.setStyleSheet(background_image)


app = QApplication([])

app.setStyleSheet('''
           MainWindow {
               background-color: transparent;
           }
           QLabel {
               background: transparent;
           }
       ''')


window.resize(400, 300)

mainline = QVBoxLayout()

menubut = QPushButton('меню')
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



ansbut = QPushButton('скіни')
mainline.addWidget(ansbut)



result = QLabel('Результат :')

result.hide()

ansbut = QPushButton('скіни')
mainline.addWidget(ansbut)


mainline.addWidget(redaguvaty)


window.setLayout(mainline)
window.show()
app.exec()