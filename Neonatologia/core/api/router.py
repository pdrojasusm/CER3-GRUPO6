from rest_framework.routers import DefaultRouter
from core.api.views import recien_nacidoApiViewSet

router_recien_nacido= DefaultRouter()

router_recien_nacido.register(prefix='core',basename='core',viewset=recien_nacidoApiViewSet)  