
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    #return HttpResponse('Hello World! このページは投稿画面です。')
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html')


# Create your views here.
