from django.shortcuts import render
from .models import Sensors,Ambience, Historic
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class SensorsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset =  Sensors.get.all()

    