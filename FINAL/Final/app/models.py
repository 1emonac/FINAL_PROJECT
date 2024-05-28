from django.db import models
from django.db.models.signals import post_save, post_delete
from django.urls import reverse

from app.mixins import ChannelLayerGroupSendMixin


class Post(ChannelLayerGroupSendMixin, models.Model):
    CHANNEL_LAYER_GROUP_NAME = "liveblog"

    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        ordering = ["-id"] # 쿼리셋의 디폴트 정렬
        # id 필드에 대한 역순정렬

# Post 저장 직후에 호출될 함수
# 함수 호출 시에 생성/수정 여부는 created(bool 타입)
# 생성 시에는 "liveblog.post.created" 타입의 메시지를 보냄
# 수정 시에는 "liveblog.post.updated" 타입의 메시지를 보냄
def post__on_post_save(instance: Post, created: bool, **kwargs):
    if created:
        message_type = "liveblog.post.created"
    else:
        message_type = "liveblog.post.updated"

    # 생성/수정 메시지 모두 Post 인스턴스의 id와 포스팅 partial.html을 조회할 수 있는 URL 문자열 포함
    post_id = instance.pk
    post_partial_url = reverse("post_partial", args=[post_id])

    # channel_layer_group_send 메서드를 통해 메시지를 채널레이어 그룹에 보냄
    instance.channel_layer_group_send({
        "type": message_type,
        "post_id": post_id,
        "post_partial_url": post_partial_url,
    })

# 저장(save) 후에(post) 호출될 함수를 지정
# post_save 시그널을 통해 포스팅이 생성/ 수정될 때 post__on_post_save 함수가 호출되도록 등록
post_save.connect(
    post__on_post_save,
    sender=Post,
    dispatch_uid="post__on_post_save",
)

# Post 삭제 직후에 호출될 함수
# post_delete 시그널을 통해 포스팅이 생성/ 수정될 때 post__on_post_delete 함수가 호출되도록 등록
def post__on_post_delete(instance: Post, **kwargs):
    post_id = instance.pk

    # "liveblog.post.deleted" 타입의 메시지를 보낼 것, Post 인스턴스이 id 담기
    instance.channel_layer_group_send({
        "type": "liveblog.post.deleted",
        "post_id": post_id,
    })

# 삭제(delete) 후에(post) 호출될 함수를 지정
post_delete.connect(
    post__on_post_delete,
    sender=Post,
    dispatch_uid="post__on_post_delete",
)