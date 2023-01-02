from django.contrib import admin

from .models import Category, Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'publish')
    search_fields = ('title', 'description')
    list_editable = ('publish',)
    ordering = ('-id', )

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
