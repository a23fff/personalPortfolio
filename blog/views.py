from django.shortcuts import render
from .models import Project

def all_blogs(request):
    blogs = Project.objects.all()
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})