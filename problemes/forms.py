from django import forms
from .models import Probleme


class ProblemeForm(forms.ModelForm):
    class Meta:
        model = Probleme
        fields = ['nom', 'email', 'telephone', 'titre', 'categorie', 'description', 'solution_souhaitee', 'condition']
        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Ex: Jean Kouassi',
                'class': 'form-input',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'votre@email.com (optionnel)',
                'class': 'form-input',
            }),
            'telephone': forms.TextInput(attrs={
                'placeholder': 'Ex: +225 07 00 00 00 00',
                'class': 'form-input',
            }),
            'titre': forms.TextInput(attrs={
                'placeholder': 'Résumez votre problème en quelques mots...',
                'class': 'form-input',
            }),
            'categorie': forms.Select(attrs={
                'class': 'form-select',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Décrivez votre situation en détail. Que se passe-t-il ? Depuis quand ? Quelles difficultés rencontrez-vous ?',
                'class': 'form-textarea',
                'rows': 5,
            }),
            'solution_souhaitee': forms.Textarea(attrs={
                'placeholder': 'Quelle solution espérez-vous ? Quel type d\'aide ou de soutien cherchez-vous ?',
                'class': 'form-textarea',
                'rows': 4,
            }),
            'condition': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'nom': 'Votre nom',
            'email': 'Email',
            'telephone': 'Téléphone',
            'titre': 'Titre du problème',
            'categorie': 'Domaine concerné',
            'description': 'Description de la difficulté',
            'solution_souhaitee': 'Solution souhaitée',
            'condition': 'Urgence de la situation',
        }
