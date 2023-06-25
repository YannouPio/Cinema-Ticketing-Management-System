"""
models.py 是 Django 用于定义项目中的数据库模型的文件
定义了两个模型：Category 和 Movie
"""


from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Category模型，用来表示电影的不同类别
class Category(models.Model):
    # 标题字段，用来存储类别的名称
    title = models.CharField(max_length=255)
    # slug字段，用来在URL中表示类别
    slug = models.SlugField()
    # 简短描述字段，描述类别的一些信息，可选
    short_description = models.TextField(blank=True, null=True)
    # 创建时间字段，自动添加创建日期
    created_at = models.DateField(auto_now_add=True)

    # 在字符串环境下，返回类别的标题
    def __str__(self):
        return self.title


# Movie模型，用来表示电影
class Movie(models.Model):
    # 与Category模型的多对多关系字段，表示一个电影可以有多个类别，一个类别也可以有多部电影
    categories = models.ManyToManyField(Category)
    # 标题字段，用来存储电影的名称
    title = models.CharField(max_length=255)
    # slug字段，用来在URL中表示电影
    slug = models.SlugField()
    # 简短描述字段，简短的描述电影的内容，可选
    short_description = models.TextField(blank=True, null=True)
    # 长描述字段，详细的描述电影的内容，可选
    long_description = models.TextField(blank=True, null=True)
    # 创建时间字段，自动添加创建日期
    created_at = models.DateField(auto_now_add=True)
    # 图片字段，存储电影的图片，可选
    image = models.ImageField(upload_to='uploads', blank=True, null=True)

    # 在字符串环境下，返回电影的标题
    def __str__(self):
        return self.title

    # 获取图片URL的方法，如果有图片，返回图片的URL，否则返回默认图片的URL
    def get_image(self):
        if self.image:
            return settings.WEBSITE_URL + self.image.url
        else:
            return 'http://bulma.io/images/placeholders/1280x960.png'
