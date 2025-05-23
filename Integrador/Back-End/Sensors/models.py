from django.db import models

class Sensors(models.Model): 
    sensors_choices = {
        ('Temp','Temperature'),
        ('Lumi','Luminosity'),
        ('Humi','Humidity'),
        ('Cont','Counter')
    }

    sensors = models.CharField(max_length=4, choices=sensors_choices)
    mac_address = models.CharField(max_length=256)
    unit_of_measure = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.CharField()
    status_choices = {
        ('ON','ON'),
        ('OFF','OFF')
    }
    status = models.CharField(max_length=3, default='N/A', primary_key= True)  

class Ambience(models.Model):
    sig = models.CharField(max)

class Historic(models.Model):
    sensors = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    ambiance = models.ForeignKey(Ambience, on_delete=models.CASCADE)
    notes = models.TextField(max_length=450)