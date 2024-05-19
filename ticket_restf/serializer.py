from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Ticket
        fields = ['id','name' ,'device','phone', 'serial_number' ,'label' , 'description' , 'file' ,"created_at"]