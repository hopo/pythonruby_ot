from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm, UpdateForm

# Create your views here.


def board_list(request):
    template = 'hpblog/board_list.html'

    post = Post.objects.order_by('-id')
    context = {'post': post}

    return render(request, template, context)


def board_item(request, p_id):
    template = 'hpblog/board_item.html'

    item = Post.objects.get(id=p_id)

    context = {'item': item}

    return render(request, template, context)


def board_insert(request):
    template = 'hpblog/board_insert.html'

    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('board_list')
    else:
        form = PostForm()

    context = {'form': form}

    return render(request, template, context)


def board_update(request, p_id):
    template = 'hpblog/board_update.html'

    form = UpdateForm(request.POST or None)
    item = Post.objects.get(id=p_id)

    if form.is_valid():
        item.title = form.title
        item.content = form.content
        return redirect('board_list')
    else:
        form = UpdateForm()

    context = {
        'item': item,
        'form': form,
    }

    return render(request, template, context)


def board_delete(request, p_id):
    template = 'hpblog/board_delete.html'

    item = Post.objects.get(id=p_id)
    item.delete()

    context = {'item': p_id}

    return render(request, template, context)
