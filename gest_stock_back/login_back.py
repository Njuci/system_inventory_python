from tkinter.messagebox import showerror
import mysql.connector


class Connexion:
    def __init__(self,user,password):
        self.user=user
        self.password=password
        self.db=None
        self.curseur=None
        try:
            self.db = mysql.connector.connect(
            host = 'localhost',
            user = self.user,
            password = self.password,
            database ='gest_stock_invent',
            autocommit=True
        )
            self.curseur=self.db.cursor()
        except Exception as e:
            self.db=None
            self.curseur=None
            showerror("Erreur",f'Erreur de connexion à la base de données motif:{e}')
            
            
    def login(self):
        try:
            if self.db.is_connected():
                 return True
        except Exception as e:
            showerror("Erreur",str(e)) 
            return False 
    def get_curseur(self):
        return self.curseur    
    def close(self):
        self.curseur.close()
