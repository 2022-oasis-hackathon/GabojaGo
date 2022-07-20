from django.urls import path
from . import views

app_name = 'headquarters'

urlpatterns = [
    path('', views.index, name='index'),
]
