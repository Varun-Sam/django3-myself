from django.shortcuts import render
from .models import Post, Author, Education

# Create your views here.
def blog(request):
    queryset = Post.objects.filter()
    colleges = Education.objects.all()
    context = {
        'object_list': queryset,
        'colleges_list' : colleges
    }

    return render(request,'blog/blog.html', context)