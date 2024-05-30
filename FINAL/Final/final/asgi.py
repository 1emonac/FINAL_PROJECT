"""
ASGI config for final project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import app.routing  # noqa: E402
import chat.routing  # noqa: E402
import dr.routing
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

django_asgi_application = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_application,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    chat.routing.websocket_urlpatterns 
                    + app.routing.websocket_urlpatterns
                    + dr.routing.websocket_urlpatterns
                )
            ),
        )
    }
)