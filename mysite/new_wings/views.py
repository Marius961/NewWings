from django.shortcuts import render ,HttpResponseRedirect
from django.core.mail import send_mail,BadHeaderError
from .forms import *
from .models import*





def home(request):
    return render(request, 'new_wings/index.html', {
        'sliders': Slider.objects.all(),
        'informations':Information.objects.all(),
        'contacts':Contact.objects.all(),
        'socials':Social.objects.all(),
        'reabils': Reabil.objects.all(),
    })


def support(request):
    form = SuportForm(request.POST or None)
    if request.method == "POST":
        print(request.POST)
        if form.is_valid():
            form = form.save()

            return HttpResponseRedirect(request.path)

    return render(request, 'new_wings/suport.html', locals(),{
        'contacts': Contact.objects.all(),
        'socials': Social.objects.all()
    })
def rehabil(request):
    return render(request, 'new_wings/reabilitation.html', {
        'contacts': Contact.objects.all(),
        'socials': Social.objects.all(),
        'reabils': Reabil.objects.all(),

    })
def donate(request):
    return render(request, 'new_wings/sponsors.html', {
        'contacts': Contact.objects.all(),
        'socials': Social.objects.all(),
        'donates': Donate.objects.all(),
        'sponsors':Sponsor.objects.all()

    })
def news(request):
    return render(request, 'new_wings/news.html', {
        'news': New.objects.all()
    })



