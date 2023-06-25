"""
Django REST框架中的序列化器用于将复杂的数据类型，
如querysets和模型实例等转化为python原生数据类型，
使得数据可以直接序列化为JSON等格式。
反之，序列化器也可以用于将接收到的数据反序列化为复杂类型。
"""


from rest_framework import serializers
from .models import Movie, Category
# 定义了三个序列化器，CategoryListSerializer、MovieListSerializer和MovieDetailSerializer，
# 这三个序列化器对应着三种不同的数据表现形式。
# 这些序列化器都是ModelSerializer的子类，它们继承了ModelSerializer的一些特性和行为。
# 每个序列化器中的内部类Meta定义了该序列化器的一些元数据。
# Category的序列化器，定义了序列化和反序列化Category模型时哪些字段应该被包含
class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # 指定对应的模型是Category
        fields = ('id', 'title', 'slug')  # 指定包含的字段

# Movie列表的序列化器，定义了序列化和反序列化Movie模型时哪些字段应该被包含
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # 指定对应的模型是Movie
        fields = ('id', 'title', 'slug', 'short_description', 'get_image')  # 指定包含的字段

# Movie详细信息的序列化器，定义了序列化和反序列化Movie模型时哪些字段应该被包含
class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # 指定对应的模型是Movie
        fields = ('id', 'title', 'slug', 'short_description', 'long_description')  # 指定包含的字段
