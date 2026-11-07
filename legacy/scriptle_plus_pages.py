from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QComboBox, QHBoxLayout, QCheckBox
from PyQt6.QtCore import Qt, QTimer, QSize
from scriptle_plus_functions import *


class MainMenuPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        checkbox_layout = QHBoxLayout()
        layout.setContentsMargins(0, 10, 0, 10)
        self.title_label = QLabel()
        self.title_label.setText(
            "<div style='text-align: center;'>"
            "<span style='font-size: 40px; font-family: \"Garamond\"'>Fern's</span><br>"
            "<span style='font-size: 60px; font-family: \"Garamond\"'>Scripture Guessing Game</span>"
            "</div>"
        )
        self.title_label.setTextFormat(Qt.TextFormat.RichText)

        self.bom_checkbox = QCheckBox('Book of Mormon')
        self.ot_checkbox = QCheckBox('Old Testament')
        self.nt_checkbox = QCheckBox('New Testament')
        


        self.play_button = QPushButton("Play Game")
        self.high_scores_button = QPushButton('View High Scores')
        layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.bom_checkbox)
        layout.addWidget(self.ot_checkbox)
        layout.addWidget(self.nt_checkbox)
        layout.addWidget(self.play_button)
        layout.addWidget(self.high_scores_button)
        self.setLayout(layout)

class GamePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        layout = QVBoxLayout()
        self.title_label = QLabel('Guess the Scripture')
        self.title_label.setStyleSheet("font-size: 30px;")
        
        # Initialize where the random scripture text and answer go
        self.scripture_label = QLabel('scripture goes here')
        self.scripture_label.setStyleSheet("font-size: 18px;")
        self.scripture_label.setWordWrap(True)
        self.scripture_label.setMinimumWidth(700)
        self.answer_label = QLabel('answer goes here')
        self.answer_label.setStyleSheet("font-size: 25px;")

        # Set up teleport buttons and answer inputs
        self.menu_return_button = QPushButton('Return to Menu')
        self.submit_button = QPushButton('Submit')
        self.answer_box = QComboBox()
        self.score_label = QLabel('')
        
        # Make it all appear
        layout.setSpacing(5)
        layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        scripture_area = QVBoxLayout()
        scripture_area.addWidget(self.scripture_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(scripture_area)
        layout.addWidget(self.answer_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.score_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.answer_box)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.menu_return_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.submit_answer)

    def showEvent(self, event):
        super().showEvent(event)
        self.update_answer_box()
        self.total_answered = 0
        self.total_correct = 0
        self.score_label.setText('')
        self.random_scripture = get_scripture(self.main_window.selected_scriptures)
        self.scripture_label.setText(self.random_scripture['scripture_text'])
        self.answer_label.setText('')

    def submit_answer(self):
        self.total_answered += 1
        if self.answer_box.currentText() == self.random_scripture['book_title']:
            self.total_correct += 1
        self.score_label.setText(f'{self.total_correct} / {self.total_answered}')
        self.answer_label.setText(self.random_scripture['verse_title'])
        QTimer.singleShot(2000, self.load_next_scripture)

    def load_next_scripture(self):
        self.random_scripture = get_scripture(self.main_window.selected_scriptures)
        self.scripture_label.setText(self.random_scripture['scripture_text'])
        # self.scripture_label.setLineWidth(500)
        self.answer_label.setText('')
    
    def update_answer_box(self):
        self.answer_box.clear()
        for item in self.main_window.book:
            match item:
                case 'Book of Mormon':
                    self.answer_box.addItems(['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni'])
                case 'New Testament':
                    self.answer_box.addItems(['Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colassions', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation'])
                case 'Old Testament':
                    self.answer_box.addItems(['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zecharaiah', 'Malachi'])

        

class HighScoresPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.high_scores_label = QLabel('Nothing here yet, sorry')
        self.menu_return_button = QPushButton('Return to Menu')
        layout.addWidget(self.high_scores_label)
        layout.addWidget(self.menu_return_button)
        self.setLayout(layout)
