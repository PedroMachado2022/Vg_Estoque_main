from PyQt5.QtWidgets import *
from template.registro import Ui_Registrar
from PyQt5 import QtCore
from db.query import DataBase


class Tela_De_Registro(QDialog):
    def __init__(self,*args, **argvs):
        super(Tela_De_Registro, self).__init__(*args, **argvs)
        self.ui = Ui_Registrar()
        self.ui.setupUi(self)
        self.setWindowTitle("Tela de registro")
        self.ui.sendbutton.clicked.connect(self.Adicionar)
        self.ui.backbutton.clicked.connect(self.Voltar)
        self.ui.sendbutton_3.clicked.connect(self.remover)
        self.ui.sendbutton_2.clicked.connect(self.att)

    def sair(self):
        self.close()

    def minimizar(self):
        self.showMinimized()

    def Adicionar(self):
        db = DataBase("./db/fun.db")
        d = self.ui.lineEdit.text()
        c = self.ui.lineEdit_2.text()
        t = self.ui.lineEdit_3.text()
        p = self.ui.lineEdit_4.text()
        q = self.ui.lineEdit_5.text()
        if d == '' or c == '' or t == '' or p == '' or q == '':
            QMessageBox.information(QMessageBox(), "INSERÇÃO INCORRETA", "Preencha todos os campos!")
        else:
            lista = db.pega_dados(
                f"SELECT codigo FROM Produtos WHERE codigo = {c}")
            if not lista:
                db.in_rm_att(
                    f"INSERT INTO Produtos (descricao, codigo, tamanho, preco, quantidade) VALUES ('{d}', '{c}','{t}', '{p}', '{q}')")
                db.total(f"UPDATE Produtos SET total = preco * quantidade WHERE codigo = {c}")
                self.ui.lineEdit.setText("")
                self.ui.lineEdit_2.setText("")
                self.ui.lineEdit_3.setText("")
                self.ui.lineEdit_4.setText("")
                self.ui.lineEdit_5.setText("")
            else:
                db.in_rm_att(f"UPDATE  Produtos  SET quantidade  = {q}, preco = {p} WHERE codigo LIKE {c}")
                self.ui.lineEdit.setText("")
                self.ui.lineEdit_2.setText("")
                self.ui.lineEdit_3.setText("")
                self.ui.lineEdit_4.setText("")
                self.ui.lineEdit_5.setText("")

    def remover(self):
        db = DataBase("./db/fun.db")
        codi = self.ui.lineEdit_9.text()
        if codi == '':
            pass
        else:
            lista = db.pega_dados(f"SELECT codigo FROM Produtos WHERE codigo = {codi}")
            if not lista:
                QMessageBox.information(QMessageBox(), "Nâo encontrado", "Dados Não existem!")
            else:
                db.in_rm_att(f"DELETE FROM  Produtos  WHERE codigo LIKE {codi}")
                QMessageBox.information(QMessageBox(), "Deletado", "Dado deletado com sucesso!")

    def att(self):
        db = DataBase("./db/fun.db")
        codi = self.ui.codi_at.text()
        quant = self.ui.quant_at.text()
        preco = self.ui.pre_at.text()
        if codi == '':
            pass
        else:
            lista = db.pega_dados(f"SELECT codigo FROM Produtos WHERE codigo = {codi}")
            if lista:
                if quant == '' and preco == '':
                    pass
                else:
                    if quant == '' and preco != '':
                        db.in_rm_att(f"UPDATE   Produtos SET preco = {preco}  WHERE codigo LIKE {codi}")
                        db.total(f"UPDATE Produtos SET total = preco * quantidade WHERE codigo = {codi}")

                    elif preco == '' and quant != '':
                        db.in_rm_att(f"UPDATE   Produtos SET quantidade = {quant} WHERE codigo LIKE {codi} ")
                        db.total(f"UPDATE Produtos SET total = preco * quantidade WHERE codigo = {codi}")

                    else:
                        db.in_rm_att(f"UPDATE  Produtos  SET quantidade  =  {quant}, preco = {preco} WHERE codigo LIKE {codi}")
                        db.total(f"UPDATE Produtos SET total = preco * quantidade WHERE codigo = {codi}")
                        QMessageBox.information(QMessageBox(), "ATUALIZADO", "Dados atualizados com sucesso!")



    def Voltar(self):
        self.window().close()


    # definir telas
    def tela_registro(self):
        self.ui.reg.show()
        self.ui.atua.hide()
        self.ui.remover.hide()

    def tela_att(self):
        self.ui.reg.hide()
        self.ui.atua.show()
        self.ui.remover.hide()

    def tela_remo(self):
        self.ui.reg.hide()
        self.ui.atua.hide()
        self.ui.remover.show()


