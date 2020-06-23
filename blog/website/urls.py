
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blog.html', views.blog, name="blog"),
    path('blog1.html', views.blog1, name="blog1"),
]