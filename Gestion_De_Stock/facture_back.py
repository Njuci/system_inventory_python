from tkinter import messagebox


class Facture_back:
    def __init__(self,id_cli):
        self.id_cli=id_cli
    def add_fact(self,curseur):
        try:
            curseur.execute('INSERT INTO tb_facture(id_client) VALUES(%s)', (self.id_cli,))
            
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout d\'une facture  à la base de données : {e}')
            
            return False
    #function update a informations 
    def update_fact(self,curseur,id_fact):
        try:
            curseur.execute('UPDATE tb_facture SET id_cli=%s WHERE id_facture=%s',(self.id_cli,id_fact))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'update de la facture  à la base de données : {e}')
         
            return False
        
    #function TO del 
    def del_fact(self,curseur,id_fac):
        try:
            curseur.execute('DELETE FROM tb_facture WHERE id_client=%s',(id_fac))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la suppression de la facture  à la base de données : {e}')
           
            return False
    #get_client
    def get_all_fact(self,curseur):
        try:
            curseur.execute('select date_format(tb_facture.date_facturation,\'%d-%m-%Y\')as date_facturation,tb_client.nom_cli from tb_client inner join tb_facture on tb_client.id_client=tb_facture.id_client order by date_facturation')
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #get distinct date 
    
    def get_distinct_date(self,curseur):
        try:
            curseur.execute('SELECT DISTINCT date_format(date_facturation,\'%d-%m-%Y\') as date_facturation FROM tb_facture order by date_facturation')
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            return False,[]
    #get facture by date
    def get_fact_by_date(self,curseur,date):
        try:
            curseur.execute('SELECT date_format(tb_facture.date_facturation,\'%d-%m-%Y\')as date_facturation,tb_client.nom_cli  FROM tb_facture INNER JOIN tb_client ON tb_facture.id_client=tb_client.id_client WHERE date_format(date_facturation,\'%d-%m-%Y\')=%s order by date_facturation',(date,))
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
            return False,[]