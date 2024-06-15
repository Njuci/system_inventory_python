from tkinter import *
import os
from tkinter.messagebox import askyesno,showinfo
from tkinter import ttk
from dashboard_Front  import Dashboard
from gestVente_Front import GestionVente
from gestClient_front import GestionClient
from gestArticles_front import GestionArticle 
from gestStock_front import GestionStock



class MenuPrincipaleFrontend:
    ver=0
    def __init__(self,Curseur,con,compte):
        self.Curseur=Curseur
        self.fen = Tk()
        self.fen.title("DANIELLO GEST-STOCK")
        self.fen.geometry("1200x600")
        self.fen.resizable(width=True,height=True)
        self.compte=compte
        self.con=con
        #les instances de la classe
        #Selection de l'annee active

  
        #Creation du conteneur de menu
        self.MenuContainer=Frame(self.fen,bg='white')
        self.MenuContainer.place(relx=0.0,rely=0.0,relwidth=1, height=120)
        self.ButtonContaineur=Frame( self.MenuContainer,bg='white')
        self.ButtonContaineur.place(relx=0.05,y=50,relwidth=0.90, height=50)
        self.titre = Label(self.MenuContainer, text = "BIENVENUE DANS DANIELLO GEST-STOCK", font =('Segoe UI bold',15),bg='white',fg='black').place(relx=0.1,y=4,relwidth=0.8,relheight=0.2)




        self.VenteContent=Frame(self.fen,bg='#ebf4f5')
        self.VenteContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)

        self.ClientContent=Frame(self.fen,bg='#ebf4f5')
        self.ClientContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
        self.ClientContent.place_forget()

        self.ArticleContent=Frame(self.fen,bg='#ebf4f5')
        self.ArticleContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
        self.ArticleContent.place_forget()

        self.GestionStock=Frame(self.fen,bg='#ebf4f5')
        self.ArticleContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
        self.ArticleContent.place_forget()

        self.CreationMenu()
       

    def CreationMenu(self):
        Menu2=GestionVente(self.VenteContent,self.con)
        Menu3=GestionClient(self.ClientContent,self.con)
        Menu4=GestionArticle(self.ArticleContent,self.con)
        Menu5=GestionStock(self.GestionStock,self.con)

        self.etatInitialBtn()

        #self.ComboContainer.place_forget()
    def etatInitialBtn(self):
        
        self.VenteContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion ventes',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide2)
        self.VenteContent_btn.place(relx=0.10,y=5, relwidth=0.18,height=40)
        self.ClientContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion clients',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide3)
        self.ClientContent_btn.place(relx=0.30,y=5, relwidth=0.18,height=40)
        self.ArticleContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion articles',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide4)
        self.ArticleContent_btn.place(relx=0.50,y=5, relwidth=0.18,height=40)
        self.GestStock_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion stock',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide5)
        self.GestStock_btn.place(relx=0.70,y=5, relwidth=0.18,height=40)
    def cacherSlide(self):
        self.VenteContent.place_forget()
        self.ClientContent.place_forget()
        self.ArticleContent.place_forget()
        self.GestionStock.place_forget()

    def AfficherSlide1(self):
        self.etatInitialBtn()
        self.cacherSlide()
        self.DashBoardContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)


    def AfficherSlide2(self):
        self.cacherSlide()
        self.VenteContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)

    def AfficherSlide3(self):
        self.cacherSlide()
        self.ClientContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
    
    def AfficherSlide4(self):
        self.cacherSlide()
        self.ArticleContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
    
    def AfficherSlide5(self):

        self.cacherSlide()
        self.GestionStock.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)

    def fenetre (self):
        return self.fen

        

       