from django.urls import path
from . import views
Urlpatterns = [
    path('quote/', views.random_quote, name='random_quote'),
]