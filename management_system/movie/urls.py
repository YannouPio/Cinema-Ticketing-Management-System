"""
Django项目的URL路由是分层的。
首先，在项目的urls.py文件中定义了一级路由，
然后在每个应用的urls.py文件中定义了二级路由(可以使URL路由更加清晰和模块化)。

这个urls.py文件位于Movie应用中，
定义了与电影相关的URL到视图的映射关系。
在Django的项目结构中，一个项目可以包含多个应用，
每个应用都可以有自己的urls.py文件，
用于定义该应用中的URL路由规则。
"""


from django.urls import path
from movie import views

urlpatterns = [
    # URL 路由到 get_movies 视图，URL 是 'api/v1/movies/' （'api/v1/movies/' + ''）
    path('', views.get_movies, name='get_movies'),

    # URL 路由到 get_frontpage_movies 视图，URL 是 'api/v1/movies/get_frontpage_movies/' 
    path('get_frontpage_movies/', views.get_frontpage_movies, name='get_frontpage_movies'),

    # URL 路由到 get_categories 视图，URL 是 'api/v1/movies/get_categories/' 
    path('get_categories/', views.get_categories, name='get_categories'),

    # URL 路由到 search_movies 视图，URL 是 'api/v1/movies/search/' 
    path('search/', views.search_movies, name='search_movies'),

    # URL 路由到 get_movie 视图，URL 是 'api/v1/movies/<slug:slug>/' ，
    # 其中 <slug:slug> 是动态部分，根据实际的 slug 参数来确定
    path('<slug:slug>/', views.get_movie, name='get_movie'),
]

"""
当用户访问某个URL时，
例如 'api/v1/movies/search/'，
Django 会先找到项目的urls.py文件，
然后通过include('movie.urls')找到Movie应用的urls.py文件，
在这个文件中找到对应的URL（'search/'），然后执行对应的视图函数（views.search_movies）。

"""