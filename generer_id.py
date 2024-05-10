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

#Comment