import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MoomooIOGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Moomoo.io")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_title = QLabel("Welcome to Moomoo.io", self)
        self.label_title.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(self.label_title)

        self.button_start = QPushButton("Start Game", self)
        self.button_start.clicked.connect(self.start_game)
        self.layout.addWidget(self.button_start)

        self.button_options = QPushButton("Options", self)
        self.button_options.clicked.connect(self.open_options)
        self.layout.addWidget(self.button_options)

        self.button_exit = QPushButton("Exit", self)
        self.button_exit.clicked.connect(self.close)
        self.layout.addWidget(self.button_exit)

    def start_game(self):
        # Додайте код для початку гри
        print("Starting the game...")

    def open_options(self):
        # Додайте код для відкриття вікна опцій
        print("Opening options...")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_window = MoomooIOGame()
    game_window.show()
    sys.exit(app.exec_())