from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from blog.models import Blog


class BlogsListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = {"title", "content", "preview"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update({
            'placeholder': 'Введите заголовок блога',
            'class': "form-control"
        })

        self.fields["content"].widget.attrs.update({
            'placeholder': "Напишите содержимое блога",
            'class': "form-control"
        })

        self.fields["preview"].widget.attrs.update({
            'class': "form-control"
        })


class BlogCreateView(CreateView):
    template_name = 'blog/blog_form.html'
    form_class = BlogForm
    success_url = reverse_lazy('blog:blogs_list')
