from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, Project

def index(request):

    # Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()
    
    projects = Project.objects.all()

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        'projects': projects
    }


    return render(request, 'index.html', context)


# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'your_template.html', {'projects': projects})
