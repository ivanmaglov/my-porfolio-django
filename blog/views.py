from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
# Create your views here.


def allblogs(request):
    blogs_list = Blog.objects.all().order_by('-p_date')[:29]
    paginator = Paginator(blogs_list, 5)  # Show 3 projects per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs})

#def allblogs(request):
#    blogs=Blog.objects.all().order_by('-p_date')
#    return render(request, 'home.html', {'blogs':blogs})


def blogdetail(request, blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blogdetail.html', {'blog': detailblog})

