# Generated by Django 5.0.4 on 2024-04-24 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_restf', '0002_ticket_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.CharField(default='no phone', max_length=12),
        ),
    ]
