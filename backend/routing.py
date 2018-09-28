from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import player.routing

application = ProtocolTypeRouter({
    #(http->django views is added by default)
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            player.routing.websocket_urlpatterns
        )
    ),
})
