# Generated by Django 4.0.4 on 2022-05-09 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0006_alter_ticket_unique_together_ticket_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='time',
            field=models.TimeField(default=datetime.datetime(2022, 5, 9, 15, 31, 19, 933285)),
            preserve_default=False,
        ),
    ]
