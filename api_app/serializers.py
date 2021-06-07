from rest_framework import serializers
from django.db.models import fields
from .models import User,Neighborhood,Business
from rest_framework import serializers


class BusinessSerializers(serializers.ModelSerializer):
  class Meta:
    model = Business
    fields = "__all__"

 
class UserSerializer(serializers.ModelSerializer):
  business=BusinessSerializers(many=True,read_only=True)
  class Meta:
    model = User
    fields = "__all__"

 
class NeighborhoodSerializer(serializers.ModelSerializer):
  users=UserSerializer(many=True,read_only=True)
  business=BusinessSerializers(many=True,read_only=True)
  class Meta:
    model = Neighborhood
    fields="__all__"

