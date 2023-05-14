import sqlite3


class DataBase:

    def __init__(self, banco=None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)

    def open(self, banco):
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("A conexão falhou!")

    def criar_tabela(self):
        cur = self.cursor
        cur.execute(
            """CREATE TABLE Produtos (
                    id integer primary key autoincrement,
                    descricao text NOT NULL,
                    codigo integer UNIQUE ,
                    tamanho text NOT NULL,
                    preco double NOT NULL,
                    quantidade integer,
                    total double
                    );"""
        )

    def criar_tabela_vendidos(self):
        cur = self.cursor
        cur.execute(
            """CREATE TABLE Historico (
            id integer primary key autoincrement,
            descricao text NOT NULL,
            preco double NOT NULL,
            data date
            );"""
        )

    def in_rm_att(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def pega_dados(self, query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()

    def total(self, query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()


#db = DataBase("./db/fun.db")

# db.in_rm_att(f"UPDATE Produtos SETT descricao = '{}' WHERE descricao = '{}'")
# db.pega_dados("SELECT * FROM Produtos")


#db.criar_tabela()
#db.criar_tabela_vendidos()
