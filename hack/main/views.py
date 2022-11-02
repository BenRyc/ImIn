from django.shortcuts import render

# Create your views here.


def index(request):
    fish = 1


    return render(request, 'index.html', {'tree': fish})
