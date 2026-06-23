from django.db import models

from django.db import models

class Message(models.Model):
    content = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.content[:50] 

class Service(models.Model):
    picture = models.ImageField()
    service_name = models.CharField(max_length=100)
    service_details = models.CharField(max_length=300)
    price = models.CharField(max_length=10)


class Barber(models.Model):
    barber_picture = models.ImageField()
    barber_name = models.CharField(max_length=20)
    barber_profession = models.CharField(max_length=100)

class Gallery(models.Model):
    galler_picture =models.ImageField()
    