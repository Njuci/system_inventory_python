from tkinter import *
from configuration import InfosApp
from produit_backend import Product_back
from fakeData import FakeData
from tkinter import ttk

from pv_back import Prix_vente_back
from verificationEntry import EntryVerification
from tkinter.messagebox import askyesno,showinfo,showwarning
class GestionArticle :
    def __init__(self,fen,con):
        self.fen = fen
        self.curseur=con.get_curseur()
        self.configApp=InfosApp
        self.FakeData=FakeData()
        self.couleur=self.configApp.ColeursApp(self)
        self.verification=EntryVerification()
        self.config=self.configApp.Configuration(self)
        self.id_art=None

        self.title_section1 = Label(self.fen, text = "Formulaire article", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background']).place(x=20, y=20)
        self.title_section1 = Label(self.fen, text = "Les articles disponibles", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background'])
        self.title_section1.place(relx=0.3, y=20)

        #-----------------------Formulaire gestion article -------------------
        self.FormulaireArticle("")

        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.3, rely=0.1,relwidth=0.68,relheight=0.8)

        #----------------------------Tab section -------------------------------
        product=Product_back('')
        #Affichage des ventes dans le tableau
        dataArticle=product.get_all_produit(self.curseur)
        self.TableauArticles(420,dataArticle)

        self.product=Product_back('')
        self.listeArticles=self.product.get_all_produit(self.curseur)[1]
        self.AllArticles={}
        self.ComboArticles=[]
        if len(self.listeArticles)!=0:
            for i in (self.listeArticles):
                self.AllArticles[''+i[1]]=i[0]
                self.ComboArticles.append(i[1])

        self.SearchClient = Label(self.fen, text='Rechercher',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.3,rely=0.12)

        self.ComboArticle=Entry(self.fen, font =('Segoe UI',10),bg='white',relief='flat')
        self.ComboArticle.place(relx=0.4,rely=0.12,relwidth=0.3, height=26)
        self.ComboArticle.bind("<KeyRelease>",self.on_SearchArticle)

        self.product=Product_back('')
        self.listeArticles=self.product.get_all_produit(self.curseur)[1]
        self.AllArticles={}
        self.ComboArticles=[]
        if len(self.listeArticles)!=0:
            for i in (self.listeArticles):
                self.AllArticles[''+i[1]]=i[0]
                self.ComboArticles.append(i[1])
    
        self.ComboArticle=ttk.Combobox(self.fen,values=self.ComboArticles)
        self.ComboArticle.place(relx=0.02,rely=0.55,width=280, height=26)
        self.ComboArticle.bind("<KeyRelease>",self.on_changeArticle)

    def on_changeArticle(self,event):
            # Get the current text from the entry widget
            input_str =self.ComboArticle.get()
            # Filter the data based on the input
            filtered_data = [x for x in self.ComboArticles if x.startswith(input_str)]
            # Update the combobox values with the filtered data
            self.ComboArticle['values'] = filtered_data
            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                   self.ComboArticle.set(filtered_data[0])
                   self.filtre_date=True
                   self.TableauArticles(530)

    def on_SearchArticle(self,event):
            # Get the current text from the entry widget
            product=Product_back('')
            #Affichage des ventes dans le tableau
            data=product.get_all_produit(self.curseur)
            input_str =self.ComboArticle.get()
            # Filter the data based on the input
            
            filtered_data = [x for x in data[1] if x[1].startswith(input_str)]
            print(filtered_data)
            # Update the combobox values with the filtered data
            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                    print(filtered_data)
                    self.TableauArticles(420,[0,filtered_data])
            if input_str == " ":
                self.TableauArticles(420,data)


    def FormulaireArticle(self,art):
        ValeurArticle=''
        #donnee de l'article
        def remplirDonnee():
            product=Product_back('')
            #Affichage des ventes dans le tableau
            dataArticle=product.get_all_produit(self.curseur)
            self.TableauArticles(420,dataArticle)
            self.FormulaireArticle("")

            self.product=Product_back('')
            self.listeArticles=self.product.get_all_produit(self.curseur)[1]
            self.AllArticles={}
            self.ComboArticles=[]
            if len(self.listeArticles)!=0:
                for i in (self.listeArticles):
                    self.AllArticles[''+i[1]]=i[0]
                    self.ComboArticles.append(i[1])

            self.ComboArticle=ttk.Combobox(self.fen,values=self.ComboArticles)
            self.ComboArticle.place(relx=0.02,rely=0.55,width=280, height=26)
            self.ComboArticle.bind("<KeyRelease>",self.on_changeArticle)
        
            
        def get_id_art(self):
            self.id_art=self.ComboArticle.get().split("|")[0]
    
            
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
        self.NomArticleEntry.insert(0,art)

        #Buttons Actions
        self.bouton_enregistrer= Button(self.ClientForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjoutArticle())
        self.bouton_enregistrer.place(relx=0.1,rely=0.28,relwidth=0.3, height=30)

        self.bouton_Modifier= Button(self.ClientForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:ModifierArticle())
        self.bouton_Modifier.place(relx=0.45, rely=0.28,relwidth=0.3, height=30)

        #Gestion de prix articles
        self.title_section1 = Label(self.ClientForm, text = "NOUVEAU PRIX ARTICLE", font = ('Segoe UI',10),fg=self.couleur['CouleurTitreText'],bg="white").place(relx=0.20, rely=0.4)
        
        self.SearchClient = Label(self.ClientForm, text='Nom Article',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.5)

        self.SearchClient = Label(self.ClientForm, text='Prix',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.62)

        self.paddingEntry=Frame(self.ClientForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.68,relwidth=0.9, height=28)
        self.PrixEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.PrixEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)



        #Buttons Actions
        self.bouton_enregistrerPrix= Button(self.ClientForm,bg='white',text='Valider',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjoutPrix())
        self.bouton_enregistrerPrix.place(relx=0.2,rely=0.8,relwidth=0.5, height=30)


        def DataSelected():
            print("cl :"+self.ComboArticle.get())
       

        def AjoutPrix():
            # Vérification des champs saisis
            if (not self.verification.Verification(self.PrixEntry.get())) or (not self.verification.Verification(self.ComboArticle.get())):
                prix_vente = Prix_vente_back(self.AllArticles[self.ComboArticle.get()], self.PrixEntry.get())
                if prix_vente.add_prix_vente(self.curseur):
                    showinfo('Succès', 'Le prix a été mis à jour')
                    remplirDonnee()
                    self.id_art = None
                else:
                    showwarning(self.config[0], 'Une erreur est survenue')
            else:
                showwarning(self.config[0], "Un des champs contient une valeur invalide")

        def AjoutArticle():
            if self.NomArticleEntry.get()!="":
                if  self.verification.Verification(self.NomArticleEntry.get())==False :
                    product=Product_back(self.NomArticleEntry.get())
                   
                   
                    if product.add_produit(self.curseur):
                        showinfo('Ajout','Article ajouté avec succès'
                                 )
                        remplirDonnee()
                        self.NomArticleEntry.delete(0,END)
                    else:
                        ra=0
                else:
                    showwarning(self.config[0],'Vous avez entré des valeurs numériques')
            else :
                    showwarning(self.config[0],"Veuillez entrer le nom de l'article")

        def ModifierArticle():
            if self.NomArticleEntry.get()!="":
                if  self.verification.Verification(self.NomArticleEntry.get())==False:
                    product=Product_back(self.NomArticleEntry.get())
                    if product.update_produit(self.curseur,self.id_art[1]):
                        showinfo('Modification','Article modifié avec succès')
                        remplirDonnee()
                        self.NomArticleEntry.delete(0,END)
                        self.id_art=None
                        
                        
                else:
                    self.id_art=None
                    showwarning(self.config[0],'Vous avez entré des valeurs numériques')
            else :
                    self.id_art=None
                    showwarning(self.config[0],"Veuillez entrer le nom de l'article")
        
            
        def ModifierPrix():
            if self.ComboArticle.get()!="" and self.ComboArticle.get()!="" :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.ComboArticle.get())==False   :
                    pass
                else:
                    showwarning(self.config[0],'un de champs contient une inapropriée')
            else :
                    showwarning(self.config[0],"Veuillez remplir tout les champs")
        
        
    
#---------------------------tableau articles et quantites globaux en stock ---------------------

    def TableauArticles(self,TailTabl,dataArticle):

        self.Contneur=Frame(self.RightContener,bg='#ebf4f5')
        self.Contneur.place(relx=0.00, rely=0.00,relwidth=0.6,relheight=1)

        #liste des produit en stock
        self.tabStockActuel=Frame(self.Contneur,bg='white')
        self.tabStockActuel.place(x=0.00, rely=0.1,relwidth=1,relheight=0.9)

        # Create a canvas to hold the scrollable content
        self.canvas =Canvas(self.tabStockActuel, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.tabStockActuel, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.95, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.title = Label(self.tabStockActuel, text="Identifiant", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.25)
        self.title = Label(self.tabStockActuel, text="Designation ", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.29, rely=0.02, relwidth=0.4)
        

        y=0
        data=dataArticle
        t=0.1
        a=1
        for item in data[1]:
            if a==1:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=13,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.3)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white').place(relx=0.6, rely=0.25,relwidth=0.3)

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=[item[1],item[0]]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.0, rely=0.25,relwidth=0.28)
                self.title2 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.3, rely=0.25,relwidth=0.45)

                self.bouton_Modifier= Button(self.label,bg='#ebf4f5',text='Modifier',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Modifier.place(relx=0.76,rely=0.25,relwidth=0.12, height=26)
                self.bouton_Modifier.configure( command=lambda article=[item[1],item[0]]:HandleUpdateArticle(article))

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.89,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Detail.configure( command=lambda article=[item[1],item[0]]:HandleClickDetails(article))
                
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[0], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.0, rely=0.25,relwidth=0.28)
                self.title2 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.3, rely=0.25,relwidth=0.45)

                self.bouton_Modifier= Button(self.label,bg='#ebf4f5',text='Modifier',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Modifier.place(relx=0.76,rely=0.25,relwidth=0.12, height=26)
                self.bouton_Modifier.configure( command=lambda article=[item[1],item[0]]:HandleUpdateArticle(article))

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Prix',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.89,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Detail.configure( command=lambda article=[item[1],item[0]]:HandleClickDetails(article))
                
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                
            # (Optional) Update the scroll
            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
        



            def HandleClickDetails(nomArticle):
            #-----------------Details stock-----------------------
               # print(nomArticle)
               
                def Capture():
                    self.DetailsStock(nomArticle,300)
                Capture()
            
            #modification de l'article
            def HandleUpdateArticle(nom):
                self.id_art=nom
                self.FormulaireArticle(nom[0])
            

    #Details stock 
    def DetailsStock(self,nomArticle,TailTabl):

        # ... other code ...

        self.Contneur = Frame(self.RightContener, bg='#ebf4f5')
        self.Contneur.place(relx=0.6, rely=0.00, relwidth=0.5, relheight=1)

        self.title_listeVente = Label(self.Contneur, text="Prix de " + nomArticle[0], font=('Segoe UI bold', 12), fg='black', bg='#ebf4f5')
        self.title_listeVente.place(relx=0.2, rely=0.02)

        # Create a frame to hold the actual list items (inside the canvas)
        self.tabStockActuel = Frame(self.Contneur, bg='white') 
        self.tabStockActuel.place(x=0.00, rely=0.1,relwidth=1,relheight=0.9)

        # Create a canvas to hold the scrollable content
        self.canvas =Canvas(self.tabStockActuel, bg='white', highlightthickness=0)
        self.canvas.place(relx=0.00, rely=0.1, relwidth=1, relheight=0.9)

        # Create a vertical scrollbar
        scrollbar =Scrollbar(self.tabStockActuel, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.place(relx=0.75, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # **Important:** Bind the content frame (`self.tabStockActuel`) to the canvas viewport
        # Variable to track the next item's y-position
        y = 0

        # Headers for the stock list
        self.title = Label(self.tabStockActuel, text="Date Modification", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.43)
        self.title = Label(self.tabStockActuel, text="Prix ", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.47, rely=0.02, relwidth=0.2)

        # Loop to generate stock list items dynamically
        t = 0.1  # Initial vertical position for the first item
        pv=Prix_vente_back('','')
        
        data = pv.get_prix_vente(self.curseur,nomArticle[1])[1]
        print(data)
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
                self.title = Label(self.label, text=item[0], font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.53)
                self.title = Label(self.label, text=item[1], font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.58, rely=0.25, relwidth=0.3)
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
                self.title = Label(self.label, text=item[0], font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.53)
                self.title = Label(self.label, text=item[1], font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.58, rely=0.25, relwidth=0.3)
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Button for details (optional, adapt placement as needed)
                # ... (place your button code here, adapting the placement as needed)

                t += 0.1  # Update vertical position for the next item

        # (Optional) Update the scroll
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
    
    def AjoutPrix(self):
            """Fonction permettant d'ajouter un nouveau prix de vente."""
            print(self.ComboArticle.get())

            if self.id_art is None:
                showwarning(self.config[0], "Veuillez sélectionner un article")
                return

            # Vérification des champs saisis
            if (not self.verification.Verification(self.PrixEntry.get())) or (not self.verification.Verification(self.ComboArticle.get())):
                prix_vente = Prix_vente_back(self.ComboArticle.get().split('|')[0], self.PrixEntry.get())
                if prix_vente.add_prix_vente(self.curseur):
                    showinfo('Succès', 'Le prix a été mis à jour')
                    self.remplirDonnee()
                    self.id_art = None
                else:
                    showwarning(self.config[0], 'Une erreur est survenue')
            else:
                showwarning(self.config[0], "Un des champs contient une valeur invalide")
