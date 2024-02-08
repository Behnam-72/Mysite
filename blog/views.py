from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
def blog_page(request):
    posts = Post.objects.filter(status = True, published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_page(request, pid):
    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=timezone.now())
    post_previous = Post.objects.filter(id__lt=pid, status=True, published_date__lte=timezone.now()).order_by('published_date').last()
    post_next = Post.objects.filter(id__gt=pid, status=True, published_date__lte=timezone.now()).order_by('published_date').first()
    post.counted_view += 1
    post.save()
    context = {'post': post, 'post_previous': post_previous, 'post_next':post_next}
    return render(request, 'blog/blog-single.html', context)

    

# Create your views here.