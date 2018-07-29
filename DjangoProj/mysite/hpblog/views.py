from django.shortcuts import render, HttpResponse

from .models import Post
from .forms import InputTextForm, TareaForm, PostForm

# Create your views here.


def board_list(request):
    template = 'hpblog/board_list.html'

    post = Post.objects.all()
    context = {
        'post': post,
    }

    return render(request, template, context)


def board_item(request, p_id):
    template = 'hpblog/board_item.html'

    item = Post.objects.get(id=p_id)

    context = {
        'item': item,
    }

    return render(request, template, context)


def board_insert(request):
    template = 'hpblog/board_insert.html'

    inputTextForm = InputTextForm
    context = {
        'inputTextForm': inputTextForm,
    }

    return render(request, template, context)


def new_post(request):
    template = 'hpblog/new_post.html'

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

