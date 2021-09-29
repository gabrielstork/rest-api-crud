from rest_framework import viewsets
from . import serializers
from . import models


class PersonViewSets(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
