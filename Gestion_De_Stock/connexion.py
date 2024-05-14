from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror,showwarning
from gest_stock_back.login_back import Connexion


class Connexion_Frontend:
    def __init__(self):
        self.fen = Tk()
        self.fen.title("STOCK-GEST ")
        self.fen.geometry("800x600")
        self.fen.resizable(width=True,height=True)
        self.conteneurTitle=Frame(self.fen,bg='white')
        self.conteneurTitle.place(relx=0.1,rely=0.1, relwidth=0.8,relheight=0.3)
        self.nomEntreprise = Label(self.conteneurTitle, text = "GESTION DE VENTES ", font =('Segoe UI bold',17),bg='white',fg='black').place(relx=0.1,rely=0.05,relwidth=0.8,relheight=0.2)
        self.nomEntreprise = Label(self.conteneurTitle, text = "LA GRACE BUSNNESS", font =('Segoe UI bold',17),bg='white',fg='black').place(relx=0.1,rely=0.22,relwidth=0.8,relheight=0.2)
        self.titre = Label(self.conteneurTitle, text = "CONNEXION", font =('Segoe UI bold',19),bg='white',fg='black').place(relx=0.1,rely=0.43,relwidth=0.8,relheight=0.2)

        self.form=Frame(self.fen)
        self.form.place(relx=0.15,rely=0.3, relwidth=0.7,relheight=0.5)

        self.idLab = Label(self.form, text='Nom utilisateur',font =('Segoe UI',12))
        self.idLab.place(relx=0.2,rely=0.1,relheight=0.1)
        self.mdpLab = Label(self.form, text='Mot de passe',font =('Segoe UI',12))
        self.mdpLab.place(relx=0.2,rely=0.3,relheight=0.1)
        
        self.idEnt=Entry(self.form,relief='flat', font =('Segoe UI',12))
        self.idEnt.place(relx=0.2,rely=0.2,relwidth=0.5, height=30)
        self.mdEnt=Entry(self.form,show='*',relief='flat',font =('Segoe UI',12))
        self.mdEnt.place(relx=0.2,rely=0.4,relwidth=0.5, height=30)
        
        self.bouton= Button(self.form,bg='#6666b9',text='Connexion',relief='flat', font =('Segoe UI',15),fg='white',command=self.login)
        self.bouton.place(relx=0.2,rely=0.6,relwidth=0.5, height=50)
        
    def fenetre(self):
        return self.fen
    def 