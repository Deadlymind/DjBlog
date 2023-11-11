from django.shortcuts import render
from .models import Post

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


