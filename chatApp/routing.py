# routing.py

from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<thread_id>\d+)/$', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),

]
