# 导入django的apps模块
from django.apps import AppConfig

# 创建一个应用配置的子类
class MovieConfig(AppConfig):
    # 指定默认的自动字段类型
    default_auto_field = 'django.db.models.BigAutoField'
    # 给这个应用一个名字
    name = 'movie'
