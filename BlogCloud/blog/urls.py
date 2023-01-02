from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name="all_blogs"),
    path('<int:id>/', views.blog, name="blog_details"),
    path('comment', views.comment, name='comment')
]
