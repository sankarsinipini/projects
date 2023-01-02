from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = RichTextField()
    published_at = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=True)
    video_link = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    allow = models.BooleanField(default=True)

    def __str__(self):
        return self.blog+" "+self.user+" "+self.comment