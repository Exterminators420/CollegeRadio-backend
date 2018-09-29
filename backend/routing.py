from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import player.routing
import chatbox.routing
from chatbox.consumers import ChatConsumer
from player.consumers import PlayerConsumer
from django.conf.urls import url



application = ProtocolTypeRouter({
    'websocket' : AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/chatbox/(?P<room_name>[^/]+)/$', ChatConsumer),
            url(r'^ws/stream/(?P<room_name>[^/]+)/$', PlayerConsumer),   
        ])
    ),
})



