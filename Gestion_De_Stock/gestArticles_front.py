from tkinter import *
from configuration import InfosApp
from fakeData import FakeData
from tkinter import ttk
from verificationEntry import EntryVerification
from tkinter.messagebox import askyesno,showinfo,showwarning
class GestionArticle :
    def __init__(self,fen,con):
        self.fen = fen
        self.configApp=InfosApp
        self.FakeData=FakeData()
        self.couleur=self.configApp.ColeursApp(self)
        self.verification=EntryVerification()
        self.config=self.configApp.Configuration(self)

        self.title_section1 = Label(self.fen, text = "Formulaire article", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background']).place(x=20, y=20)
        self.title_section1 = Label(self.fen, text = "Les articles disponibles", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background'])
        self.title_section1.place(relx=0.3, y=20)

        #-----------------------Formulaire gestion article -------------------
        self.FormulaireArticle(['empty'],'')

        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.3, rely=0.1,relwidth=0.68,relheight=0.8)

        #----------------------------Tab section -------------------------------
        self.TableauArticles(330)



    def FormulaireArticle(self,listeArticles,ValeurArticle):
        #Formulaire clients
        self.ClientForm=Frame(self.fen,bg='white')
        self.ClientForm.place(x=20, rely=0.1,relwidth=0.25,relheight=0.8)
        self.title_section1 = Label(self.ClientForm, text = "AJOUT ET MODIFICATION ARTICLE", font = ('Segoe UI',10),fg=self.couleur['CouleurTitreText'],bg="white").place(relx=0.15, rely=0.03)

        #Barre de recherche
        self.SearchClient = Label(self.ClientForm, text='Nom article',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.12)

        self.paddingEntry=Frame(self.ClientForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.17,relwidth=0.9, height=28)
        self.NomArticleEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.NomArticleEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)
        self.NomArticleEntry.insert(0,ValeurArticle)

        #Buttons Actions
        self.bouton_enregistrer= Button(self.ClientForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjoutArticle())
        self.bouton_enregistrer.place(relx=0.1,rely=0.28,relwidth=0.3, height=30)

        self.bouton_Modifier= Button(self.ClientForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:ModifierArticle())
        self.bouton_Modifier.place(relx=0.45, rely=0.28,relwidth=0.3, height=30)

        #Gestion de prix articles
        self.title_section1 = Label(self.ClientForm, text = "NOUVEAU PRIX ARTICLE", font = ('Segoe UI',10),fg=self.couleur['CouleurTitreText'],bg="white").place(relx=0.20, rely=0.4)
        
        self.SearchClient = Label(self.ClientForm, text='Nom Article',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.5)

        self.ComboArticle=ttk.Combobox(self.ClientForm, font =('Segoe UI',10),values=listeArticles)
        self.ComboArticle.place(relx=0.02,rely=0.55,relwidth=0.9, height=26)
        self.ComboArticle.bind("<<ComboboxSelected>>")

        self.SearchClient = Label(self.ClientForm, text='Prix',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.62)

        self.paddingEntry=Frame(self.ClientForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.68,relwidth=0.9, height=28)
        self.PrixEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.PrixEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

        #Buttons Actions
        self.bouton_enregistrerPrix= Button(self.ClientForm,bg='white',text='Valider',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjoutPrix())
        self.bouton_enregistrerPrix.place(relx=0.1,rely=0.8,relwidth=0.3, height=30)

        self.bouton_ModifierPrix= Button(self.ClientForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:ModifierPrix())
        self.bouton_ModifierPrix.place(relx=0.45, rely=0.8,relwidth=0.3, height=30)

        def AjoutArticle():
            if self.NomArticleEntry.get()!="":
                if  self.verification.Verification(self.NomArticleEntry.get())==False :
                    pass
                else:
                    showwarning(self.config[0],'Vous avez entré des valeurs numériques')
            else :
                    showwarning(self.config[0],"Veuillez entrer le nom de l'article")

        def ModifierArticle():
            if self.NomArticleEntry.get()!="":
                if  self.verification.Verification(self.NomArticleEntry.get())==False :
                    pass
                else:
                    showwarning(self.config[0],'Vous avez entré des valeurs numériques')
            else :
                    showwarning(self.config[0],"Veuillez entrer le nom de l'article")
        
        def AjoutPrix():
            if self.ComboArticle.get()!="" and self.ComboArticle.get()!="" :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.ComboArticle.get())==False   :
                    pass
                else:
                    showwarning(self.config[0],'un de champs contient une inapropriée')
            else :
                    showwarning(self.config[0],"Veuillez remplir tout les champs")
        
        def ModifierPrix():
            if self.ComboArticle.get()!="" and self.ComboArticle.get()!="" :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.ComboArticle.get())==False   :
                    pass
                else:
                    showwarning(self.config[0],'un de champs contient une inapropriée')
            else :
                    showwarning(self.config[0],"Veuillez remplir tout les champs")
        
        
        
#---------------------------tableau articles et quantites globaux en stock ---------------------

    def TableauArticles(self,TailTabl):

        self.Contneur=Frame(self.RightContener,bg='#ebf4f5')
        self.Contneur.place(relx=0.00, rely=0.00,relwidth=0.5,relheight=1)

        self.SearchClient = Label(self.RightContener, text='Rechercher',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.00,rely=0.02)

        self.ComboArticle=Entry(self.RightContener, font =('Segoe UI',10),bg='white',relief='flat')
        self.ComboArticle.place(relx=0.1,rely=0.02,relwidth=0.3, height=26)

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

        self.title = Label(self.tabStockActuel, text="Identifiant", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.43)
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
                self.title1.place(relx=0.03, rely=0.25,relwidth=0.45)
                self.title2 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.45, rely=0.25,relwidth=0.4)

                # A revoir pour la modification
                self.title2.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(item[0]))
                self.title1.bind('<Double-Button-1>', lambda article=item[0]: HandleUpdateArticle(article))


                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.84,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.45)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white').place(relx=0.45, rely=0.25,relwidth=0.4)
                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.84,rely=0.25,relwidth=0.15, height=26)
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
    def DetailsStock(self,nomArticle,TailTabl):

        # ... other code ...

        self.Contneur = Frame(self.RightContener, bg='#ebf4f5')
        self.Contneur.place(relx=0.5, rely=0.00, relwidth=0.5, relheight=1)

        self.title_listeVente = Label(self.Contneur, text="TABLEAU DE PRIX DE  " + nomArticle, font=('Segoe UI bold', 12), fg='black', bg='#ebf4f5')
        self.title_listeVente.place(relx=0.2, rely=0.02)

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
        self.title = Label(self.tabStockActuel, text="Date Modification", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.43)
        self.title = Label(self.tabStockActuel, text="Prix ", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.47, rely=0.02, relwidth=0.4)

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
    
