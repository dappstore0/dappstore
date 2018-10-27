from django.shortcuts import render

from .models import Dapp

st = {
    "prototype": "mvp",
    "mvp": "alpha",
    "alpha": "beta",
    "beta": "live",
    "live": None
}
def home(request):
    if request.method == "POST":
        add = int(request.POST.get("eth"))
        name = request.POST.get("name")
        print(name, add)
        x = Dapp.objects.all().filter(name__exact=name)[0]
        x.current_fund += add
        #x.current_fund = 0
        if x.current_fund >= x.fund_next_stage:
            x.status = st[x.status.lower()]
            x.fund_next_stage += 19
        x.save()

    dapps = Dapp.objects.all()
    prototypes = dapps.filter(status__iexact='prototype')
    mvps = dapps.filter(status__iexact='mvp')
    alphas = dapps.filter(status__iexact='alpha')
    betas = dapps.filter(status__iexact='beta')
    lives = dapps.filter(status__iexact='live')
    context = {
        'prototypes': prototypes,
        'mvps': mvps,
        'alphas': alphas,
        'betas': betas,
        'lives': lives,
        'title': 'Welcome to The DappStore!',
    }
    return render(request, 'home.html', context)
