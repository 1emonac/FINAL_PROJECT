from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.utils.functional import cached_property

class ChannelLayerGroupSendMixin:
    CHANNEL_LAYER_GROUP_NAME = None

    # channel_layer 속성을 위해 cached_property 장식자를 적용
    # get_channel_layer() 함수가 호출되도록 함   
    @cached_property
    def channel_layer(self):
        return get_channel_layer()

    # group_send API를 호출하도록 래핑
    def channel_layer_group_send(self, message_dict):
        async_to_sync(self.channel_layer.group_send)(
            self.CHANNEL_LAYER_GROUP_NAME,
            message_dict
        )