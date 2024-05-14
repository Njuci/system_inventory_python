from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno,showinfo,showwarning
from configuration import InfosApp
from fakeData import FakeData
from tkinter.messagebox import askyesno,showinfo,showwarning
from verificationEntry import EntryVerification
from Rapport_Facture import FacturePDF
#from tkcalendar import DateEntry
class GestionVente :
    def __init__(self,fen,con):
        self.fen = fen
        self.infosApp=InfosApp
        self.FakeData=FakeData()
        self.RapportPDF=FacturePDF()
        self.title_section1 = Label(self.fen, text = "Formulaire de vente", font = ('Segoe UI bold',14),fg='black',bg='#ebf4f5').place(x=20, y=20)
        self.verification=EntryVerification()
        #Formulaire de vente
        self.listeArtticle=[]
        self.FormulaireVente()


        #------------------------entete gauche---------------------------
                #-----------------------------------Conteneur gauche---------------------------------------
        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.45, rely=0.1,relwidth=0.5,relheight=0.8)

        #Search vente
        self.SearchClient = Label(self.RightContener, text='Recherche',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.02,rely=0.02)

        self.paddingEntry=Frame(self.RightContener,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.2,rely=0.02,relwidth=0.5, height=28)
        self.SearchEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='white')
        self.SearchEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

 

        self.title_listeVente = Label(self.RightContener, text = "Liste de vente", font = ('Segoe UI bold',12),fg='black',bg='#ebf4f5')
        self.title_listeVente.place(relx=0.02, rely=0.12)

        self.bouton_Rapport= Button(self.RightContener,bg='#416b70',text='Imprimer',relief='flat', font =('Segoe UI',9),fg='white',command=self.genererRapportJournalier)
        self.bouton_Rapport.place(relx=0.8,rely=0.02,relwidth=0.22, height=26)

        #les filtres 
        self.SearchClient = Label(self.RightContener, text='Filtre :',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.3,rely=0.12)
        self.bouton_Plus= Button(self.RightContener,bg='#416b70',text='Toutes le ventes',relief='flat', font =('Segoe UI',9),fg='white',command=self.ShowForm)
        self.bouton_Plus.place(relx=0.4,rely=0.12,relwidth=0.22, height=26)

        self.ListeDateVente=ttk.Combobox(self.RightContener, font =('Segoe UI',10))
        self.ListeDateVente.place(relx=0.7,rely=0.12,relwidth=0.3, height=26)
        self.ListeDateVente.bind("<<ComboboxSelected>>")

         #----------------------------Tab section -------------------------------

        self.TableauArticles(530)
        self.listeArtticle=[]

    def genererRapportJournalier(self):
        self.RapportPDF.genererRapportJournalier([])
        
    def FormulaireVente(self):
        #Formulaire de ventes 
        self.VenteForm=Frame(self.fen,bg='white')
        self.VenteForm.place(x=20, rely=0.1,relwidth=0.4,relheight=0.8)

        #Barre de recherche
        self.SearchClient = Label(self.VenteForm, text='Rechercher',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.02)

        self.paddingEntry=Frame(self.VenteForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.24,rely=0.02,relwidth=0.68, height=28)
        self.SearchEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.SearchEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

        #Infos clients
        self.SearchClient = Label(self.VenteForm, text='Nom Client',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.11)
        self.paddingEntry=Frame(self.VenteForm,bg='white')
        self.paddingEntry.place(relx=0.24,rely=0.1,relwidth=0.68, height=30)

        self.NomClient=ttk.Combobox(self.paddingEntry, font =('Segoe UI',10))
        self.NomClient.place(relx=0.00,rely=0.1,relwidth=0.99, height=26)
        self.NomClient.bind("<<ComboboxSelected>>")

        self.NumVente = Label(self.VenteForm, text='Num Vente',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumVente.place(relx=0.02,rely=0.18)

        self.paddingEntry=Frame(self.VenteForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.24,rely=0.18,relwidth=0.3, height=28)
        self.numVente=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.numVente.place(relx=0.02,rely=0.18,relwidth=0.96, height=26)

        self.NumFact = Label(self.VenteForm, text='Fact',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.55,rely=0.18)

        self.paddingEntry=Frame(self.VenteForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.65,rely=0.18,relwidth=0.27, height=28)
        self.numFact=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.numFact.place(relx=0.02,rely=0.18,relwidth=0.96, height=26)

        #Details ventes 
        self.SearchClient = Label(self.VenteForm, text='Détails vente',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.27)


        #Buttons Actions
        self.bouton_enregistrer= Button(self.VenteForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda :AddVente())
        self.bouton_enregistrer.place(relx=0.28,rely=0.27,relwidth=0.2, height=30)

        self.bouton_Modifier= Button(self.VenteForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70')
        self.bouton_Modifier.place(relx=0.49,rely=0.27,relwidth=0.2, height=30)

        self.bouton_Imprimer= Button(self.VenteForm,bg='#416b70',text='Imprimer',relief='flat', font =('Segoe UI',9),fg='white',command=lambda:genererFacture())
        self.bouton_Imprimer.place(relx=0.70,rely=0.27,relwidth=0.2, height=30)

        #Contenue details facture
        self.ligne=Frame(self.VenteForm,bg='#d6d4d4',height=-20)
        self.ligne.place(relx=0.02, rely=0.45,relwidth=0.9)
        nom=self.infosApp.Configuration(self)


        self.NumFact = Label(self.VenteForm, text='ID PRODUIT',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.02,rely=0.38,relwidth=0.25)
        self.NumFact = Label(self.VenteForm, text='NOM ARTICLE',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.28,rely=0.38,relwidth=0.35)
        self.NumFact = Label(self.VenteForm, text='Qnt',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.64,rely=0.38,relwidth=0.15)

        self.bouton_Plus= Button(self.VenteForm,bg='#ebf4f5',text='Plus',relief='flat', font =('Segoe UI',9),fg='#adabab',command=self.ShowForm)
        self.bouton_Plus.place(relx=0.81,rely=0.38,relwidth=0.11, height=26)

        if len(self.listeArtticle)!=0:
            self.articleContent=Frame(self.VenteForm,bg='white')
            self.articleContent.place(relx=0.02, rely=0.47,relwidth=0.9,relheight=2)
            #creation du scroll bar
   
        else :
            self.message = Label(self.VenteForm, text="pas d'articles pour cette vente",font =('Segoe UI',12),fg='#adabab',bg='white')
            self.message.place(relx=0.02,rely=0.68,relwidth=0.9)
        self.numberInput=0

        def AddVente():
            if(self.numVente.get()!="" or self.NomClient.get()!="" or self.numFact.get()!=""):
                if len(self.listeArtticle)!=0:
                    showinfo(nom[0],'Succes')
                else :
                    showwarning(nom[0],'Veuillez ajouter les produits')
            else :
                showwarning(nom[0],'Veuillez remplir tout les champs')

        #--------------------Generation pdf ---------------------

        def genererFacture():
            if(self.numVente.get()!="" or self.NomClient.get()!="" or self.numFact.get()!=""):
                if len(self.listeArtticle)!=0:
                    showinfo(nom[0],'Succes')
                    self.RapportPDF.genererFacture([])
                else :
                    showwarning(nom[0],'Veuillez ajouter les produits')
            else :
                showwarning(nom[0],'Veuillez remplir tout les champs')




        #-----------------------------------Fin formulaire de vente-----------------------------------

    


    def TableauArticles(self,TailTabl):

        self.Contneur=Frame(self.RightContener,bg='red')
        self.Contneur.place(relx=0.00, rely=0.2,relwidth=1,relheight=1)

        #liste des produit en stock
        self.tabStockActuel=Frame(self.Contneur,bg='white')
        self.tabStockActuel.place(x=0.00, rely=0.00,relwidth=1,relheight=0.9)

        # Create a canvas to hold the scrollable content
        self.canvas =Canvas(self.tabStockActuel, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.tabStockActuel, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.95, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.title = Label(self.tabStockActuel, text="Date vente", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.3)
        self.title = Label(self.tabStockActuel, text="Nom client", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.3, rely=0.02, relwidth=0.5)

        y=0
        #Affichage des ventes dans le tableau
        data=self.FakeData.dataArticleDisponible()
        t=0.1
        a=1
        for item in data:
            if a==1:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=13,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.3)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white').place(relx=0.4, rely=0.25,relwidth=0.3)

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.00, rely=0.25,relwidth=0.32)
                self.title2 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.325, rely=0.25,relwidth=0.6)


                # A revoir pour la modification
                self.title2.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(item[0]))
                self.title1.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(article))


                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Details',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.85,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.00, rely=0.25,relwidth=0.32)
                self.title2 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.325, rely=0.25,relwidth=0.6)


                # A revoir pour la modification
                self.title2.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(item[0]))
                self.title1.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(article))


                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Details',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.85,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                
            # (Optional) Update the scroll
            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
        



            def HandleClickDetails(nomArticle):
            #-----------------Details stock-----------------------
                print(nomArticle)
                def Capture():
                    self.DetailsStock(nomArticle,330)
                Capture()
            
            #modification de l'article
            def HandleUpdateArticle(nom):
                self.FormulaireArticle(['empty'],nom)

    #Details stock 


    def SupprimerproduitSurDetails(self,index):
            result=askyesno("Confirmation","Voulez-vous vraiment supprimer ce produit sur cette vente ?")
            if result :
                self.actualiser()
    
    def actualiser(self):
        self.Articles=Frame(self.articleContent,bg='white')
        self.Articles.place(x=0, rely=0.04,relwidth=1,height=130)

        self.canvas =Canvas(self.Articles, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.Articles, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.95, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)


        #Actualiser Produits
        self.incr=0.00
        #Affichages de produits sur facture
        liste1=[]
        index=0
        y=0
        a=1
        #if (len(self.listeArtticle)<5):

        for item in (self.listeArtticle):

            if a==1:

                self.label = Frame(self.canvas, bg='white',height=13,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text='OO1')
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.28, relheight=0.7)
                self.Idlab.bind('<Double-Button-1>', lambda event: self.SupprimerproduitSurDetails(0))
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text='biscuit')
                self.nomArt.place(relx=0.29,rely=0.0,relwidth=0.39, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text='10')
                self.Qnt.place(relx=0.69,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text='200')
                self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, relheight=0.7)

                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                self.label = Frame(self.canvas, bg='white',height=40,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text='OO1')
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.28, relheight=0.7)
                self.Idlab.bind('<Double-Button-1>', lambda event: self.SupprimerproduitSurDetails(0))
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text='biscuit')
                self.nomArt.place(relx=0.29,rely=0.0,relwidth=0.39, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text='10')
                self.Qnt.place(relx=0.69,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text='200')
                self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, relheight=0.7)

                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                a=0
            else :
                self.label = Frame(self.canvas, bg='white',height=40,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text='OO1')
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.28, relheight=0.7)
                self.Idlab.bind('<Double-Button-1>', lambda event: self.SupprimerproduitSurDetails(0))
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text='biscuit')
                self.nomArt.place(relx=0.29,rely=0.0,relwidth=0.39, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text='10')
                self.Qnt.place(relx=0.69,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text='200')
                self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, relheight=0.7)

                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5



        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
        



    #Fonction pour le vider les champs 
    def ViderChamps(self):
        self.inputID.delete(0,END)
        self.nomArticle.delete(0,END)
        self.inputQnt.delete(0,END)

    #Fonction d'ajout d'articles
    def AddArticle(self):
        n=self.infosApp.Configuration(self)
        if(self.inputID.get()!="" or self.nomArticle.get()!="" or self.inputQnt.get()!="" ):
            if self.verification.Verification(self.inputQnt.get()):
                self.listeArtticle.append([self.inputID.get(),self.nomArticle.get(),self.inputQnt.get()])
                self.actualiser()
                self.ViderChamps()
            else :
                showwarning(n[0],'La quantité doit être un entier')

        else :
            showwarning(n[0],'Veuillez remplir tout les champs')
    


    def ShowForm(self):
        if len(self.listeArtticle)==0:
            self.bouton_Plus= Button(self.VenteForm,bg='#ebf4f5',text='Ajouter',relief='flat', font =('Segoe UI',9),fg='#adabab',command=self.AddArticle)
            self.bouton_Plus.place(relx=0.81,rely=0.38,relwidth=0.11, height=26)

            self.articleContent=Frame(self.VenteForm,bg='white')
            self.articleContent.place(relx=0.02, rely=0.46,relwidth=0.9,relheight=2)

            self.ContLigne=Frame(self.articleContent,bg='white')
            self.ContLigne.place(x=0, rely=0.00,relwidth=1,height=33)

            self.inputID=ttk.Combobox(self.ContLigne,font =('Segoe UI',10))
            self.inputID.place(relx=0.0,rely=0.0,relwidth=0.28, height=26)

            self.nomArticle=Entry(self.ContLigne,font =('Segoe UI',10),bg='white',relief='flat')
            self.nomArticle.place(relx=0.29,rely=0.0,relwidth=0.39, height=26)

            self.inputQnt=Entry(self.ContLigne,font =('Segoe UI',10),bg='white')
            self.inputQnt.place(relx=0.69,rely=0.0,relwidth=0.16, height=26)
            self.Prix=Label(self.ContLigne,font =('Segoe UI',10),bg='white',text='200')
            self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, height=26)
            self.ligne=Frame(self.ContLigne,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)

            #Ligne de total
            self.TitreTotal=Label(self.VenteForm,font =('Segoe UI bold',12),bg='white',text='Total')
            self.TitreTotal.place(relx=0.00,rely=0.84,relwidth=0.15, height=26)
            self.TitreTotal=Label(self.VenteForm,font =('Segoe UI bold',12),bg='white',text='200000 CDF')
            self.TitreTotal.place(relx=0.5,rely=0.84,relwidth=0.6, height=26)
    
    



        



            





