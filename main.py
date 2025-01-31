import requests
import json
from datetime import datetime

# Configuration des headers
headers = {
    'User-Agent': 'Scraping Bot (ADRESSE@MAIL.COM)',
}

# URL de l'endpoint
url = 'https://www.mk2.com/_next/data/mOVXSxj35n-aMKdxIktJ2/ile-de-france/films/tous-les-films.json?category=tous-les-films&cinemaGroupId=ile-de-france'

try:
    # Effectuer la requête HTTP
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Récupérer les données JSON
    data = response.json()
    
    # Extraire uniquement les films du pageProps.pageContent.films
    films = data.get('pageProps', {}).get('pageContent', {}).get('films', [])
    
    # Générer le nom du fichier avec la date et l'heure
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'mk2_films_{timestamp}.json'
    
    # Sauvegarder les données des films dans un fichier JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(films, f, ensure_ascii=False, indent=2)
    
    print(f"Les données des films ont été sauvegardées dans '{filename}'")
    print(f"Nombre de films récupérés : {len(films)}")
    
except requests.exceptions.RequestException as e:
    print(f"Une erreur s'est produite lors de la requête : {e}")
except json.JSONDecodeError as e:
    print(f"Une erreur s'est produite lors du décodage JSON : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}") 