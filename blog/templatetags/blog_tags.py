from django import template
from blog.models import Post
from blog.models import Category
register = template.Library()

@register.simple_tag
def totalposts():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg):
    return value[:arg] + '...'

@register.inclusion_tag('blog/latest-posts.html')
def latest_post():
    posts = Post.objects.filter(status=1).order_by('published_date')[:2]
    return {'posts':posts}

@register.inclusion_tag('blog/post-category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {'categories':cat_dict}