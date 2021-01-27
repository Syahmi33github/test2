from django.shortcuts import render

from .models import PostModels
from .forms import PostForm
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView

def testparallax(request):
    context = {
        'Judul' : 'Home Blog',
    }
    return render(request, 'blog/test.html', context)

def detailPost(request, slugInput):
    posts = PostModels.objects.get(slug = slugInput)

    context = {
        'Judul' : 'Posts',
        'Content' : 'Halaman Post',
        'Posts' : posts,

    }
    return render(request, 'blog/detail.html', context)

def ceritaSingkat(request, slugInput):
    posts = PostModels.objects.get(slug = slugInput)

    context = {
        'Judul' : 'Posts',
        'Content' : 'Halaman Post',
        'Posts' : posts,

    }
    return render(request, 'blog/ceritasingkat.html', context)

def categoryPost(request, categoryInput):
    posts = PostModels.objects.filter(category = categoryInput)
    categories = PostModels.objects.values('category').distinct()

    paginator = Paginator(posts, 10) #jumlahitem/halaman
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'Judul' : 'Posts',
        'Content' : 'Tampilkan Berdasarkan Category',
        'Posts' : posts,
        "Categories" : categories,
    }
    return render(request, 'blog/category.html', context)

# CLASS LIST
# class categoryPost(ListView):
#     model = PostModels
#     ordering = ['nama'] #urutan
#     paginate_by = 10
#     posts = PostModels.objects.filter(category = categoryInput)
#     categories = PostModels.objects.values('category').distinct()

#     extra_context = {
#         'Judul' : 'Posts',
#         'Content' : 'Tampilkan Berdasarkan Category',
#         'Posts' : posts,
#         "Categories" : categories,
#     }

#     def get_context_data(self,*args,**kwargs):
#         self.kwargs.update(self.extra_context)
#         kwargs = self.kwargs
#         return super().get_context_data(*args,**kwargs)

class BlogListView(ListView):
    model = PostModels
    ordering = ['nama'] #urutan
    paginate_by = 10
    posts = PostModels.objects.all()
    categories = PostModels.objects.values('category').distinct()

    extra_context = {
        'title' : 'List',
        'Posts' : posts,
        "Categories" : categories,
    }

    def get_context_data(self,*args,**kwargs):
        self.kwargs.update(self.extra_context)
        kwargs = self.kwargs
        return super().get_context_data(*args,**kwargs)


    