from django.shortcuts import render, redirect

from .models import Blog, Comment

def blogs(request):
    # blogs = Blog.objects.order_by('-id').all()
    blogs = Blog.objects.filter(publish=True).order_by('-id')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/blogs.html', context)

def blog(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=id)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(request, 'blog/blog-details.html', context)

def comment(request):
    if request.method == "POST":
        comment = request.POST.get("comment")
        blog_id = request.POST.get("blog_id")
        path = request.POST.get("path")

        blog = Blog.objects.get(id=blog_id)
        user = request.user

        c = Comment(blog=blog, user=user, comment=comment)
        c.save()
        return redirect(path)
