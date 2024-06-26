from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno,showinfo,showwarning
from configuration import InfosApp
from fakeData import FakeData
from verificationEntry import EntryVerification
from Rapport_Facture import FacturePDF
#from tkcalendar import DateEntry
from produit_backend import Product_back
from client_backend import Client_back
from facture_back import Facture_back
from pv_back import Prix_vente_back
from stock_backend import Stock_back
from vente_back import Vente_back

class GestionVente :
    def __init__(self,fen,con):
        self.fen = fen
        self.infosApp=InfosApp
        self.FakeData=FakeData()
        self.db=con
        self.curseur=self.db.get_curseur()
        self.RapportPDF=FacturePDF()
        self.title_section1 = Label(self.fen, text = "Formulaire de vente", font = ('Segoe UI bold',14),fg='black',bg='#ebf4f5').place(x=20, y=20)
        self.verification=EntryVerification()
        #Formulaire de vente
        self.listeArtticle=[]
        self.listeArticleFacture=[]
        self.FrameFacture=0
        self.EtatFacture=False
        self.FormulaireVente()
        self.select_facture=''
        #liste des articles supprimé
        self.listeArticleSupprime=[]
        self.listeArtticle2=[]
        self.listeChoix=[] 
        self.infos_detail_facture={}
        self.PanierArticle=0
        self.ArticleSupprimer=[]
        prod=Product_back('')
        data=prod.get_all_produit(self.curseur)[1]
        product_list=[]
        for i in data:
            product_list.append(i[0]+"|"+i[1])
        self.listeArtticle2=product_list

        self.AllArticle={}
        self.listeArtticle2=[]
        if len(data)!=0:
                for i in (data):
                    self.AllArticle[''+i[1]]=i[0]
                    self.listeArtticle2.append(i[1])


        #------------------------entete gauche---------------------------
                #-----------------------------------Conteneur gauche---------------------------------------
        self.RightContener=Frame(self.fen,bg='#ebf4f5')
        self.RightContener.place(relx=0.45, rely=0.1,relwidth=0.5,relheight=0.8)

        #Search vente
        self.SearchClient = Label(self.RightContener, text='TOTAL VENTE :',font =('Segoe UI bold',12),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.02,rely=0.02)


        self.title_listeVente = Label(self.RightContener, text = "Liste de vente", font = ('Segoe UI bold',12),fg='black',bg='#ebf4f5')
        self.title_listeVente.place(relx=0.02, rely=0.12)

        self.bouton_Rapport= Button(self.RightContener,bg='#416b70',text='Imprimer',relief='flat', font =('Segoe UI',9),fg='white',command=self.genererRapportJournalier)
        self.bouton_Rapport.place(relx=0.8,rely=0.02,relwidth=0.22, height=26)
        self.filtre_date=False
        #les filtres 
        self.SearchClient = Label(self.RightContener, text='Filtre :',font =('Segoe UI',10),fg='#adabab',bg='#ebf4f5')
        self.SearchClient.place(relx=0.3,rely=0.12)
        self.bouton_Plus= Button(self.RightContener,bg='#416b70',text='Toutes le ventes',relief='flat', font =('Segoe UI',9),fg='white',command=self.On_click_button)
        self.bouton_Plus.place(relx=0.4,rely=0.12,relwidth=0.22, height=26)

        self.ListeDateVente=ttk.Combobox(self.RightContener, font =('Segoe UI',10))
        self.ListeDateVente.place(relx=0.7,rely=0.12,relwidth=0.3, height=26)
        fact=Facture_back('')
        data=fact.get_distinct_date(self.curseur)[1]
        listeDate=[]
        for i in data:
            listeDate.append(i[0])
        self.ListeDateVente['values']=listeDate 
        self.ListeDateVente.bind("<<ComboboxSelected>>",self.On_element_selected)
        self.ListeDateVente.bind("<KeyRelease>",self.on_changeDate)
        self.dataDateFac=listeDate 

         #----------------------------Tab section -------------------------------
        self.TableauArticles(530)
        self.listeArtticle=[]
    def on_changeDate(self,event):
            # Get the current text from the entry widget
            input_str =self.ListeDateVente.get()
            # Filter the data based on the input
            filtered_data = [x for x in self.dataDateFac if x.startswith(input_str)]
            # Update the combobox values with the filtered data
            self.ListeDateVente['values'] = filtered_data
      
            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                   self.ListeDateVente.set(filtered_data[0])
                   self.filtre_date=True
                   self.TableauArticles(530)
            else:
                self.ListeDateVente['values'] = filtered_data


    def On_element_selected(self,event):
        self.filtre_date=True
        self.TableauArticles(530)
    
    def On_click_button(self):
        self.filtre_date=False
        self.TableauArticles(530)

    def genererRapportJournalier(self):
        if (self.ListeDateVente.get()==""):
            showwarning("GEST-DANIELLO","Veuillez selectionner la date de vente")
        else:
            fact=Facture_back('')
            data=fact.report_journey(self.curseur,self.ListeDateVente.get())
            self.RapportPDF.genererRapportJournalier(data[1],self.ListeDateVente.get())
        
    def FormulaireVente(self):
        #Formulaire de ventes 
        self.VenteForm=Frame(self.fen,bg='white')
        self.VenteForm.place(x=20, rely=0.1,relwidth=0.4,relheight=0.8)

        #Barre de recherche
        self.SearchClient = Label(self.VenteForm, text='AJOUT VENTE',bg='white',font = ('Segoe UI bold',14),fg='black')
        self.SearchClient.place(relx=0.02,rely=0.02,relwidth=1)


        #Infos clients
        self.SearchClient = Label(self.VenteForm, text='Nom Client',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.11)
        self.paddingEntry=Frame(self.VenteForm,bg='white')
        self.paddingEntry.place(relx=0.24,rely=0.1,relwidth=0.68, height=30)
        #get_client
        client=Client_back('','')
        clientData=client.get_all_client(self.curseur)[1]
      
       
        self.AllClients={}
        self.ComboClients=[]
        if len(clientData)!=0:
                for i in (clientData):
                    self.AllClients[''+i[2]]=i[1]
                    self.ComboClients.append(i[2])
        
        self.NomClient=ttk.Combobox(self.paddingEntry, font =('Segoe UI',10))
        self.NomClient.place(relx=0.00,rely=0.1,relwidth=0.99, height=26)
        self.NomClient['values']=self.ComboClients
        self.NomClient.bind("<<ComboboxSelected>>")
        self.NomClient.bind("<KeyRelease>",lambda event: on_change(event))

        #Buttons Actions
        self.bouton_enregistrer= Button(self.VenteForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=lambda :AddVente())
        self.bouton_enregistrer.place(relx=0.68,rely=0.02,relwidth=0.3, height=30)


        #Contenue details facture
        self.ligne=Frame(self.VenteForm,bg='#d6d4d4',height=-20)
        self.ligne.place(relx=0.02, rely=0.28,relwidth=0.9)
        nom=self.infosApp.Configuration(self)


        self.NumFact = Label(self.VenteForm, text='NOM ARTICLE',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.02,rely=0.2,relwidth=0.25)
        self.NumFact = Label(self.VenteForm, text='QUANT',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.35,rely=0.2,relwidth=0.16)
        self.NumFact = Label(self.VenteForm, text='Prix U.',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.52,rely=0.2,relwidth=0.14)

        self.NumFact = Label(self.VenteForm, text='Prix T.',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.67,rely=0.2,relwidth=0.14)

        self.bouton_Plus= Button(self.VenteForm,bg='#416b70',text='PRODUIT',relief='flat', font =('Segoe UI',9),fg='white',command=self.ShowForm)
        self.bouton_Plus.place(relx=0.81,rely=0.2,relwidth=0.11, height=26)
        

        if len(self.listeArtticle)!=0:
            self.articleContent=Frame(self.VenteForm,bg='white')
            self.articleContent.place(relx=0.02, rely=0.2,relwidth=0.5,relheight=2)
            #creation du scroll bar
   
        else :
            self.message = Label(self.VenteForm, text="pas d'articles selectionnés ",font =('Segoe UI',12),fg='#adabab',bg='white')
            self.message.place(relx=0.02,rely=0.68,relwidth=0.9)
        self.numberInput=0
        def on_change(event):
            # Get the current text from the entry widget
            input_str = self.NomClient.get()
            # Filter the data based on the input
            filtered_data = [x for x in self.ComboClients if x.startswith(input_str)]

            # Update the combobox values with the filtered data
            self.NomClient['values'] = filtered_data
   

            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                    self.NomClient.set(filtered_data[0])

        def AddVente():
            if(self.NomClient.get()!=""):
                if len(self.listeArtticle)!=0:
                    """                    from ajout_ventes import InventoryManagementSystem
                    fact=InventoryManagementSystem(self.db.db,self.listeArtticle)
                    
                    if fact.add_invoice(self.NomClient.get().split('|')[0]):
                        self.listeArtticle=[]
                        self.db.dn.autocommit=True"""
                    
                    self.transaction_ajout_facture2(self.AllClients[self.NomClient.get()])
                    self.FormulaireVente()
                    self.TableauArticles(530)
                    self.PanierArticle=0
                    showinfo(nom[0],'Succes')
                else :
                    showwarning(nom[0],'Veuillez ajouter les produits')
            else :
                showwarning(nom[0],'Veuillez remplir tout les champs')

        #--------------------Generation pdf ---------------------
#-----------------------------------Fin formulaire de vente-----------------------------------

#-------------------------------------------Visualisation de vente ------------------------------
    def SupprimerProduits(self,index,tot):
            result=askyesno("Confirmation","Voulez-vous vraiment supprimer ce produit sur cette Facture ?")
            #initialisation de la liste des produits
            
            info_total=Facture_back('').get_total_fact(self.curseur,self.select_facture)
          
            if info_total[0] and len(info_total[1])!=0:
                total=info_total
            else:
                total=(True, [('', 0.0)])
                
                
     
            inf=Facture_back('').get_client_by_id_fact(self.curseur,self.select_facture)[1][0]
          
            self.infos_detail_facture['num_fac']=self.select_facture
            self.infos_detail_facture['date_fac']=inf[1]
            self.infos_detail_facture['nom_client']=inf[0]      
            self.infos_detail_facture['total']=total[1][0][1]
            
            
            if result :
                self.listeArticleSupprime.append(self.listeArticleFacture[index])
                self.ArticleSupprimer.append(tot)
                self.listeArticleFacture.pop(index)
                self.EtatFacture=True
                
                self.FormulaireModificationVente()

# La fonction permettant de verifier s'il y a eu des modifications sur la facture 
    def closeDetails(self):
        if self.EtatFacture :
            result=askyesno("Confirmation","Voulez-vous enregsitrer les modifications  ?")
            if result :
                supr_vente=Vente_back('','','','','')
                
                if len(self.listeArticleSupprime)!=0:
                    for i in self.listeArticleSupprime:
                        
                        if supr_vente.del_vente(self.curseur,i[0]):
                            f=True
                      
                showinfo('Confirmation','Modification enregistrée')    
                self.FormulaireVente()
                self.ArticleSupprimer=[]
                self.EtatFacture=False      
                   
            else :
                self.FormulaireVente()
                self.ArticleSupprimer=[]
                self.EtatFacture=False
        else :
                self.FormulaireVente()
                self.EtatFacture=False

# La fonction d'enregistrement des modifications sur facture 
    
    def UpdateFacture(self):
        pass
        


    def ActualiserDetails(self):
        if len(self.ArticleSupprimer)==0 :
            self.NomCli = Label(self.VenteForm, text="0 $",font =('Segoe UI bold',10),fg='red',bg='white')
            self.NomCli.place(relx=0.35,rely=0.32)
        else:
            # calcul de somme total deja supprimee
            total=0
            for item in self.ArticleSupprimer:
                total+=item
            self.NomCli = Label(self.VenteForm, text=f"{total} $",font =('Segoe UI bold',10),fg='red',bg='white')
            self.NomCli.place(relx=0.35,rely=0.32)
        if len(self.listeArticleFacture)!=0:

            self.Articles=Frame(self.FrameFacture,bg='white')
            self.Articles.place(x=0, rely=0.48,relwidth=1,height=130)

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
            a=0
            #if (len(self.listeArtticle)<5):
            
            for item in (self.listeArticleFacture):
                if a<1:
                    self.label = Frame(self.canvas, bg='white',height=13)
                    self.label.place(relx=0.0, rely=0, relwidth=1, relheight=0.1)

                    self.Idlab=Label(self.label,font =('Segoe UI',10),text="")
                    self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.28, relheight=0.7)
                    self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text="")
                    self.nomArt.place(relx=0.29,rely=0.0,relwidth=0.39, relheight=0.7)

                    self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text="")
                    self.Qnt.place(relx=0.69,rely=0.0,relwidth=0.16, relheight=0.7)
                    self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text='')
                    self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, relheight=0.7)

                    self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                    self.incr+=0.2

                    window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                    y += self.label.winfo_reqheight() + 5

                    self.label = Frame(self.canvas, bg='white',height=40,width=380)
                    self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                    self.Idlab=Label(self.label,font =('Segoe UI',10),text=item[1],bg='white')
                    self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.35, relheight=0.7)
                    self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text=item[3])
                    self.nomArt.place(relx=0.37,rely=0.0,relwidth=0.16, relheight=0.7)

                    self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[2]}$")
                    self.Qnt.place(relx=0.54,rely=0.0,relwidth=0.16, relheight=0.7)
                    self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[4]} $")
                    self.Prix.place(relx=0.71,rely=0.0,relwidth=0.16, relheight=0.7)

                    self.Sup=Label(self.label,font =('Segoe UI',10),text="Sup",bg='#961919',fg="white")
                    self.Sup.place(relx=0.89,rely=0.0,relwidth=0.1, relheight=0.7)
                    self.Sup.bind('<Button-1>', lambda event,ide=index,tot=item[4]: self.SupprimerProduits(ide,tot))

                    self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                    self.incr+=0.2
                    index+=1

                    window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                    y += self.label.winfo_reqheight() + 5

                    a=+1
                else :
                    self.label = Frame(self.canvas, bg='white',height=40,width=380)
                    self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                    self.Idlab=Label(self.label,font =('Segoe UI',10),text=item[1],bg='white')
                    self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.35, relheight=0.7)
                    self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text=item[3])
                    self.nomArt.place(relx=0.37,rely=0.0,relwidth=0.16, relheight=0.7)

                    self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[2]}$")
                    self.Qnt.place(relx=0.54,rely=0.0,relwidth=0.16, relheight=0.7)
                    self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[4]}$")
                    self.Prix.place(relx=0.71,rely=0.0,relwidth=0.16, relheight=0.7)

                    self.Sup=Label(self.label,font =('Segoe UI',10),text="Sup",bg='#961919',fg="white")
                    self.Sup.place(relx=0.89,rely=0.0,relwidth=0.1, relheight=0.7)
                    self.Sup.bind('<Button-1>', lambda event,ide=index,tot=item[4]: self.SupprimerProduits(ide,tot))


                    self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                    self.incr+=0.2
                    index+=1

                    window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                    y += self.label.winfo_reqheight() + 5



            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
            
                #creation du scroll bar
        else :
            self.message = Label(self.VenteForm, text="pas d'articles pour cette vente",font =('Segoe UI',12),fg='#adabab',bg='white')
            self.message.place(relx=0.02,rely=0.68,relwidth=0.9)

    def FormulaireModificationVente(self):
        #Formulaire de ventes 
        self.VenteForm=Frame(self.fen,bg='white')
        self.VenteForm.place(x=20, rely=0.1,relwidth=0.4,relheight=0.8)
 
        #Barre de recherche
        self.SearchClient = Label(self.VenteForm, text='DETAILS VENTE ',bg='white',font = ('Segoe UI bold',12),fg='black')
        self.SearchClient.place(relx=0.02,rely=0.02,relwidth=1)

        self.bouton_Imprimer= Button(self.VenteForm,bg='#416b70',text='Imprimer',relief='flat', font =('Segoe UI',9),fg='white',command=lambda:genererFacture())
        self.bouton_Imprimer.place(relx=0.70,rely=0.02,relwidth=0.2, height=30)


        #Infos clients
        self.SearchClient = Label(self.VenteForm, text='Numéro Facture',font =('Segoe UI',10),fg='black',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.11)

        self.NumFact = Label(self.VenteForm, text=self.infos_detail_facture['num_fac'],font =('Segoe UI',10),fg='black',bg='white')
        self.NumFact.place(relx=0.3,rely=0.11)

        self.SearchClient = Label(self.VenteForm, text='Date vente',font =('Segoe UI',10),fg='black',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.15)

        self.DateFact = Label(self.VenteForm, text=self.infos_detail_facture['date_fac'],font =('Segoe UI',10),fg='black',bg='white')
        self.DateFact.place(relx=0.3,rely=0.15)

        self.SearchClient = Label(self.VenteForm, text='Nom client',font =('Segoe UI',10),fg='black',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.2)

        self.NomCli = Label(self.VenteForm, text=self.infos_detail_facture['nom_client'],font =('Segoe UI',10),fg='black',bg='white')
        self.NomCli.place(relx=0.3,rely=0.2)

        self.SearchClient = Label(self.VenteForm, text='Montan total',font =('Segoe UI',10),fg='black',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.25)

        self.NomCli = Label(self.VenteForm, text=f'{self.infos_detail_facture['total']} $',font =('Segoe UI bold',14),fg='black',bg='white')
        self.NomCli.place(relx=0.3,rely=0.25)

        self.SearchClient = Label(self.VenteForm, text='Total Produit(s) Suprimé ',font =('Segoe UI',10),fg='black',bg='white')
        self.SearchClient.place(relx=0.02,rely=0.32)

        #Buttons Actions
        self.bouton_enregistrer= Button(self.VenteForm,bg='white',text='Enregistrer',relief='groove', font =('Segoe UI',9),fg='#416b70',command=self.closeDetails)
        self.bouton_enregistrer.place(relx=0.28,rely=0.9,relwidth=0.2, height=30)

        self.bouton_Modifier= Button(self.VenteForm,bg='white',text='Retour',relief='groove', font =('Segoe UI',9),fg='#416b70',command=self.closeDetails)
        self.bouton_Modifier.place(relx=0.49,rely=0.9,relwidth=0.2, height=30)


        #Contenue details facture
        self.ligne=Frame(self.VenteForm,bg='#d6d4d4',height=-20)
        self.ligne.place(relx=0.02, rely=0.45,relwidth=0.9)
        nom=self.infosApp.Configuration(self)


        self.NumFact = Label(self.VenteForm, text='NOM ARTICLE',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.02,rely=0.38,relwidth=0.25)
        self.NumFact = Label(self.VenteForm, text='QUANT',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.35,rely=0.38,relwidth=0.16)
        self.NumFact = Label(self.VenteForm, text='Prix U.',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.52,rely=0.38,relwidth=0.14)

        self.NumFact = Label(self.VenteForm, text='Prix T.',font =('Segoe UI',10),fg='#adabab',bg='white')
        self.NumFact.place(relx=0.67,rely=0.38,relwidth=0.14)
       
 
        self.FrameFacture=self.VenteForm
        self.ActualiserDetails()

        def genererFacture():
            result=askyesno("Confirmation","Voulez-vous imprimer  ?")
            if result :
                if len(self.listeArticleFacture)!=0:
                    self.RapportPDF.genererFacture([self.infos_detail_facture,self.listeArticleFacture])
                else :
                    showwarning(nom[0],'Cette facture n\'a pas des produits')
            else :
                pass

       

#-------------------------------------------Fin visualisation vente -----------------------------

    


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

        self.title = Label(self.tabStockActuel, text="Num Facture", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.03, rely=0.02, relwidth=0.18)
        self.title = Label(self.tabStockActuel, text="Date vente", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.22, rely=0.02, relwidth=0.18)
        self.title = Label(self.tabStockActuel, text="Nom client", font=('Segoe UI ', 10), fg='#416b70', bg='white').place(relx=0.41, rely=0.02, relwidth=0.26)


        y=0
        #Affichage des ventes dans le tableau
        if self.filtre_date:
            fact=Facture_back('')
            data=fact.get_fact_by_date(self.curseur,self.ListeDateVente.get())[1]
            total=fact.get_total_all_fact_for_date(self.curseur,self.ListeDateVente.get())[1][0][0]
            dataa=fact.get_fact_by_date(self.curseur,self.ListeDateVente.get())
         
            if total==None:
                total=0.0
            self.LabelTotal=Label(self.RightContener,text=str(total)+"$",font =('Segoe UI bold',12),bg='#ebf4f5')
            self.LabelTotal.place(relx=0.2,rely=0.02,relwidth=0.2)
        else:
                
            fact=Facture_back('')
            data=fact.get_all_fact(self.curseur)[1]
            total=fact.get_total_all_fact(self.curseur)[1][0][0]
            if total==None:
                total=0.0
            self.LabelTotal=Label(self.RightContener,text=str(total)+"$",font =('Segoe UI bold',12),bg='#ebf4f5')
            self.LabelTotal.place(relx=0.2,rely=0.02,relwidth=0.2)
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

                self.title1 = Label(self.label, text =item[2], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.00, rely=0.25,relwidth=0.2)
                self.title2 = Label(self.label, text =item[0], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.21, rely=0.25,relwidth=0.2)
                self.title3 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title3.place(relx=0.42, rely=0.25,relwidth=0.3)


                # A revoir pour la modification
                self.title2.bind('<Button-1>', lambda article=item[0]: HandleUpdateArticle(item[0]))
                self.title1.bind('<Button-1>', lambda article=item[0]: HandleUpdateArticle(article))


                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.73,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Detail.configure( command=lambda article=item[2]:HandleClickDetails(article))
                self.bouton_Sup= Button(self.label,bg='#961919',text='Sup',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Sup.place(relx=0.85,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Sup.configure( command=lambda article=item[2]:HandleClickDelete(article))

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                a=0
            else:
                # Create a frame for each item
                self.label = Frame(self.canvas, bg='white',height=40,width=TailTabl)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)
                ligne = Frame(self.label, bg='#d6d4d4', height=-20).place(relx=0.0, rely=0.1, relwidth=1)


                self.title1 = Label(self.label, text =item[2], font = ('Segoe UI',10),fg='#adabab',bg='white')
                self.title1.place(relx=0.00, rely=0.25,relwidth=0.2)
                self.title2 = Label(self.label, text =item[0], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title2.place(relx=0.21, rely=0.25,relwidth=0.2)
                self.title3 = Label(self.label, text =item[1], font = ('Segoe UI ',10),fg='#adabab',bg='white')
                self.title3.place(relx=0.42, rely=0.25,relwidth=0.3)


                # A revoir pour la modification
                self.title2.bind('<Button-1>', lambda article=item[0]: HandleUpdateArticle(item[0]))
                self.title1.bind('<Button-1>', lambda article=item[0]: HandleUpdateArticle(article))


                self.bouton_Detail= Button(self.label,bg='#ebf4f5',text='Détails',relief='flat', font =('Segoe UI',9),fg='#adabab')
                self.bouton_Detail.place(relx=0.73,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Detail.configure( command=lambda article=item[2]:HandleClickDetails(article))

                self.bouton_Sup= Button(self.label,bg='#961919',text='Sup',relief='flat', font =('Segoe UI',9),fg='white')
                self.bouton_Sup.place(relx=0.85,rely=0.25,relwidth=0.1, height=26)
                self.bouton_Sup.configure( command=lambda article=item[2]:HandleClickDelete(article))

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5
                
            # (Optional) Update the scroll
            self.canvas.update_idletasks()
            self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))

            def HandleClickDelete(nomArticle):
              
                
            #-----------------Details stock-----------------------
                if self.EtatFacture :
                    result=askyesno("Confirmation","Voulez-vous enregsitrer les modifications  ?")
                    if result :
                        # veuillez supprimer tous les produits sur la facture et ajouter de nouveau les produits qui se 
                        
                        fact=Facture_back("")
                        total=fact.get_total_fact(self.curseur,nomArticle)[1][0][1]
                        if total==0 or total==None:
                            fact.del_fact(self.curseur,nomArticle)
                            #affi
                            showinfo("Suppression Réussi",f"Vous avez supprimé la facture {nomArticle}")
                        else:
                            showwarning("Echec de suppression","Veuillez vous assurer que la facture a un solde de 0.0")
                            
                        # trouvent dans la liste apres modification  voici la liste self.listeArticleFacture
                        pass
                    else :
                        self.FormulaireModificationVente()
                        self.EtatFacture=False
                else :
                    result=askyesno("Confirmation","Voulez-vous supprimer cette facture  ?")
                    if result :
                        
                        
                        fact=Facture_back("")
                        if len(fact.get_total_fact(self.curseur,nomArticle)[1])!=0:
                            total=fact.get_total_fact(self.curseur,nomArticle)[1][0][1]
                        else:
                            total=0
                        if total==0 or total==None:
                            fact.del_fact(self.curseur,nomArticle)
                            #affi
                            showinfo("Suppression Réussi",f"Vous avez supprimé la facture {nomArticle}")
                            self.TableauArticles(530)
                        else:
                            showwarning("Echec de suppression","Veuillez vous assurer que la facture a un solde de 0.0")
                        # Ajouter le script pour supprimer une vente
                        

        

            def HandleClickDetails(nomArticle):
              
                self.select_facture=nomArticle
            #-----------------Details stock-----------------------
            
                info_total=Facture_back('').get_total_fact(self.curseur,self.select_facture)
                if info_total[0] and len(info_total[1])!=0:
                    total=info_total
                else:
                    total=(True, [('', 0.0)])

                inf=Facture_back('').get_client_by_id_fact(self.curseur,self.select_facture)[1][0]
            
                self.infos_detail_facture['num_fac']=self.select_facture
                self.infos_detail_facture['date_fac']=inf[1]
                self.infos_detail_facture['nom_client']=inf[0]
                self.infos_detail_facture['total']=total[1][0][1]
                self.listeArticleFacture=Facture_back('').get_item_by_id_fact(self.curseur,self.select_facture)[1]
                if self.EtatFacture :
                    result=askyesno("Confirmation","Voulez-vous enregsitrer les modifications  ?")
                    if result :
                        # veuillez supprimer tous les produits sur la facture et ajouter de nouveau les produits qui se 
                        # trouvent dans la liste apres modification  voici la liste self.listeArticleFacture
                        pass
                    else :
                        self.FormulaireModificationVente()
                        self.EtatFacture=False
                else :
                        self.FormulaireModificationVente()
                        self.EtatFacture=False
              
            
            #modification de l'article
            def HandleUpdateArticle(nom):
                self.FormulaireArticle(['empty'],nom)

    #Details stock 


    def SupprimerproduitSurDetails(self,index,tot):
            result=askyesno("Confirmation","Voulez-vous vraiment supprimer ce produit sur cette vente ?")
            if result :
                self.listeArtticle.pop(index)
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
        a=0
        #if (len(self.listeArtticle)<5):
        
        for item in (self.listeArtticle):
            if a<1:

                self.label = Frame(self.canvas, bg='white',height=13,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text="")
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.28, relheight=0.7)
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text="")
                self.nomArt.place(relx=0.29,rely=0.0,relwidth=0.39, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text="")
                self.Qnt.place(relx=0.69,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text='')
                self.Prix.place(relx=0.85,rely=0.0,relwidth=0.16, relheight=0.7)

                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                self.label = Frame(self.canvas, bg='white',height=40,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text=item[1],bg='white')
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.35, relheight=0.7)
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text=item[2])
                self.nomArt.place(relx=0.37,rely=0.0,relwidth=0.16, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[3]}$")
                self.Qnt.place(relx=0.54,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[4]} $")
                self.Prix.place(relx=0.71,rely=0.0,relwidth=0.16, relheight=0.7)

                self.Sup=Label(self.label,font =('Segoe UI',10),text="SUP",bg='red',fg="white")
                self.Sup.place(relx=0.89,rely=0.0,relwidth=0.1, relheight=0.7)
                self.Sup.bind('<Button-1>', lambda event,ide=index,tot=item[3]*item[4]: self.SupprimerproduitSurDetails(ide,tot))

                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2
                index+=1

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5

                a=+1
            else :
                self.label = Frame(self.canvas, bg='white',height=40,width=380)
                self.label.place(relx=0.02, rely=0, relwidth=1, relheight=0.1)

                self.Idlab=Label(self.label,font =('Segoe UI',10),text=item[1],bg='white')
                self.Idlab.place(relx=0.0,rely=0.0,relwidth=0.35, relheight=0.7)
                self.nomArt=Label(self.label,font =('Segoe UI',10),bg='white',text=item[2])
                self.nomArt.place(relx=0.37,rely=0.0,relwidth=0.16, relheight=0.7)

                self.Qnt=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[3]}$")
                self.Qnt.place(relx=0.54,rely=0.0,relwidth=0.16, relheight=0.7)
                self.Prix=Label(self.label,font =('Segoe UI',10),bg='white',text=f"{item[4]} $")
                self.Prix.place(relx=0.71,rely=0.0,relwidth=0.16, relheight=0.7)

                self.Sup=Label(self.label,font =('Segoe UI',10),text="SUP",bg='red',fg="white")
                self.Sup.place(relx=0.89,rely=0.0,relwidth=0.1, relheight=0.7)
                self.Sup.bind('<Button-1>', lambda event,ide=index,tot=item[3]*item[4]: self.SupprimerproduitSurDetails(ide,tot))


                self.ligne=Frame(self.label,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)
                self.incr+=0.2
                index+=1

                window_id = self.canvas.create_window(20, y, anchor=W, window=self.label)  # Adjust x-position (20 here) as needed
                y += self.label.winfo_reqheight() + 5



        self.canvas.update_idletasks()
        self.canvas.config(scrollregion=(0, 0, self.canvas.winfo_width(), self.canvas.winfo_height() + y))
        



    #Fonction pour le vider les champs 
    def ViderChamps(self):
        self.inputIDPro.delete(0,END)
        self.inputQnt.delete(0,END) 

    #Fonction d'ajout d'articles
    def AddArticle(self):
        n=self.infosApp.Configuration(self)
        if(self.inputIDPro.get()!=""  or self.inputQnt.get()!="" ):
            if self.verification.Verification(self.inputQnt.get()):
                #voir leprix 
                price=Prix_vente_back("",0).get_prix_vente(self.curseur,self.AllArticle[self.inputIDPro.get()])
                if(len(price[1])==0):
                    showwarning("Daniello_Gest-Vente&Stock","il n'y a pas de prix pour cet article !")
                else:
                    h=[self.AllArticle[self.inputIDPro.get()],self.inputIDPro.get(),self.inputQnt.get(),price[1][0][1],int(self.inputQnt.get())*price[1][0][1]]
                    if self.PanierArticle<10:
                        if any(h[0] == el[0] for el in self.listeArtticle ):
                            showwarning(n[0],'Vous avez déjà ajouter cet article !!')
                        else :
                            self.PanierArticle+=1
                            self.listeArtticle.append(h)
                            self.Total_fac()
                            #effqcer l'article de la liste2
                            self.actualiser()
                            self.ViderChamps()
                    else:
                        showwarning(n[0],'Vous avez déjà atteint 10 articles !!')

            else :
                showwarning(n[0],'La quantité doit être un entier')

        else :
            showwarning(n[0],'Veuillez remplir tout les champs')

    def ShowForm(self):
        if len(self.listeArtticle)==0:
            self.bouton_Plus= Button(self.VenteForm,bg='#ebf4f5',text='Ajouter',relief='flat', font =('Segoe UI',9),fg='#adabab',command=self.AddArticle)
            self.bouton_Plus.place(relx=0.81,rely=0.0,relwidth=0.11, height=26)

            self.articleContent=Frame(self.VenteForm,bg='white')
            self.articleContent.place(relx=0.02, rely=0.1,relwidth=0.9,relheight=2)

            self.ContLigne=Frame(self.articleContent,bg='white')
            self.ContLigne.place(x=0, rely=0.00,relwidth=1,height=33)
            #####

            self.inputID
                         
        pass

    def onselect(self,evt):
        values=self.inputID.get()
        
    def ShowForm(self):
        if len(self.listeArtticle)==0:
            self.bouton_Plus= Button(self.VenteForm,bg='#ebf4f5',text='Ajouter',relief='flat', font =('Segoe UI',9),fg='#adabab',command=self.AddArticle)
            self.bouton_Plus.place(relx=0.81,rely=0.2,relwidth=0.11, height=26)

            self.articleContent=Frame(self.VenteForm,bg='white')
            self.articleContent.place(relx=0.02, rely=0.3,relwidth=0.9,relheight=2)

            self.ContLigne=Frame(self.articleContent,bg='white')
            self.ContLigne.place(x=0, rely=0.00,relwidth=1,height=33)
            #####

            self.inputIDPro=ttk.Combobox(self.ContLigne,font =('Segoe UI',10))
            self.inputIDPro.place(relx=0.0,rely=0.0,relwidth=0.35, height=26)
            self.inputIDPro['values']=self.listeArtticle2
            self.inputIDPro.bind("<KeyRelease>",self.on_changeCombo)

            

            self.inputQnt=Entry(self.ContLigne,font =('Segoe UI',10),bg='white')
            self.inputQnt.place(relx=0.38,rely=0.0,relwidth=0.16, height=26)
            self.Prix=Label(self.ContLigne,font =('Segoe UI',10),bg='white',text='')
            self.Prix.place(relx=0.55,rely=0.0,relwidth=0.16, height=26)
            self.PrixT=Label(self.ContLigne,font =('Segoe UI',10),bg='white',text='')
            self.PrixT.place(relx=0.72,rely=0.0,relwidth=0.16, height=26)
            self.ligne=Frame(self.ContLigne,bg='#d6d4d4',height=-20).place(x=0, rely=0.9,relwidth=1)

            #Ligne de total
            self.TitreTotal=Label(self.VenteForm,font =('Segoe UI bold',12),bg='white',text='Total')
            self.TitreTotal.place(relx=0.00,rely=0.8,relwidth=0.15, height=26)
            self.Total_fac()
    def on_changeCombo(self,event):
            # Get the current text from the entry widget
            input_str =self.inputIDPro.get()
            # Filter the data based on the input
            filtered_data = [x for x in self.listeArtticle2 if x.startswith(input_str)]
            # Update the combobox values with the filtered data
            self.inputIDPro['values'] = filtered_data
            # Clear the combobox selection if no matches
            if filtered_data:
                if(len(filtered_data)<=2):
                   self.inputIDPro.set(filtered_data[0])
    def Total_fac(self):
        if len(self.listeArtticle)==0:
            self.TitreTotal=Label(self.VenteForm,font =('Segoe UI bold',12),bg='white',text='00 $')
            self.TitreTotal.place(relx=0.5,rely=0.8,relwidth=0.6, height=26)
        else:
            total=0
            for i in self.listeArtticle:
                total+=i[4]
            
            self.TitreTotal=Label(self.VenteForm,font =('Segoe UI bold',12),bg='white',text= str(total)+'$')
            self.TitreTotal.place(relx=0.5,rely=0.8,relwidth=0.6, height=26)

# 
    def transaction_ajout_facture2(self, client_id):
      
        fact = Facture_back(client_id)
        try:
            # Start transaction
            self.db.db.autocommit = False
            self.db.db.start_transaction()
            if fact.add_fact(self.curseur):
                self.curseur.execute('SELECT MAX(id_facture) FROM tb_facture')
                fact_id = self.curseur.fetchone()[0]
              

                # Record each sale
                for item in self.listeArtticle:
                    # Retrieve the selling price
                    prix = Prix_vente_back("", 0).get_last_pv(self.curseur, item[0])[1][0][0]
                 

                    # Verify stock availability
                    quantite_demande = int(item[2])
                    
                    stock=Stock_back("",0,0)
                    # Vérification de la disponibilité du stock et interaction avec l'utilisateur
                    quantite_restante = stock.get_stock_restant_produit(self.curseur, item[0])[1][1]
                    nom_produit = stock.get_stock_restant_produit(self.curseur, item[0])[1][0]
                    if quantite_restante < quantite_demande:
                        # Demander à l'utilisateur s'il veut prendre la quantité restante
                        prendre_tout = askyesno("Stock insuffisant", f'La quantité restante pour le produit "{nom_produit}" est inférieure à la quantité demandée ({quantite_demande}).\nVoulez-vous prendre tout le stock restant ({quantite_restante}) ?')
                        if prendre_tout:
                            quantite_demande = quantite_restante  # Ajuster la quantité demandée à la quantité restante
                        else:
                            continue  # Passer à l'article suivant sans effectuer de vente pour cet article

                    # Suite de la logique pour effectuer la vente...
                    
                    quantite_dispo, stock =self.chercher_stock_fifo(item[0])
                    
                   
                    

                    # Check if stock is sufficient
                    if quantite_dispo >= quantite_demande:
                        vente = Vente_back(item[0], stock, fact_id, prix, quantite_demande)
                        vente.add_vente(self.curseur)
                    
                    else:
                        # Handle insufficient stock using FIFO
                        while quantite_dispo < quantite_demande:
                            vente = Vente_back(item[0], stock, fact_id, prix, quantite_dispo)
                            vente.add_vente(self.curseur)
                            quantite_demande -= quantite_dispo
                            quantite_dispo, stock = self.chercher_stock_fifo(item[0])
                            if stock is None:
                                break  # No more stock available
                            else:
                                vente = Vente_back(item[0], stock, fact_id, prix, quantite_demande)
                                vente.add_vente(self.curseur)


                # Commit transaction
                self.db.db.commit()
                self.listeArtticle = []
                return True
            else:
                return False  # Provide a reason for failure
        except Exception as e:
            # Rollback in case of error
            self.db.db.rollback()
            showwarning("Erreur", "Erreur lors de l'enregistrement de la facture: " + str(e))
            return False
        finally:
            # Ensure autocommit is reset
            self.db.db.autocommit = True

    # Define the chercher_stock_fifo function outside the loop
    def chercher_stock_fifo(self, id_produit):
        # Implement FIFO logic here
        # ...
        stock=Stock_back("",0,0).get_stock_dispo_id(self.curseur,id_produit)[1][0]
                            #verifier si le stock est suffisant
                      
                            
                            
        quantite_info=Stock_back("",0,0).get_stock_ecoule(self.curseur,stock[1])[1][0]
     

        quantite_dispo=quantite_info[2]-quantite_info[3]
                         
        return quantite_dispo,stock[1]
                            