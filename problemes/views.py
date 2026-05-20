from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Probleme, CATEGORIES
from .forms import ProblemeForm


def accueil(request):
    problemes = Probleme.objects.all()
    categorie = request.GET.get('categorie', '')
    condition = request.GET.get('condition', '')
    search = request.GET.get('search', '')

    if categorie:
        problemes = problemes.filter(categorie=categorie)
    if condition:
        problemes = problemes.filter(condition=condition)
    if search:
        problemes = problemes.filter(titre__icontains=search) | problemes.filter(description__icontains=search)

    context = {
        'problemes': problemes,
        'total': Probleme.objects.count(),
        'nouveaux': Probleme.objects.filter(statut='nouveau').count(),
        'resolus': Probleme.objects.filter(statut='resolu').count(),
        'categories': CATEGORIES,
        'categorie_active': categorie,
        'condition_active': condition,
        'search': search,
    }
    return render(request, 'problemes/accueil.html', context)


def soumettre(request):
    if request.method == 'POST':
        form = ProblemeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre problème a été soumis avec succès. Merci de partager votre situation !')
            return redirect('accueil')
    else:
        form = ProblemeForm()
    return render(request, 'problemes/soumettre.html', {'form': form})


def detail(request, pk):
    probleme = get_object_or_404(Probleme, pk=pk)
    return render(request, 'problemes/detail.html', {'probleme': probleme})
