from django.db import models

# Create your models here.

class Ticket(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12 ,default='no phone')
    serial_number = models.CharField(max_length=12)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/')
    
    def __str__(self) -> str:
        return 'name  : ' + self.name + '  serial number :  ' + self.serial_number