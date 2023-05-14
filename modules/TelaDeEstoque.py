from PyQt5.QtWidgets import *
from template.estoque import Ui_estoque
from modules.TelaDeRegistro import Tela_De_Registro
from PyQt5 import QtCore
from db.query import DataBase


class Tela_Estoque(QDialog):
    def __init__(self, *args, **argvs):
        super(Tela_Estoque, self).__init__(*args, **argvs)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_estoque()
        self.ui.setupUi(self)
        self.setWindowTitle("Estoque")
        self.ui.voltar.clicked.connect(self.Voltar)
        self.ui.atualizar.clicked.connect(self.att_estoque)
        self.ui.pushButton_2.clicked.connect(self.adicionar)
        self.ui.remover.clicked.connect(self.remove_estoque)
        self.ui.pushButton_3.clicked.connect(self.sair)
        self.ui.pushButton_5.clicked.connect(self.minimizar)
        self.ui.remover_2.clicked.connect(self.carrega_dados)

    def sair(self):
        self.close()

    def minimizar(self):
        self.showMinimized()

    def Voltar(self):

        self.window().close()

    def carrega_dados(self):
        db = DataBase("./db/fun.db")
        lista = db.pega_dados("SELECT descricao, codigo, tamanho, preco, quantidade, total FROM Produtos")
        lista2 = db.pega_dados("SELECT SUM(total) FROM Produtos")
        self.ui.lcdNumber_2.display(lista2[0][0])
        self.ui.tableWidget.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha, coluna_n, QTableWidgetItem(str(dados)))


    def adicionar(self):
        add = Tela_De_Registro()
        add.exec_()

    def remove_estoque(self):
        add = Tela_De_Registro()
        add.tela_remo()
        add.exec_()

    def att_estoque(self):
        add = Tela_De_Registro()
        add.tela_att()
        add.exec_()


