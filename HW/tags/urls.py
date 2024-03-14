from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('<str:tag>/', views.quotes_by_tag, name='tags'),
]
