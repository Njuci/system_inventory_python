


import tkinter

class Product_back:
    def __init__(self,nom_produit):
        self.nom_produit = nom_produit
    #function to add a product
    def add_produit(self,curseur):
        try:
            curseur.execute('INSERT INTO tb_produit(designation_produit) VALUES(%s)', (self.nom_produit,))
            
            return True
        except Exception as e:
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
         
            return False
    #function update a informations 
    def update_produit(self,curseur,id_produit):
        try:
            curseur.execute('UPDATE tb_produit SET designation_produit=%s WHERE id_produit=%s',(self.nom_produit,id_produit,))
            return True
        except Exception as e:
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False
        
    #function TO del 
    def del_produit(self,curseur,id):
        try:
            curseur.execute('DELETE FROM tb_produit WHERE id_produit=%s',(id))
            return True
        except Exception as e:
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            
            return False
    #get_product
    def get_all_produit(self,curseur):
        try:
            curseur.execute('SELECT id_produit,designation_produit FROM tb_produit ORDER BY id DESC')
            return True,curseur.fetchall()
        
        except Exception as e:
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
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
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat
    # chercher la somme des produits en stock dans la bd (where statut_stock est diffqrent de finis)
    def search_stock (self,curseur):
        try:
            curseur.execute(f'select tp.designation_produit,sum(ts.nombre_piece),case when sum(ts.nombre_piece)<=10 then " Trop Bas" when sum(ts.nombre_piece)>10 and sum(ts.nombre_piece)<=20 then "Stock bas" else "Disponible" end  as statut_st from tb_stock ts join tb_produit tp on tp.id_produit=ts.id_produit where ts.statut_stock!="finis" group by tp.designation_produit')
            resultat=curseur.fetchall()
            return resultat
        except Exception as e:
            resultat=[]
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat
    def nom_produit_dispo(self,curseur):
        try:
            curseur.execute(f'select ts.id_produit,tp.designation_produit,sum(ts.nombre_piece),case when sum(ts.nombre_piece)<=10 then " Trop Bas" when sum(ts.nombre_piece)>10 and sum(ts.nombre_piece)<=20 then "Stock bas" else "Disponible" end  as statut_st from tb_stock ts join tb_produit tp on tp.id_produit=ts.id_produit where ts.statut_stock!="finis" group by ts.id_produit')
            resultat=curseur.fetchall()
            return resultat
        except Exception as e:
            resultat=[]
            tkinter.messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat