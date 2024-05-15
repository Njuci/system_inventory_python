def generate_key(prefix,long,id):
  """
  Fonction pour générer une clé de type I000001.

  :return: La clé générée.
  """
  # Numéro de base
  base_number =id

  # Longueur de la clé
  key_length = long

  # Préfixe
  prefix =prefix

  # Formatage du numéro
  formatted_number = str(base_number).zfill(key_length - 1)

  # Clé générée
  generated_key = prefix + formatted_number

  return generated_key

#Comment recuperer le nombre d'entrees dans une table;
def recuperer_dernier(nom_table,prefix,long,curseur):
    try:
        #comment gernerer une clé pour un nouvel enregistrement dans une table donnée en tenant compte du nombre d'enregistrement déjà existant dans la table meme si quelques enregistrements ont été supprimés
        
        
        
        curseur.execute(f'select count(*) from {nom_table}')
        resultat=curseur.fetchall()
        id=resultat[0][0]+1
        cle=generate_key(prefix,long,id)
        return cle
    except Exception as e:
        pass        
        
        
        
        
        
        
    except Exception as e:
        resultat=[]
        
    
    
    
    
    pass
    