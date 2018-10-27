from django.shortcuts import render
from random import randint

from .forms import FeedbackForm
from .models import Dapp, Feedback

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
            x.fund_next_stage += randint(10, 30)
        x.save()

    dapps = Dapp.objects.all()
    prototypes = dapps.filter(status__iexact="prototype")
    mvps = dapps.filter(status__iexact="mvp")
    alphas = dapps.filter(status__iexact="alpha")
    betas = dapps.filter(status__iexact="beta")
    lives = dapps.filter(status__iexact="live")
    context = {
        "prototypes": prototypes,
        "mvps": mvps,
        "alphas": alphas,
        "betas": betas,
        "lives": lives,
        "title": "Welcome to The DappStore!",
    }
    return render(request, "home.html", context)


def feedback(request, name):
    dapp = Dapp.objects.all().filter(name__iexact=name)[0]
    form = FeedbackForm()
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            text = form.cleaned_data["text"]
            rating = form.cleaned_data["rating"]
            f = Feedback(dapp=dapp, text=text, rating=rating)
            f.save()

    feedbacks = Feedback.objects.all().filter(dapp__exact=dapp)

    context = {
        "form": form,
        "name": name,
        "feedbacks": feedbacks,
    }
    return render(request, "feedback.html", context)
