from django.shortcuts import render

from .models import Post
from .forms import InsertForm, MDForm

# Create your views here.


def board_list(request):

    template = 'hpblog/board_list.html'

    post = Post.objects.all()
    context = {'post' : post}

    return render(request, template, context)

def board_insert(request):


    template = 'hpblog/board_insert.html'
    
    form = InsertForm.text
#     md = MDForm.content

    context = {
        'form' : form,
#         'md' : md,
    }

    return render(request, template, context)
