from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import *
from django.dispatch import receiver
from django.utils import timezone
from .models import *
from .api.v1.serializers import * 

# @receiver(post_save, sender=Room)
# def post_save_room(sender, instance, created, **kwargs):
#     if not created:
#         channel_layer = get_channel_layer()
#         room_name = str(instance.id)
#         async_to_sync(channel_layer.group_send)(room_name, {"type": "send_message",
#                                                             "message": {'instance': RoomSerializer(instance).data}})


# @receiver(post_save, sender=Match)
# def post_save_room(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         room_name = str(instance.room.id)
#         async_to_sync(channel_layer.group_send)(room_name, {"type": "send_message",
#                                                             "message": {'instance': MatchSerializer(instance).data}})




# @receiver(post_save, sender=MatchUser)
# def post_save_room(sender, instance, created, **kwargs):
#     if created:
#         channel_layer = get_channel_layer()
#         room_name = str(instance.match.room.id)
#         async_to_sync(channel_layer.group_send)(room_name, {"type": "send_message",
#                                                             "message": {'instance': MatchUserSerializer(instance).data}})
