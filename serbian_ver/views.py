from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/index.html', context)

def contact(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/contact.html', context)


def treatmentGamblers(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/treatment_of_gamblers.html', context)


def weaningProgram(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/family_and_gambler.html', context)


def gamblingProblem(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/gambling_problem_scene.html', context)


def gamblingAddiction(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/gambling_addiction.html', context)

def pathologicalGambling(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/pathological_gambling.html', context)


def dealingGambling(request):
    
    
    context = {
        

    }
    
    return render(request, 'serbian/index/dealing_with_gambling_problem.html', context)