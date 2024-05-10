from tkinter.messagebox import showerror
import mysql.connector


class Connexion:
    def __init__(self,user,password):
        self.user=user
        self.password=password

        
        try:
            self.db = mysql.connector.connect(
            host = '127.0.0.1',
            user = self.user,
            password = self.password,
            database ='gest_stock_invent',
            autocommit=True
        )
            self.curseur=self.db.cursor()
        except Exception as e:
            self.db=None
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
        self.db.close()
        self.curseur.close()
