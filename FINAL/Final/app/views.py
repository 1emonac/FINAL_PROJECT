from django.shortcuts import render, get_object_or_404
from app.models import Post

# Create your views here.
def echo_page(request):
    return render(request, "app/echo_page.html")

# 장고 템플릿 랜더링을 통해, 포스팅 목록을 렌더링
# HTML 페이지 전체를 렌더링
# feed/chatting.html을 활용
def liveblog_index(request):
    post_qs = Post.objects.all()
    return render(request, "app/liveblog_index.html", {
        "post_list": post_qs,
    })

# 지정 post_id의 HTML만을 렌더링
def post_partial(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "app/partial/post.html", {
        "post": post,
    })