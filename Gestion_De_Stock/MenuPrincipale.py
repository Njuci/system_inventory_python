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
        self.fen.title("GRACE BUSNESS")
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

        #Creation des conteneurs d'ecrant
        self.DashBoardContent=Frame(self.fen,bg='#ebf4f5')
        self.DashBoardContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
        

        self.VenteContent=Frame(self.fen,bg='#ebf4f5')
        self.VenteContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
        self.VenteContent.place_forget()

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
        Menu1=Dashboard(self.DashBoardContent,self.con)
        Menu2=GestionVente(self.VenteContent,self.con)
        Menu3=GestionClient(self.ClientContent,self.con)
        Menu4=GestionArticle(self.ArticleContent,self.con)
        Menu5=GestionStock(self.GestionStock,self.con)

        self.etatInitialBtn()

        #self.ComboContainer.place_forget()
    def etatInitialBtn(self):
        self.DashBoardContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Dashboard',fg='white',relief="flat", font = ('Segoe UI',12),command=self.AfficherSlide1)
        self.DashBoardContent_btn.place(relx=0.0,y=5, relwidth=0.18,height=40)
        self.VenteContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion ventes',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide2)
        self.VenteContent_btn.place(relx=0.20,y=5, relwidth=0.18,height=40)
        self.ClientContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion clients',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide3)
        self.ClientContent_btn.place(relx=0.40,y=5, relwidth=0.18,height=40)
        self.ArticleContent_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion articles',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide4)
        self.ArticleContent_btn.place(relx=0.60,y=5, relwidth=0.18,height=40)
        self.GestStock_btn= Button(self.ButtonContaineur,bg='#416b70',text='Gestion stock',fg='white',relief="flat",font = ('Segoe UI',12),command=self.AfficherSlide5)
        self.GestStock_btn.place(relx=0.80,y=5, relwidth=0.18,height=40)
    def cacherSlide(self):
        self.DashBoardContent.place_forget()
        self.VenteContent.place_forget()
        self.ClientContent.place_forget()
        self.ArticleContent.place_forget()
        self.GestionStock.place_forget()

    def AfficherSlide1(self):
        self.etatInitialBtn()
        self.DashBoardContent_btn= Button(self.ButtonContaineur,bg='white',text='DASHBOARD',fg='#416b70',relief="flat", font = ('Segoe UI bold',9),command=self.AfficherSlide1)
        self.DashBoardContent_btn.place(relx=0.0,y=5, relwidth=0.18,height=40)
        self.CreationMenu()
        self.cacherSlide()
        self.DashBoardContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)


    def AfficherSlide2(self):
        self.etatInitialBtn()
        self.VenteContent_btn= Button(self.ButtonContaineur,bg='white',text='GESTION VENTES',fg='#416b70',relief="flat", font = ('Segoe UI bold',9),command=self.AfficherSlide2)
        self.VenteContent_btn.place(relx=0.20,y=5, relwidth=0.18,height=40)
        self.CreationMenu()
        self.cacherSlide()
        self.VenteContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)

    def AfficherSlide3(self):
        self.etatInitialBtn()
        self.ClientContent_btn= Button(self.ButtonContaineur,bg='white',text='GESTION CLIENTS',fg='#416b70',relief="flat", font = ('Segoe UI bold',9),command=self.AfficherSlide3)
        self.ClientContent_btn.place(relx=0.40,y=5, relwidth=0.18,height=40)
        self.CreationMenu()
        self.cacherSlide()
        self.ClientContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
    
    def AfficherSlide4(self):
        self.etatInitialBtn()
        self.ArticleContent_btn= Button(self.ButtonContaineur,bg='white',text='GESTION ARTICLES',fg='#416b70',relief="flat", font = ('Segoe UI bold',9),command=self.AfficherSlide4)
        self.ArticleContent_btn.place(relx=0.60,y=5, relwidth=0.18,height=40)
        self.CreationMenu()
        self.cacherSlide()
        self.ArticleContent.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)
    
    def AfficherSlide5(self):
        self.etatInitialBtn()
        self.GestStock_btn= Button(self.ButtonContaineur,bg='white',text='GESTION STOCK',fg='#416b70',relief="flat", font = ('Segoe UI bold',9),command=self.AfficherSlide5)
        self.GestStock_btn.place(relx=0.80,y=5, relwidth=0.18,height=40)
        self.CreationMenu()
        self.cacherSlide()
        self.GestionStock.place(relx=0.0,rely=0.17,relheight=0.9,relwidth=1)

    def fenetre (self):
        return self.fen

        

       