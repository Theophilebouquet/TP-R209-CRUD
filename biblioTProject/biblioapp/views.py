from django.shortcuts import render
from .form import PersonnageForm
from . import models

# Create your views here.
def index(request):
    return render(request, 'biblioapp/index.html')

def formulaire(request):
    return render(request, 'biblioapp/formulaire.html')

def bonjour(request):
    nom=request.GET["nom"]
    prenom = request.GET["prenom"]
    return render(request, 'biblioapp/bonjour.html',{"nom":nom},{"prenom":prenom})

def ajout(request):
    if request.method == "POST":
        form = PersonnageForm(request)
        if form.is_valid():
            personnage = form.save()
            return render(request,"bibliapp/ajout.html",{"personnage": personnage})
        else:
            return render(request,"bibliapp/ajout.html",{"form": form})
    else:
        form = PersonnageForm()
        return render(request,"bibliapp/ajout.html",{"form": form})
