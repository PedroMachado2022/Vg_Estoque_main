from PyQt5.QtWidgets import *
from template.historico import Ui_historico
import datetime
import random

from db.query import DataBase


class Tela_De_Historico(QDialog):
    def __init__(self, *args, **argvs):
        super(Tela_De_Historico, self).__init__(*args, **argvs)
        self.ui = Ui_historico()
        self.ui.setupUi(self)

        #mostrar tela
        self.ui.label_5.setText('0')
        self.ui.label_6.setText('0')
        self.ui.pushButton.clicked.connect(self.buscar_data)
        self.mes = datetime.date.today().month
        self.ano = datetime.date.today().year
        self.ui.pushButton_3.clicked.connect(self.close)

    def carrega_dados(self):
        db = DataBase("./db/fun.db")
        self.ui.tableWidget_2.setRowCount(0)
        #lista = db.pega_dados(f"SELECT  descricao,  preco, data FROM Historico")
        if self.mes < 10:
            self.mes = '0'+str(self.mes)
        print(self.mes)
        if self.mes != '00':
            l = db.pega_dados(f"SELECT descricao, preco, data FROM Historico WHERE strftime('%m-%Y', data) = '{str(self.mes)}-{str(self.ano)}';")
        else:
            l = db.pega_dados(f"SELECT  descricao,  preco, data FROM Historico")
        print(l)
        if l:
            soma = sum(item[1] for item in l)
            print(soma)
            self.ui.label_6.setText(str(soma))
            self.ui.label_5.setText(str(len(l)))
            self.ui.tableWidget_2.setRowCount(0)
            for linha, dados in enumerate(l):
                self.ui.tableWidget_2.insertRow(linha)
                for coluna_n, dados in enumerate(dados):
                    self.ui.tableWidget_2.setItem(linha, coluna_n, QTableWidgetItem(str(dados)))

    def buscar_data(self):
        self.mes = self.ui.comboBox.currentIndex()
        self.ano = self.ui.dateEdit.date().year()
        print(self.mes, self.ano)
        self.ui.tableWidget_2.setRowCount(0)
        self.carrega_dados()

    def inicializar(self):
        self.mes = datetime.date.today().month
        self.ano = datetime.date.today().year
        self.limpar_cache()
        self.carrega_dados()


    #----------apagarrrr--------
    def inserir_aleatorio(self):
        db = DataBase("./db/fun.db")
        start_date = datetime.date(2015, 1, 1)
        end_date = datetime.date(2023, 12, 31)

        for i in range(0, 10000):
            random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
            db.in_rm_att(f"INSERT INTO Historico ( descricao, preco, data) VALUES ('banana', '{random.randint(20, 100)}','{random_date}')")

    def limpar_cache(self):
        db = DataBase("./db/fun.db")
        ano = datetime.date.today().year - 1
        print(ano)
        db.in_rm_att(f"DELETE FROM Historico WHERE data < '{str(ano)}-01-01';")




