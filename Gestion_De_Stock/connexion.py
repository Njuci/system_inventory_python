import dashboard_Front
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showerror,showwarning
from login_back import Connexion
import MenuPrincipale

class Connexion_Frontend:
    def __init__(self):
        self.fen = Tk()
        self.fen.title("DANIELLO GEST-STOCK")
        self.fen.geometry("800x600")
        self.fen.config(bg="#ebf4f5")
        self.fen.resizable(width=True,height=True)
        self.conteneurTitle=Frame(self.fen,bg='#ebf4f5')
        self.conteneurTitle.place(relx=0.1,rely=0.1, relwidth=0.8,relheight=0.3)
        self.titre = Label(self.conteneurTitle, text = "AUTHENTIFICATION", font =('Segoe UI bold',15),bg='#ebf4f5',fg='black').place(relx=0.1,rely=0.43,relwidth=0.8,relheight=0.2)

        self.form=Frame(self.fen,bg="#ebf4f5")
        self.form.place(relx=0.15,rely=0.3, relwidth=0.7,relheight=0.5)

        self.idLab = Label(self.form, text='Nom utilisateur',bg='#ebf4f5',font =('Segoe UI',12))
        self.idLab.place(relx=0.2,rely=0.1,relheight=0.1)
        self.mdpLab = Label(self.form, text='Mot de passe',bg='#ebf4f5',font =('Segoe UI',12))
        self.mdpLab.place(relx=0.2,rely=0.3,relheight=0.1)
        
        self.idEnt=Entry(self.form,relief='flat', font =('Segoe UI',12))
        self.idEnt.place(relx=0.2,rely=0.2,relwidth=0.5, height=30)
        self.mdEnt=Entry(self.form,show='*',relief='flat',font =('Segoe UI',12))
        self.mdEnt.place(relx=0.2,rely=0.4,relwidth=0.5, height=30)
        
        self.bouton= Button(self.form,bg='#416b70',text='Valider',relief='flat', font =('Segoe UI',15),fg='white',command=self.connect_back)
        self.bouton.place(relx=0.2,rely=0.6,relwidth=0.5, height=50)
        
    def fenetre(self):
        return self.fen
    def connect_back(self):
        db=Connexion(self.idEnt.get(),self.mdEnt.get())
        if db.login():
            
            Dash=MenuPrincipale.MenuPrincipaleFrontend(db.get_curseur(),db,self.idEnt.get())
            self.fen.destroy()
            Dash.fenetre().mainloop()
        else:
            showerror("Erreur","Nom d'utilisateur ou mot de passe incorrect")
    
            
        
    