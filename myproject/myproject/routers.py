from rest_framework import routers
from myapi import viewsets

router = routers.DefaultRouter()
router.register('myapi', viewsets.PersonViewSets)
