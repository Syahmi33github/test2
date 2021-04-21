from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import PostModel


# Create your views here.
def index(request):
    contact_form = PostForm()

    if request.method == 'POST':
        PostModel.objects.create(
            judul 		= request.POST.get('judul'),
        )
        return redirect('index')

    context = {
        'Judul' : 'ATTA',
        'Content' : '',
        'contact_form' : contact_form,
    }

    return render(request, 'video.html', context)

def liat(request):
    postmodel = PostModel.objects.all()
    context = {
        'Judul' : 'ATTA',
        'Content' : '',
        'posts' : postmodel,
    }
    return render(request, 'liat.html', context)
    