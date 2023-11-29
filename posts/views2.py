
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post


class PostList(ListView):  # context : default name is modelname_list =  post_list or object_list
    model = Post           # template model_action = post_list , post_detail, post_delet


class PostDetail(DetailView): # context : post , object
    model = Post              # template : post_detail 


class AddPost(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'

class EditPost(UpdateView):
    model = Post
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/edit.html'


class DeletPost(DeleteView):
    model = Post
    success_url = '/posts/'