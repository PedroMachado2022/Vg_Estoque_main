import sys

from PyQt5.QtWidgets import QDialog, QApplication
from modules.TelaDeLogin import Login

app = QApplication(sys.argv)
if QDialog.Accepted:
	window = Login()
	window.show()

sys.exit(app.exec_())