from django.contrib import admin
from .models import Probleme


@admin.register(Probleme)
class ProblemeAdmin(admin.ModelAdmin):
    list_display = ['titre', 'nom', 'categorie', 'condition', 'statut', 'date_creation']
    list_filter = ['categorie', 'condition', 'statut']
    search_fields = ['titre', 'nom', 'description']
    list_editable = ['statut']
    ordering = ['-date_creation']
