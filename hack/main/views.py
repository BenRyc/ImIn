from django.shortcuts import render

# Create your views here.


def index(request):
    fish = 1


    return render(request, 'index.html', {'tree': fish})


# def serch(request):
#     return render(request, 'serch.html', {'tree': 'fish'})
#
#
#
# def import(request):
#     return render(request, 'import.html', {'tree': 'fish'})
