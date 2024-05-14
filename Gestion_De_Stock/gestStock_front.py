from tkinter import *
from configuration import InfosApp
from fakeData import FakeData
from tkinter import ttk
from verificationEntry import EntryVerification
from tkinter.messagebox import askyesno,showinfo,showwarning
from configuration import InfosApp
class GestionStock :
    def __init__(self,fen,con):
        self.fen = fen
        self.configApp=InfosApp
        self.FakeData=FakeData()
        self.config=self.configApp.Configuration(self)
        self.couleur=self.configApp.ColeursApp(self)
        self.verification=EntryVerification()

        #Appprovisionnement UI 
        self.FormulaireApro()
        
        #Conteneur
        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.3, rely=0.1,relwidth=0.68,relheight=0.8)

        #--------stock general ui------------------------
        self.QuantiteGeneralStock(270)




    def FormulaireApro(self):
        #Formulaire clients
        self.ApproForm=Frame(self.fen,bg='white')
        self.ApproForm.place(x=20, rely=0.1,relwidth=0.25,relheight=0.8)
        self.title_section1 = Label(self.ApproForm, text = "Nouveau Stock", font = ('Segoe UI',10),fg=self.couleur['CouleurTitreText'],bg="white").place(relx=0.27, rely=0.03)

        
        self.ArticleLabel = Label(self.ApproForm, text='Nom Article',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.ArticleLabel.place(relx=0.02,rely=0.1)

        self.NomArticle=ttk.Combobox(self.ApproForm, font =('Segoe UI',10))
        self.NomArticle.place(relx=0.02,rely=0.15,relwidth=0.9, height=26)
        self.NomArticle.bind("<<ComboboxSelected>>")

        self.ArticleLabel = Label(self.ApproForm, text="Prix d'achat Unit.",font =('Segoe UI',10),fg='#adabab',bg='white')
        self.ArticleLabel.place(relx=0.02,rely=0.25)

        self.paddingEntry=Frame(self.ApproForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.3,relwidth=0.9, height=28)
        self.PrixEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.PrixEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)


        self.ArticleLabel = Label(self.ApproForm, text="Quantité.",font =('Segoe UI',10),fg='#adabab',bg='white')
        self.ArticleLabel.place(relx=0.02,rely=0.4)

        self.paddingEntry=Frame(self.ApproForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.45,relwidth=0.9, height=28)
        self.QuantEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.QuantEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

        #Buttons Actions
        self.bouton_enregistrer= Button(self.ApproForm,bg='white',text='Ajouter',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjouterStock())
        self.bouton_enregistrer.place(relx=0.02,rely=0.6,relwidth=0.3, height=30)

        self.bouton_Modifier= Button(self.ApproForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70', command=lambda:Modifier())
        self.bouton_Modifier.place(relx=0.4, rely=0.6,relwidth=0.3, height=30)

        def AjouterStock():
            if self.PrixEntry.get()!="" and self.QuantEntry.get()!="" and self.NomArticle.get()!=""  :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.QuantEntry.get()) :
                    pass
                else:
                    showwarning(self.config[0],'Vous avez entrer des mauvaises données')
            else :
                    showwarning(self.config[0],'Veuillez remplir tout les champs')
        
        def Modifier():
            if self.PrixEntry.get()!="" and self.QuantEntry.get()!="" and self.NomArticle.get()!=""  :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.QuantEntry.get()) :
                    pass
                else:
                    showwarning(self.config[0],'Vous avez entrer des mauvaises données')
            else :
                    showwarning(self.config[0],'Veuillez remplir tout les champs')
    
    #---------------------------tableau articles et quantites globaux en stock ---------------------

    def QuantiteGeneralStock(self,TailTabl):

        self.Contneur=Frame(self.RightContener,bg='#ebf4f5')
        self.Contneur.place(relx=0.00, rely=0.00,relwidth=0.4,relheight=1)

        self.title_listeVente = Label(self.Contneur, text = "STOCK GENERAL", font = ('Segoe UI bold',12),fg='black',bg='#ebf4f5')
        self.title_listeVente.place(relx=0.02, rely=0.00)

        #liste des produit en stock
        self.tabStockActuel=Frame(self.Contneur,bg='white')
        self.tabStockActuel.place(x=0.00, rely=0.1,relwidth=1,relheight=0.9)

        # Create a canvas to hold the scrollable content
        self.canvas =Canvas(self.tabStockActuel, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.tabStockActuel, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.9, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.title = Label(self.tabStockActuel, text="Nom article", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.43)
        self.title = Label(self.tabStockActuel, text="Quantité ", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.47, rely=0.02, relwidth=0.4)


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
                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.3)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white').place(relx=0.4, rely=0.25,relwidth=0.3)
                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.3)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white').place(relx=0.4, rely=0.25,relwidth=0.3)
                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
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
                    self.DetailsStock(nomArticle,345)
                Capture()




    #Details stock 
    def DetailsStock(self,nomArticle,TailTabl):

        # ... other code ...

        self.Contneur = Frame(self.RightContener, bg='#ebf4f5')
        self.Contneur.place(relx=0.4, rely=0.00, relwidth=0.5, relheight=1)

        self.title_listeVente = Label(self.Contneur, text="DETAILS STOCK " + nomArticle, font=('Segoe UI bold', 12), fg='black', bg='#ebf4f5')
        self.title_listeVente.place(relx=0.02, rely=0.00)

        # Create a frame to hold the actual list items (inside the canvas)
        self.tabStockActuel = Frame(self.Contneur, bg='white') 
        self.tabStockActuel.place(x=0.00, rely=0.1,relwidth=1,relheight=0.9)

        # Create a canvas to hold the scrollable content
        self.canvas =Canvas(self.tabStockActuel, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.tabStockActuel, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.9, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # **Important:** Bind the content frame (`self.tabStockActuel`) to the canvas viewport
        # Variable to track the next item's y-position
        y = 0

        # Headers for the stock list
        self.title = Label(self.tabStockActuel, text="Date entrée", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.43)
        self.title = Label(self.tabStockActuel, text="Quantité ", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.47, rely=0.02, relwidth=0.4)

        # Loop to generate stock list items dynamically
        t = 0.1  # Initial vertical position for the first item
        data = self.FakeData.dataArticleDisponible()
        a=1
        for item in data:

            if a==1:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=13,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                # Labels for article name and quantity
                self.title = Label(self.label, text='gfg', font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
                self.title = Label(self.label, text="gfg", font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                # Labels for article name and quantity
                self.title = Label(self.label, text=item[0], font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
                self.title = Label(self.label, text=item[1], font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5



                t += 0.1  # Update vertical position for the next item
                a=0
            else :
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                # Labels for article name and quantity
                self.title = Label(self.label, text=item[0], font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
                self.title = Label(self.label, text=item[1], font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Button for details (optional, adapt placement as needed)
                # ... (place your button code here, adapting the placement as needed)

                t += 0.1  # Update vertical position for the next item

        # (Optional) Update the scroll
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
    


