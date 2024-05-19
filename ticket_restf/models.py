from django.db import models
# Create your models here.

class Ticket(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    device = models.CharField(max_length=50 , default= "unknows")
    phone = models.CharField(max_length=12 ,default='no phone')
    serial_number = models.CharField(max_length=12)
    label = models.CharField(max_length=25 , null=True)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self) -> str:
        return 'name  : ' + self.name + '  serial number :  ' + self.serial_number