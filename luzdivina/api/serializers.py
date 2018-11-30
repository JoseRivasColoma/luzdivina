from core.models import Comunidad
from rest_framework import serializers

class ComunidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = ('id', 'nombre', 'ubicacion')