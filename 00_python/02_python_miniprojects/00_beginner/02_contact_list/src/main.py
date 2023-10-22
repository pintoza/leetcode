from PyQt5.QtWidgets import QApplication
from src.ui.contact_window import ContactWindow
import sys

app = QApplication(sys.argv)
window = ContactWindow()
window.show()
sys.exit(app.exec_())
