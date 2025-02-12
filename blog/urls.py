from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogsListView, BlogCreateView, BlogDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogsListView.as_view(), name='blogs_list'),
    path('blog_create/', BlogCreateView.as_view(), name='add_blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail')
]