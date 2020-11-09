from django.shortcuts import render, get_object_or_404
from users.models import User
from .models import Post, Video
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
# from django.http import HttpResponse
# from django.core.files import File
# import os
# from unicodedata import name
# from django.template.loader import render_to_string
# from weasyprint import HTML
# import tempfile
# import datetime

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas


class NotesListView(ListView):
    model = Post
    template_name = 'notes/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class VideoListView(ListView):
    model = Video
    template_name = 'notes/video_list.html'
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


class UserVideoListView(ListView):
    model = Video
    template_name = 'notes/user_video.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Video.objects.filter(author=user).order_by('-date_posted')


class NotesDetailView(DetailView):
    model = Post


class VideoDetailView(DetailView):
    model = Video


class NotesCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'description', 'document', )

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    fields = ('caption', 'video', )
    template_name = ('notes/video_post.html')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        form.instance.author = self.request.user
        self.object.save()
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


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Video
    fields = ('caption', 'video', )

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


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Video
    messages.success = (f'Your Video has been deleted')
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'notes/about.html')


# def readFile(request):
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#     p.drawString(100, 100, "Hello world.")
#     p.showPage()
#     p.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

# def download(request, pk):
#     # post = Post.objects.get(pk=post.pk)
#     path_to_file = os.path.realpath("random.xls")
#     f = open(path_to_file, 'r')
#     myfile = File(f)
#     response = HttpResponse(myfile, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=' + name
#     return response


# def readFile(request):
#     response = HttpResponse(content_type='application/vnd.pdf')
#     response['Content-Disposition'] = 'inline; attachment; filename=' + \
#         str(datetime.datetime.now()) + '.pdf'
#     response['Content-Transfer-Encoding'] = 'binary'

#     html_string = render_to_string(
#         'notes/pdf_output.html', {'posts': []})
#     html = HTML(string=html_string)
#     results = html.write_pdf()

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(results)
#         output.flush()
#         output = open(output.name, 'rb')
#         response.write(output.read())

#     return response


# def handle_uploaded_file(f):
#     path_to_file = os.path.realpath('media/documents'+name)
#     f = open(path_to_file, 'r')
#     myfile = File(f)
#     with open(myfile, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# class Latest_post(CreateView):
#     model = Post
#     fields = ('latest_post',)

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
