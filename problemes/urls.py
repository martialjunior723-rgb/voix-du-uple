from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('soumettre/', views.soumettre, name='soumettre'),
    path('probleme/<int:pk>/', views.detail, name='detail'),
]
