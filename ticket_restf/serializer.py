from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    class Meta:
        model = Ticket
        fields = ['name' ,'phone', 'serial_number' , 'description' , 'file']