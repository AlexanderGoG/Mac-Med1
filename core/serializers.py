from rest_framework.serializers import ModelSerializer

from core.models import Obrashenie


class ObrashenieSerializer(ModelSerializer):
    class Meta:
        model = Obrashenie
        fields = '__all__'

