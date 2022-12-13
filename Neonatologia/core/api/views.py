from rest_framework.viewsets import ModelViewSet
from core.models import recien_nacido
from core.api.serializers import recien_nacidoSerializer

class recien_nacidoApiViewSet(ModelViewSet):
    serializer_class = recien_nacidoSerializer
    queryset = recien_nacido.objects.all