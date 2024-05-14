


from tkinter import messagebox


class Product_back:
    def __init__(self,nom_produit):
        self.nom_produit = nom_produit
    #function to add a product
    def add_produit(self,curseur):
        try:
            curseur.execute('INSERT INTO tb_produit(designation_produit) VALUES(%s)', (self.nom_produit))
            
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            curseur.rollback()
            return False
    #function update a informations 
    def update_produit(self,curseur,id_produit):
        try:
            curseur.execute('UPDATE tb_produit SET designation_produit=%s WHERE id_produit=%s',(id_produit))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            curseur.rollback()
            return False
        
    #function TO del 
    def del_produit(self,curseur,id):
        try:
            curseur.execute('DELETE FROM tb_produit WHERE id_produit=%s',(id))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            curseur.rollback()
            return False
    #get_product
    def get_all_produit(self,curseur):
        try:
            curseur.execute('SELECT * FROM tb_produit')
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #function  to search one or many product
    def search_produit (self,curseur,critere):
        resultat=[] 
        try:
            
            curseur.execute(f'select *from tb_produit {critere}')
            resultat=curseur.fetchall()
            return resultat
        except Exception as e:
            resultat=[]
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat
        