from template.login import Ui_Login
from modules.TelaPrincipal import Tela_Principal
from PyQt5.QtWidgets import *
from db.query import DataBase


class Login(QDialog):
    def __init__(self, *args, **argvs):
        super(Login, self).__init__(*args, **argvs)
        #self.window = None
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.pushButton_3.clicked.connect(self.sair)
        self.ui.pushButton_5.clicked.connect(self.minimizar)

    def sair(self):
        QApplication.quit()

    def minimizar(self):
        self.showMinimized()

    def login(self):
        db = DataBase("./db/fun.db")
        user = self.ui.lineEdit.text()
        pasd = self.ui.lineEdit_2.text()

        if user == '' or pasd == '':
            QMessageBox.information(QMessageBox(), "FALHA DE LOGIN", "Por favor, complete os campos!")
        else:
            dados = db.pega_dados(f"SELECT acesso FROM usuarios WHERE username = '{user}' and password = '{pasd}'")
            if dados:
                self.window = Tela_Principal()

                #self.window.setWindowFlags(Tela_Principal().windowFlags() | QtCore.Qt.FramelessWindowHint)

                self.window.show()

                self.close()
            else:
                QMessageBox.information(QMessageBox(), "Dados incorretos", "!!")
