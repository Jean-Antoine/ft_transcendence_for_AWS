import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import pong.routing
import friendship.routing


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(pong.routing.websocket_urlpatterns 
                               + friendship.routing.websocket_urlpatterns),
    }
)