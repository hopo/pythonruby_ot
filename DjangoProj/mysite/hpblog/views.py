from django.shortcuts import render, HttpResponse

from .models import Post
from .forms import InputTextForm, TareaForm

# Create your views here.


def board_list(request):
    post = Post.objects.all()
    context = {
        'post': post,
    }

    template = 'hpblog/board_list.html'

    return render(request, template, context)


def board_item(request, p_id):
    
    item = Post.objects.get(id=p_id)

    context = {
        'item': item,
    }

    template = 'hpblog/board_item.html'

    return render(request, template, context)


def board_insert(request):
    inputTextForm = InputTextForm
    context = {
        'inputTextForm': inputTextForm,
    }

    template = 'hpblog/board_insert.html'

    return render(request, template, context)
