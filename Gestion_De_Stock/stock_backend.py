from tkinter import messagebox

class Stock_back:
    def __init__(self,id_produit,nombre_piece,prix_unitaire):
        self.id_produit=id_produit
        self.nombre_piece=nombre_piece
        self.prix_unitaire=prix_unitaire
        if int(self.nombre_piece)<=10 and int(self.nombre_piece)!=0:
            self.statut_stock='Bas niveau'
        elif int(self.nombre_piece)>10:
            self.statut_stock='Disponible'
    #insert new stock
    def add_stock(self,curseur):
        try:
            curseur.execute('Insert into tb_stock(id_produit,nombre_piece,prix_unitaire,statut_stock) values(%s,%s,%s,%s)',
                            (self.id_produit,self.nombre_piece,self.prix_unitaire,self.statut_stock))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du stock  à la base de données : {e}')
            return False
    #udapte
    def update_stock(self,curseur,id_stock):
        try:
            curseur.execute('update tb_stock set id_produit=%s,nombre_piece=%s,prix_unitaire=%s,statut_stock=%s where id_stock=%s',(self.id_produit,self.nombre_piece,
                                                                                                                                    self.prix_unitaire,self.statut_stock,id_stock))
            return True
        except Exception as e:
            
            messagebox.showerror('Erreur',f'Erreur lors de la modification  du stock  à la base de données : {e}')
            return False
            
    #del
    def del_stock(self,curseur,id_stock):
        try:
            curseur.execute('delete from tb_stock where id_stock=%s',(id_stock,)
                            )
            return True
        except Exception as e:
            
            messagebox.showerror('Erreur',f'Erreur lors de la suppression  du stock  à la base de données : {e}')
            return False
    #get_stock
    def get_stock_restant(self,curseur):
        try:
            string_query=f"""SELECT tb_produit.designation_produit, 
                            (IFNULL(SUM(tb_stock.nombre_piece),0) - IFNULL(SUM(tb_vente.quantite), 0)) AS somme_restante
                            FROM tb_produit
                         LEFT JOIN tb_stock ON tb_produit.id_produit = tb_stock.id_produit
                         LEFT JOIN tb_vente ON tb_produit.id_produit = tb_vente.id_produit
                        GROUP BY tb_produit.designation_produit
                            HAVING somme_restante > 0;
                                                    """
    
            curseur.execute(string_query)
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    
    
    def get_all_stock(self,curseur):
        try:
            curseur.execute('SELECT * FROM tb_stock')
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #function  to search one or many product
    def search_stock (self,curseur,critere):
        resultat=[] 
        try:
            
            curseur.execute(f'select *from tb_stock {critere}')
            resultat=curseur.fetchall()
            return resultat
        except Exception as e:
            resultat=[]
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return resultat
    def get_detail_stock_produit(self,curseur,designation_produit):
        try:
            
            string_query=f"""SELECT tb_produit.designation_produit,
                            tb_stock.date_entree AS 'Date d entrée',
                            tb_stock.nombre_piece AS 'Nombre de pièce en stock',
                            COALESCE(MAX(tb_facture.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
                            COALESCE(SUM(tb_vente.quantite), 0) AS 'Quantité sortie'
                            FROM tb_produit
                            LEFT JOIN tb_stock ON tb_produit.id_produit = tb_stock.id_produit
                            LEFT JOIN tb_vente ON tb_produit.id_produit = tb_vente.id_produit
                            LEFT JOIN tb_facture ON tb_vente.id_facture = tb_facture.id_facture
                            WHERE tb_produit.designation_produit = '{designation_produit}'
                            GROUP BY tb_produit.designation_produit, tb_stock.date_entree, tb_stock.nombre_piece
                            ORDER BY COALESCE(MAX(tb_facture.date_facturation), '0000-00-00 00:00:00') DESC;

                                                    """
            curseur.execute(string_query)
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return False,[]