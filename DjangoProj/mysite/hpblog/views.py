from django.shortcuts import render

from .models import Post

# Create your views here.


def board_list(request):

    post = Post.objects.all()

    context = {'post' : post}

    return render(request, 'hpblog/board_list.html', context)

