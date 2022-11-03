from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('other/<int:thing>', views.other, name='other'),
    path('import', views.importJSON, name='importJSON'),
]
