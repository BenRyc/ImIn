from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    fish = 1


    if request.method == "POST":

        return render(request, 'index.html', {'tree': request.POST["gender"], 'branch': request.POST["pdate"],'branch2': request.POST["text"]})

    return render(request, 'index.html', {'tree': fish})



def importJSON(request):

    if request.method == 'POST':

    return render(request, 'import.html', {'tree': 'fish'})
