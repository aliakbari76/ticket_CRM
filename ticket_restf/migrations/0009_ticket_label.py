# Generated by Django 5.0.4 on 2024-05-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_restf', '0008_alter_ticket_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='label',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
