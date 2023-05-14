from PyQt5.QtWidgets import *
from template.principal import Ui_MainWindow
from modules.TelaDeRegistro import Tela_De_Registro
from PyQt5.QtCore import QRect, QPropertyAnimation, QSize, QEasingCurve
from db.query import DataBase
import datetime
import random
import locale

class Tela_Principal(QMainWindow):
    def __init__(self, *args, **argvs):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        super(Tela_Principal, self).__init__(*args, **argvs)
        self.center_window()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tela Principal")

        #---------------ORGANIZAÇAO INICIAL--------------
        self.ui.frame.setGeometry(-10,-20,0,0)
        self.ui.historico.setGeometry(20, 90, 880, 500)
        self.ui.estoque.setGeometry(30, 120, 921, 571)
        self.ui.avender.setGeometry(20, 150, 950, 550)
        self.ui.historico.hide()

        self.ui.avender.show()



        self.ui.estoque.hide()
        self.ui.frame_2.hide()
        self.ui.doubleSpinBox.hide()
        self.ui.pushButton_13.hide()

        # -----------------------------------------------

        # --------------- BOTOES MENU------------------
        self.ui.pushButton_12.clicked.connect(self.tela_main)
        self.ui.pushButton_11.clicked.connect(self.tela_historic)
        self.ui.pushButton_10.clicked.connect(self.tela_stock)
        self.ui.pushButton_14.clicked.connect(self.adc_estoque)


        # ----------BOTOES TELA INICIAL-------------------
        self.ui.pushButton_4.clicked.connect(self.cancelar)
        self.ui.pushButton.clicked.connect(self.procurar)
        self.ui.pushButton_2.clicked.connect(self.confirmar)
        # -----------------------------------------

        #-----------BOTOES TELA DE CONFIRMAR---------
        self.ui.pushButton_17.clicked.connect(self.voltar)
        self.ui.pushButton_5.clicked.connect(self.compra_cartao)
        self.ui.pushButton_3.clicked.connect(self.compra_cash)
        self.ui.pushButton_13.clicked.connect(self.ger_troco)
        self.ui.pushButton_16.clicked.connect(self.cabo_poha)
        # ---------------------------------------------
        # -----------VARIAVEIS TELA ESTOQUE----------------
        self.ui.atualizar.clicked.connect(self.att_estoque)
        self.ui.pushButton_6.clicked.connect(self.adc_estoque)
        self.ui.remover.clicked.connect(self.remove_estoque)
        self.ui.remover_2.clicked.connect(self.carregar_dados_estoque)
        # ---------------------------------------------

        # -----------TELA HISTORICO--------------------
        self.ui.label_18.setText('0')
        self.ui.label_19.setText('0')
        self.ui.pushButton_7.clicked.connect(self.buscar_data)
        self.mes = datetime.date.today().month
        self.ano = datetime.date.today().year
        # ---------------------------------------------

        #-----------variaveis pro codigo-------
        self.page = 1
        self.total = 0
        self.linha = 0
        self.lista_de_baixa = [] #produtos na tela
        # -----------------------------------------

        #-------------ANIMAÇAO SOON----------------
        self.ui.fecharmenu.clicked.connect(self.fechar)
        self.ui.showmenu.clicked.connect(self.abrir)
        # -----------------------------------------
#---------- FUNÇAO BASICA TELA ---------

    #def closeEvent(self, event):
        #reply = QMessageBox.question(self, 'Alerta!',
                                     #"Tem certeza que deseja sair?", QMessageBox.Yes |
                                     #QMessageBox.No)
        #if reply == QMessageBox.Yes:
            #QApplication.quit()
        #else:
            #pass

#-------------------------------------
# -----------FUNÇOES MENU-------------

    def center_window(self):
        # Create a QDesktopWidget instance
        desktop = QApplication.desktop()

        # Get the screen geometry
        screen_rect = desktop.screenGeometry()

        # Get the window geometry
        window_rect = self.geometry()

        # Calculate the center position for the window
        x = screen_rect.width() // 2 - window_rect.width() // 2
        y = screen_rect.height() // 2 - window_rect.height() // 2

        # Set the window position
        self.move(x, y)

    def adicionar(self):
        add = Tela_De_Registro()
        add.exec_()

    def tela_main(self):
        self.sis_fechar()
        self.page = 1
        self.ui.avender.show()

    def tela_stock(self):
        self.sis_fechar()
        self.page = 2
        self.carregar_dados_estoque()
        self.ui.estoque.show()

    def tela_historic(self):
        self.sis_fechar()
        self.ui.historico.show()
        self.inicializar()
        self.page = 3

    def sis_fechar(self):
        if self.page == 1:
            self.ui.avender.hide()
        if self.page == 2:
            self.ui.estoque.hide()
        if self.page == 3:
            self.ui.historico.hide()


#---------------ANIMAÇAO-------------------

    def fechar(self):
        self.anim_2 = QPropertyAnimation(self.ui.frame, b"size")
        self.anim_2.setEndValue(QSize(0, 0))
        self.anim_2.setDuration(500)
        self.anim_2.setEasingCurve(QEasingCurve.OutQuart)
        self.anim_2.start()
        self.animation = QPropertyAnimation(self.ui.pushButton_12, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEndValue(QRect(-40, -200, 121, 41))
        self.animation.setEasingCurve(QEasingCurve.OutQuart)
        self.animation.start()
        self.animation2 = QPropertyAnimation(self.ui.pushButton_11, b"geometry")
        self.animation2.setDuration(500)
        self.animation2.setEndValue(QRect(-40, -100, 121, 41))
        self.animation2.setEasingCurve(QEasingCurve.OutQuart)
        self.animation2.start()
        self.animation3 = QPropertyAnimation(self.ui.pushButton_10, b"geometry")
        self.animation3.setDuration(500)
        self.animation3.setEndValue(QRect(-40, -50, 121, 41))
        self.animation3.setEasingCurve(QEasingCurve.OutQuart)
        self.animation3.start()
        self.animation4 = QPropertyAnimation(self.ui.pushButton_14, b"geometry")
        self.animation4.setDuration(500)
        self.animation4.setEndValue(QRect(-40, -150, 121, 41))
        self.animation4.setEasingCurve(QEasingCurve.OutQuart)
        self.animation4.start()


    def abrir(self):
        self.anim_2 = QPropertyAnimation(self.ui.frame, b"size")
        self.anim_2.setEndValue(QSize(91, 351))
        self.anim_2.setDuration(500)
        self.anim_2.setEasingCurve(QEasingCurve.OutQuart)
        self.anim_2.start()
        self.animation = QPropertyAnimation(self.ui.pushButton_12, b"geometry")
        self.animation.setDuration(250)
        self.animation.setEndValue(QRect(-20, 100, 121, 41))
        self.animation.start()
        self.animation2 = QPropertyAnimation(self.ui.pushButton_11, b"geometry")
        self.animation2.setDuration(500)
        self.animation2.setEndValue(QRect(-20, 215, 121, 41))
        self.animation2.setEasingCurve(QEasingCurve.OutQuart)
        self.animation2.start()
        self.animation3 = QPropertyAnimation(self.ui.pushButton_10, b"geometry")
        self.animation3.setDuration(500)
        self.animation3.setEndValue(QRect(-20, 268, 121, 51))
        self.animation3.setEasingCurve(QEasingCurve.OutQuart)
        self.animation3.start()
        self.animation4 = QPropertyAnimation(self.ui.pushButton_14, b"geometry")
        self.animation4.setDuration(500)
        self.animation4.setEndValue(QRect(-17, 150, 121, 51))
        self.animation4.setEasingCurve(QEasingCurve.OutQuart)
        self.animation4.start()

# ------------SISTEMA DE TELA PRINCIPAL--------------
    def procurar(self):
        db = DataBase("./db/fun.db")
        codigo_sele = self.ui.lineEdit_2.text()
        if codigo_sele != '' and codigo_sele.isdigit():
            lista = db.pega_dados(f"SELECT codigo, descricao, preco, quantidade FROM Produtos WHERE codigo = {codigo_sele} AND quantidade > 0")

            self.ui.lineEdit_2.setText('')
            # ---------------- !!!!EVENTO ITEM NAO ACHADO ou sem unidade -----------------
            if lista:
                # separar o que vai pra lista principal
                codi, desc, preco, quant = lista[0]
                self.lista_de_baixa.append([codi, quant]) #add lista de baixa
                self.att_tabela(codi, -1)

                if int(quant) > 0:
                    #---adcionar tabela principal
                    self.ui.tableWidget.insertRow(self.linha)                               #INSERIR LINHA
                    self.total += float(preco)                                                         # ADICIONAR NO FINAL
                    self.ui.tableWidget.setItem(self.linha, 0, QTableWidgetItem(str(codi)))    #SET ITEM
                    self.ui.tableWidget.setItem(self.linha, 1, QTableWidgetItem(str(desc)))
                    self.ui.tableWidget.setItem(self.linha, 2, QTableWidgetItem(str(preco)))#SET ITEM PRECO

                    self.linha += 1                                                         #TER LINHA BASE
                    self.ui.lcdNumber.display(self.total)                                   #LCD
            elif not lista:
                QMessageBox.information(QMessageBox(), "ERRO", "PRODUTO NÃO ENCONTRADO OU SEM ESTOQUE")
        else:
            pass

    def cancelar(self):
        self.linha = 0
        self.total = 0
        self.ui.tableWidget.setRowCount(0)
        self.ui.lcdNumber.display(self.total)
        #voltar com itens na tabela
        for dados in self.lista_de_baixa:
            self.att_tabela(dados[0], 1)
        self.lista_de_baixa=[]

    def att_tabela(self, cod, quant):
        db = DataBase("./db/fun.db")
        db.in_rm_att(f"UPDATE  Produtos  SET quantidade  = quantidade + {quant} WHERE codigo LIKE {cod}")
        db.total(f"UPDATE Produtos SET total = preco * quantidade WHERE codigo = {cod}")

    def confirmar(self):
        if self.lista_de_baixa:
            self.ui.frame_2.show()
            self.ui.pushButton.hide()
            self.ui.lineEdit_2.hide()
            self.ui.label_3.hide()

# ----------------TELA MENU CONFIRMA COMPRA---------------------
    def compra_cash(self):
        self.ui.pushButton_3.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_13.show()
        self.ui.doubleSpinBox.show()
        self.ui.doubleSpinBox.setValue(0.0)
        self.ui.pushButton_16.setEnabled(False)

    def compra_cartao(self):
        self.ui.pushButton_16.setEnabled(True)
        self.ui.pushButton_3.hide()
        self.ui.pushButton_5.hide()
        self.ui.troco.setText("Se vendido, confirme")

    def ger_troco(self):
        # Formate o valor como um valor monetário em reais

        valor = self.ui.doubleSpinBox.value()
        troco = valor - self.total
        valor_formatado = locale.currency(troco, grouping=True, symbol='R$')
        if troco >= 0:
            self.ui.troco.setText(f"{valor_formatado}")
            self.ui.pushButton_13.hide()
            self.ui.pushButton_16.setEnabled(True)
        else:
            self.ui.pushButton_13.hide()
            self.ui.troco.setText(f"valor insuficiente:{troco*-1}:.2f")

    def cabo_poha(self):
        db = DataBase("./db/fun.db")
        dia = datetime.datetime.now().date()

        if self.lista_de_baixa:
            for d in self.lista_de_baixa:
                lista = db.pega_dados(
                    f"SELECT  descricao, preco FROM Produtos WHERE codigo = {d[0]}")
                db.in_rm_att(
                    f"INSERT INTO Historico ( descricao, preco, data) VALUES ('{lista[0][0]}', '{lista[0][1]}', '{dia}')")
        self.lista_de_baixa = []
        self.voltar()
        self.linha = 0
        self.total = 0
        self.ui.pushButton_3.show()
        self.ui.pushButton_5.show()
        self.ui.troco.setText("")
        self.ui.tableWidget.setRowCount(0)
        self.ui.lcdNumber.display(self.total)
        self.ui.frame_2.hide()
        self.ui.pushButton.show()
        self.ui.lineEdit_2.show()
        self.ui.label_3.show()

    def voltar(self):
        self.cancelar()
        self.ui.pushButton_3.show()
        self.ui.pushButton_5.show()
        self.ui.pushButton_13.hide()
        self.ui.frame_2.hide()
        self.ui.troco.setText('')
        self.ui.pushButton.show()
        self.ui.lineEdit_2.show()
        self.ui.label_3.show()
        self.ui.doubleSpinBox.hide()
        self.ui.pushButton_16.setEnabled(False)
        self.tela_main()

# --------------------------------------------

# ------------FUNÇOES FRAME ESTOQUE-----------

    def carregar_dados_estoque(self):
        db = DataBase("./db/fun.db")
        lista = db.pega_dados("SELECT descricao, codigo, tamanho, preco, quantidade, total FROM Produtos")
        lista2 = db.pega_dados("SELECT SUM(total) FROM Produtos")
        # Defina o locale para o Brasil


        # Supondo que `lista2[0][0]` seja um valor numérico
        valor = lista2[0][0]

        # Formate o valor como um valor monetário em reais
        valor_formatado = locale.currency(valor, grouping=True, symbol='R$')

        # Defina o valor formatado no texto do QLabel
        self.ui.label_7.setText(valor_formatado)
        self.ui.tableWidget_2.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.tableWidget_2.insertRow(linha)
            for coluna_n, dados in enumerate(dados):
                self.ui.tableWidget_2.setItem(linha, coluna_n, QTableWidgetItem(str(dados)))

    def remove_estoque(self):
        add = Tela_De_Registro()
        add.tela_remo()
        add.exec_()

    def att_estoque(self):
        add = Tela_De_Registro()
        add.tela_att()
        add.exec_()

    def adc_estoque(self):
        add = Tela_De_Registro()
        add.exec_()


# --------------------------------------------

# -----------FUNÇOES FRAME HISTORICO----------
    def carrega_dados(self):
        db = DataBase("./db/fun.db")
        self.ui.tableWidget_3.setRowCount(0)
        #lista = db.pega_dados(f"SELECT  descricao,  preco, data FROM Historico")
        if self.mes < 10:
            self.mes = '0'+str(self.mes)
        if self.mes != '00':
            l = db.pega_dados(f"SELECT descricao, preco, data FROM Historico WHERE strftime('%m-%Y', data) = '{str(self.mes)}-{str(self.ano)}';")
        else:
            l = db.pega_dados(f"SELECT  descricao,  preco, data FROM Historico")
        if l:
            soma = sum(item[1] for item in l)
            valor_formatado = locale.currency(soma, grouping=True, symbol='R$')
            self.ui.label_19.setText(f"{valor_formatado}")
            self.ui.label_18.setText(str(len(l)))
            self.ui.tableWidget_3.setRowCount(0)
            for linha, dados in enumerate(l):
                self.ui.tableWidget_3.insertRow(linha)
                for coluna_n, dados in enumerate(dados):
                    self.ui.tableWidget_3.setItem(linha, coluna_n, QTableWidgetItem(str(dados)))

    def buscar_data(self):
        self.mes = self.ui.comboBox.currentIndex()
        self.ano = self.ui.dateEdit.date().year()
        self.ui.tableWidget_3.setRowCount(0)
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
            db.in_rm_att(f"INSERT INTO Historico ( descricao, preco, data) VALUES ('banana', '{random.randint(20, 100)}', '{random_date}')")

    def limpar_cache(self):
        db = DataBase("./db/fun.db")
        ano = datetime.date.today().year - 1
        db.in_rm_att(f"DELETE FROM Historico WHERE data < '{str(ano)}-01-01';")