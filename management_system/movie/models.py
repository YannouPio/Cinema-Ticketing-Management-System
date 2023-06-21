from django.db import models

# 创建你的模型在这里

# Category模型表示电影可以归属的不同类别。
# 每个Category具有一个唯一的标题，一个用于URL友好版本的标题（slug），
# 一个可选的简短描述以及Category创建的时间戳。


class Category(models.Model):
    # 类别的标题，标题的最大长度设定为255
    title = models.CharField(max_length=255)

    # 标题的URL友好版本，用于路由，SEO等。
    slug = models.SlugField()

    # 类别的简短描述，此字段是可选的
    short_description = models.TextField(blank=True, null=True)

    # 创建类别的日期，当类别首次创建时自动设定
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# Movie模型表示单个电影。
# 每部电影可以归属于多个类别，每个类别可以拥有多部电影。
# 它包含一个标题，一个slug，一个简短描述，一个详细描述以及创建时间戳。
class Movie(models.Model):
    # 与Category模型的多对多关系
    # 这意味着一部电影可以归属于多个类别，一个类别可以有多部电影
    categories = models.ManyToManyField(Category)

    # 电影的标题，最大长度设定为255
    title = models.CharField(max_length=255)

    # 标题的URL友好版本，用于路由，SEO等。
    slug = models.SlugField()

    # 电影的简短描述，此字段是可选的
    short_description = models.TextField(blank=True, null=True)

    # 电影的详细描述，此字段是可选的
    long_description = models.TextField(blank=True, null=True)

    # 创建电影的日期，当电影首次创建时自动设定
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
