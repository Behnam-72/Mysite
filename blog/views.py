from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from blog.models import Post, Comment
from django.utils import timezone
from blog.form import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def blog_page(request, cat_name=None, author_name=None, tag_name = None):
    posts = Post.objects.filter(status=True, published_date__lte=timezone.now())
    if cat_name:
        posts = posts.filter(category__name=cat_name, status=True, published_date__lte=timezone.now())
    if author_name:
        posts = posts.filter(author__username=author_name, status=True, published_date__lte=timezone.now())
    if tag_name:
        posts = posts.filter(tags__name=tag_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_page(request, pid):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment didnt submit')

    post = get_object_or_404(Post, pk=pid, status=True, published_date__lte=timezone.now())
    post_previous = Post.objects.filter(id__lt=pid, status=True, published_date__lte=timezone.now()).last()
    post_next = Post.objects.filter(id__gt=pid, status=True, published_date__lte=timezone.now()).first()
    post.counted_view += 1
    post.save()
    if not post.login_require:
        comments = Comment.objects.filter(post=post.id, approved=True)
        context = {'post': post, 'post_previous': post_previous, 'post_next':post_next, 'comments':comments}
        return render(request, 'blog/blog-single.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def test(request):
    return render(request, 'test.html')



# Create your views here.
