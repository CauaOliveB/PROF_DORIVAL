from django.db import models

class Sensors(models.Model): 
    sensors_choices = {
        ('Temp','Temperature - °C'),
        ('Lumi','Luminosity -lux'),
        ('Humi','Humidity - %'),
        ('Cont','Counter - num')
    }

    sensors = models.CharField(max_length=4, choices=sensors_choices)
    mac_address = models.CharField(max_length=256)
    unit_of_measure = models.CharField(max_length=256)
    value = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.CharField()
    status = models.BooleanField(default=False, primary_key= True)  

class Ambience(models.Model):
    sig = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    ni = models.CharField(max_length=256)
    task = models.CharField(max_length=256)

class Historic(models.Model):
    sensors = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    ambiance = models.ForeignKey(Ambience, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.IntegerField()  