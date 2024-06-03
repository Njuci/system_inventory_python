
from tkinter import messagebox


class Prix_vente_back:
    def __init__(self,id_produit,montant):
        self.id_produit=id_produit
        self.montant=montant
    
    #add PV
    
    def add_prix_vente(self,curseur):
        try:
            curseur.execute('Insert into tb_prix_vente(id_produit,montant) values(%s,%s)',
                            (self.id_produit,self.montant))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du prix_x de vente  à la base de données : {e}')
            return False
        
 
    #get_dernier prix d'un produit
    def get_last_pv(self,curseur,id_produit):
        try:
            curseur.execute(f"SELECT id_pv FROM tb_prix_vente where id_produit='{id_produit}' order by(date_fixation) desc")
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #dans db
    def get_prix_vente(self,curseur,id_produit):
        try:
            curseur.execute(f"SELECT date_fixation,montant FROM tb_prix_vente where id_produit='{id_produit}' order by(date_fixation) desc")
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
        