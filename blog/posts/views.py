import os
from .models import Post
from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404


# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'posts/home.html', {'posts':posts})

def post_details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/posts_detail.html', {'post':post})

def cv(requests):
    return render(requests, 'posts/cv.html')

def download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'posts/static/juraj_gabriel_cv.pdf')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
