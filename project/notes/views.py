from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.http import HttpResponse
from django.core.files import File
import os
from unicodedata import name


class NotesListView(ListView):
    model = Post
    template_name = 'notes/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserNotesListView(ListView):
    model = Post
    template_name = 'notes/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class NotesDetailView(DetailView):
    model = Post


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'description', 'document', )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'description', 'document', )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class NotesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    messages.success = (f'Your Document has been deleted')
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'notes/about.html')


def download(request, pk):
    post = Post.objects.get(pk=post.pk)
    path_to_file = os.path.realpath("random.xls")
    f = open(path_to_file, 'r')
    myfile = File(f)
    response = HttpResponse(myfile, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + name
    return response


class Latest_post(CreateView):
    model = Post
    fields = ('latest_post',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
