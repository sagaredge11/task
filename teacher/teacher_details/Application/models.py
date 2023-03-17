from django.db import models

# Create your models here.
from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    room_number = models.CharField(max_length=20)
    subjects_taught = models.CharField(max_length=255)
    profile_picture = models.ImageField( null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"