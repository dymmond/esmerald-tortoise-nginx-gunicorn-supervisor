from esmerald import Gateway

from .views import WelcomeAPIView

route_patterns = [Gateway(handler=WelcomeAPIView, name="welcome")]
