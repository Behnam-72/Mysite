from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone
register = template.Library()


@register.inclusion_tag('blog/popular-posts.html')
def popular_post():
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

@register.inclusion_tag('blog/latest-post.html')
def latest_post():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return {'posts': posts}

