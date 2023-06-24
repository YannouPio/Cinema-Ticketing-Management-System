"""
这个 views.py 文件包含了 Django REST framework 中定义的多个视图，
这些视图为前端提供了 API 接口来获取和操作后端数据。
视图函数主要负责接收 HTTP 请求，处理请求，并返回 HTTP 响应。

前端与后端的结合主要通过 API 接口进行。
前端发送 HTTP 请求到这些 API 接口，然后后端的视图函数处理这些请求，
并将数据以 JSON 格式返回给前端。前端再根据返回的数据来更新页面。

修改 get_frontpage_movies 视图函数中的 [0:8] 为 [0:4]，
改变了这个函数返回的电影数量。
在 Django 的查询语句中，Movie.objects.all()[0:8] 表示获取所有电影并返回前 8 部，
将它改为 Movie.objects.all()[0:4]，所以它现在返回前 4 部电影

"""


from django.shortcuts import render
from django.http import Http404
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Category
from .serializers import MovieListSerializer, MovieDetailSerializer, CategoryListSerializer
from django.db.models import Q

# 搜索电影的视图函数，根据查询参数搜索电影
@api_view(['GET'])
def search_movies(request):
    # 获取查询参数
    query = request.GET.get('query', '')
    # 使用查询参数从数据库中查询电影
    movies = Movie.objects.filter(Q(title__icontains=query))
    # 使用序列化器将查询结果序列化为 JSON 格式
    serializer = MovieListSerializer(movies, many=True)

    # 返回序列化后的数据
    return Response(serializer.data)

# 获取所有电影类别的视图函数
@api_view(['GET'])
def get_categories(request):
    # 查询所有电影类别
    categories = Category.objects.all()
    # 使用序列化器将查询结果序列化为 JSON 格式
    serializer = CategoryListSerializer(categories, many=True)

    # 返回序列化后的数据
    return Response(serializer.data)

# 获取电影的视图函数，根据类别查询电影
@api_view(['GET'])
def get_movies(request):
    # 获取类别 id 查询参数
    category_id = request.GET.get('category_id', '')
    # 查询所有电影
    movies = Movie.objects.all()

    # 如果提供了类别 id 查询参数，那么过滤出该类别的电影
    if category_id:
        movies = movies.filter(categories__id=int(category_id))

    # 使用序列化器将查询结果序列化为 JSON 格式
    serializer = MovieListSerializer(movies, many=True)

    # 返回序列化后的数据
    return Response(serializer.data)

# 获取首页电影的视图函数，返回前 8 部电影
@api_view(['GET'])
def get_frontpage_movies(request):
    # 查询所有电影并返回前 8 部
    movies = Movie.objects.all()[0:8]

    # 使用序列化器将查询结果序列化为 JSON 格式
    serializer = MovieListSerializer(movies, many=True)

    # 返回序列化后的数据
    return Response(serializer.data)

# 获取单部电影的视图函数
@api_view(['GET'])
def get_movie(request, slug):
    try:
        # 根据 slug 查询电影
        movie = Movie.objects.get(slug=slug)
    except Movie.DoesNotExist:
        # 如果电影不存在，那么抛出 404 错误
        raise Http404("电影未找到")
    # 使用序列化器将查询结果序列化为 JSON 格式
    serializer = MovieDetailSerializer(movie)
    # 返回序列化后的数据
    return Response(serializer.data)

