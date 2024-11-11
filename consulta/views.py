from django.shortcuts import render
import requests

SWAPI_BASE_URL = "https://swapi.dev/api"

def home(request):
    """Página inicial."""
    return render(request, 'home.html')

# def people(request):
#     """Lista de personagens."""
#     response = requests.get(f"{SWAPI_BASE_URL}/people/")
#     data = response.json()
    
#     people_with_ids = []
#     for person in data['results']:
#         # Extrai o ID da URL
#         person_id = person['url'].rstrip('/').split('/')[-1]
#         people_with_ids.append({**person, 'id': person_id})
    
#     return render(request, 'people.html', {'people': people_with_ids})

import requests
from django.shortcuts import render

SWAPI_BASE_URL = "https://swapi.dev/api"

def people(request):
    """Lista de personagens com seus filmes."""
    response = requests.get(f"{SWAPI_BASE_URL}/people/")
    data = response.json()
    
    people_with_ids_and_films = []
    
    for person in data['results']:
        person_id = person['url'].rstrip('/').split('/')[-1]
        films = []
        for film_url in person.get('films', []):
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film_data = film_response.json()
                films.append({
                    'title': film_data['title'],
                })
                
        people_with_ids_and_films.append({
            **person,
            'id': person_id,
            'films': films,
        })
    
    return render(request, 'people.html', {'people': people_with_ids_and_films})


def planets(request):
    """Lista de planetas."""
    response = requests.get(f"{SWAPI_BASE_URL}/planets/")
    data = response.json()
    
    planet_with_ids = []
    for planet in data['results']:
        # Extrai o ID da URL
        planet_id = planet['url'].rstrip('/').split('/')[-1]
        planet_with_ids.append({**planet, 'id': planet_id})
    
    return render(request, 'planets.html', {'planets': planet_with_ids})

def films(request):
    """Lista de filmes."""
    response = requests.get(f"{SWAPI_BASE_URL}/films/")
    data = response.json()
    
    film_with_ids = []
    for film in data['results']:
        # Extrai o ID da URL
        film_id = film['url'].rstrip('/').split('/')[-1]
        film_with_ids.append({**film, 'id': film_id})
        
    return render(request, 'films.html', {'films': film_with_ids})

# def person_detail(request, id): 
#     """Detalhes de um personagem específico."""
#     response = requests.get(f"{SWAPI_BASE_URL}/people/{id}/")
#     data = response.json()
#     return render(request, 'person_detail.html', {'person': data})

def person_detail(request, id):
    """Detalhes de um personagem específico com lista de filmes."""
    try:
        response = requests.get(f"{SWAPI_BASE_URL}/people/{id}/")
        response.raise_for_status()
        person_data = response.json()
        
        films = []
        for film_url in person_data.get('films', []):
            film_response = requests.get(film_url)
            if film_response.status_code == 200:
                film_data = film_response.json()
                films.append({
                    'title': film_data['title'],
                    'episode_id': film_data['episode_id'],
                    'director': film_data['director'],
                    'release_date': film_data['release_date'],
                })
        
        context = {
            'person': person_data,
            'films': films,
        }
        return render(request, 'person_detail.html', context)
    
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'message': 'Erro ao consultar a API', 'details': str(e)})


def planet_detail(request, id): 
    """Detalhes de um personagem específico."""
    response = requests.get(f"{SWAPI_BASE_URL}/planets/{id}/")
    data = response.json()
    return render(request, 'planet_detail.html', {'planet': data})

def film_detail(request, id): 
    """Detalhes de um personagem específico."""
    response = requests.get(f"{SWAPI_BASE_URL}/films/{id}/")
    data = response.json()
    return render(request, 'film_detail.html', {'film': data})


