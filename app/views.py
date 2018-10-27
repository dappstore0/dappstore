from django.shortcuts import render

from .models import Dapp


def home(request):
    dapps = Dapp.objects.all()
    prototypes = dapps.filter(status__exact='prototype')
    mvps = dapps.filter(status__exact='mvp')
    alphas = dapps.filter(status__exact='alpha')
    betas = dapps.filter(status__exact='beta')
    lives = dapps.filter(status__exact='live')
    context = {
        'prototypes': prototypes,
        'mvps': mvps,
        'alphas': alphas,
        'betas': betas,
        'lives': lives,
        'title': 'Welcome to The dApp Store!'
    }
    return render(request, 'home.html', context)
