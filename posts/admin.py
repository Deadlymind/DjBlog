from django.contrib import admin


from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin



class ProductAdmin(SummernoteModelAdmin):
    list_display = ['title', 'category','draft']
    list_filter = ['draft', 'tags', 'category']
    search_fields = ['title', 'tags']
    summernote_fields = ('content',)
    

admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
