
"""
create table tb_vente(
    id int auto_increment unique key,
	id_vente varchar(10),
    id_produit varchar(10),
    id_pv varchar(10),
    quantite integer,
    id_facture varchar(10),
    id_stock varchar(10),
    constraint pf_fac_vente foreign key (id_facture) references tb_facture (id_facture),
    constraint pf_vente_produit foreign key(id_produit) references tb_produit(id_produit),
    constraint pf_vente_id_stock foreign key (id_stock) references tb_stock(id_stock),
    constraint pf_pv_vente foreign key(id_pv) references tb_prix_vente (id_pv),
    constraint pk_vente primary key(id_stock,id_facture,id_produit)
    );
    
"""
from tkinter import messagebox


class Vente_back:
    def __init__(self,id_produit,id_stock,id_facture,id_pv,quantite):
        self.id_produit=id_produit
        self.id_stock=id_stock
        self.id_facture=id_facture
        self.id_pv=id_pv
        self.quantite=quantite
    #add vente
    def add_vente(self,curseur):
        try:
            curseur.execute('Insert into tb_vente(id_produit,id_stock,id_facture,id_pv,quantite) values(%s,%s,%s,%s,%s)',
                            (self.id_produit,self.id_stock,self.id_facture,self.id_pv,self.quantite,))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de l\'ajout de la vente  à la base de données : {e}')
            return False
    #update vente
    def update_vente(self,curseur,id_vente):
        try:
            curseur.execute('update tb_vente set id_produit=%s,id_stock=%s,id_facture=%s,id_pv=%s,quantite=%s where id=%s',(self.id_produit,self.id_stock,self.id_facture,self.id_pv,self.quantite,id_vente))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la modification  de la vente  à la base de données : {e}')
            return False
    #delete vente
    def del_vente(self,curseur,id_vente):
        try:
            curseur.execute('delete from tb_vente where id=%s',(id_vente,))
            return True
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la suppression  de la vente  à la base de données : {e}')
            return False
        
    #get vente
    def get_vente(self,curseur):
        try:
            curseur.execute('select * from tb_vente')
            rows=curseur.fetchall()
            return rows
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la récupération  des ventes  à la base de données : {e}')
            return False
    #get vente by id
    def get_vente_by_id(self,curseur,id_vente):
        try:
            curseur.execute('select * from tb_vente where id=%s',(id_vente,))
            rows=curseur.fetchall()
            return rows
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la récupération  de la vente  à la base de données : {e}')
            return False
    #get vente by id_facture
    def get_vente_by_id_facture(self,curseur,id_facture):
        try:
            curseur.execute('select * from tb_vente where id_facture=%s',(id_facture,))
            rows=curseur.fetchall()
            return rows
        except Exception as e:
            messagebox.showerror('Erreur',f'Erreur lors de la récupération  de la vente  à la base de données : {e}')
            return False
        
    #get vente by
