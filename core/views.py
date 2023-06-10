from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'core/home.html', context)



class PostListView(ListView):
    model = Post
    template_name = 'core/home.html'         # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'photos']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def post_form(request):
        submitted = False
        if request.method == 'POST':
            form = PostCreateView(request.POST, request.FILES)
            if form.is_valid():
                form.save()




class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'photos']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                return True
            return False



def about(request):
    return render(request, 'core/about.html', {'title':'About'})