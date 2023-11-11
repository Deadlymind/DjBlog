from django.shortcuts import render
from .models import Post


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


from django.views.generic import ListView, DetailView

class PostList(ListView):  # context : default name is modelname_list =  post_list or object_list
    model = Post           # template model_action = post_list , post_detail, post_delet


class PostDetail(DetailView): # context : post , object
    model = Post              # template : post_detail 