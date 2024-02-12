from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [

    path('', blog_page, name = 'index'),
    path('<int:pid>', single_page, name = 'single'),
    path('test', test, name = 'test'),
    path('category/<str:cat_name>', blog_page, name = 'category'),
    path('author/<str:author_name>', blog_page, name = 'author')
]