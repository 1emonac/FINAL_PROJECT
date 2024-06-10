<<<<<<< HEAD
=======

>>>>>>> cb46744a52d08bd58c5e15ec9047541b2f6ccf27
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def index(request):
    post_list = Post.objects.all().order_by('-pk')
    paginator = Paginator(post_list, 9)  # 페이지당 9개의 게시글 표시
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'feed/blog_list.html', context)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'feed/blog_detail.html', context)
