from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('people/', views.people, name='people'),
    path('planets/', views.planets, name='planets'),
    path('films/', views.films, name='films'),
    path('people/<int:id>/', views.person_detail, name='person_detail'),
]