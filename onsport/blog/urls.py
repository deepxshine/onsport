from django.urls import path
from . import views
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>', views.blog_category, name='blog_cat')
]