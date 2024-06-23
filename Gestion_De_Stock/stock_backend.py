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
            string_query=f"""
            
            
                                                        SELECT 
                                                
                                                p.designation_produit,
                                                IFNULL(s.total_entree, 0) - IFNULL(v.total_vente, 0) AS stock_restant
                                            FROM 
                                                tb_produit p
                                            LEFT JOIN (
                                                SELECT 
                                                    id_produit,
                                                    SUM(nombre_piece) AS total_entree
                                                FROM 
                                                    tb_stock
                                                GROUP BY 
                                                    id_produit
                                            ) s ON p.id_produit = s.id_produit
                                            LEFT JOIN (
                                                SELECT 
                                                    id_produit,
                                                    SUM(quantite) AS total_vente
                                                FROM 
                                                    tb_vente
                                                GROUP BY 
                                                    id_produit
                                            ) v ON p.id_produit = v.id_produit;

                                                    """
    
            curseur.execute(string_query)
            return True,curseur.fetchall()
        
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout du client  à la base de données : {e}')
          
            return False,[]
    #get stock restant par produit
    def get_stock_restant_produit(self,curseur,id_produit):
        try:
            string_query="""
            
            
                                                        SELECT 
                                                
                                                p.designation_produit,
                                                IFNULL(s.total_entree, 0) - IFNULL(v.total_vente, 0) AS stock_restant
                                            FROM 
                                                tb_produit p
                                            LEFT JOIN (
                                                SELECT 
                                                    id_produit,
                                                    SUM(nombre_piece) AS total_entree
                                                FROM 
                                                    tb_stock
                                                GROUP BY 
                                                    id_produit
                                            ) s ON p.id_produit = s.id_produit
                                            LEFT JOIN (
                                                SELECT 
                                                    id_produit,
                                                    SUM(quantite) AS total_vente
                                                FROM 
                                                    tb_vente
                                                GROUP BY 
                                                    id_produit
                                            ) v ON p.id_produit = v.id_produit
                                            
                                            where p.id_produit=%s
                                            ;

                                                    """
    
            curseur.execute(string_query,(id_produit,))
            return True,curseur.fetchone()
        
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
            
            string_query="""SELECT tb_produit.designation_produit,
                            tb_stock.date_entree AS 'Date d entrée',
                            tb_stock.nombre_piece AS 'Nombre de pièce en stock',
                            COALESCE(MAX(tb_facture.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
                            COALESCE(SUM(tb_vente.quantite), 0) AS 'Quantité sortie' 
                            FROM tb_stock
                            LEFT JOIN tb_vente ON tb_stock.id_stock = tb_vente.id_stock
                            JOIN tb_produit ON tb_produit.id_produit = tb_stock.id_produit
                            LEFT JOIN tb_facture ON tb_vente.id_facture = tb_facture.id_facture
                            WHERE tb_produit.designation_produit =%s
                            GROUP BY tb_stock.id_stock
                            ORDER BY COALESCE(MAX(tb_stock.date_entree), '0000-00-00 00:00:00') DESC;

                                                    """
            curseur.execute(string_query,(designation_produit,))
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la recuperation des données  à la base de données : {e}')
            return False,[]
    def get_stock_dispo_id(self,curseur,id_produit):
        string_query="""WITH VentesCumulees AS (
            SELECT 
                                    id_produit,
                                    id_stock,
                                    SUM(quantite) AS quantite_vendue
                                FROM 
                                    tb_vente
                                GROUP BY 
                                    id_produit, id_stock
                            ),
                            Stocks AS (
                                SELECT 
                                    id_stock,
                                    id_produit,
                                    nombre_piece,
                                    ROW_NUMBER() OVER (PARTITION BY id_produit ORDER BY date_entree ASC) AS rang_fifo
                                FROM 
                                    tb_stock
                            ),
                            StocksDisponibles AS (
                                SELECT 
                                    s.id_stock,
                                    s.id_produit,
                                    s.nombre_piece - COALESCE(v.quantite_vendue, 0) AS stock_restant
                                FROM 
                                    Stocks s
                                LEFT JOIN 
                                    VentesCumulees v ON s.id_stock = v.id_stock AND s.id_produit = v.id_produit
                                WHERE 
                                    s.nombre_piece - COALESCE(v.quantite_vendue, 0) > 0
                            )
                            SELECT 
                                sd.id_produit,
                                MIN(sd.id_stock) AS id_stock_utiliser
                            FROM 
                                StocksDisponibles sd where sd.id_produit=%s
                            GROUP BY 
                                sd.id_produit; """
      
        try:
            curseur.execute(string_query,(id_produit,))
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur de {e}')
            return False,[]
    def get_stock_ecoule(self,curseur,id_stock):
        string_query="""SELECT     tb_produit.designation_produit, 
                                    tb_stock.date_entree, 
                                    tb_stock.nombre_piece, 
                                    COALESCE(SUM(tb_vente.quantite), 0) AS quantite_vendue
                                FROM 
                                    tb_stock
                                JOIN 
                                    tb_produit ON tb_stock.id_produit = tb_produit.id_produit
                                LEFT JOIN 
                                    tb_vente ON tb_stock.id_stock = tb_vente.id_stock
                                WHERE 
                                    tb_stock.id_stock = %s
                                GROUP BY 
                                    tb_produit.designation_produit, tb_stock.date_entree, tb_stock.nombre_piece;"""
        try:
            curseur.execute(string_query,(id_stock,))
            return True,curseur.fetchall()
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur de {e}')
            return False,[]
    