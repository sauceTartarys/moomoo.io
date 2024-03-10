import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QDialog, QFormLayout, QLineEdit
from PyQt5.QtCore import QTimer
import random

class StartMenu(QDialog):
    def init(self):
        super().init()

        self.player_name = ""

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Start Menu')

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.name_label = QLabel('Enter your name:')
        self.name_edit = QLineEdit()

        self.play_button = QPushButton('Play')
        self.play_button.clicked.connect(self.start_game)

    def create_layout(self):
        layout = QFormLayout()
        layout.addRow(self.name_label, self.name_edit)
        layout.addRow(self.play_button)

        self.setLayout(layout)

    def start_game(self):
        self.player_name = self.name_edit.text()
        self.accept()


class MinerGame(QWidget):
    def init(self, player_name):
        super().init()

        self.ore = 0
        self.coins = 0
        self.upgrades = 1
        self.player_position = 0
        self.player_name = player_name

        self.bot_coins = 100
        self.bot_items = {'Pickaxe': 20, 'Axe': 15}

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(f'Miner Game - {self.player_name}')

        self.create_widgets()
        self.create_layout()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.bot_trade)
        self.timer.start(5000)

    def create_widgets(self):
        self.mine_button = QPushButton('Mine Ore', self)
        self.mine_button.clicked.connect(self.mine_ore)

        self.sell_button = QPushButton('Sell Ore', self)
        self.sell_button.clicked.connect(self.sell_ore)

        self.upgrade_button = QPushButton('Buy Upgrade', self)
        self.upgrade_button.clicked.connect(self.buy_upgrade)

        self.move_left_button = QPushButton('Move Left', self)
        self.move_left_button.clicked.connect(self.move_left)

        self.move_right_button = QPushButton('Move Right', self)
        self.move_right_button.clicked.connect(self.move_right)

        self.bot_trade_button = QPushButton('Bot Trade', self)
        self.bot_trade_button.clicked.connect(self.bot_trade)

        self.ore_label = QLabel()
        self.coins_label = QLabel()
        self.upgrades_label = QLabel()
        self.position_label = QLabel()

    def create_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.ore_label)
        layout.addWidget(self.coins_label)
        layout.addWidget(self.upgrades_label)
        layout.addWidget(self.position_label)
        layout.addWidget(self.mine_button)
        layout.addWidget(self.sell_button)
        layout.addWidget(self.upgrade_button)
        layout.addWidget(self.move_left_button)
        layout.addWidget(self.move_right_button)
        layout.addWidget(self.bot_trade_button)

        self.setLayout(layout)

    def mine_ore(self):
        mined_ore = random.randint(1, 5) * self.upgrades
        self.ore += mined_ore
        self.update_labels()

    def sell_ore(self):
        sell_price = 2
        total_coins = self.ore * sell_price
        self.coins += total_coins
        self.ore = 0
        self.update_labels()

    def buy_upgrade(self):
        upgrade_cost = 5 * self.upgrades
        if self.coins >= upgrade_cost:
            self.coins -= upgrade_cost
            self.upgrades += 1
            self.update_labels()

    def move_left(self):
        self.player_position -= 1
        self.update_labels()

    def move_right(self):
        self.player_position += 1
        self.update_labels()

    def bot_trade(self):
        for item, price in self.bot_items.items():
            if self.coins >= price:
                self.coins -= price
                self.bot_coins += price
                print(f"Bought {item} for {price} coins from the bot.")
                break

        self.update_labels()
def update_labels(self):
        self.ore_label.setText(f'Total Ore: {self.ore}')
        self.coins_label.setText(f'Total Coins: {self.coins}')
        self.upgrades_label.setText(f'Total Upgrades: {self.upgrades}')
        self.position_label.setText(f'Player Position: {self.player_position}')


if __name__ == 'main':
    app = QApplication(sys.argv)

    start_menu = StartMenu()
    if start_menu.exec_() == QDialog.Accepted:
        player_name = start_menu.player_name
        game = MinerGame(player_name)

    sys.exit(app.exec_())