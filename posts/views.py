from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm



'''
def post_list(request):

    data = Post.objects.all()                                : query

    context = {'mahmoud' : data}                             : context

    return render(request,'posts/post_list.html', context)   : template
'''
# Create your views here.

def post_list(request):

    data = Post.objects.all() # db : all posts --> list [1, 2]

    context = {
        'mahmoud' : data
    }
     

    return render(request,'posts/post_list.html', context)



def post_details(request, post_id):
    data = Post.objects.get(id=post_id)

    context = {
        'post' : data
    }

    return render(request,'posts/post_detail.html',context) 



def create_post(request):

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm()

    return render(request, 'posts/new.html', {'form':form})


def edit_post(request,pk):

    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit.html', {'form':form})


def delete_post(request, pk):

    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')









from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

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