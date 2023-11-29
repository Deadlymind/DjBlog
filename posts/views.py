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
        'object_list' : data
    }
     

    return render(request,'posts/post_list.html', context)



def post_details(request, pk):
    data = Post.objects.get(id=pk)

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

    return render(request, 'posts/post_form.html', {'form':form})


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








