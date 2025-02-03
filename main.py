import requests
import json
from datetime import datetime

# Configuration des headers
headers = {
    'User-Agent': 'Scraping Bot (ADRESSE@MAIL.COM)',
}

# URL de l'endpoint
url = 'https://www.mk2.com/_next/data/mOVXSxj35n-aMKdxIktJ2/ile-de-france/films/tous-les-films.json?category=tous-les-films&cinemaGroupId=ile-de-france'

def get_director(cast):
    """Extraire le réalisateur du casting"""
    for person in cast:
        if person.get('personType') == 'Director':
            return {
                'firstName': person.get('firstName'),
                'lastName': person.get('lastName')
            }
    return None

def filter_movie_data(movie):
    """Filtrer les données d'un film pour ne garder que les informations nécessaires"""
    return {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'synopsis': movie.get('synopsis'),
        'runTime': movie.get('runTime'),
        'graphicUrl': movie.get('graphicUrl'),
        'openingDate': movie.get('openingDate'),
        'director': get_director(movie.get('cast', [])),
        'detailUrl': f"https://www.mk2.com/ile-de-france/film/{movie.get('slug')}"
    }

try:
    # Effectuer la requête HTTP
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    # Récupérer les données JSON
    data = response.json()
    
    # Extraire et filtrer les films
    films = data.get('pageProps', {}).get('pageContent', {}).get('films', [])
    filtered_films = [filter_movie_data(film) for film in films]
    
    # Générer le nom du fichier avec la date et l'heure
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'mk2_films_filtered_{timestamp}.json'
    
    # Sauvegarder les données filtrées des films dans un fichier JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(filtered_films, f, ensure_ascii=False, indent=2)
    
    print(f"Les données des films ont été sauvegardées dans '{filename}'")
    print(f"Nombre de films récupérés : {len(filtered_films)}")
    
except requests.exceptions.RequestException as e:
    print(f"Une erreur s'est produite lors de la requête : {e}")
except json.JSONDecodeError as e:
    print(f"Une erreur s'est produite lors du décodage JSON : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}") 