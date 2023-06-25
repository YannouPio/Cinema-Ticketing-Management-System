"""
admin.py文件是用来设置应用的后台管理页面的。
在Django的后台管理页面中，可以对在models.py文件中定义的模型进行增删改查操作。
admin.site.register(Category)和admin.site.register(Movie)这两行代码
就是将Category模型和Movie模型注册到后台管理页面，
让这两个模型可以在后台管理页面进行管理。
"""


# 导入django的admin模块，这个模块帮助我们创建和管理网站的后台管理界面
from django.contrib import admin

# 从当前目录下的models.py文件中导入Category和Movie这两个模型
from .models import Category, Movie

# 在后台管理界面注册Category模型，这样我们就能在后台管理这个模型的数据了
admin.site.register(Category)

# 在后台管理界面注册Movie模型，这样我们就能在后台管理这个模型的数据了
admin.site.register(Movie)
