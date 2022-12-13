from rest_framework.serializers import ModelSerializer
from core.models import recien_nacido

class recien_nacidoSerializer(ModelSerializer):
    class Meta:
        model = recien_nacido
        fields =['__all__']