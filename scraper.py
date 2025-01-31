import requests
import os
from datetime import datetime

# Configuration des headers avec un user agent personnalisé
headers = {
    'User-Agent': 'Scraping Bot (ADRESSE@MAIL.COM)',
}

# URL cible
url = 'https://www.mk2.com/salle/mk2-bastille-beaumarchais-fg-st-antoine'

try:
    # Effectuer la requête HTTP
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lever une exception si la requête échoue
    
    # Générer le nom du fichier avec la date et l'heure
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'mk2_bastille_{timestamp}.html'
    
    # Sauvegarder le contenu HTML dans un fichier
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    print(f"Le contenu HTML a été sauvegardé dans '{filename}'")
    
except requests.exceptions.RequestException as e:
    print(f"Une erreur s'est produite : {e}")