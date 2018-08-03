from django.shortcuts import render
from .models import MyModel
from .forms import MyForm

# Create your views here.

def app(request):

    myModel = MyModel.objects.all()

    form = None
#     form = MyForm()

    context = {
        'myModel' : myModel,
        'form' : form,
    }

    return render(request, 'app/markdownx.html', context)
