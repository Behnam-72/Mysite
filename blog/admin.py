from django.contrib import admin
from blog.models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'creaded_date'
    empty_value_display = "-empty-"
    list_display = ['title','author', 'counted_view', 'status', 'published_date', 'creaded_date', 'updated_date']
    list_filter = ['title', 'author']
    ordering = ('creaded_date',)
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = "-empty-"
    list_display = ['name','email', 'subject', 'approved', 'created_date']
    list_filter = ['post', 'approved']
    ordering = ('created_date',)
    search_fields = ['name', 'post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# Register your models here.
