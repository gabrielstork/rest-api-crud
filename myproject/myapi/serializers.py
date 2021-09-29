from rest_framework import serializers
from . import models


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'