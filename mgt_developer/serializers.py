from rest_framework.serializers import ModelSerializer
from .models import *

class dev_serializer(ModelSerializer):
    class Meta:
        model = developer
        fields = '__all__'