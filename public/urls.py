from django.urls import path
from . import views

app_name = 'public'

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post, name='post'),
    path('analysis', views.analysis, name='analysis'),
    path('list', views.list, name='list'),
    path('search', views.search, name='search'),
]
