from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton
from src.db.db_operations import add_contact


class ContactWindow(QWidget):
    def __init__(self):
        super(ContactWindow, self).__init__()

        layout = QVBoxLayout()

        self.nameInput = QLineEdit(self)
        self.nameInput.setPlaceholderText("Name")
        layout.addWidget(self.nameInput)

        self.phoneInput = QLineEdit(self)
        self.phoneInput.setPlaceholderText("Phone")
        layout.addWidget(self.phoneInput)

        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.add_new_contact)
        layout.addWidget(self.addButton)

        self.setLayout(layout)

    def add_new_contact(self):
        name = self.nameInput.text()
        phone = self.phoneInput.text()
        add_contact(name, phone)
