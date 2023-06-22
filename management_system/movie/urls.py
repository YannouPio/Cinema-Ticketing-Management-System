from django.urls import path

from movie import views

urlpatterns = [
    path('', views.get_movies),
    path('get_frontpage_movies/', views.get_frontpage_movies),
    path('get_categories/', views.get_categories),
    path('search/', views.search_movies),  # 新增路由
    path('<slug:slug>/', views.get_movie),
]

