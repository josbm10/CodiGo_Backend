from pyexpat import model
from .models import *
from rest_framework import serializers

class FavoritosSerializers(serializers.ModelSerializer):
    class Meta:
        model=Favorito
        fields='__all__'
        