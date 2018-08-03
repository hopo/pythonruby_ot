from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
# from django.http import Http404

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

#     item = Post.objects.get(id=p_id)
    item = get_object_or_404(Post, id=p_id)

    if request.method == "POST":
        form = UpdateForm(request.POST, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
#             item.title = request.title
            print('>>> req: {}'.format(request.user))
            item.published_date = timezone.now()
            item.save()

            return redirect('board_list')
    else:
        form = UpdateForm(instance=item)

    context = {
        'form': form,
        'item' : item,
    }

    return render(request, template, context)


def board_delete(request, p_id):
    template = 'hpblog/board_delete.html'

#     item = Post.objects.get(id=p_id)
    item = get_object_or_404(Post, id=p_id)
    item.delete()

    context = {'item': p_id}

    return render(request, template, context)
