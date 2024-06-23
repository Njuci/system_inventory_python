from login_back import Connexion
from pv_back import Prix_vente_back
from client_backend import Client_back
connex=Connexion("root","3670njci")
curseur=connex.get_curseur()
from stock_backend import Stock_back
ag="07-09-2024"
bg=ag.split('-')

print(bg.reverse())


"""
client=Client_back('Njuci 4','Bukavu')
Pv=Prix_vente_back('PRO0000002',00)
Pv.add_prix_vente(curseur)

client=Client_back('Njuci 4','Bukavu')
Pv=Prix_vente_back('CLI0000004',500)
Pv.add_prix_vente(curseur)

print(Pv.get_last_pv('CLI0000004')[1][1])


for i in client.get_all_client(curseur)[1]:
    print(i)
client.update_client(curseur,'CLI0000004')

if client.add_client(curseur):
    print('ok')
else:
    print('erreur')
    
"""

