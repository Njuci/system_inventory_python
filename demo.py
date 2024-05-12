from login_back import Connexion
from client_backend import Client_back
connex=Connexion("root","3670njci")
curseur=connex.get_curseur()
client=Client_back('Njuci 4','Bukavu')
client.update_client(curseur,'CLI0000004')
"""if client.add_client(curseur):
    print('ok')
else:
    print('erreur')
"""

