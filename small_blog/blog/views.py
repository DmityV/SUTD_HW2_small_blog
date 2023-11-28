from django.shortcuts import get_object_or_404, render
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .forms import *
from .models import *


def post(request, pk=None):
    if pk is not None:
        instance = get_object_or_404(Post, pk=pk)
    else:
        instance = None
    form = PostForm(
        request.POST or None,
        files=request.FILES or None,
        instance=instance
    )
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'blog/post_create.html', context)


class PostListView(ListView):
    model = Post
    ordering = '-pub_date'
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('blog:list') 


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list') 
