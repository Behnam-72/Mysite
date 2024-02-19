from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
def blog_page(request, cat_name=None, author_name=None, tag_name = None):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name, status=True, published_date__lte=timezone.now())
    if author_name:
        posts = posts.filter(author__username=author_name, status=True, published_date__lte=timezone.now())
    if tag_name:
        posts = posts.filter(tags__name__in=tag_name, status=True, published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_page(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=timezone.now())
    post_previous = Post.objects.filter(id__lt=pid, status=True, published_date__lte=timezone.now()).last()
    post_next = Post.objects.filter(id__gt=pid, status=True, published_date__lte=timezone.now()).first()
    post.counted_view += 1
    post.save()
    context = {'post': post, 'post_previous': post_previous, 'post_next':post_next}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'test.html')


# Create your views here.
