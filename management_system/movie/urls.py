from django.urls import path

from movie import views

urlpatterns = [
    path('', views.get_movies, name='get_movies'),
    path('get_frontpage_movies/', views.get_frontpage_movies, name='get_frontpage_movies'),
    path('get_categories/', views.get_categories, name='get_categories'),
    path('search/', views.search_movies, name='search_movies'),  
    path('<slug:slug>/', views.get_movie, name='get_movie'),
]


