from django.shortcuts import render
from blog.models import Post

# Create your views here.


def index(request):
    posts=Post.objects.all()[:4]
    post_dicc={'listaPost':posts}
    return render(request, 'home/index.html',post_dicc)

def mision(request):
    
    return render(request, 'home/mision.html')

