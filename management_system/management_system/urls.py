"""
URL configuration for management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
urls.py 文件在 Django 项目中起到了路由的作用。
它定义了 URL 到视图的映射关系，当用户访问某个 URL 时，
Django 会根据 urls.py 文件中定义的映射关系，找到对应的视图来处理用户的请求。

这个文件与前端的结合是通过 HTTP 请求实现的。
当用户在前端执行某个操作（例如点击一个链接或提交一个表单）时，
前端会向后端发送一个 HTTP 请求，
请求的 URL 就是 urls.py 文件中定义的 URL。
Django 接收到这个请求后，会根据 urls.py 文件找到对应的视图来处理这个请求。

"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin 的 URL 配置
    path('admin/', admin.site.urls),

    # 用户注册、登录、注销等功能的 URL 配置，这些 URL 都以 'api/v1/' 开头，
    # 路径后面的部分由 'djoser.urls' 和 'djoser.urls.authtoken' 模块提供
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),

    # 电影相关的 URL 配置，这些 URL 都以 'api/v1/movies/' 开头，
    # 路径后面的部分由 'movie.urls' 模块提供
    path('api/v1/movies/', include('movie.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 静态文件的 URL 配置，这让 Django 能正确地处理静态文件（例如图片）
# settings.MEDIA_URL 是静态文件的 URL 前缀，
# settings.MEDIA_ROOT 是静态文件在服务器上的物理路径
