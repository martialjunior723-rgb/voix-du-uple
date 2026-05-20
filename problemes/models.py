from django.db import models

CATEGORIES = [
    ('commerce', 'Commerce & Affaires'),
    ('agriculture', 'Agriculture'),
    ('sante', 'Santé'),
    ('education', 'Éducation'),
    ('transport', 'Transport'),
    ('finance', 'Finance'),
    ('logement', 'Logement'),
    ('autre', 'Autre'),
]

CONDITIONS = [
    ('urgent', 'Urgent – Besoin d\'aide immédiate'),
    ('court_terme', 'Court terme – Dans les prochaines semaines'),
    ('long_terme', 'Long terme – Pas de pression immédiate'),
    ('information', 'Information seulement – Juste partager'),
]

STATUTS = [
    ('nouveau', 'Nouveau'),
    ('en_cours', 'En cours de traitement'),
    ('resolu', 'Résolu'),
]


class Probleme(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Votre nom")
    email = models.EmailField(blank=True, verbose_name="Email (optionnel)")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone (optionnel)")
    titre = models.CharField(max_length=200, verbose_name="Titre du problème")
    categorie = models.CharField(max_length=50, choices=CATEGORIES, default='autre', verbose_name="Catégorie")
    description = models.TextField(verbose_name="Description du problème")
    solution_souhaitee = models.TextField(verbose_name="Solution souhaitée")
    condition = models.CharField(max_length=50, choices=CONDITIONS, default='information', verbose_name="Urgence / Condition")
    statut = models.CharField(max_length=20, choices=STATUTS, default='nouveau', verbose_name="Statut")
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Problème"
        verbose_name_plural = "Problèmes"

    def __str__(self):
        return f"{self.titre} – {self.nom}"

    def get_categorie_icon(self):
        icons = {
            'commerce': '🛒',
            'agriculture': '🌾',
            'sante': '🏥',
            'education': '📚',
            'transport': '🚗',
            'finance': '💰',
            'logement': '🏠',
            'autre': '💬',
        }
        return icons.get(self.categorie, '💬')

    def get_condition_color(self):
        colors = {
            'urgent': 'urgent',
            'court_terme': 'court',
            'long_terme': 'long',
            'information': 'info',
        }
        return colors.get(self.condition, 'info')
