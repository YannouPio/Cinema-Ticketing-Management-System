from django.urls import path

from movie import views

urlpatterns = [
    path('', views.get_movies)
]