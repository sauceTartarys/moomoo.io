
from PyQt5.QtWidgets import *

def nastrigs():


    window = QDialog()

    mainline = QVBoxLayout()

    questbl = QLabel("Звук :")

    spnbox = QSpinBox()

    h1 = QHBoxLayout()
    h1.addWidget(questbl)
    h1.addWidget(spnbox)
    mainline.addLayout(h1)



    donebut = QPushButton('готово')
    mainline.addWidget(donebut)





    window.setLayout(mainline)

    window.show()
    window.exec()