from django.shortcuts import render
from .models import Slider, PersonalDate
from .forms import PersonalDateForm

#
def PersonalDate(request):
    if request.method == 'POST':
        form = PersonalDateForm(request.POST)
        if form.is_valid():
            model.PersonalDate = form.cleaned_data['PersonalDate']
            model.save()
        else:
            form = PersonalDate()
        return render_to_respose('suport.html',{'form':form})



def home(request):
    return render(request, 'new_wings/index.html', {
        'sliders': Slider.objects.all(),


    })


def support(request):
    return render(request, 'new_wings/suport.html', {

    })


def rehabil(request):
    return render(request, 'new_wings/reabilitation.html', {

    })


def donate(request):
    return render(request, 'new_wings/sponsors.html', {

    })
