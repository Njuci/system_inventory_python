from produit_backend import Product_back
from tkinter import *
from configuration import InfosApp
from fakeData import FakeData
from tkinter import ttk
from stock_backend import Stock_back
from verificationEntry import EntryVerification
from tkinter.messagebox import askyesno,showinfo,showwarning
from configuration import InfosApp
from stock_backend import Stock_back
class GestionStock :
    def __init__(self,fen,con):
        self.fen = fen
        self.db=con
        self.curseur=self.db.get_curseur()
        self.configApp=InfosApp
        self.FakeData=FakeData()
        self.config=self.configApp.Configuration(self)
        self.couleur=self.configApp.ColeursApp(self)
        self.verification=EntryVerification()
        self.id_asup=None

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
        self.NomArticle.bind("<KeyRelease>",lambda event: on_change(event))
        
        liste_valeur=[]
        product=Product_back('')
        self.listeArticles=product.get_all_produit(self.curseur)[1]
            #Formulaire clients
        self.AllArticles={}
        self.liste_valeur=[]
        if len(self.listeArticles)!=0:
            for i in (self.listeArticles):
                self.AllArticles[''+i[1]]=i[0]
                self.liste_valeur.append(i[1])
        self.NomArticle['values']=self.liste_valeur
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

        def on_change(event):
            # Get the current text from the entry widget
            input_str = self.NomArticle.get()
            # Filter the data based on the input
            filtered_data = [x for x in self.liste_valeur if x.startswith(input_str)]

            # Update the combobox values with the filtered data
            self.NomArticle['values'] = filtered_data
            print(filtered_data)

            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                    self.NomArticle.set(filtered_data[0])
            else :
                    self.NomArticle['values'] = filtered_data


        def AjouterStock():
            if self.PrixEntry.get()!="" and self.QuantEntry.get()!="" and self.NomArticle.get()!=""  :
                if  self.verification.Verification(self.PrixEntry.get()) and self.verification.Verification(self.QuantEntry.get()) :
                    stock=Stock_back(self.AllArticles[self.NomArticle.get()],self.QuantEntry.get(),self.PrixEntry.get())
                    if stock.add_stock(self.curseur):
                        showinfo('Ajout','Ajout Stock Réussi')
                        self.QuantiteGeneralStock(270)    
                        self.PrixEntry.delete(0,END)
                        self.QuantEntry.delete(0,END)
                        self.NomArticle.delete(0,END)

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

        self.title = Label(self.tabStockActuel, text="Nom article", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.5)
        self.title = Label(self.tabStockActuel, text="Qnt", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.55, rely=0.02, relwidth=0.1)


        y=0
        #Affichage des ventes dans le tableau
        #data=self.FakeData.dataArticleDisponible()
        stock=Stock_back('',0,0)
        data=stock.get_stock_restant(self.curseur)[1]
        t=0.1
        a=1
        for item in data:
            if a==1:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=13,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',8),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.3)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',8),fg='#adabab',bg='white').place(relx=0.4, rely=0.25,relwidth=0.3)
                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=item[0]:HandleClickDetails(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',8),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.54)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',8),fg='#adabab',bg='white').place(relx=0.6, rely=0.25,relwidth=0.1)
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

                self.title = Label(self.label, text = item[0], font = ('Segoe UI',8),fg='#adabab',bg='white').place(relx=0.03, rely=0.25,relwidth=0.54)
                self.title = Label(self.label, text =item[1], font = ('Segoe UI ',8),fg='#adabab',bg='white').place(relx=0.6, rely=0.25,relwidth=0.1)
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
                    self.DetailsStock(nomArticle,450)
                Capture()

    #Details stock 
    def DetailsStock(self,nomArticle,TailTabl):

        # ... other code ...

        self.Contneur = Frame(self.RightContener, bg='#ebf4f5')
        self.Contneur.place(relx=0.4, rely=0.00, relwidth=0.7, relheight=1)

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
        scrollbar.place(relx=0.8, rely=0.1, relheight=0.9)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # **Important:** Bind the content frame (`self.tabStockActuel`) to the canvas viewport
        # Variable to track the next item's y-position
        y = 0

        # Headers for the stock list
        self.title = Label(self.tabStockActuel, text="Date entrée", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.2)
        self.title = Label(self.tabStockActuel, text="Qnt ", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.24, rely=0.02, relwidth=0.1)

        self.title = Label(self.tabStockActuel, text="Date de sortie", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.345, rely=0.02, relwidth=0.2)
        self.title = Label(self.tabStockActuel, text="Qnt Sortie", font=('Segoe UI ', 9), fg='#416b70', bg='white').place(relx=0.55, rely=0.02, relwidth=0.15)

        # Loop to generate stock list items dynamically
        t = 0.1  # Initial vertical position for the first item
        data = self.FakeData.dataArticleDisponible()
        stock=Stock_back(nomArticle,0,0)
        data=stock.get_detail_stock_produit(self.curseur,stock.id_produit)[1]
        a=1
        for item in data:
            

            if a==1:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=10,width=TailTabl)
                self.label.place(relx=0.00, rely=0, relwidth=0.8, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=8)

                # Labels for article name and quantity
                self.title = Label(self.label, text='gfg', font=('Segoe UI', 10), fg='#adabab', bg='white').place(relx=0.03, rely=0.25, relwidth=0.43)
                self.title = Label(self.label, text="gfg", font=('Segoe UI ', 10), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.43)
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                # Labels for article name and quantity
                self.title = Label(self.label, text=item[1], font=('Segoe UI', 9), fg='#adabab', bg='white').place(relx=0.00, rely=0.25, relwidth=0.25)
                self.title = Label(self.label, text=item[2], font=('Segoe UI ', 9), fg='#adabab', bg='white').place(relx=0.26, rely=0.25, relwidth=0.13)
                self.title = Label(self.label, text=item[3], font=('Segoe UI', 9), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.25)
                self.title = Label(self.label, text=item[4], font=('Segoe UI ', 9), fg='#adabab', bg='white').place(relx=0.66, rely=0.25, relwidth=0.17)
                self.bouton_Sup= Button(self.label,bg='#961919',text='Sup',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Sup.place(relx=0.85,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Sup.configure( command=lambda stock=(item[5],item[4],nomArticle):SupprimerStock(stock))
                
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
                self.title = Label(self.label, text=item[1], font=('Segoe UI', 9), fg='#adabab', bg='white').place(relx=0.00, rely=0.25, relwidth=0.25)
                self.title = Label(self.label, text=item[2], font=('Segoe UI ', 9), fg='#adabab', bg='white').place(relx=0.26, rely=0.25, relwidth=0.13)
                self.title = Label(self.label, text=item[3], font=('Segoe UI', 9), fg='#adabab', bg='white').place(relx=0.4, rely=0.25, relwidth=0.25)
                self.title = Label(self.label, text=item[4], font=('Segoe UI ', 9), fg='#adabab', bg='white').place(relx=0.66, rely=0.25, relwidth=0.17)
                self.bouton_Sup= Button(self.label,bg='#961919',text='Sup',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Sup.place(relx=0.85,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Sup.configure( command=lambda stock=(item[5],item[4],nomArticle):SupprimerStock(stock))

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Button for details (optional, adapt placement as needed)
                # ... (place your button code here, adapting the placement as needed)

                t += 0.1  # Update vertical position for the next item

        # (Optional) Update the scroll
        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))

        def SupprimerStock(item):
        
        
            stock=Stock_back('',0,0)
            if askyesno('Suppression','Voulez-vous vraiment supprimer cet article du stock?'):
                if item[1]==0:
                    
                    if stock.del_stock(self.curseur,item[0]):
                        showinfo('Suppression','Suppression Réussie')
                        self.DetailsStock(item[2],450)
                    else:
                        showinfo('Suppression','Suppression Echouée')
                #Veuillez placer une boite de dialogue de demande d'avis d'utilisateur oui ou non
                else:
                    showinfo('Suppression','Impossible de supprimer ce stock de cet article car il a été vendu')
                    #Veuillez place une boite de dialogue de demande d'avis d'utilisateur oui ou non
        

    


