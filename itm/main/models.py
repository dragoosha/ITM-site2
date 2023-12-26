from django.db import models

class Contacts(models.Model):
    name = models.CharField (
        max_length=255,
    )

    surname = models.CharField (
        max_length=255,
    )

    firma = models.CharField (        
        max_length=255,
    )

    position = models.CharField (        
        max_length=255,
    )

    telefon = models.CharField (
        max_length=30,
    )

    place = models.CharField (
        max_length=100,
    )

    country = models.CharField (
        max_length=100,
    )

    email = models.EmailField (
        
    )
    plz = models.CharField(
        max_length=250,
        
    )

    time_create = models.DateTimeField (auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"