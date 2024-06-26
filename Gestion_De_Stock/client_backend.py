"""_summary_
se basant de bd_invent{python .sql}
cree une classe client_back qui me permettra de  reagir avec avec labd
en utilisant mysqlconnector python

    """
from tkinter import messagebox

class Client_back:
    def __init__(self,nom_cli,adresse_cli):
        self.nom_client = nom_cli
        self.adresse_client = adresse_cli
    #function to add a client
    def add_client(self,curseur):
        try:
            curseur.execute('INSERT INTO tb_client(nom_cli,adresse) VALUES(%s,%s)', (self.nom_client,self.adresse_client))
            
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            curseur.rollback()
            return False
    #function to get a total amount client by id
    def get_facture_by_client(self,curseur,id_client):
        string_query="""
                       SELECT
                        c.id_client,
                        c.nom_cli,
                        COALESCE(SUM(pv.montant * v.quantite), 0) AS total_facture
                        FROM tb_facture f
                        LEFT JOIN tb_client c ON f.id_client = c.id_client
                        LEFT JOIN tb_vente v ON f.id_facture = v.id_facture
                        LEFT JOIN tb_prix_vente pv ON v.id_produit = pv.id_produit
                        WHERE c.id_client=%s
                        
                        GROUP BY c.id_client, c.nom_cli;

        
                    """
        try:
            curseur.execute(string_query,(id_client,))
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return False,[]
    #function update a informations 
    def update_client(self,curseur,id_client):
        try:
            curseur.execute('UPDATE tb_client SET nom_cli=%s,adresse=%s WHERE id_client=%s',(self.nom_client,self.adresse_client,id_client))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            curseur.rollback()
            return False
        
    #function TO del 
    def del_client(self,curseur,id_client):
        try:
            curseur.execute('DELETE FROM tb_client WHERE id_client=%s',(id_client,))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la suppression du client  à la base de données : {e}')
            curseur.rollback()
            return False
    #get_client
    def get_all_client(self,curseur):
        try:
            curseur.execute('SELECT * FROM tb_client')
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #function  to search one or many cloent
    def search_client (self,curseur,critere):
        resultat=[]
        try:
            
            curseur.execute(f'select *from tb_client {critere}')
            resultat=curseur.fetchall()
            return resultat
        except Exception as e:
            resultat=[]
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat