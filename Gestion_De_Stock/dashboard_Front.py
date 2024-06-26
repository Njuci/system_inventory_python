from tkinter import * 
from fakeData import FakeData

class Dashboard:
    def __init__(self,fen,con):
        self.fen = fen
        self.FakeData=FakeData()
        #Section pour l'etat actuel du stock

        self.title_section1 = Label(self.fen, text = "Stock Actuel", font = ('Segoe UI bold',14),fg='black').place(x=20, y=20)
        self.tabStockActuel=Frame(self.fen,bg='white')
        self.tabStockActuel.place(x=20, rely=0.12,relwidth=0.4,relheight=0.7)

        self.title = Label(self.tabStockActuel, text = "Nom Article", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.03, rely=0.05,relwidth=0.3)
        self.title = Label(self.tabStockActuel, text = "Quantité", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.38, rely=0.05,relwidth=0.3)
        self.title = Label(self.tabStockActuel, text = "Status", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.7, rely=0.05,relwidth=0.3)


        data=self.FakeData.dataArticleDisponible()
        t=0.15
        for item in (data):        
            self.ContLigne=Frame(self.tabStockActuel,bg='white')
            self.ContLigne.place(x=0, rely=t,relwidth=1,height=60)
            self.ligne=Frame(self.ContLigne,bg='#d6d4d4',height=-20).place(x=0, y=0.12,relwidth=1)
            self.title = Label(self.ContLigne, text = item[0], font = ('Segoe UI',11),fg='#adabab',bg='white').place(relx=0.03, rely=0.14,relwidth=0.3)
            self.title = Label(self.ContLigne, text =item[1], font = ('Segoe UI ',11),fg='#adabab',bg='white').place(relx=0.38, rely=0.14,relwidth=0.3)
            self.title = Label(self.ContLigne, text =item[2], font = ('Segoe UI',11),fg='#adabab',bg='white').place(relx=0.7, rely=0.14,relwidth=0.3)
            t+=0.1

        #Fin section Stock Actuel

        #Section tableau comparatifs de vente 
        self.title_section1 = Label(self.fen, text = "Tableau Comparatif des ventes selon les cinq mois passé", font = ('Segoe UI bold',14),fg='black').place(relx=0.45, y=20)
        self.tabStockActuel=Frame(self.fen,bg='white')
        self.tabStockActuel.place(relx=0.45, rely=0.12,relwidth=0.5,relheight=0.7)

        self.title = Label(self.tabStockActuel, text = "Nom Article", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.03, rely=0.05,relwidth=0.25)
        self.title = Label(self.tabStockActuel, text = "Jan", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.31, rely=0.05,relwidth=0.1)
        self.title = Label(self.tabStockActuel, text = "Fev", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.42, rely=0.05,relwidth=0.1)
        self.title = Label(self.tabStockActuel, text = "Mars", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.53, rely=0.05,relwidth=0.1)
        self.title = Label(self.tabStockActuel, text = "Avril", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.64, rely=0.05,relwidth=0.1)
        self.title = Label(self.tabStockActuel, text = "Mai", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.75, rely=0.05,relwidth=0.1)
        self.title = Label(self.tabStockActuel, text = "Juin", font = ('Segoe UI ',12),fg='#416b70',bg='white').place(relx=0.86, rely=0.05,relwidth=0.1)


        """
        data=self.FakeData.dataArticleDisponible()
        t=0.15
        for item in (data):        
            self.ContLigne=Frame(self.tabStockActuel,bg='white')
            self.ContLigne.place(x=0, rely=t,relwidth=1,height=60)
            self.ligne=Frame(self.ContLigne,bg='#d6d4d4',height=-20).place(x=0, y=0.12,relwidth=1)
            self.title = Label(self.ContLigne, text = item[0], font = ('Segoe UI',11),fg='#adabab',bg='white').place(relx=0.03, rely=0.14,relwidth=0.3)
            self.title = Label(self.ContLigne, text =item[1], font = ('Segoe UI ',11),fg='#adabab',bg='white').place(relx=0.38, rely=0.14,relwidth=0.3)
            self.title = Label(self.ContLigne, text =item[2], font = ('Segoe UI',11),fg='#adabab',bg='white').place(relx=0.7, rely=0.14,relwidth=0.3)
            t+=0.1"""







