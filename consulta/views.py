from django.shortcuts import render

from django.shortcuts import render
import requests

SWAPI_BASE_URL = "https://swapi.dev/api"

def home(request):
    """Página inicial."""
    return render(request, 'home.html')

def people(request):
    """Lista de personagens."""
    response = requests.get(f"{SWAPI_BASE_URL}/people/")
    data = response.json()
    return render(request, 'people.html', {'people': data['results']})

def planets(request):
    """Lista de planetas."""
    response = requests.get(f"{SWAPI_BASE_URL}/planets/")
    data = response.json()
    return render(request, 'planets.html', {'planets': data['results']})

def films(request):
    """Lista de filmes."""
    response = requests.get(f"{SWAPI_BASE_URL}/films/")
    data = response.json()
    return render(request, 'films.html', {'films': data['results']})

def person_detail(request, id): 
    """Detalhes de um personagem específico."""
    response = requests.get(f"{SWAPI_BASE_URL}/people/{id}/")
    data = response.json()
    return render(request, 'person_detail.html', {'person': data})
