from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def board_list(request):
    param = '***test_parameter'
    return render(request, 'hpblog/board_list.html', {'param': param})
