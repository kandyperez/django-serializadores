print ("empezemos ps")

from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
print ("terminamos")

from rest_framework import serializers
from marvel.e_commerce.models import WishList  # Ajusta la ruta del modelo si es necesario

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'user', 'product', 'created_at']  # Ajusta según los campos del modelo
