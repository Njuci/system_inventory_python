from tkinter import *
from configuration import InfosApp
from fakeData import FakeData
from verificationEntry import EntryVerification
from tkinter.messagebox import askyesno,showinfo,showwarning
from client_backend import Client_back
class GestionClient :
    def __init__(self,fen,con):
        self.fen = fen
        self.configApp=InfosApp
        self.db=con
        self.id_achange=None
        self.curseur=self.db.get_curseur()
        self.FakeData=FakeData()
        self.verification=EntryVerification()
        self.config=self.configApp.Configuration(self)

        self.couleur=self.configApp.ColeursApp(self)
        self.title_section1 = Label(self.fen, text = "Formulaire Client", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background']).place(x=20, y=20)
        self.title_section1 = Label(self.fen, text = "La liste de clients", font = ('Segoe UI bold',14),fg=self.couleur['CouleurTitreText'],bg=self.couleur['Background'])
        self.title_section1.place(relx=0.5, y=20)
        #Formulaire clients
        self.formulaireClient(['','','',''])

        #Conteneur des clients
        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.36, rely=0.1,relwidth=0.68,relheight=0.8)
        self.SearchClient = Label(self.fen, text='Rechercher',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.4,rely=0.12)

        self.EntrySearch=Entry(self.fen, font =('Segoe UI',10),bg='white',relief='flat')
        self.EntrySearch.place(relx=0.5,rely=0.12,relwidth=0.3, height=26)
        self.EntrySearch.bind("<KeyRelease>",self.on_SearchClient)

        client=Client_back('','')
        data=client.get_all_client(self.curseur)[1]
        self.TableauClients(560,data)

    def on_SearchClient(self,event):
            # Get the current text from the entry widget
            client=Client_back('','')
            data=client.get_all_client(self.curseur)[1]
            input_str =self.EntrySearch.get()
            # Filter the data based on the input
            
            filtered_data = [x for x in data if x[2].startswith(input_str)]
            # Update the combobox values with the filtered data
            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                   self.TableauClients(560,filtered_data)
            if input_str == " ":
                self.TableauClients(560,data)



    def formulaireClient(self,data):
        self.ClientForm=Frame(self.fen,bg='white')
        self.ClientForm.place(x=20, rely=0.1,relwidth=0.3,relheight=0.4)

        #Barre de recherche
        self.SearchClient = Label(self.ClientForm, text='Nom client',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.02)

        self.paddingEntry=Frame(self.ClientForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.15,relwidth=0.9, height=28)
        self.NomEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.NomEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

        #Infos clients
        self.SearchClient = Label(self.ClientForm, text='Num Tél',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.3)
  
        self.paddingEntry=Frame(self.ClientForm,bg='#ebf4f5')
        self.paddingEntry.place(relx=0.02,rely=0.4,relwidth=0.9, height=28)
        self.NumEntry=Entry(self.paddingEntry,relief='flat', font =('Segoe UI',10),bg='#ebf4f5')
        self.NumEntry.place(relx=0.02,rely=0.02,relwidth=0.96, height=26)

        self.NumEntry.insert(0,data[3])
        self.NomEntry.insert(0,data[2])
        self.id_achange=data[1]

        #Buttons Actions
        self.bouton_enregistrer= Button(self.ClientForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:AjoutClient())
        self.bouton_enregistrer.place(relx=0.1,rely=0.6,relwidth=0.3, height=30)

        self.bouton_Modifier= Button(self.ClientForm,bg='white',text='Modifier',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda:ModifierClient())
        self.bouton_Modifier.place(relx=0.5, rely=0.6,relwidth=0.3, height=30)

        def AjoutClient():
            if self.NomEntry.get()!="" or self.NumEntry.get()!="" :
                if  self.verification.Verification(self.NomEntry.get())==False and self.verification.Verification(self.NumEntry.get())==True :
                    client=Client_back(self.NomEntry.get(),self.NumEntry.get())
                    if client.add_client(self.curseur):
                        showinfo(self.config[0],'Client ajouté avec succès')
                        self.NomEntry.delete(0,END)
                        self.NumEntry.delete(0,END)      
                        client=Client_back('','')
                        data=client.get_all_client(self.curseur)[1]
                        self.TableauClients(560,data)
                else:
                    showwarning(self.config[0],'Veuillez respecter le type de données ')
            else :
                    showwarning(self.config[0],"Veuillez renseigner tout les champs")
        
        def ModifierClient():
            if self.NomEntry.get()!="" or self.NumEntry.get()!="" :
                if self.verification.Verification(self.NomEntry.get())==False and self.verification.Verification(self.NumEntry.get())==True :
                   
                    if self.id_achange!=None:
                        if askyesno("Modification","Voulez-vous vraiment modifier les cordonnées du client"):
                           client=Client_back(self.NomEntry.get(),self.NumEntry.get())
                           if client.update_client(self.curseur,self.id_achange):
                               showinfo("Succès","Client modifié") 
                            
                           self.NomEntry.delete(0,END)
                           self.NumEntry.delete(0,END)
                           self.id_achange=None
                           data=client.get_all_client(self.curseur)[1]
                           self.TableauClients(560,data)
                        
                        else:
                            
                            self.NomEntry.delete(0,END)
                            self.NumEntry.delete(0,END)
                            self.id_achange=None
                        
                        print(self.id_achange)
                
                else:
                    showwarning(self.config[0],'Veuillez respecter le type de données ')
            else :
                    showwarning(self.config[0],"Veuillez renseigner tout les champs")


    def TableauClients(self,TailTabl,dataClient):

        self.Contneur=Frame(self.RightContener,bg='#ebf4f5')
        self.Contneur.place(relx=0.00, rely=0.00,relwidth=0.8,relheight=1)



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

        self.title = Label(self.tabStockActuel, text="Noms", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.06, rely=0.02, relwidth=0.3)
        self.title = Label(self.tabStockActuel, text="Numéro Télephone", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.38, rely=0.02, relwidth=0.2)

        y=0
        #Affichage des ventes dans le tableau
        data=self.FakeData.dataArticleDisponible()
        data=dataClient
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

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Modifier',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.72,rely=0.25,relwidth=0.25, height=26)
                self.bouton_Detail.configure( command=lambda article=item[1]:HandleUpdateClient(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[2], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.03, rely=0.25,relwidth=0.35)
                self.title2 = Label(self.label, text =item[3], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.4, rely=0.25,relwidth=0.25)


                self.bouton_Detail= Button(self.label,bg='#961919',text='Supprimer',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Detail.place(relx=0.67,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item[1]:HandleDeleteClient(article))

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Modifier',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.84,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item:HandleUpdateClient(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)

                self.title1 = Label(self.label, text = item[2], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.03, rely=0.25,relwidth=0.35)
                self.title2 = Label(self.label, text =item[3], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.4, rely=0.25,relwidth=0.25)


                self.bouton_Detail= Button(self.label,bg='#961919',text='Supprimer',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Detail.place(relx=0.67,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item[1]:HandleDeleteClient(article))

                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Modifier',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.84,rely=0.25,relwidth=0.15, height=26)
                self.bouton_Detail.configure( command=lambda article=item:HandleUpdateClient(article))
                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                
            # (Optional) Update the scroll
            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
    


             
            def HandleClickDetails(nomArticle):
            #-----------------Details stock-----------------------
                print(nomArticle)
            
            #modification de l'article
            def HandleUpdateClient(data):
                
                
                self.formulaireClient(data)
            
            def HandleDeleteClient(id):
                # veuillez mettre la boite de dialogue de demande d'avis oui ou non
                if askyesno("Suppression Client","Voulez-vous vraiment supprimer ce client"):
                    client=Client_back('','')
                    #verifier si la somme des factures de ce client est egale a zero on le supprime sinon on affiche un message d'erreur
                    fact=client.get_facture_by_client(self.curseur,id)
                    if fact[0]==True:
                        if fact[1][0][2]==0:
                            if client.del_client(self.curseur,id):
                                showinfo("Succès","Client supprimé") 
                                client=Client_back('','')
                                data=client.get_all_client(self.curseur)[1]
                                self.TableauClients(560,data)
                        else:
                            showwarning("Erreur","Impossible de supprimer ce client car il a des factures, pour le supprimer, veuillez vous assurer que toutes ses factures sont Nulles")
                    else:
                        showwarning("Erreur","Impossible de supprimer ce client car il a des factures. pour le supprimer, veuillez vous assurer que toutes ses factures sont Nulles")
    #Details stock 