# Generated by Django 4.0.4 on 2022-05-11 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0008_passenger_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='purchase_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='qunatity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='successful',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='transaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flight.payment'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='volume',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
